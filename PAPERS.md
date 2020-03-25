## [Feynman Machine: The Universal Dynamical Systems Computer](https://arxiv.org/abs/1609.03971)
### Eric Laukien, Richard Crowder, Fergal Byrne

Introduce Feynman Machines, a universal computer paradigms for dynamical
systems (vs Turing machines, a universal computer for symbolic systems).  Claim
that hierarchies of interacting dynamical systems closely resemble what's going
on in the mammalian context.

* TODO: Theorem of Floris Takens - models derived from time series signals are
  essentially true analogues of the system producing the signals.

Science is the study of things that change over time, a search for rules and
laws which describe their structure and evolution over time, and is based on
the premise that the world is lawful and its rules are discoverable. 

* Dynamical system -- a system governed by express update rules (either
  continuous or discrete)

* Lorenz atmospheric convection model - an example of a dynamical system (3
  coupled differential equations) that exhibits deterministic chaos; the
  further out in the future you want to predict the state, the more precise
  your initial measurements of the system must be.

* Takens theorem - a model constructed from a time series is fundamentally
  the same as the system being observed (diffeomorphic).

Feynman Machine is divided into regions.  Each region has a visible/downward
and an hidden/upward face.  Each face has inputs and outputs.

* visible/downward input - sensorimotor data from lower regions

* visible/downward output - predictions of future inputs (alternatively,
  control/behavior/feedback/routing signals)

* hidden/upward input - receives predictions of future inputs from higher
  regions 

* hidden/upward output - encodings of the sensorimotor data received from the
  visible input

Each region is wired up with internal recurrent channels.  Hidden output is
combined with hidden input to generate the visible output.  This is compared
with the visible input and the error is used to drive learning.

In implementation, this looks like a hierarchy of paired encoders and decoders
(predictors).  Each one attempts to predict the state of the predictors below
it one time step in advance.  This drives learning.

They then go into detail about the specific encoder/decoder they implement
(Spatiotemporal K-sparse autoencoder) and discuss several benchmarks that
they've gotten good results on with lower compute requirements.

* TODO - Friston on free energy
* TODO - Jeff Hawkins, On Intelligence and follow-on work
* TODO - Autoencoders
* TODO - AIXI model


## [Neural Networks are Surprisingly Modular](https://arxiv.org/abs/2003.04881)
### Daniel Filan, Shlomi Hod, Cody Wild, Andrew Critch, Stuart Russell

A look at the modularity of neural networks.  They develop a notion of
modularity.  Specifically, modules in neural nets are groups of neurons that
are highly connected internally and weakly connected externally.

First experiment is to train a network on a classification task, and then try
to cluster modules.  Then they reshuffle the weights of the network and again
re-cluster.  They find that the generally trained networks are more modular than
the randomly shuffled ones. Interestingly, though, CIFAR is not very modular by
this metric (i.e. the trained network tends to be LESS modular than the
shuffled one).

They then try this experiment with dropout.  Dropout makes the networks much
more modular.

They then examine whether this modularity is a result of the optimization
algorithm (ADAM).  They show that running ADAM on an unlearnable dataset does
not result in a particularly modular network (although they had some outliers
on some of the longer training runs that were very modular).

Similarly, they tried to memorize a small, random noise dataset.  They show
that generally the networks that memorize the data are more clusterable
(although dropout seems to prevent this but also does not learn the data).

They then do lesioning experiments where they "kill" certain modules.  They
show that some of these modules end up being highly impactful in the
classification accuracy of the network.


## [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)
### Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, Shan Carter

Makes three speculative claims about the understandability of neural networks:

* Features - Features are the fundamental unit of neural networks (e.g. curve detectors).
* Circuits -  Features are connected by weights, forming circuits. A “circuit”
  is a computational subgraph of a neural network. It consists of a set of
  features, and the weighted edges that go between them in the original
  network.
* Universality - Analogous features and circuits form across models and tasks.

They claim all these can be examined manually and often understood.  One
interesting technique is they implement a curve detector feature by hand in a
neural net.

Also, however, note that neural networks often contain “polysemantic neurons”
that respond to multiple unrelated inputs. For example, InceptionV1 contains
one neuron that responds to cat faces, fronts of cars, and cat legs. 

Features build up into circuits.  They dig into a dog head detector that's
built up of smaller curve detectors and snout detectors and various connections
(both excitatory and inhibitory) between them.

They then highlight a case of superposition: a bunch of features feed into a
singular "car detector" neuron but then that neuron gets redistributed to a
bunch of other polysemantic neurons that detect dogs and cars.  From the
article: "Why would it do such a thing? We believe superposition allows the
model to use fewer neurons, conserving them for more important tasks. As long
as cars and dogs don’t co-occur, the model can accurately retrieve the dog
feature in a later layer, allowing it to store the feature without dedicating a
neuron".

They then discuss anecdotal evidence for universality--that there are some
features that re-appear again and again in neural nets (e.g. edge detection).
Strong universality might guide the nature of future interpretability  research.

**TODO** in the glossary there are a bunch of related articles that seem useful,
including:

* [Feature Visualization (2017)](https://distill.pub/2017/feature-visualization/)
* [The Building Blocks of Interpretability (2018)](https://distill.pub/2018/building-blocks/)
* [Exploring Neural Networks with Activation Atlases (2019)](https://distill.pub/2019/activation-atlas/)
