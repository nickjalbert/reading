---
layout: post
title:  "Strang Lecture 10: The Four Fundamental Subspaces"
date:   2020-04-30 12:07:00 -0700
paper-url: https://www.youtube.com/watch?v=nHlE7EgJFds
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---


* 4 fundamental subspaces (assume $$A$$ is $$m \times n$$):
  * Columnspace: $$C(A)$$ is in $$R^m$$
  * Nullspace: $$N(A)$$ is in $$R^n$$
  * Rowspace: all combinations the rows of $$A$$ (i.e. $$C(A^T)$$) is
    in $$R^n$$
  * Left Nullspace: $$N(A^T)$$ is in $$R^m$$

* Dimension of the subspaces:
  * Columnspace: $$rank(A)$$
  * Nullspace: $$n - rank(A)$$
  * Rowspace: $$rank(A)$$
  * Left Nullspace: $$m - rank(A)$$

* Note the sum of the dimensions of the nullspace and rowspace give $$n$$ (and
  they are both in $$R^n$$) and the sum of the dimensions of the columnspace
  and left nullspace give $$m$$ (and they are both in $$R^m$$).

* How to produce a basis for each subspace:
  * Columnspace: row reduction, use the original vectors that correspond to
    the pivot columns.
  * Nullspace: set each free variable to 1 (and others to zero) to find basis
    vectors (i.e. find the special solutions).
  * Rowspace: the pivot rows directly after getting $$A$$ into rref.
  * Left Nullspace: row reduce $$A^T$$ and find the special solutions.


