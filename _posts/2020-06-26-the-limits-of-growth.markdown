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
the Milky Way's energy" and those buy us at most a couple thousand years.

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

**[The Energy Trap](https://dothemath.ucsd.edu/2011/10/the-energy-trap/)**

This post explores *the energy trap*, which is a term the author uses to
describe the short-term shockwaves that ripple through society when we can no
longer sustain exponential growth in energy usage.  More specifically: once
fossil fuel availability declines and energy is in short supply, then building
out renewables requires even more energy from our already-constrained budget.

We look again at energy return on energy invested (EROEI).  Fossil fuels tend
to have high EROEI (100:1 in the early days of oil), solar and wind less so
(roughly 10:1 and 20:1 respectively).  Now let's play out several scenarios of
decline:

1. Assume we expect 2% decline in fossil fuel availability and in year 0 we
   have 100 units of energy and want to build out renewable resources to make
   up for the expected decline.  Using a 10:1 EROEI over a 40 year lifespan
   where most of the energy invested up front, we'd need to spend 8 units of
   energy to build out the resources.

   Thus our year 0 energy budget looks like an 8% decline to arrest a 2%
   decline next year.  Most importantly, if we decide to do nothing, the year 0
   budget is untouched and year 1 only sees the 2% decline.  With these
   assumptions, one step forward long term (in the form of renewables) always
   results in four steps back in the short term (in the current energy budget).

   An additional complicating factor: to replace the 2% energy decline in the
   U.S., we'd have to build a 1GW power plant every week.  As a point of
   comparison, France built 56 plants in 15 years when they went big on
   nuclear.  Construction at the 2% replacement scale is difficult to imagine
   and probably can't be ramped up immediately.

2. The second scenario explores a world where there's a ramp up time in
   construction capacity.  Once we expect the 2% decline, it takes several
   years to get building at the scale needed to replace our dwindling fossil
   fuel resources. The initial investment is less burdensome, but the dip in
   total energy budget is greater.  The energy trap still exists, because at
   any point we can give up on the construction of new capacity and ease the
   pain.


Another issue is that much of our infrastructure depends on liquid fuels.  This
analysis does not take into the account the additional energy required to
either convert our liquid fuel infrastructure to electric or to turn
electricity into liquid fuel.

I'll quote the conclusion of the blog post directly:

> Politically, the Energy Trap is a killer. In my lifetime, I have not
> witnessed in our political system the adult behavior that would be needed to
> buckle down for a long-term goal involving short-term sacrifice.  Or at least
> any brief bouts of such maturity have not been politically rewarded.  I’m not
> blaming the politicians. We all scream for ice cream. Politicians simply
> cater to our demands. We tend to vote for the candidate who promises a
> bigger, better tomorrow—even if such a path is untenable.

> The only way out of the political trap is for a substantial fraction of our
> population to understand the dimensions of the problem: to understand that
> we’ve been spoiled by the surplus energy available through fossil fuels, and
> that we will have to make decade-level sacrifices to put ourselves on a new
> track. The only way to accomplish this is through sober education, which is
> what [Do the Math](https://dothemath.ucsd.edu/) is all about. It’s a trap!
> Spread the word!


Tidbits:

* When put in the long view, the fossil fuel age is a blip in the timeline of
  human history.

* If the EROEI is the equivalent to the lifetime (e.g. 40:1 in the 40 year
  lifetime case), then we can avoid the trap.  The trap also doesn't apply if
  the source of energy doesn't require large upfront investment (as is often
  the case with fossil fuels).


**Challenge question**

In the spirit of the [Fermi
problems](https://en.wikipedia.org/wiki/Fermi_problem) explored in these posts,
I attempted to estimate how many floating point operations we have left in our
budget given the Milky Way's energy reserve.

Let's start the sun's power output[^2] of $$3.8\times10^{33} \frac{ergs}{sec}$$

We'll convert that to watts:

$$
3.8\times10^{33} \frac{ergs}{sec}
*
\frac{1J}{10^7\text{ }ergs}
=
3.8 \times 10^{26} J/sec = 3.8\times10^{26}\text{ }watts
$$

So the Sun produces  $$3.8 \times 10^{26}$$ watts continuously.

How much does a floating point operation cost in terms of energy?  Looking at
the
[Green 500](https://en.wikipedia.org/wiki/Performance_per_watt#Green500_List),
our most efficient supercomputers perform about
$$1.6\times10^{10} \frac{FLOPS}{watt}$$.

So, how many FLOPS can we run with the Sun's energy output?

$$
3.8\times10^{26}\text{ }watts
*
1.6\times10^{10}\text{ }\frac{FLOPS}{watt}
=
6\times10^{36}\text{ }FLOPS
$$

So now, we've wired up our supercomputer to the sun and we're performing
$$6\times10^{36}\text{ }FLOPS$$.
How many operations will we be able to squeeze of the sun during its lifetime?

The sun is expected to live another 8 billion years[^3]. That translates to:

$$
8x10^9\text{ years}* 365\frac{days}{year} *24\frac{hours}{day}*60\frac{min}{hour}*60\frac{sec}{hour} = 2.5\times10^{17} sec
$$

Thus we can expect to get about

$$
6\times10^{36}\text{ }FLOPS
*
2.5\times10^{17} sec
= 1.5\times10^{54}\text{ floating point ops}
$$

out of our sun.  Let's assume that the sun is about average for the Milky Way.
The Milky Way contains about $$4\times10^{11}$$ stars[^4].  This gives us a
budget of

$$
1.5\times10^{54}\frac{\text{ floating point ops}}{\text{star}}
*
4\times10^{11}\text{ stars}
=
6\times10^{65}\text{ floating point ops}
$$


So, we have roughly $$6\times10^{65}$$ floating point ops before we exhaust
all the energy in the Milky Way.  AlphaGoZero is estimated to have taken
$$2\times10^{23}$$ floating point operations to train[^5].  Thus, the Milky Way
has another $$3\times10^{42}$$ AlphaGoZeros in it.


**Future work**

* I'd like to better understand what breaks in the economy when we give up
  exponential growth.

* Think more about the psychology of society.  Would spending 8 units of energy
  to build out a yearly capacity of 2 units look like energy deprivation or
  more jobs in renewables?

* Read up more on sustainable steady-state economies (e.g.
  [CASSE](https://steadystate.org/))


**Appendix**

[Useful Energy Relations](https://dothemath.ucsd.edu/useful-energy-relations/)
covers some common units.  Points to remember:

* Energy is the quantitative property that that must be transferred to an
  object in order to perform work on, or to heat, the object[^6].

* Energy is measured in Joules (J) which has units
  $$\frac{\text{kg} \cdot \text{m}^2}{\text{sec}^2}$$.

* Power is a measure of the rate of energy usage.  This is measured in Watts
  (W), which is Joules per second.  Alternatively, Watts have units
  $$\frac{\text{kg} \cdot \text{m}^2}{\text{sec}^3}$$.

* Think of energy as the water reservoir behind a dam and the power as the flow
  in or out of the reservoir.

| Unit                        | Joule Equivalent           |
|:--------                    |:-------:                   |
| eV                          | $$1.6\times10^{−19}$$ J    |
| erg                         | $$1\times10^{-7}$$ J       |
| BTU                         | 1055 J                     |
| Cal or kcal (food calorie)  | 4184 J                     |
| kWh                         | 3.6 MJ                     |
| 1 gal of gasoline           | 125 MJ                     |

<hr>

[^1]: See section 12 of this
      [Solar FAQ](https://www.sandia.gov/~jytsao/Solar%20FAQs.pdf) for
      more detailed calculations.

[^2]:  See this
       [NASA site](https://cosmicopia.gsfc.nasa.gov/qa_sun.html#power)
       and this
       [wiki page](https://en.wikipedia.org/wiki/Orders_of_magnitude_(power)#1015_to_1026_W).

[^3]: [When Will the Sun Die?](https://www.space.com/14732-sun-burns-star-death.html)

[^4]: [Wikipedia: Milky Way](https://en.wikipedia.org/wiki/Milky_Way)

[^5]: [AI and Compute](https://openai.com/blog/ai-and-compute/)

[^6]: [Wikipedia: Energy](https://en.wikipedia.org/wiki/Energy)
