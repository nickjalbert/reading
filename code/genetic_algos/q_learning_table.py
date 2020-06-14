# Runs tabular q-learning on cartpole
#
# Run with:
#   python q_learning_table.py
#
# View progress at http://localhost:5000 with:
#   mlflow ui

import random
import statistics

# from decimal import get_context
from decimal import Decimal
from collections import defaultdict

# import numpy as np
# import tensorflow as tf
import mlflow.tracking
import gym

MAX_EPISODES = 100000
DISCOUNT = 0.9
LEARNING_RATE = 0.1
INITIAL_EPSILON = 0.5
DROP_RATE = 0.5
EPISODES_PER_DROP = 1000


class DiscreteCartpole:
    def __init__(self):
        self.env = gym.make("CartPole-v1")
        self.action_space = self.env.action_space

    def _quantize(self, state):
        return tuple([Decimal(el).quantize(Decimal(".01")) for el in state])

    def reset(self):
        return self._quantize(self.env.reset())

    def step(self, action):
        state, reward, done, info = self.env.step(action)
        return self._quantize(state), reward, done, info


class QTable:
    def __init__(self):
        self.storage = defaultdict(int)

    def get(self, state, action):
        return self.storage[(state, action)]

    def set(self, state, action, value):
        self.storage[(state, action)] = value

    def update(self, state, action, next_state, reward):
        curr_q = self.get(state, action)
        max_next_q = max([self.get(next_state, a) for a in [0, 1]])
        discounted_next_q = DISCOUNT * max_next_q
        q_error = LEARNING_RATE * (reward + discounted_next_q - curr_q)
        updated_curr_q = curr_q + q_error
        self.set(state, action, updated_curr_q)


def train():
    env = DiscreteCartpole()
    q_values = QTable()
    is_training = True
    for episode in range(MAX_EPISODES):
        run_episode(episode, env, q_values, is_training)
        evaluate_policy(episode, env, q_values)


def run_episode(episode, env, q_values, is_training):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action = get_next_action(episode, q_values, state, is_training)
        next_state, reward, done, info = env.step(action)
        if is_training:
            q_values.update(state, action, next_state, reward)
        total_reward += reward
        state = next_state
    return total_reward


def get_next_action(episode, q_values, state, is_training):
    if random.random() < get_effective_epsilon(episode) and is_training:
        return random.choice([0, 1])
    else:
        return 0 if q_values.get(state, 0) > q_values.get(state, 1) else 1


def evaluate_policy(episode, env, q_values):
    if episode % 1000 != 0:
        return
    is_training = False
    rewards = [run_episode(i, env, q_values, is_training) for i in range(10)]
    max_reward = max(rewards)
    mean_reward = statistics.mean(rewards)
    median_reward = statistics.median(rewards)
    min_reward = min(rewards)
    mlflow.log_metric("Max steps", max_reward, step=episode)
    mlflow.log_metric("Median steps", median_reward, step=episode)
    mlflow.log_metric("Mean steps", mean_reward, step=episode)
    mlflow.log_metric("Min steps", min_reward, step=episode)
    print()
    print(f"Iteration {episode}")
    print(f"\tMax steps per run: {max_reward}")
    print(f"\tMedian steps per run {median_reward}")
    print(f"\tMean steps per run {mean_reward}")
    print(f"\tMin steps per run {min_reward}")
    print()


# https://towardsdatascience.com/learning-rate-schedules-and-adaptive-learning-rate-methods-for-deep-learning-2c8f433990d1
def get_effective_epsilon(episode):
    return INITIAL_EPSILON * (DROP_RATE ** (episode / EPISODES_PER_DROP))


if __name__ == "__main__":
    with mlflow.start_run():
        train()
