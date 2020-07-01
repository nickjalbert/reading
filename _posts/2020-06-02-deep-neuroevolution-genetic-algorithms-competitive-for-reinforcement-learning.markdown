---
layout: post
title:  "Deep Neuroevolution: Genetic Algorithms are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning"
date:   2020-06-02 12:07:00 -0700
paper-url: https://arxiv.org/pdf/1712.06567.pdf
paper-year: 2018
paper-authors:
  - Felipe Petroski Such
  - Vashisht Madhavan
  - Edoardo Conti
  - Joel Lehman
  - Kenneth O. Stanley
  - Jeff Clune
author: Nick Jalbert
---

* The goal of the paper is to compare non-gradient population-based genetic
  algorithms (GAs) to state of the art gradient-based algorithms such as deep
  neural nets (NNs), policy gradient, q-learning, and evolutionary strategies
  (ES) on difficult reinforcement learning tasks.

* Regarding general performance on the Atari benchmarks: 

  > While the GA always outperforms random search, interestingly we discovered
  > that in some Atari games random search outperforms powerful deep RL
  > algorithms (DQN on 3/13 games, A3C on 6/13, and ES on 3/13).

* The GAs they tested in this paper train using many fewer resources than
  current deep NN implementations.

* One of their conclusions is that gradient-based search impedes progress on
  some tasks and GAs or other gradient-free methods might be more appropriate
  for those domains.

* **TODO**: find out more about ES.  They don't calculate the gradient
  directly, but they approximate.

* A rundown of genetic algorithms as used in this paper:
  * GAs evolve a population $$P$$ of $$N$$ individuals over successive
    generations.
  * Each individual is a neural network parameter vector $$\theta$$.
  * Every individual $$\theta_i$$ gets a fitness score $$F(\theta_i)$$ each
    generation.
  * The top $$T$$ individuals become the parents for the next generation.
  * To produce the next generation, the following is done $$N-1$$ times:
    * A parent $$\theta$$ is selected uniformly at random
    * The parent is mutated by applying Gaussian noise $$\theta'=\theta +
      \sigma\epsilon$$ where $$\epsilon \sim \mathcal{N}(0,I)$$ (unclear how
      $$I$$ is determined, $$\sigma$$ is determined empirically).
    * The $$N^{th}$$ individual is the best performer from the previous
      generation ("elitism").  There is no crossover between parents.

* They introduce a compact representation for individuals: Rather than storing
  the whole vector $$\theta$$, they store the random seed used to generate
  $$\theta$$ and the seeds used to generate the Gaussian noise for each
  successive generation.
  * Size increases linearly with the number of generations (often thousands of
    generations) and it is independent of the size of $$\theta$$ itself (often
    millions of parameters).
  * This representation parallelizes well and can be used with CPUs instead of
    GPUs.

* They also test a variant of genetic algorithm novelty search (GA-NS).  In
  this algorithm, reward is ignored during evolution and novel behavior is
  rewarded instead.  This is theorized to help with avoidance of local
  mins/maxes.

* They run experiments on Atari, maze, and locomotion benchmarks.
  * In a head-to-head comparisons, the GA performs better than ES, A3C, and DQN
    on 6 games out of 13

* GAs will often find high performing individuals in few generations.  This
  suggests that many high-quality policies exist in the region where the random
  initialization produces policies.  

* Next question: are we doing any better than random search?  GAs outperformed
  random search in every game tested.
  * Random search outperforms DQN on 3 of 13 games, ES on 3 of 13 games, and
    A3C on 6 of 13 games.
  * In one example, random search found a policy with a very high score of
    3,620 in less than 1 hour vs an average score of 797 produced by DQN after
    7-10 days of optimization.
  * The difficulty that NNs have with beating random policies suggest that for
    some tasks gradient-based methods may be getting trapped in local minima.


* They then test a maze benchmark designed to have deceptive reward signals and
  local min/maxes.  GA-NS performs well in this scenario because it ignores
  reward and encourages exploration.

* GAs disappointed on a robot locomotion task; they were significantly
  slower at finding a solution than the other algorithms.

* These results suggest that densely sampling policies in a region around the
  origin is sufficient to find good policies for some tasks.  This sometimes
  beats state-of-the-art, gradient-based methods. 
  * Tasks with densely packed "good" policies seem like they'd be well tailored
    for GAs.


### Thoughts

* It seems that the performance of RL algorithms are heavily affected by the
  distribution of good policies in the policy space which is a property of the
  task itself.

* I like the idea of "blindly" modifying the parameters of the NN directly.  It
  is interesting to think that a trained net is, ultimately, a vector of
  numbers and that you can operate on that vector outside of its NN context.
