---
layout: post
title:  "Introduction to Bayesian data analysis, Part 2: Why use Bayes?"
date:   2020-04-08 12:05:00 -0700
paper-url: https://www.youtube.com/watch?v=mAUwjSo5TJE
paper-authors:
  - Rasmus Bååth
author: Nick Jalbert
---

This video illustrates how you might take a Bayesian approach to A/B testing.
The setup:

* We have our brochure experiment (method A) from before where 6 out of 16
  people signed up.
* We have a new experiment (brochure + sample, method B) where 10 out of 16
  people signed up.

We run the same algorithm from before to generate a posterior for method B.
Interestingly, you have to run the experiments in parallel and only keep the
results if both match (i.e. you draw a **p** from both priors, run the
simulation, and only keep the draws if both matched the observed data).  You
end up with a posterior distribution for both method A and method B.

What you also end up with is a set of rows where each row has two columns: the
chosen **p** for method A and the chosen **p** for method B that generated the
observed data. You can then add another processing step where you take the
difference between the two columns to get a third distribution and reason
about how likely it is that the true parameter for A is greater (or less than)
the true parameter for B.

Note, you can incorporate other information (e.g. expert opinion) in the
priors.  In the video, they model this using a beta distribution.  The
posterior ends up looking like a mix of the prior and the data.  The more data
you have, the more the posterior ends up looking like the data.

Bayesian analysis also retains the uncertainty around the estimated parameters
which can be useful for decision making. (Question: what if we're uncertain
about the generative model?).
