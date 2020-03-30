## [Six views of embodied cognition](https://cogdev.sitehost.iu.edu/labwork/WilsonSixViewsofEmbodiedCog.pdf)
### Margaret Wilson

## [Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics](https://arxiv.org/abs/1706.04317)
### Ken Kansky, Tom Silver, David A. Mély, Mohamed Eldawy, Miguel Lázaro-Gredilla, Xinghua Lou, Nimrod Dorfman, Szymon Sidor, Scott Phoenix, Dileep George

Examines transfer learning using the game of Breakout as an example.  Current
state-of-the-art RL techniques can learn to play Breakout very well.  However,
minor modifications to the game rules (e.g. changing size or shape of paddle,
changing how the bricks react) to which humans can easily adapt will break
deep neural net based agents.

Techniques like model-free DQN make no assumption about the domain. This makes
it useful for one off tasks but it can overfit the particulars of the domain
and limit its ability to generalize to closely related (in human terms)
domains.  Object-based and relational representations have been explored to
address this limitation.  This paper throws causality into the mix by
introducing Schema Networks – a generative model for object-oriented
reinforcement learning and planning.

* NOTE: they mention reasoning backward from an objective in order to plan.
  Very similar to one of the heuristics in the RAND paper.

* NOTE: might want to explore more from the related work section

The basics of their model is that there are **entities** (e.g. objects parsed from
an image input), each of these entities have **attributes** and each of the
attributes have a value.  Then there are **schemas** which capture the relationship
between entities, entity attributes, actions, and rewards over time. An example
of this is Entity 1's position attribute at timestep 5 may be predicated on
Entity 1's position attribute at timestep 4 and taking the "UP" action.

They distinguish between **ungrounded schema** and **grounded schema**. An
ungrounded schema is a template that expresses a relationship (e.g. action "UP"
on an entity will increase its position attribute), and a grounded schema is a
particular instantiation of an ungrounded (e.g. action "UP" on Entity 1 will
increase its position attribute to 5).

They then extend the standard MDP formalism so that a given state simply
consists of the set of all entities and their particular attribute values.
Then schemas can be placed upon all the attributes in the entities in a given
state to predict their next values.  Each schema is a set of AND'd
preconditions.  And each attribute value can be predicted by multiple schema
OR'd together.  The OR-ing of multiple schemas allow explicit reasoning about
multiple causation.

* TODO: lookup object-oriented MDPs and relational MDPs

Now, we must figure out how to **learn** a schema network and then use it for
**planning**.

There is some magic pre-processing that picks out entities.  Then they
represent the current state using a neighbor-based algorithm (seemingly to
capture entities which are nearby each other).  They use epsilon-greedy
exploration algorithm.

To learn the structure of the Schema Network, they "cast the problem as a
supervised learning problem over a discrete space of parameterizations (the
schemas),  and then apply a greedy algorithm that solves a sequence of LP
relaxations."  This seems like a probably-well-understood method of learning.
A key balance they're trying to strike is to both minimize prediction error
WHILE minimizing the complexity of the schema network.  The general problem is
NP-hard, so they use a greedy approximation method to generate a solution.

Once they learn a Schema Network, they then use it for planning to get to a
desired state (e.g. collect positive rewards, avoid negative rewards). They do
this by (roughly):

* Working forward in their model for T time steps to figure out reachable
  states.
* Choosing the reachable state with the best reward.
* Backtracking to confirm its the chosen state's reachability and discover the
  set of actions that will maximize the chance of reaching that state.

They then compare Schema Networks to A3C and Progressive Networks (PNs) on
several variations of Breakout.  They show that Schema Networks transfer their
learning much faster than A3C or PNs to different variants of Breakout.  They
then show that Schema Networks can adapt to variants of the game (that exhibit
the same dynamics) much better than A3C or PNs (e.g. when paddle is offset by N
pixels) in a zero-shot setting (i.e. train only on regular breakout and then
have it play the variant).

From the conclusion: "Instead of learning policies to maximize rewards, the
learning objective for Schema Networks is designed to understand causality
within these environments.  The fact that Schema Networks are able to achieve
rewards more efficiently than state-of-the-art model-free methods like A3C is
all the more notable, since high scores are a byproduct of learning an accurate
model of the game."

**THOUGHTS:** Interesting whirlwind tour of the PGM world and how one might try
to learn higher-level models.  Don't have enough background to evaluate how
novel or effective this particular technique is, but seems promising from their
results. A lot of pointers to work worth following up on (e.g. OO-MDPs, PGMs in
general, MAP/MBPB, planning, etc)


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

**THOUGHTS:** This reads a lot like a white paper.  We would be interested in
more details of their evaluation. Still intriguing, and harmonizes with a lot
of what is coming out of the neuroscience world (e.g see Clark's Surfing
Uncertainty), esp. because we found them because they were getting interesting
results training and running on a Raspberry Pi.

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
