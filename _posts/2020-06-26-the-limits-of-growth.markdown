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

### [Galactic-Scale Energy](https://dothemath.ucsd.edu/2011/07/galactic-scale-energy/)

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

This leaves us with the question: **how do we build a society that doesn't
require sustained growth to function?**


[^1]: See section 12 of this
      [Solar FAQ](https://www.sandia.gov/~jytsao/Solar%20FAQs.pdf) for
      more detailed calculations.
