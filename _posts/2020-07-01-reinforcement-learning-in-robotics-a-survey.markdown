---
layout: post
title:  "Reinforcement Learning in Robotics: A Survey"
date:   2020-07-01 12:07:00 -0400
paper-url: https://dl.acm.org/doi/10.1177/0278364913495721
paper-year: 2013
work-in-progress: true
paper-authors:
  - Jens Kober
  - J. Andrew Bagnell
  - Jan Peters
author: Nick Jalbert
---

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

#### Value Function-Based RL

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

#### Policy Search RL

* Policy search has a number of features that make it amenable to robotics:
  * It allows for integration of expert knowledge
  * It allows for pre-structured policies
  * An optimal policy will often have fewer parameters than an optimal
    value-function
  * Local policy search can often lead to good results
  * External constraints can be incorporated naturally


* In general, policy search will optimize a given policy $$\pi$$ parameterized
  by $$\theta$$ by iteratively calculating the parameter gradient
  $$\nabla\theta$$ that will increase the expected return:
  $$\theta_{i+1} = \theta_i + \nabla\theta_i$$

* Calculation of the policy update is the key differentiator between
  algorithms, and generally comes in two flavors:
  *  *Black box methods* -  These methods do not leverage the internal
     structure of the problem, instead relying on sampling to estimate the
     gradient.
  *  *White box methods* - These methods take advantage of specifics of the
     problem to calculate policy updates.  This includes model-based
     approaches.

* Following the gradient of the expected return $$J$$, that is
  $$\theta_{i+1} = \theta_i + \alpha\nabla_\theta J_{}$$, is a white box
  method that has proven particularly useful in a lot of research work.
  This gradient can be estimated using finite difference methods perturbing
  $$\theta$$, REINFORCE or likelihood ratio methods, expectation-maximization
  methods, or dynamic programming methods.

#### Policy Search vs Value Functions

* Value functions are difficult to translate to robotics because the
  high-dimensional spaces require function approximation out of the box. These
  approximations are often brittle and expensive.

* Value functions require total coverage of the state space and the largest
  local error determines the quality of the policy.  Additionally, small
  changes in the value function can result in large changes in the policy that
  then feedback into the value function.  This can result in expensive
  recalculations as well as instability.

* Policy search often considers only local changes and thus is more amenable to
  high dimensional spaces.  It, however, risks getting caught at local optima.

* Terminology: policy search methods are sometimes called **actor methods**,
  while value function search methods are sometimes called **critic methods**.
  These can be combined to form **actor-critic methods** where the policy
  is used to guide action while the value function is used to decide when
  to update the policy.

#### Function Approximation

* Typically in RL, function approximation is based on experience collected by
  interacting with the environment.

* Function approximation is critical in continuous-space problems and often
  needed even in large discrete-space problems to generalize behavior to
  similar states.

* There are many flavors of function approximation and these approximators can
  be used to represent policies, value functions, and/or models.
  * *Parametric approximators* have a fixed set of parameters and are used to
    fit observed data.  Examples include neural nets and linear basis
    functions.
  * *Non-parametric approximators* expand representational power in proportion
    to the data collected.  Gaussian process regression is an example.

* One general problem of using function approximation techniques developed in
  the supervised learning world is that they often assume independently and
  identically distributed data.  This is often not feasible in RL settings
  because the data is often path-dependent and that path can be influenced by
  the function approximator itself.


### 3. Challenges in Robot Reinforcement Learning

Robotics is a challenging arena for reinforcement learning:
* Continuous state spaces and actions must be represented; do you discretize or
  approximate?  How fine-grained should your controls be?  How much
  dimensionality can your learning algorithm handle?
* The physicality is difficult: samples are expensive, there's jitter and
  uncertainty in real world system, there's maintenance, sometimes a system
  needs to be manually reset, algorithms must run in real-time.
* Simulation can alleviate some problems with physicality, but must be robust
  to model errors.
* Goal specification (in the form of specifying a reward function) often
  requires some thought.

#### The Curse of Dimensionality

* As the number of dimensions grow in a state or action space, the amount of
  data needed to cover it grows exponentially.
