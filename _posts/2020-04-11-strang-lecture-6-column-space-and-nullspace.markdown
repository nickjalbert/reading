---
layout: post
title:  "Strang Lecture 6: Column Space and Nullspace"
date:   2020-04-11 12:01:00 -0700
paper-url: https://www.youtube.com/watch?v=8o5Cmfpeo6g
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---


* Discussion of subspaces plane $$P$$ through zero and line $$L$$ through zero
  in $$R^3$$.  A bit confusing the exact definition of union and intersection,
  but if union is not a subspace in general (assuming $$L$$ is not coplanar
  with $$P$$) while intersection is.

* Interestingly:  overdetermined equations (in this example, 3 unknowns and 4
  equations) don't fill the $$R^4$$ space so they can't always be solved.
  Overdetermined doesn't fill the subspace in this case.

* Column space :  all $$b$$'s that solve $$Ax=b$$.  In an $$m \times n$$
  matrix, column space is a subspace $$R^m$$

* Nullspace: all $$x$$'s that solve $$Ax=0$$. In an $$m \times n$$ matrix, null
  space is a subspace of $$R^n$$

* Note that the solutions to $$Ax=b$$ do not form a subspace in general for
  $$b$$ (generally will not include the zero vector).  The nullspace is a
  vector space.

* Previewing the idea that you will have a particular solution to $$Ax=b$$, but
  then you can add a vector from the nullspace to also get another solution.
