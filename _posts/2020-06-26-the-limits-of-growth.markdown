---
layout: post
title:  "The Limits of Growth"
date:   2020-06-26 12:07:00 -0700
author: Nick Jalbert
---

I came across a series of blog posts from 2011 by UCSD's [Tom
Murphy](https://tmurphy.physics.ucsd.edu/) that attempt to estimate the limits
of civilizational growth.  I thought these posts were great reads and worth
summarizing here.

**[Galactic-Scale Energy](https://dothemath.ucsd.edu/2011/07/galactic-scale-energy/)**

Since the mid-1600s, energy usage in the U.S. has grown by roughly ~2-3% a year
(doubling roughly every 25 to 35 years).  This growth is closely tied to
improvements in quality of life; modern conveniences like cars, electricity,
HVAC, medicine, and computers all require energy for manufacture and operation.
Beyond that, we've baked assumptions about the continuity of growth into our
economic system.

So how long will physics allow us to continue growing like this?
This post is a cautionary tale on exponential growth.

We start with global energy usage which is ~12TW continuous (~3TW of which is
the U.S.).  Roughly 90,000TW worth of sunlight hit the earth's surface
continuously[^1].  How long until we will need to capture and use the entirety
of the sun's energy that hits earth while growing 2%?

$$
12 * 1.02^x = 90000
$$

$$
x = 450 \text{ years (at 2% growth)}
$$

How about if we grow at 3%?

$$
12 * 1.03^x = 90000
$$

$$
x = 300 \text{ years (at 3% growth)}
$$


All these numbers are estimates and they ignore a bunch of constants (e.g. the
atmosphere reflects 30% of the sun, solar panels are 20% efficient).
Regardless, the punchline is that we have 300-450 years before we've used up
all the easily accessible energy; a blink of the eye in civilizational terms.
After that, growth (or, at least, growth predicated on deploying energy to
productive ends) stops.

Highlighting the unforgiving nature of exponential growth, we can extend the
analysis to scenarios like "capturing all the sun's energy" and "capturing all
the milky way's energy" and those buy us at most a couple thousand years.

Another tack is taken by examining how much heat necessarily would be produced
in a scenario when we continue our energy growth (say, through fusion) and
remain planet-bound.  The math shows the equilibrium temperature of the earth's
surface becomes hotter than the sun's surface in less than a thousand years.

This leaves us with the question: **how do we build a society that doesn't
require sustained exponential growth to function?**

**[Does the Logistic Shoe Fit](https://dothemath.ucsd.edu/2011/08/does-the-logistic-shoe-fit/)**

This post addresses a criticism of the Galactic-Scale Energy post; specifically
that a different function might be a better fit for the recent energy-usage
data rather than the exponential.

This post explores three scenarios.  Any scenario could plausibly fit the data,
but each trajectory comes with its own implications:

* **Infinite growth (exponential curve)** - We run out of energy sources in a
  few hundred years.
* **Sustainable trajectory (logistic curve)** -  We go through a linear
  inflection and leveling off on our growth of energy use.  This means that
  current societal systems that expect X% growth a year will break.
* **Finite resource (logistic curve on total energy extracted)** - The least
  appealing case, we get caught in an energy trap and run out of fossil fuels
  before we can transition to renewable sources.  This implies contraction in
  our energy budget (and, likely, economy)


**[Can Economic Growth Last?](https://dothemath.ucsd.edu/2011/07/can-economic-growth-last/)**

From 1900 to 1950, economic growth essentially paced the growth of societal
energy usage.  From 1950 onward, economic growth increased more than energy
growth (5% vs 3%).  Is this good news?  Can we continue to grow the economy
uncoupled from energy consumption?

This post divides non-energy-consumptive economic growth into two categories: 

* **Efficiency gains** - Doing more productive work per energy unit consumed.
* **The non-physical economy** - Non-manufacturing activity: services, finance, real
  estate, virtual tech.

In the efficiency arena, you generally can't make processes and machines more
than 100% efficient.  Thus, this caps how much juice we can squeeze out of this
strategy.  Two thirds of the energy we use is burned in heat engines, and these
have a factor of 2 to 3 in efficiency improvement before we've hit the hard
cap. A reasonable estimate in plausible efficiency gains for society as a whole
is in the 2x to 4x range.  If we guess efficiency has been improving at roughly
1% a year, that leaves us roughly 150 years before we exhaust this avenue.

In the non-physical arena, a toy model is setup where:

* Energy availability levels off (the "sustainable trajectory" above)
* Efficiency gains continue but saturate at some multiple
* The economy continues to grow exponentially (e.g. 5% a year)
* The rest of the yearly growth comes from the non-physical economy

The result is that the non-physical economy fast approaches 100% of economic
activity, and this has all sorts of bizarre and contradictory implications.
For example, given that we still require physical food to sustain our
existence, and that there is a hard limit to the efficiency improvement of the
food production processes, we end up in a scenario where (either or both) food
cost approaches zero or growth gets dragged down by its interface points with
the physical world.

The result is that even the untethering of the economy from physical production
processes is quickly exhausted in exponential scenarios as long as we still
have physical needs.  Again, we are left with the question of what the future
looks like once we exhaust growth?


Tidbits:

* Energy return on energy invested (EROEI) is important when thinking about
  energy sources.  Fossil fuels are in the 20:1 to 100:1 range, renewables are
  in the 10:1 to 20:1 range.  If the only sources of energy we had were less
  than 1:1 then our energy budget would necessarily contract.


**Future work**:

* I'd like to better understand what breaks in the economy when we give up
  exponential growth.

* Read up more on sustainable steady-state economies (e.g.
  [CASSE](https://steadystate.org/))



<hr>

[^1]: See section 12 of this
      [Solar FAQ](https://www.sandia.gov/~jytsao/Solar%20FAQs.pdf) for
      more detailed calculations.
