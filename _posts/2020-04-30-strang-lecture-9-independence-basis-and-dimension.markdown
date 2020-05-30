---
layout: post
title:  "Strang Lecture 9: Independence, Basis and Dimension"
date:   2020-04-30 12:05:00 -0700
paper-url: https://www.youtube.com/watch?v=yjBerM5jWsc
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

* Suppose $$A$$ is an $$m \times n$$ matrix with $$m < n$$ (more unknowns than
  equations).  Then there are nonzero solutions to $$Ax=0$$ (there is
  something besides the zero vector in the nullspace of $$A$$).  There will be
  at least one free variable.

* Vectors $$x_1, x_2, x_3, x_n$$ are **independent** if the only linear
  combination of those vectors that give the zero vector is all zeros.

* If the zero vector is in the set, then the set is always dependent.

* 3 vectors in 2D space are dependent because there will be free variables.

* When $$v_1, ..., v_n$$ are the columns of $$A$$, they are independent if the
  nullspace of $$A$$ is only the zero vector.  They are dependent if $$Ac=0$$
  for some nonzero $$c$$.  In the independent case, the rank of $$A$$ is
  $$n$$. In the dependent case, the rank of $$A$$ is less than $$n$$.

* The columns of matrix $$A$$ ($$v_1, ..., v_n$$) **span** the columnspace of
  $$A$$.  That is, the space consists of all combinations of those vectors.
  They are not necessarily independent.  However, we're generally interested
  in a set of vectors that both span and space and are independent.  A
  spanning, independent set (a **basis**) is "just right": you need all the
  vectors to generate the space and none are redundant.

* Example: a basis for $$R^3$$ is $$(1,0,0), (0,1,0), (0,0,1)$$.

* Asking if the vectors composing a matrix are a basis is the same as asking if
  the matrix is invertible.

* A basis (e.g. for $$R^3$$) is not unique.  All basis for a space will have
  the same number of vectors.  This number is the **dimension** of the space.

* The (original) pivot columns are the columns you need for a basis of a space.

* The rank of $$A$$ (the number of pivot columns) is the dimension of the
  columnspace.

* $$dim(A) = r$$ and $$dim(N(A)) = n - r$$ for $$m \times n$$ matrix.
