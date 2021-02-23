---
layout: post
title:  "Reductionism in Reinforcement Learning"
date:   2021-02-23 12:02:00 -0700
paper-url: https://www.youtube.com/watch?v=Pa7-ZwMs9nM
paper-year: 2020
paper-authors:
  - Dale Schuurmans
author: Nick Jalbert
---

* The common framing of RL (agent - environment loop) hides a lot of
  complexity found in real world problems:

  * Multi-agent interactions -> non-stationarity

  * Partial observability -> construct memory

  * Exploration -> explore/exploit trade off

  * Sequential decisions -> long horizon planning

  * Exploitation -> policy optimization


* Schuurmans proposes thinking about RL as the process of:

  * **Learning** - looking at data and identifying patterns
  * **Decision Making** - planning/optimal control
  * **Interactively** - online as you are acting within an environment

* Each of the above definitional components contains sub-problems  (many of
  which have been well studied).


### Single Step Decision Making

* Sets up the batch policy optimization problem: You are given a sparse matrix
  where the rows are contexts or observations, the columns are actions, and
  entries are the rewards received while taking the columnar action in the
  row's context.


* Relates this to the supervised learning paradigm where you don't maximize
  expected reward (a.k.a. expected accuracy in supervised learning) directly,
  but instead maximize a surrogate objective (often maximum likelihood or log
  likelihood).

  * Why? Because maximum likelihood has a nice relationship with expected
    accuracy (it's *calibrated*) and the structure of maximum likelihood is
    *concave* and thus it is cleaner to optimize over.  In general, maximum
    likelihood is all we consider optimizing over in supervised learning.

  * This is not directly applicable to RL, but the basic idea is related to
    minimizing the KL divergence of the policy from an implicit reference
    distribution.


* Softmax is a key source of optimization difficulty.

    * For tabular Q, directly optimizing expected reward converges to a global
      maximum even though it's a non-concave maximization problem (Agarwal et
      al COLT-2020).

    * Even though we can optimize against this objective, constants matter and
      bad initialization and/or bad luck can lead to arbitrarily long waits
      until convergence.

    * Why are we committed to softmax?  There are other transfer functions that
      avoid this initialization problem.

* How do you handle missing data?  In RL, often the reward matrix is very
  sparse.

    * Many RL strategies impute unobserved rewards.  Often this is simplistic
      but unbiased.

    * Another approach would be to model missing data, and then fill in with
      experience (with some transformations to preserve unbiasedness).
      Choosing a good model of missing data can help with the optimization
      problem too.

### Sequential Decision Making

* Because of path dependence, you must think of the long term consequences of
  decision making.

* Classic solution (Bellman) is to reduce the search to local choice (i.e.
  myopically choose the best action in your current state by propagating back
  information from future states).

    * Plans to maximum horizon (i.e. you consider discounted reward) but the
      policy acts at a minimum horizon (i.e. you only choose the next action).
      Thus the value function has to compile all future search down to this
      minimal horizon.

    * "An endless source of distraction in RL"

* An alternative is to define both a short term and long term horizon (tactical
  vs strategic horizon) instead of assuming your tactical horizon is one action
  and your strategic horizon is infinite as in the classical case.

    * Allows you to leverage search in decision making and reduce complexity of
      the strategic compilation process.

    * If you make your tactical and strategic horizon equal, you greatly
      simplify the function you're trying to learn

    * Some problems (e.g. underactuated pendulum) need longer tactical horizon
      so you can make locally "bad" moves that put you on a better long term
      path.

* Takeaway: tactical proficiency does not always automatically emerge from
  maximum-horizon strategic optimality (or it can take a very long time to
  emerge).

  * Reasoning horizons other than the default that falls out of Bellmans may
    not always be appropriate

  * Looks a bit like hierarchical RL - learning how to solve subproblems and
    how to combine those solutions smartly.


### Conclusion

* Isolating and understanding subproblems in RL is a fruitful approach toward
  better understanding and more robust algorithms.

### Interesting Ideas

* This may not have been the exact intent when mentioned in the lecture, but
  conceptualizing the approximation of V or Q function as compilation of future
  discounted reward down to something useful for myopic decision making is
  something I should think more about!
