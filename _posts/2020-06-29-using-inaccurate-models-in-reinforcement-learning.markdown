---
layout: post
title:  "Using Inaccurate Models in Reinforcement Learning (2006)"
date:   2020-06-29 12:07:00 -0400
paper-url: https://ai.stanford.edu/~ang/papers/icml06-usinginaccuratemodelsinrl.pdf
paper-authors:
  - Pieter Abbeel
  - Morgan Quigley
  - Andrew Y. Ng
author: Nick Jalbert
---

This paper proposes an algorithm to integrate an agent's experience in an
environment with an internal (potentially inaccurate) model of that environment
in a way that both improves the model and the agent's policy.  Essentially, the
agent integrates its experience into its model, and improves its policy on the
model before attempting another real-life trial.

The motivating example discussed is learning to drive.  When we learn to make a
left turn, for example, perhaps we oversteer and turn too far.  Even if we only
have have a very rough, approximate model of the car in our head, we can still
learn to correct our oversteering without making the same mistake over and
over.

A major limitation of this technique is that it requires a deterministic Markov
decision process (MDP). Specifically, given a state, action, and time (this
paper examines non-stationary, continuous-state, continuous-action MDPs) the
resulting state should be deterministic.

The core algorithm works on an approximate MDP
$$\hat{M}^0 = (S, A, \hat{T}^0, H, s_0, R)$$ where:

* $$S$$ is a set of states
* $$A$$ is a set of actions
* $$\hat{T}^0$$ is an approximate transition model of the environment
* $$H$$ is a time horizon (the max number of steps)
* $$s_0$$ is an initial state
* $$R$$ is the reward function

We assume we have some initial policy $$\pi_\theta^0$$ parameterized by
$$\theta$$ and a policy improvement algorithm $$A$$. We assume there exists a
true MDP that models the process we're trying to learn $$M=(S,A,T,H,s_0,R)$$.
The algorithm proceeds as follows:

1. Run our policy improvement algorithm $$A$$ on our initial approximate MDP
   $$\hat{M}^0$$ and policy $$\pi_\theta^0$$ to get $$\pi_\theta^1$$.
2. Execute our policy $$\pi_\theta^1$$ on the real MDP $$M_{}$$ to get a real
   state-action trajectory
3. Update our approximate MDP's model $$\hat{T}^0$$ such that the it will
   produce the trajectory we just observed in $$M$$.  This gives us
   $$\hat{T}^1$$ and an updated approximate MDP $$\hat{M}^1$$.
4. Use the updated approximate MDP $$\hat{M}^1$$ and the policy improvement
   algorithm to find the gradient direction that will improve the performance
   of $$\pi_\theta^1$$ and use this gradient to get $$\pi_\theta^2$$.
6. Go back to step 2 if an improvement is found, otherwise terminate.


The paper then goes on to prove some theoretic properties of the algorithm and
show its utility in a flight simulator and as a controller for an RC car.  The
key observation is that the model continues to improve as training runs
increase and this allows the algorithm to be more sample efficient when
interacting with the real MDP.
