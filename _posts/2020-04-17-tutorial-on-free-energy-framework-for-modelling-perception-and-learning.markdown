---
layout: post
title:  "A tutorial on the free-energy framework for modelling perception and learning"
date:   2020-04-17 12:07:00 -0700
paper-url: https://www.sciencedirect.com/science/article/pii/S0022249615000759
paper-year: 2017
paper-authors:
  - Rafal Bogacz
author: Nick Jalbert
---

* The predictive coding model provides a biologically-plausible account of how
  organisms infer stimuli from noisy inputs.  Introduced by Rao and Ballard
  in 1999.  Friston extended the model in 2005 to also learn uncertainty
  associated with different features (e.g. attentional mechanism).  Friston's
  model can also be viewed as approximate Bayesian inference based on a
  minimization of free energy.

* This paper provides a tutorial that aims to be broadly accessible to a
  technical audience.

* Conditions for a model to be biological plausible:
    * Local computation - each neuron need only know about its inputs and
      outputs.
    * Local plasticity - localized changes can be used to train the model.

* We start with a problem: a single organism is trying to infer the diameter
  of a food item on the basis of observed light intensity from one noisy light
  receptor.  There exists a non-linear function $$g$$ relating average light
  intensity with size.

* Interesting to note: once distributions aren't standard (e.g. normal or
  otherwise well known) you can't represent them compactly with summary
  statistics.  It seems likely there has to be some sort of approximation
  going on in the brain.

* Also interesting: calculating the bayesian normalization term (the
  denominator) seems difficult for neural systems (also, not super
  straightforward for computer systems, either).

* Suggests that instead of find the whole posterior, we just find the most
  likely size of the food item given the sensor reading.  This is claimed to
  be much more plausible to implement in neural circuits.

* Importantly, the value that maximizes the likelihood ($$\phi$$) does not
  depend on the denominator so we can not consider it.  Take the natural log
  of the numerator $$p(u | \phi) * p(\phi)$$ to get 
  $$ln(p(u | \phi)) + ln(p(\phi))$$.

