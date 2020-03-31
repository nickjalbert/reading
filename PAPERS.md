## [Six views of embodied cognition](https://cogdev.sitehost.iu.edu/labwork/WilsonSixViewsofEmbodiedCog.pdf)
### Margaret Wilson

Overview of the notion that cognitive processes are deeply rooted in the body's
interaction with the world.  Specific claims examined:

* Cognition is situated - it takes place in a real world environment and is
  inherently contextual.

* Cognition is time pressured - the limits imposed by the real-time nature of
  cognition inherently shape the process.

* We offload cognitive work onto the environment - due to resource
  limitations, we offload cognition to the environment.

* The environment is part of the cognitive system - the link between mind and
  environment is so high-bandwidth that it doesn't make sense to study the mind
  separate from the environment (note: this claim is described as "deeply
  problematic" in the abstract).

* Cognition is for action - if cognition is for controlling our biological
  body, it must be understood in the context of performing actions.

* Offline cognition is body based - because the mind evolved contextually with
  the environment, even "abstract" thought hijacks sensorimotor facilities for
  cognition.

Notes there are (at least) two schools in the philosophy of mind/cognitive
sciences: the mind is an abstract information processor and sensorimotor
inputs/outputs are peripheral.  Alternatively, brains are control systems for
biological bodies and thus sensorimotor processing is intimately tied to
cognition.

A deeper examination of the claims:

#### Cognition is situated

A distinction is drawn between situated and unsituated cognition.  The former
is the cognition that happens as you do a task (e.g. hunting an animal), the
latter is the cognition that happens when you plan or daydream. These might be
variations on a theme (i.e. see the body-based cognition claim).

The author concludes that the argument that all important cognition is situated
(or rooted in situatedness) isn't strongly persuasive.  I feel a lot of this is
splitting hairs on definitions of particular technical terms.

#### Cognition is time pressured

This claim is, roughly, that the time pressure involved in situated cognition
is one of the primary shaping forces of cognition.  Brains evolved to, for
example, help us flee predators as they jump out of bushes and this deeply
influences how evolution shaped our cognitive processes.

Definition: representational bottleneck - time pressure causes a bottleneck
which forces us to rely on heuristic tricks

To temper this claim, a lot of what we identify as human cognition is not
aggressively time constrained.  For example, we do some of our best,
recognizably-human work when we can sit and reflect and plan.

It is noted that spatiotemporal and movement behaviors are probably deeply
influenced by time constraints.  However, the author is unpersuaded that this
can be "scaled up" and applied usefully to all of cognition.

#### We offload cognitive work to the environment

This is using the environment to work around real-time representational
bottlenecks.  This is distinct from offloading to prevent memorizing (e.g.
using a calendar) although they are sometimes conflated in the literature.

This, for example, could be moving furniture around a room to see how it looks
rather than trying to imagine how it would look.  This is also referred to as
"using the world as its own best model".

The author notes that it seems we use the environment for both time-pressured
situated tasks as well as unsituated tasks and that this may have far reaching
consequences for how we think about cognition.

#### The environment is part of the cognitive system

A stronger claim than previous; if we use the environment to offload
processing then the environment should always be considered a part of
cognition.

Alternatively, directly from the paper: "The claim is this: The forces that
drive cognitive activity do not reside solely inside the head of the
individual, but instead are distributed across the individual and the situation
as they interact. Therefore, to understand cognition we must study the
situation and the situated cognizer together as a single, unified system."

The author claims that causes of cognition are undeniably environmental and
internal, but that shouldn't necessarily constrain the examination of cognition
as a modular process.  The issue ends up being "how best to carve nature at its
joints" and depends deeply on what you're studying and what you're trying to
get out of the study.

The author gives the example of hydrogen from chemistry. Before there was a
theory of an atom, much was known about how hydrogen reacts in many different
situations.  As atomic theory was developed though, so was a useful
understanding of hydrogen as something unto itself.  Both lines of research
were fertile.

#### Cognition is for action

The proposal here is that memory shouldn't be viewed as a tool for recording
abstract information, but rather a tool for encoding patterns of possible
action in a 4D world.  

This claim is tempered by the fact that we remember things that we cannot
directly interact with (e.g. sunsets are mentioned, even though we do look at
them).  More broadly, there is suggestion that there different types of memory.
Some are more closely coupled with action and others are more abstract.

The other tempering fact is that it seems we often build up richer
representation of objects beyond the here-and-now usefulness. For example, the
piano that is a musical instrument that becomes firewood once the blizzard
strikes.  The representations allow us to be creative when the environment
changes.

#### Offline cognition is body based

The claim is that we hijack our sensorimotor tools to do other, higher-levels
of cognition. Examples include mental imagery, different types of
sensory-linked working memory, episodic memories, etc.

Excerpts from the paper's conclusion: 

* "One benefit of greater specificity [of the claims around embodied cognition]
  is the ability to distinguish on-line aspects of embodied cognition from
  off-line aspects."

* In online, situated cases of cognition, "the mind can be seen as operating to
  serve the needs of a body interacting with a real-world situation."  Issues
  of time pressure may come into play.  We should be careful, however, in
  scaling up the processes that come into play to explain all of cognition.


* In offline, unsituated forms of cognition, "rather than the mind operating to
  serve the body, we find the body (or its control systems) serving the mind.
  This takeover by the mind, and the concomitant ability to mentally represent
  what is distant in time or space, may have been one of the driving forces
  behind the runaway train of human intelligence that separated us from other
  hominids."


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
