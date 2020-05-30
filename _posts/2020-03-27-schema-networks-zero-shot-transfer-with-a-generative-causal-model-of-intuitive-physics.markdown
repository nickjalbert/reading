---
layout: post
title:  "Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics"
date:   2020-03-27 12:01:00 -0700
paper-url: https://arxiv.org/abs/1706.04317
paper-authors:
  - Ken Kansky
  - Tom Silver
  - David A. Mély
  - Mohamed Eldawy
  - Miguel Lázaro-Gredilla
  - Xinghua Lou
  - Nimrod Dorfman
  - Szymon Sidor
  - Scott Phoenix
  - Dileep George
author: Nick Jalbert
---

Examines transfer learning using the game of Breakout as an example.
Current state-of-the-art RL techniques can learn to play Breakout
very well.  However, minor modifications to the game rules (e.g.
changing size or shape of paddle, changing how the bricks react) to
which humans can easily adapt will break deep neural net based
agents.

Techniques like model-free DQN make no assumption about the domain.
This makes it useful for one off tasks but it can overfit the
particulars of the domain and limit its ability to generalize to
closely related (in human terms) domains.  Object-based and
relational representations have been explored to address this
limitation.  This paper throws causality into the mix by introducing
Schema Networks – a generative model for object-oriented
reinforcement learning and planning.

* NOTE: they mention reasoning backward from an objective in order to
  plan.  Very similar to one of the heuristics in the RAND paper.

* NOTE: might want to explore more from the related work section

The basics of their model is that there are **entities** (e.g.
objects parsed from an image input), each of these entities have
**attributes** and each of the attributes have a value.  Then there
are **schemas** which capture the relationship between entities,
entity attributes, actions, and rewards over time. An example of this
is Entity 1's position attribute at timestep 5 may be predicated on
Entity 1's position attribute at timestep 4 and taking the "UP"
action.

They distinguish between **ungrounded schema** and **grounded
schema**. An ungrounded schema is a template that expresses a
relationship (e.g. action "UP" on an entity will increase its
position attribute), and a grounded schema is a particular
instantiation of an ungrounded (e.g. action "UP" on Entity 1 will
increase its position attribute to 5).

They then extend the standard MDP formalism so that a given state
simply consists of the set of all entities and their particular
attribute values.  Then schemas can be placed upon all the attributes
in the entities in a given state to predict their next values.  Each
schema is a set of AND'd preconditions.  And each attribute value can
be predicted by multiple schema OR'd together.  The OR-ing of
multiple schemas allow explicit reasoning about multiple causation.

* TODO: lookup object-oriented MDPs and relational MDPs

Now, we must figure out how to **learn** a schema network and then
use it for **planning**.

There is some magic pre-processing that picks out entities.  Then
they represent the current state using a neighbor-based algorithm
(seemingly to capture entities which are nearby each other).  They
use epsilon-greedy exploration algorithm.

To learn the structure of the Schema Network, they "cast the problem
as a supervised learning problem over a discrete space of
parameterizations (the schemas),  and then apply a greedy algorithm
that solves a sequence of LP relaxations."  This seems like a
probably-well-understood method of learning.  A key balance they're
trying to strike is to both minimize prediction error WHILE
minimizing the complexity of the schema network.  The general problem
is NP-hard, so they use a greedy approximation method to generate a
solution.

Once they learn a Schema Network, they then use it for planning to
get to a desired state (e.g. collect positive rewards, avoid negative
rewards). They do this by (roughly):

* Working forward in their model for T time steps to figure out
  reachable states.
* Choosing the reachable state with the best reward.
* Backtracking to confirm its the chosen state's reachability and
  discover the set of actions that will maximize the chance of
  reaching that state.

They then compare Schema Networks to A3C and Progressive Networks
(PNs) on several variations of Breakout.  They show that Schema
Networks transfer their learning much faster than A3C or PNs to
different variants of Breakout.  They then show that Schema Networks
can adapt to variants of the game (that exhibit the same dynamics)
much better than A3C or PNs (e.g. when paddle is offset by N pixels)
in a zero-shot setting (i.e. train only on regular breakout and then
have it play the variant).

From the conclusion: "Instead of learning policies to maximize
rewards, the learning objective for Schema Networks is designed to
understand causality within these environments.  The fact that Schema
Networks are able to achieve rewards more efficiently than
state-of-the-art model-free methods like A3C is all the more notable,
since high scores are a byproduct of learning an accurate model of
the game."

**THOUGHTS:** Interesting whirlwind tour of the PGM world and how one
might try to learn higher-level models.  Don't have enough background
to evaluate how novel or effective this particular technique is, but
seems promising from their results. A lot of pointers to work worth
following up on (e.g. OO-MDPs, PGMs in general, MAP/MBPB, planning,
etc)
