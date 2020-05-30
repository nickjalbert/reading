---
layout: post
title:  "Introduction to Bayesian data analysis, Part 1: What is Bayes?"
date:   2020-04-08 12:04:00 -0700
paper-url: https://www.youtube.com/watch?v=3OJEae7Qb_o
paper-authors:
  - Rasmus Bååth
author: Nick Jalbert
---

Key insight here is you can think of Bayes as requiring:

* Some data
* A generative model
* Priors

The motivating example was a fish-of-the-month club.  You run an experiment
where 6 out of 16 people (data) sign up after receiving a brochure.  You want
to get an estimate of the true sign-up rate.  You model the sign up choice as
a binomial with some unknown **p** (generative model) and you don't have a strong
thought on what the actual sign up rate is (uniform prior between 0% and
100%).

We will generate our posterior "guess" of the actual **p** as follows
(Approximate Bayesian Computation):

* Pick a **p** from the prior (uniform so p=.1 and p=.9 are equally likely to
  be selected)

* Plug the selected **p** into a binomial model, simulate the binomial with
  n=16 and p=**p**

* If the proportion of "successful" flips in the simulation equals the 6 we
  observed in the data, count the trial as a success.

* Repeat thousands of times.

What you end up with is a posterior distribution of the **p**'s most likely to
generate the 6 out of 16 you saw.  This looks normal around 37.5%.  This is
Bayes in a nutshell.  You take your prior, gather some evidence, and update
your prior into the posterior to incorporate your evidence.

**THOUGHTS**: very useful video series to generate some Bayesian intuition.
