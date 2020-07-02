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

A crash course in RL:

* An agent tries to maximize the accumulated reward over its lifetime.  An
  environment can either be *episodic* with well-defined start, stop, and reset
  points or ongoing.

* An environment has a set of states $$S$$ and a set of actions $$A$$ available to
  an agent in every state.  A state contains all relevant information (i.e. the
  process is memory-less).

* Transitions between states generate rewards.

* The goal of RL is to find a mapping from states to actions called a policy
  $$\pi$$ such that the policy maximizes reward.  An optimal policy is referred
  to as $$\pi^ * $$.  A policy can be deterministic or probabilistic.

* An RL agent needs to discover the relationship between states, actions, and
  rewards.  Thus RL algorithms will have exploration and exploitation
  components built into them.

* The above environmental properties taken together are a Markov Decision
  Process (MDP).  Most of classical RL is built against MDPs.

* There are different behaviors that can be optimized in $$\pi^ * $$.  One is a
  finite-time horizon optimization where you are maximizing the expected reward
  over the next $$h$$ time steps.  Another (more common) formulation is that
  you optimize the expected discounted reward with a manually chosen discount
  factor $$\gamma$$.  Small $$\gamma$$ are greedier and prefer immediate
  rewards to further out rewards.

*  In real-world domains, often you prefer optimizing for average reward (the
   expected reward as the time horizon approaches infinity) rather than
   discounted reward.

*  Generally, an agent does not know anything about its environment at the
   start of learning.  It must navigate the *explore-exploit trade-off* as it
   attempts to learn an optimal policy.  While learning algorithms that are
   polynomial with respect to the action and state space are known, these are
   generally difficult to apply to robotics (where state is often large and
   continuous).

* *Off-policy* methods explore the state space independent of the best-learned
  policy.  *On-policy* methods explore the state space while following the
  best-learned policy and thus exploration has to be baked into $$\pi$$.

* An additional complication in the RL setting is that there's path dependence
  in that an agent's earlier actions can affect later rewards.  This is
  referred to as the *credit assignment problem*.

* Optimizing the primal formulation of the RL problem is known as *policy
  search* while optimizing the Lagrangian dual is known as a *value
  function-based approach*.

* Value function-based approaches generally attempt to learn a value function
  $$V^{\pi}(s)$$ or a state-action value function $$Q^{\pi}(s,a)$$ which
  measure the "goodness" of states and actions.  Given correct value functions,
  then $$\pi^ * $$ becomes selecting the best action in each state as
  determined by $$V$$ or $$Q$$.  Note that:
    * $$V$$ and $$Q$$ are parameterized by the policy $$\pi$$.  As the policy
      changes, so too will the value functions.
    * $$V$$ can only be used as a basis of a policy if you know the transition
      probabilities to successor states after the current state.
    * Often times $$V$$ and $$Q$$ will be approximated using neural nets or
      similar.

* Three high-level approaches to value function-based RL:
  * **Dynamic Programming** - usable when you have a model of the transition
    probabilities and reward function.  These methods are model based and
    include policy iteration and value iteration.  They have the flavor of
    calculating your value function based on a policy and then greedily
    improving your policy based on this calculation.
  * **Monte Carlo** - These techniques directly sample the environment
    performing complete rollouts to learn the dynamics and improve the value
    estimates.
  * **Temporal Difference Methods** - These techniques are similar to Monte
    Carlo techniques, but learn at each timestep of a rollout rather than
    waiting for complete traces.


**TODO 2.2.2**

