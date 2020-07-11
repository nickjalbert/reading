---
layout: post
title:  "Personal Energy Usage"
date:   2020-07-03 12:07:00 -0700
work-in-progress: true
author: Nick Jalbert
---

Inspired by the [posts](https://dothemath.ucsd.edu/post-index/) of UCSD's Tom
Murphy on societal energy consumption
(see also [The Limits of Growth]({{site.baseurl }}/{% post_url 2020-06-26-the-limits-of-growth %})),
I wanted to dig deeper into the implications of our energy consumptions
habits at an individual level.


**An individual's energy consumption**

How much energy do Americans consume on a per capita basis?  The USA had
roughly $$3.3\times10^8$$ people in it in 2019[^1] and we consumed 100
quadrillion BTUs in 2019 (roughly $$1\times10^{20}$$ joules)[^2].  This works
out to $$3\times10^{11}$$ joules per person in 2019.  Given that there are
roughly $$3\times10^7$$ seconds in a year, we find that each American draws a
continuous $$1\times10^4$$ watts.

That is to say, our energy consumption is equivalent to every American drawing
10,000 watts at all times.  That sounds like a lot![^3]  Obviously, this
varies greatly at the individual level and these numbers include energy from
electricity as well as transportation and manufacturing.  So while noting the
previous caveats, I'll be using this 10 kW figure as a proxy for the energy
required to maintain an American lifestyle for the rest of this post.

As a baseline for comparison, we can also calculate how much energy our bodies
consume just by existing.  Assuming we need 2000 calories a day to sustain
ourselves, we find that humans draw about 100 watts to sustain life[^4].  Thus
a modern American lifestyle requires two orders of magnitude more energy than
the basal energy requirements of sustaining a person's life.

**Sustaining an individual's energy consumption with solar**

Let's say I wanted to sustain my lifestyle's energy consumption by capturing
the most available and abundant renewable: solar power. How much land would I
need?  The solar energy hitting ground level varies considerably depending on
your location.  Fortunately, the NREL has mapped out the availability of solar power.[^5]

We'll start with some optimistic numbers. Assuming I have a chunk of land out
in the desert southwest. The NREL data suggests that we could expect roughly
$$6\text{ }\frac{\text{kWh}}{\text{m}^2}$$ per day on average.  Our 10 kW
constant draw corresponds to 240 kWh per day.  If we were able to magically
capture all the solar energy we were receiving, then we'd need roughly 40
$$\text{m}^2$$ to sustain my 10kW draw.  This is a 6.5m$$\times$$6.5m
(21ft$$\times$$21ft) patch of land.

Now, how much land does that represent when we make our assumptions more
realistic?  Modern solar panels vary from 6% to 40% efficiency.[^6]  We'll use
15% as a ballpark figure for economical mass-produced panels.  If we're only
able to capture 15% of the energy hitting our patch of land, then we'll end up
getting roughly $$0.9\text{ }\frac{\text{kWh}}{\text{m}^2}$$ per day on
average. This means we'll now need 267$$\text{m}^2$$ to satisfy our energy
requirements; a 16.5m$$\times$$16.5m (55ft$$\times$$55ft) square.

If we do the math for our basal energy requirements, we find we need about
3$$\text{m}^2$$ to get our daily 2000 cal equivalent using mass-produced solar
panels.

**Sustaining an individual's energy consumption with low-tech solar**

The math above is both incomplete and assumes too much.  One of the many ways
it's incomplete is that electricity doesn't make for a satisfying meal (even 10
kW!).  So, if we want to live on our little desert plot, we'll have to figure
out a way to convert our electricity into something more palatable.  I'm
interested in exploring this further, but for now I'll just note that this
introduces another inefficiency into the system which will make our 2000
cal/day requirement more expensive at the generation stage.

That aside, our analysis also assumes too much.  For example, it assumes that
the energy consumption of our lifestyle would remain unchanged if we were
interested in living off-the-grid in the desert.  I suspect, though, that
without the infrastructure of society making it easy to consume vast quantities
of energy without necessarily realizing it (highways, airplanes, internet
shopping anyone?), our 240kWh per day might be overkill for living a full and
satisfying life.

We also assume that we will be able to import infrastructure from larger
society to serve our needs.  However, when we build artificial general
intelligence and--oops!--turns out it's more Terminator than Star Trek, we may
not be able to source our solar panels from the wider world.  So it's probably
worth checking out the math using nature's original solar panel: plants.

So let's see how the math works out using plants.

**References**
* [The feasibility of switchgrass for biofuel production](https://www.researchgate.net/publication/280661407_The_feasibility_of_switchgrass_for_biofuel_production)
* [Net energy of cellulosic ethanol from switchgrass](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2206559/)


**TODO**
* How much land do we need to cover an individual's energy needs (optimal vs
  realistic)?
* Math for storage buffer of energy
* How much land do we need to cover an individual's energy needs using "low
  tech" solutions?
* How do we convert energy to satisfy Maslow's hierarchy (food, water, etc)?
* What would a low-tech sustainable lifestyle look like?  How much energy/land
  would be required?
* Is there a low tech way to create solar panels?  Would would a completely
  off-the-grid existence look like?
* Storage?  How much space for storage of energy?
* Culmination: what does a sustainable off-the-grid life look like with AND
  without modern society surrounding you?
* Plausibility of the argument re offloading energy consumption to other societies via overseas manufacturing etc.







<hr>

[^1]: [Demographics of the United States (wikipedia.org)](https://en.wikipedia.org/wiki/Demographics_of_the_United_States)

[^2]: [US energy facts explained (eia.gov)](https://www.eia.gov/energyexplained/us-energy-facts/)

[^3]: I find it less surprising when converted to gallons of gasoline.  This
      10 kilowatt continuous draw is equivalent to burning 7 gallons of gas a
      day to sustain each of our energy demands.  That I find this
      formulation less surprising probably suggests that my intuitions around
      the energy stored in gas are off.

[^4]: $$
      4.184\times10^3\frac{\text{joules}}{\text{cal}}
      \cdot 2\times10^3\frac{\text{cal}}{\text{day}}
      = 8.36\times10^6\frac{\text{joules}}{\text{day}}
      $$

      $$
      8.36\times10^6\frac{\text{joules}}{\text{day}}
      \cdot 8.64\times10^{-4}\frac{\text{day}}{\text{sec}}
      = 100 \frac{\text{joules}}{\text{sec}} = 100\text{ watts}
      $$

[^5]: [Solar Resource Data, Tools, and Maps (nrel.gov)](https://www.nrel.gov/gis/solar.html) and [Global Horizontal Solar Irradiance (nrel.gov)](https://www.nrel.gov/gis/assets/images/nsrdb-v3-ghi-2018-01.jpg)

[^6]: [Solar cell efficiency (wikipedia.org)](https://en.wikipedia.org/wiki/Solar_cell_efficiency#Comparison)
