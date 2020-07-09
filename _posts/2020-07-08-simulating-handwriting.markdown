---
layout: post
title:  "Simulating Handwriting"
date:   2020-07-08 12:07:00 -0400
author: Nick Jalbert
---

*A break from regularly scheduled programming.*

I got to thinking about handwriting while on a walk yesterday. Like so many
things we do, it's beautiful how we seamlessly coordinate half a dozen joints
to externalize our memory.

I also find it interesting how most people have an identifiable scrawl.  Mine
is pure slop, but I suspect I could pick it out of a lineup.  I bet this is
true for most folks.

This got me wondering how hard it would be to generate a unique "hand" for a
computer.  My initial thought was to model the major joints and try to actuate
these joints to generate letters.  I'm not sure if this is already a
Reinforcement Learning benchmark, but it's closely related to a number of
physics-based robotics tasks that *are* RL benchmarks.

After some toying around, I decided to go even simpler. You can see my proof
of concept below:


<script type="text/javascript">
{% include assets/js/2020-07-08/handwritten-e1a0bff.js %}
</script>
<div id="handwritten-js" style="margin-bottom: 0.5rem"></div>
<button id="rewrite-button" class="rounded-button">Rewrite</button>

You can click the "rewrite" button to regenerate the letters.

I developed this little widget using JavaScript and HTML5 canvas. Canvas gives
you a stroke based API for generating lines and curves, and I ported the
strokes I use to write these letters by hand over to this API.  I then generate
some Gaussian noise to perturb the start, curve, and end of each stroke.  This
adds slop and gives it a bit of a human feel.  I find the results quite
pleasing even though it took very little code to achieve.

Further extensions I might explore:

* *Correlated errors* - When I write an "E", first I write an "L" and then add
  the middle and top horizontal bar.  I suspect the errors for the horizontal
  bars are correlated (i.e. they might slant upward or they might slant
  downward, but they will probably all slant in the same direction).
* *Scale error by distance* - I suspect error increases the further you move
  your pen (a corollary of [Fitts's
  Law](https://en.wikipedia.org/wiki/Fitts%27s_law)).  Thus long strokes (or
  long moves that don't generate lines) should be noisier than short strokes.

* *Scale error by direction* - Suppose you're moving the pen vertically.  I
  suspect your going to get more error in the vertical direction than you are
  in the horizontal direction.  I believe this generalizes to any axis of
  motion.

Finally, if you happen to be Drake and you need a new album cover, let me know
and I'll definitely flesh out the text generation engine!

<div class="centered">
  <a href="https://en.wikipedia.org/wiki/If_You%27re_Reading_This_It%27s_Too_Late">
    <img src="{{ site.baseurl }}/assets/img/2020-07-08/drake-cover.png" />
  </a>
</div>



