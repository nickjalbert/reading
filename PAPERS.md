## [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)

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

They then discuss anecdotal evidence for univesality--that there are some
features that re-appear again and again in neural nets (e.g. edge detection).
Strong universality might guide the nature of future interpretability  research.

TODO--in the glossary there are a bunch of related articles that seem useful,
including:

* [Feature Visualization (2017)](https://distill.pub/2017/feature-visualization/)
* [The Building Blocks of Interpretability (2018)](https://distill.pub/2018/building-blocks/)
* [Exploring Neural Networks with Activation Atlases (2019)](https://distill.pub/2019/activation-atlas/)
