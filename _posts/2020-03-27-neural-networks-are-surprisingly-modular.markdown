---
layout: post
title:  "Neural Networks are Surprisingly Modular"
date:   2020-03-27 12:02:00 -0700
paper-url: https://arxiv.org/abs/2003.04881
paper-year: 2020
paper-authors:
  - Daniel Filan
  - Shlomi Hod
  - Cody Wild 
  - Andrew Critch
  - Stuart Russell
author: Nick Jalbert
---

A look at the modularity of neural networks.  They develop a notion
of modularity.  Specifically, modules in neural nets are groups of
neurons that are highly connected internally and weakly connected
externally.

First experiment is to train a network on a classification task, and
then try to cluster modules.  Then they reshuffle the weights of the
network and again re-cluster.  They find that the generally trained
networks are more modular than the randomly shuffled ones.
Interestingly, though, CIFAR is not very modular by this metric (i.e.
the trained network tends to be LESS modular than the shuffled one).

They then try this experiment with dropout.  Dropout makes the
networks much more modular.

They then examine whether this modularity is a result of the
optimization algorithm (ADAM).  They show that running ADAM on an
unlearnable dataset does not result in a particularly modular network
(although they had some outliers on some of the longer training runs
that were very modular).

Similarly, they tried to memorize a small, random noise dataset.
They show that generally the networks that memorize the data are more
clusterable (although dropout seems to prevent this but also does not
learn the data).

They then do lesioning experiments where they "kill" certain modules.
They show that some of these modules end up being highly impactful in
the classification accuracy of the network.
