--
layout: post
title:  "Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems"
date:   2021-02-18 12:07:00 -0400
paper-url: https://arxiv.org/abs/2005.01643
paper-year: 2012
work-in-progress: true
paper-authors:
  - Sergey Levine
  - Aviral Kumar
  - George Tucker
  - Justin Fu
author: Nick Jalbert
---

### 1. Introduction

Classic reinforcement learning (RL) is fundamentally *online*.  The paradigm
generally involves an agent interacting with its environment to gain
experience; this experience is then later incorporated into the agent to
improve future interactions.

**Problem:** Sometimes it is expensive or dangerous to learn in an online
manner.  It's no good to have your driverless car speed off a cliff because it
hasn't figured out that cliffs are bad.

**Solution:** As in other areas of machine learning, it'd be ideal to throw a
ton of data about past interactions in an environment at the RL algorithms and
let them learn without (or with minimal) direct interaction with their
environment.  This data could ideally be simulated or gathered in some way that
doesn't require you to drive your autonomous car off the cliff.

The challenge, however, is reconciling this "stored data" vision (a.k.a.
offline RL) with the online nature of many classic RL algorithms.  The payoff
to tackling this challenge will be to usher in a new class of "decision making
engines" (in the same way that scaling up supervised learning ushered in a new
class of "pattern recognition engines").