* The high degree of freedom in many robotic assemblies naturally leads to this
  curse of dimensionality.
* One approach is to impose a hierarchy: e.g. the robot plans at the grid level
  and then lower-level systems produce motion unaware of the grid.
* Dimensionality reduction can often limit the dynamic capabilities of a robot.

#### The Curse of Real-World Samples

* Robots are expensive and repairs take time and money.  Safe exploration is an
  understudied field.
* Often the environment is not fully captured by the state space, and thus
  learning may not converge as conditions change (e.g. a strong wind affecting
  the mobility of a robot).
* Often human involvement is needed to reset a robot so it can re-sample the
  environment.  This is slow and expensive.  Sample efficiency is important to
  ameliorate this.
* Real time requirements can complicate the sampling and learning procedures.
* Time discretization and variable signal processing delays can affect the
  ability to learn and control a robot.

#### The Curse of Under-Modeling and Uncertainty

* Modeling can be used to ameliorate some of the difficulties of the physical
  world, but brings its own issues.
* Model errors can compound and thus make behavior transfer difficult
* Tasks that are self-stabilizing (e.g. the robot doesn't need to actively
  control itself to avoid crash-and-burn) allow for better transfer of modelled
  learning.  This is less true for tasks that require constant control (e.g.
  pole-balancing).

#### The Curse of Goal Specification

* Goals are implicitly specified by the reward function.  Crafting a good
  reward function is often non-trivial.
* Variance in reward must be able to be leveraged to improve the policy,
  otherwise no learning will occur.
* A sparse reward can be overly difficult for a robot to use as a learning cue
  so sometimes intermediate rewards will be added.
* The difficulty of programming the control algorithm is partially transferred
  to the shaping of the reward.
* Inverse optimal control - trying to learn a reward function from a series of
  expert demonstrations.

### 4. Tractability Through Representation

* Success in robotics RL has been achieved by leveraging:
    * Effective representations
    * Approximate models
    * Prior knowledge

#### Smart State-Action Discretization

* Hand crafted discretization is the standard.  Care is taken to balance
  expressiveness against state space reduction.

* One can also attempt to automatically learn a discretization.  This seemingly
  complicates the task because you are optimizing the state representation AND
  the learning performance simultaneously.

* Meta-actions/options - automatically constructing high-level actions has
  "fascinated" RL researchers.  A number of success have been demonstrated in
  the hierarchical RL space, although most seem to occur in fairly constrained
  environments and/or on toy tasks.

#### Value Function Approximation


* Function approximation can be used to model the value function OR to model
  the system.

* Unfortunately, unstable behavior and divergence is often observed in practice
  when using function approximators (some linear models are immune to this,
  though).

* If good features are known, value function approximation can use a linear
  approximator. However, this relies on the quality of the features and is not
  a general solution (in fact, it can make some problems impossible).

* Neural nets have (unsurprisingly) shown to be useful for some tasks, but
  obviously divergence must be contended with.

* Other tactics:
    * Generalization heuristics for neighboring states
    * Using local models for particular parts of the state space
    * Gaussian methods (Gaussian Process Regression)

#### Pre-structured Policies

* Picking a good approximator to represent the policy is important.  For
  example, trade-offs between speed of learning and representational power
  might be considered.

* Depending on the task, a number of different approximators might be
  appropriate.  Researchers have seen success using:
  * Linear models
  * Motor primitives
  * Gaussian mixture models
  * Neural nets
  * Non parametric approximators


### 5. Tractibility through Prior Knowledge

* Incorporating prior knowledge can constrain the search space and dramatically
  increase the ability to learn effective policies.  This prior knowledge
  can look like:
  * Initial policies
  * Demonstrations
  * Initial models
  * Physical constraints (e.g. torque limits)

* Sometimes hard constraints (such as ones designed to protect robot hardware)
  pose difficulties for standard RL algos (i.e. hitting a discontinuous wall)

#### Prior Knowledge Through Demonstration

* People and animals often learn from imitation as well as trial and error.  In
  the RL world, this is termed imitation and/or apprenticeship learning.

* Demonstrations can remove the need for global exploration (i.e. by telling
  the learner the critical states to focus on) and allow for much less
  expensive local optimization.   Learning a good global solution, however,
  requires a good demonstration (see "Fosbury Flop" in Olympic High Jump).

