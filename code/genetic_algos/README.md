## Genetic Algorithms

The file `genetic.py` implements the genetic algorithm described in Such et
al.'s paper "Deep Neuroevolution: Genetic Algorithms are a Competitive
Alternative for Training Deep Neural Networks for Reinforcement Learning".
Run it using `python genetic.py` after installing the requirements by running
`pip install -r ../requirements.txt`

Highlights of the algorithm:
* We run for up to 1000 generations.
* We start with 10 randomly initialized densely connected sequential neural
  nets (4 input neurons to a 16 neuron relu layer to a 8 layer relu layer to a
  sigmoid output neuron which represents the probability of going left).
* For each generation, we instantiate 90 children neural nets which have the
  weights of the fittest nets from previous generations perturb by Gaussian
  noise.  We also port forward the 10 best performing nets from the previous
  generation (so each generation contains 100 nets).
* We evaluate each net in each generation on 10 runs of Cartpole, we take the
  mean reward of these 10 runs as the fitness of the net.
* We carry forward the 10 fittest nets to the next generation and instantiate
  new child nets from those fittest nets.


### Results

Running on commit #fba9cde, we observed the following results:

TODO
