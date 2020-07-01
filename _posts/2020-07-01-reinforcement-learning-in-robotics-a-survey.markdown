---
layout: post
title:  "Reinforcement Learning in Robotics: A Survey"
date:   2020-07-01 12:07:00 -0400
paper-url: https://dl.acm.org/doi/10.1177/0278364913495721
paper-year: 2013
paper-authors:
  - Jens Kober
  - J. Andrew Bagnell
  - Jan Peters
author: Nick Jalbert
---

**Work in progress**

### 1. Introduction

There is a useful synergy between the fields of Reinforcement Learning (RL) and
robotics:  RL techniques allow robots to autonomously learn complex-to-engineer
behaviors while robotics problems can provide a useful testbed for RL
algorithms.

One way to to classify machine learning problems is to look at their complexity
of reward structure and their complexity of environmental interaction.  RL is
relatively high on both scales, and simpler problems (e.g. supervised learning)
can often be rephrased to fit into the RL paradigm.

Robotics benchmarks generally have several characteristics that separate them
from other interesting benchmarks in the RL domain:

* Problems are often best represented with high-dimensional continuous state
  and action spaces.
* It is often unrealistic to assume the true state is observable and noise
  free.
* Experience in physical systems is expensive to obtain.
* As a corollary to the above, reward shaping is important and can be difficult
  when experience is expensive to obtain.
* Most RL successes in robotics (as of 2013) has been demonstrated with
  model-based algorithms using policy-search methods (vs value function
  methods)

### 2. A Concise Introduction to Reinforcement Learning

TODO

