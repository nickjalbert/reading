# Quick script that evaluates the performance of:
#   1. A completely random policy (aka coin flip)
#   2. A randomly initialized neural net
# playing CartPole-v1
#
# Run:
#    python cartpole_difficulty.py
#
# See RESULTS.md for raw results
#

import numpy as np
import tensorflow as tf
import gym
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
import random


TRIALS = 2000


def print_do_better_than(all_rewards, threshold):
    success = [r for r in all_rewards if r > threshold]
    print(
        f"\tNets that do better than {threshold}: "
        f"{len(success)} ("
        f"{len(success)*100/len(all_rewards):.2f}%)"
    )


def evaluate(use_random):
    env = gym.make("CartPole-v1")
    all_rewards = []
    for i in range(TRIALS):
        if not use_random:
            nn = tf.keras.Sequential(
                [
                    tf.keras.layers.Dense(
                        4, activation="relu", input_shape=(4,)
                    ),
                    tf.keras.layers.Dense(1, activation="sigmoid"),
                ]
            )
        # Run using Neural Net as policy
        state = env.reset()
        total_reward = 0
        done = False
        while not done and total_reward < 200:
            if use_random:
                action = random.choice([0, 1])
            else:
                p_left = float(nn(np.reshape(state, (1, 4)))[0][0])
                action = 0 if p_left > 0.5 else 1
            state, reward, done, info = env.step(action)
            total_reward += reward
        all_rewards.append(total_reward)
    descriptor = "random" if use_random else "nn"
    print("----------")
    print(all_rewards)
    print("----------")
    print()
    print(f"Results for {len(all_rewards)} {descriptor} trials")
    print(f"\tMax reward: {max(all_rewards)}")
    print(f"\tMedian reward: {statistics.median(all_rewards)}")
    print(f"\tMean reward: {statistics.mean(all_rewards):.2f}")
    print(f"\tStddev reward: {statistics.stdev(all_rewards):.2f}")
    print(f"\tMin reward: {min(all_rewards)}")
    print()
    print_do_better_than(all_rewards, 5)
    print_do_better_than(all_rewards, 10)
    print_do_better_than(all_rewards, 15)
    print_do_better_than(all_rewards, 20)
    print_do_better_than(all_rewards, 25)
    print_do_better_than(all_rewards, 30)
    print_do_better_than(all_rewards, 50)
    print_do_better_than(all_rewards, 100)
    print_do_better_than(all_rewards, 150)
    perfect_runs = [r for r in all_rewards if r >= 200]
    print(
        f"\tPerfect nets (200 reward): {len(perfect_runs)} ("
        f"{len(perfect_runs)*100/len(all_rewards):.2f}%)"
    )
    plt.clf()
    title = "Randomly Initialized NNs play CartPole"
    if use_random:
        title = "Random Policy plays CartPole"
    sns.distplot(
        all_rewards, axlabel="CartPole-v1 reward", kde=False,
    ).set_title(title)
    plt.savefig(f"{descriptor}-results.png")
    plt.clf()
    title = "Randomly Initialized NNs play CartPole and score more than 15"
    if use_random:
        title = "Random Policy plays CartPole and scores more than 15"
    sns.distplot(
        [r for r in all_rewards if r > 15],
        axlabel="CartPole-v1 reward",
        kde=False,
    ).set_title(title)
    plt.savefig(f"{descriptor}-results-gt-15.png")


if __name__ == "__main__":
    print("Random Policy:")
    evaluate(True)
    print()
    print()
    print("Randomly Initialized NN:")
    evaluate(False)
