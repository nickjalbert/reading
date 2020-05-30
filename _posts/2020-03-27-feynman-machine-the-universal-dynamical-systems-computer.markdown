---
layout: post
title:  "Feynman Machine: The Universal Dynamical Systems Computer"
date:   2020-03-27 12:00:00 -0700
paper-url: https://arxiv.org/abs/1609.03971
paper-authors:
  - Eric Laukien
  - Richard Crowder
  - Fergal Byrne
author: Nick Jalbert
---

Introduce Feynman Machines, a universal computer paradigms for
dynamical systems (vs Turing machines, a universal computer for
symbolic systems).  Claim that hierarchies of interacting dynamical
systems closely resemble what's going on in the mammalian context.

* TODO: Theorem of Floris Takens - models derived from time series
  signals are essentially true analogues of the system producing the
  signals.

Science is the study of things that change over time, a search for
rules and laws which describe their structure and evolution over
time, and is based on the premise that the world is lawful and its
rules are discoverable.

* Dynamical system -- a system governed by express update rules
  (either continuous or discrete)

* Lorenz atmospheric convection model - an example of a dynamical
  system (3 coupled differential equations) that exhibits
  deterministic chaos; the further out in the future you want to
  predict the state, the more precise your initial measurements of
  the system must be.

* Takens theorem - a model constructed from a time series is
  fundamentally the same as the system being observed
  (diffeomorphic).

Feynman Machine is divided into regions.  Each region has a
visible/downward and an hidden/upward face.  Each face has inputs and
outputs.

* visible/downward input - sensorimotor data from lower regions

* visible/downward output - predictions of future inputs
  (alternatively, control/behavior/feedback/routing signals)

* hidden/upward input - receives predictions of future inputs from
  higher regions

* hidden/upward output - encodings of the sensorimotor data received
  from the visible input

Each region is wired up with internal recurrent channels.  Hidden
output is combined with hidden input to generate the visible output.
This is compared with the visible input and the error is used to
drive learning.

In implementation, this looks like a hierarchy of paired encoders and
decoders (predictors).  Each one attempts to predict the state of the
predictors below it one time step in advance.  This drives learning.

They then go into detail about the specific encoder/decoder they
implement (Spatiotemporal K-sparse autoencoder) and discuss several
benchmarks that they've gotten good results on with lower compute
requirements.

* TODO - Friston on free energy
* TODO - Jeff Hawkins, On Intelligence and follow-on work
* TODO - Autoencoders
* TODO - AIXI model

**THOUGHTS:** This reads a lot like a white paper.  We would be
interested in more details of their evaluation. Still intriguing, and
harmonizes with a lot of what is coming out of the neuroscience world
(e.g see Clark's Surfing Uncertainty), esp. because we found them
because they were getting interesting results training and running on
a Raspberry Pi.
