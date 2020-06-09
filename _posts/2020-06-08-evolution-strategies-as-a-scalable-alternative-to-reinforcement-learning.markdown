---
layout: post
title:  "Evolution Strategies as a Scalable Alternative to Reinforcement Learning"
date:   2020-06-08 12:07:00 -0700
paper-url: https://arxiv.org/pdf/1703.03864.pdf
paper-authors:
  - Tim Salimans
  - Jonathan Ho
  - Xi Chen
  - Szymon Sidor
  - Ilya Sutskever
author: Nick Jalbert
---

### 1. Introduction

* RL methods based on the Markov Decision Process (MDP) formalism have been one
  strategy that has seen success in learning complex behavior.

* Another approach is black-box optimization methods. This is also known as
  direct policy search or neuro-evolution when applied to neural nets (NNs).

* This paper explores Evolution Strategies as a black box approach to solving
  RL problems.  Key contributions and observations about ES:
  * Virtual batch normalization and reparameterization greatly improves ES
    performance.
  * ES is highly parallelizable using CPUs.
  * Less data efficient than A3C (needs 3x to 10x the data) but more
    computationally efficient.
  * Broader exploration than typically seen with gradient-based methods.
  * Generally robust and not much hyperparameter tuning to move between
    environments.

* Black-box optimization algorithms are attractive because:
  * Indifference to sparse or dense reward distribution
  * No need for backpropagation or gradient calculations
  * Tolerance for long time horizons

### 2. Evolution Strategies

* At a high-level: you have generations and each generation has a population.
  Each member of the population is tested for fitness.  The top performers are
  recombined into the next generation and the process repeats.

* This paper looks at a Natural Evolution Strategy (NES).  The description here
  is too condensed for me to fully grok (TODO: checkout Sehnke et al.'s
  "Parameter-exploring policy gradients") but my guess is it works as follow:
  * You represent a population as a distribution over parameters.  This
    distribution is parameterized by $$\psi$$.
  * You run the population on a few episodes to evaluate the fitness.
  * You calculate the gradient with regard to fitness and adjust $$\psi$$ in a
    way that improves fitness across the population.
  * They use some trick to smooth the rewards from the potentially-sparse RL
    environment so they can calculate a closed-form for the gradients (gaussian
    blurring).

* Overall the algorithm proceeds as following:
  * Perturb the parameters and run an episode of the resulting policy in the
    environment.
  * Combine the episode results, calculate the stochastic gradient, and update
    the parameters.

* ES algorithms are amenable to parallelization.
  * They operate on complete episodes
  * We only care about (in a global sense) the scalar reward of each episode
  * We don't require value function approximations (and the resulting
    dependencies on a particular policy).

* They note that in the extreme this reduces to finite difference if every
  worker only perturbs a single parameter (TODO: lookup finite difference
  methods).

* Q-learning and policy gradients derive the learning signal from sampling a
  policy. ES derives a signal from perturbing a policy.  Thus you have to
  ensure some perturbations perform better than others or else you won't get
  any exploration.  This required some normalization in some benchmarks.

### 3. Smoothing

>  A large source of difficulty in RL stems from the lack of informative
>  gradients of policy performance: such gradients may not exist due to
>  non-smoothness of the environment or policy, or may only be available as
>  high-variance estimates because the environment usually can only be accessed
>  via sampling.

* Policy gradient methods add noise to the action space (probabilistic sampling
  like softmax for selecting actions) to smooth gradients.  ES adds noise to
  the parameter space.

* ES variance is fixed whereas it grows nearly linearly for policy-gradient
  methods as the length of an episode grows.  ES should thus have an advantage
  for long episodes (in practice, discounting often reduces the effective
  length of the episode).

* ES can be reduced to a finite difference method.

* Because only total episode reward is used, ES can more easily handle sparse
  rewards.

### 4. Experiments

* They compared ES to TRPO to solve a number of MuJoCo benchmarks.  In some it
  trained to TRPO levels significantly faster (i.e. using 30% of the training
  time) in others it took longer.

* They compared ES to A3C on the Atari suite. It beat A3C in 23 games and lost
  to A3C in 28 games.

* ES algorithms parallelize well on EC2.

* Never heard of frameskip before, but apparently sometimes you just ignore
  some frames and only choose an action, for example, every fourth frame.


### See also

* [Evolution Strategies by Lilian Weng](https://lilianweng.github.io/lil-log/2019/09/05/evolution-strategies.html)
* [A Visual Guide to Evolution Strategies](https://blog.otoro.net/2017/10/29/visual-evolution-strategies/)
