# Trains a NN on cartpole using a policy gradient method.
#
# Run with:
#   python nn.py
#
# View progress at http://localhost:5000 with:
#   mlflow ui
#

import random
import statistics
import numpy as np
import tensorflow as tf
import mlflow.tracking
import gym


def get_agent():
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Dense(32, activation="relu", input_shape=(4,)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(0.01),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=["accuracy"],
    )
    return model


def get_run_batch(agent):
    RUNS_PER_BATCH = 50
    return [get_run(agent, True) for i in range(RUNS_PER_BATCH)]


def get_run(agent, explore):
    env = gym.make("CartPole-v1")
    state = env.reset()
    done = False
    total_reward = 0
    run = []
    while not done and total_reward < 200:
        p_left = agent(np.reshape(state, (1, 4)))[0][0]
        if explore:
            action = 0 if random.random() <= p_left else 1
        else:
            action = 0 if p_left <= 0.5 else 1
        state, reward, done, info = env.step(action)
        total_reward += reward
        run.append((state, action))
    return run


def get_training_data(runs):
    DISCOUNT = 0.95
    discounted_runs = []
    for run in runs:
        discounted_run = []
        run.reverse()
        discounted_reward = 0
        for state, action in run:
            discounted_reward = discounted_reward * DISCOUNT + 1
            discounted_run.append((state, action, discounted_reward))
        discounted_run.reverse()
        discounted_runs.append(discounted_run)
        run.reverse()

    rewards = [
        r for discounted_run in discounted_runs for s, a, r in discounted_run
    ]
    mean = statistics.mean(rewards)
    stdev = statistics.stdev(rewards)
    input_data = []
    target = []
    for run in discounted_runs:
        for state, action, reward in run:
            input_data.append(state)
            normalized_score = (reward - mean) / stdev
            if normalized_score > 0 and action == 0:
                target.append(1)
            elif normalized_score > 0 and action == 1:
                target.append(0)
            elif normalized_score < 0 and action == 0:
                target.append(0)
            else:
                target.append(1)
    return input_data, target


def train_agent(agent, runs):
    x_train, y_train = get_training_data(runs)
    assert len(x_train) > 0
    assert len(x_train) == len(y_train)
    np_x_train = np.reshape(x_train, (len(x_train), 4))
    np_y_train = np.reshape(y_train, (len(y_train), 1))
    agent.fit(np_x_train, np_y_train)


def test_agent(agent, iteration):
    RUNS_PER_BATCH = 10
    runs = [get_run(agent, False) for i in range(RUNS_PER_BATCH)]
    run_steps = [len(run) for run in runs]
    mlflow.log_metric("Max steps", max(run_steps), step=iteration)
    mlflow.log_metric(
        "Median steps", statistics.median(run_steps), step=iteration
    )
    mlflow.log_metric("Mean steps", statistics.mean(run_steps), step=iteration)
    mlflow.log_metric("Min steps", min(run_steps), step=iteration)
    print()
    print(f"Iteration {iteration}")
    print(f"\tMax steps per run: {max(run_steps)}")
    print(f"\tMedian steps per run {statistics.median(run_steps)}")
    print(f"\tMean steps per run {statistics.mean(run_steps)}")
    print(f"\tMin steps per run {min(run_steps)}")
    print()


def train():
    TRAINING_ITERATIONS = 100000
    agent = get_agent()
    for i in range(TRAINING_ITERATIONS):
        runs = get_run_batch(agent)
        train_agent(agent, runs)
        test_agent(agent, i)


if __name__ == "__main__":
    with mlflow.start_run():
        train()
