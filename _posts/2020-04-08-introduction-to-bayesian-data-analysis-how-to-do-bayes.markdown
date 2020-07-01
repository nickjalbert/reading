---
layout: post
title:  "Introduction to Bayesian data analysis, Part 3: How to do Bayes?"
date:   2020-04-08 12:06:00 -0700
paper-url: https://www.youtube.com/watch?v=Ie-6H_r7I5A
paper-year: 2017
paper-authors:
  - Rasmus Bååth
author: Nick Jalbert
---

* How to actual use Bayes in practice:  Approximate Bayesian computation (as
  we did in part 1 and 2) is slow.  Faster models all require that the
  generative model allows you to directly calculate the probability of seeing
  a particular result.  Faster models also explore the parameter space in a
  smarter way.

* relates Bayes to maximum likelihood estimation

* I find the model at time 5:30 a bit confusing.  My guess is that `y` is
  sampled from a normal distribution where the mean of the distribution is
  determined by `intercept + slope * x` and the stddev is held constant.  So,
  to generate a y, you select an x, plug it into the line equation to get the
  mean, and then sample for the normal with the determined mean (and chosen
  stddev).  Presumably, the sampling of the normal represents noise in the
  process.

* "Now this is a generative model, but it is not yet a Bayesian model.  For
  that, we need to represent all uncertainty by probability, and add prior
  distributions over all parameters.

* Result of Bayesian linear regression gives you an idea of how likely the
  various parameters are to have generated the data.

* TODO: find another explanation of a Bayesian approach to linear regression.

* Markov Chain Monte Carlo (MCMC) allows for exploration of complicated parameter
  spaces.  They walk around the parameter space and sample from the probability
  distributions.  They will revisit and sample each parameter set in proportion
  to how likely it is (to have generated the data).

* Stan is a language for Bayesian modelling.  You define your model in Stan and
  then it takes cares of fitting it.

* Things that can go wrong in MCMC: initial parameter values are way off, our
  algorithm doesn't have enough time to explore the parameter space, algorithm
  gets stuck at a local maximum.  Very similar to optimization.
