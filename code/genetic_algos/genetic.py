# Applies the genetic algorithm described in the paper
#   "Deep Neuroevolution: Genetic Algorithms are a Competitive Alternative
#    for Training Deep Neural Networks for Reinforcement Learning"
# to Cartpole.
#
# Run with:
#   python genetic.py
#
# View progress at http://localhost:5000 by running:
#   mlflow ui
#
# See README.md for results
#

import random
import statistics
import numpy as np
import tensorflow as tf
import mlflow.tracking
import gym


def train():
    GENERATIONS = 1000
    child_pool = get_child_pool()
    fittest = [random.choice(child_pool) for i in range(10)]
    for generation in range(GENERATIONS):
        generate_children(fittest, child_pool)
        results = evaluate_children(child_pool)
        evaluate_results(results, generation)
        fittest = [r[1] for r in results]


def get_child_pool():
    CHILD_COUNT = 100
    children = []
    # Allocating a new keras NN takes a while, instead reuse a pool of nets
    for i in range(CHILD_COUNT):
        model = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),
                tf.keras.layers.Dense(8, activation="relu"),
                tf.keras.layers.Dense(1, activation="sigmoid"),
            ]
        )
        model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss=tf.keras.losses.BinaryCrossentropy(),
        )
        children.append(model)
    return children


def generate_children(fittest, child_pool):
    # Create new, randomly-perturbed children
    for child in child_pool:
        parent = random.choice(fittest)
        create_child(child, parent, with_noise=True)
    # Bring the previous fittest nets directly into the new generation
    for fit in fittest:
        child = random.choice(child_pool)
        create_child(child, fit, with_noise=False)


def create_child(child, parent, with_noise):
    for child_layer, parent_layer in zip(child.layers, parent.layers):
        weights = parent_layer.get_weights()
        if with_noise:
            new_weights = [
                w + np.random.normal(0, 0.1, w.shape) for w in weights
            ]
        else:
            new_weights = weights
        child_layer.set_weights(new_weights)
    return child


def evaluate_children(child_pool):
    FITTEST_CUTOFF = -10
    results = []
    for child in child_pool:
        runs = get_run_batch(child)
        mean_run_length = statistics.mean([len(run) for run in runs])
        results.append((mean_run_length, child))
    return sorted(results, key=lambda x: x[0])[FITTEST_CUTOFF:]


def get_run_batch(agent):
    RUNS_PER_BATCH = 10
    return [get_run(agent) for i in range(RUNS_PER_BATCH)]


def get_run(agent):
    env = gym.make("CartPole-v1")
    state = env.reset()
    done = False
    total_reward = 0
    run = []
    p_lefts = []
    while not done and total_reward < 200:
        p_left = float(agent(np.reshape(state, (1, 4)))[0][0])
        p_lefts.append(p_left)
        action = 0 if random.random() <= p_left else 1
        state, reward, done, info = env.step(action)
        total_reward += reward
        run.append((state, action))
    return run


def evaluate_results(results, generation):
    mean_run_lengths = [r[0] for r in results]
    mlflow.log_metric("Max run length", max(mean_run_lengths), step=generation)
    mlflow.log_metric(
        "Median run length",
        statistics.median(mean_run_lengths),
        step=generation,
    )
    mlflow.log_metric(
        "Mean run length", statistics.mean(mean_run_lengths), step=generation
    )
    mlflow.log_metric("Min run length", min(mean_run_lengths), step=generation)
    print()
    print(f"Generation {generation}")
    print(f"\tMax steps per run: {max(mean_run_lengths)}")
    print(f"\tMedian steps per run {statistics.median(mean_run_lengths)}")
    print(f"\tMean steps per run {statistics.mean(mean_run_lengths)}")
    print(f"\tMin steps per run {min(mean_run_lengths)}")


if __name__ == "__main__":
    with mlflow.start_run():
        train()