* Both value function and policy search methods seem to work best in practice
  when they're constrained to making small changes to the distribution over
  states while learning.

* When teaching a robot, the teacher can either demonstrate directly or control
  the robot.  Direct demonstration requires translation to "robot world" while
  controlling the robot requires the teacher learning how to control it.

* When teaching is not straightforward, a hard-coded policy can be used as
  demonstration.  This has been shown to work in robotic walking tasks.

#### Prior Knowledge Through Task Structuring

* Decomposing tasks into simpler tasks (as in Hierarchical RL) and composing
  simpler tasks into more complicated actions can both be used to learn better
  policies.


#### Directing Exploration with Prior Knowledge

* Prior knowledge can be used to fine tune the trade-off between exploration
  and exploitation and increase overall reward.


### 6. Tractability Through Models

* Many robotics RL problems can be made tractable by learning approximate
  models of the transition system (vs attempting to directly learn value
  function approximations or policies from live interaction).

* It is desirable to build a model esp. because simulation or rehearsal is
  much faster than gathering actual experience in the physical world.

#### Core Issues and General Techniques

* Model-based methods that learn a model from data can be much more sample
  efficient.  However, there can be problems with:
    * Expansive compute resource requirements
    * Simulation biases
    * Real world stochasticity
    * Difficulties sampling from the simulator

**Simulation Biases**

* Any simulation will not capture all the dynamics of the real world.  If these
  dynamics are important to the task, then this can break the learning
  algorithm and generate policies that work in the simulator but not in the
  real world.

* An interesting distinction is the type of simulator errors that compound vs
  non-compounding errors.

* Adding noise to the model can help reduce tendencies to overfit policies to
  quirks of the simulator.

* Uncertainties about environmental dynamics maintained in the model
  itself can be leveraged to create policies that generalize better.

* Tricks around model randomization have also proven to be useful.

#### Successful Approaches for Learning Forward Models

How can we obtain a candidate policy from a forward model?

* Rollouts using the model can be used to calculate rough gradients to update
  policies or learn approximate value functions.

* The model can be directly interrogated to generate plausible policies using
  techniques from control systems research.

### 7. A Case Study: Ball-in-a-Cup

* This section describes a case study of teaching a robot to catch a ball in a
  cup.  The cup is held in one hand, the ball is attached to the bottom of the
  cup with a string, and initially the ball is at a dead hang under the cup.
  The cup is quickly moved to fling the ball above the cup and then caught with
  the cup.

* The naive rendering of the scenario would have an intractable-for-RL ~20
  state and ~7 action dimensions.

* Reward shaping is important: the "catch the ball"-only reward was too sparse
  to learn effectively.  The "closeness to cup" reward got stuck in local
  minimums (hitting the ball with the cup edge).

* Creating a faithful simulator is difficult.

* The policy is represented as a dynamical system of motor primitives.  Over
  the course of successive research projects, the policy representation was
  distilled.  The particular policy representation choice has the nice property
  that it is easy to include knowledge learned from demonstration.

* An initial demonstration was done by having a human directly manipulate the
  robot arm.  RL was then used to search the local space "around" the
  demonstrated movement to optimize.

* Policy search methods are better suited for episodic tasks that need local
  optimization (thanks to the demo) with a large, high-dimensional state/action
  space.  An EM method was employed instead of a gradient based method to be
  more sample efficient and require less hyperparameter tuning.  This algorithm
  performs a local search around the demonstrated policy.

* They used a simulator for rehearsal training, but often a good simulator
  policy would just miss getting the ball into the cup.  Thus the ability to
  switch between the simulator and the physical system and incorporate data
  from both was important.

* Getting data from the physical system was slow and tedious.

* Ultimately, the policy converged and the robot was regularly able to get the
  ball into the cup after ~100 episodes.

* A different value-function-based approach was also tested (perhaps by another
  team?) where the task was decomposed into two separate phases (swing-up and
  catch).  The catch phase was hard coded, but a swing-up policy was learned
  using SARSA and state-action discretization.

### 8. Discussion


**TODO**
