---
layout: post
title:  "Strang Lecture 14: Orthogonal Vectors and Subspaces"
date:   2020-05-28 12:07:00 -0700
paper-url: https://www.youtube.com/watch?v=YzZUIYRCE38
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

* The rowspace and nullspace are orthogonal (the angle between them is 90
  degrees).  Same for the columnspace and the left nullspace.

* Orthogonal - in N-dimensional space, the angle between vectors is 90 degrees.

* Test for orthogonality - two vectors are orthogonal if the dot product
  ($$x^Ty$$) is zero.

* Shows the connection between the Pythagorean theorem and orthogonality.
  * Pythagorean theorem:
    $$\lvert x\rvert^2 + \lvert y\rvert^2 = \lvert x+y\rvert^2$$
  * Squared length of vector $$x$$: $$x^Tx$$
  * When vectors are orthogonal (sub into Pythagorean):

$$
x^Tx + y^Ty = (x+y)^T(x+y)
$$

$$
x^Tx + y^Ty = x^Tx + y^Ty + x^Ty + y^Tx
$$

$$
0 = 2x^Ty
$$

$$
0 = x^Ty
$$

* Zero vector is orthogonal to all vectors.

* Subspace $$S$$ is orthogonal to subspace $$T$$ when every vector in $$S$$ is
  orthogonal to every vector in $$T$$.

* Rowspace is orthogonal to the nullspace.  Why?
  * $$Ax = 0$$ defines the nullspace
  * Alternatively, you can think of it as:

$$
    \begin{bmatrix}
        \begin{array}{c}
            \text{row 1 of A} \\
            \text{row 2 of A} \\
            ... \\
            \text{row m of A} \\
        \end{array}
    \end{bmatrix} *
    \begin{bmatrix}
        \begin{array}{r}
            x_1  \\
            ...  \\
            x_n  \\
        \end{array}
    \end{bmatrix}  =  \begin{bmatrix} 0 \\ 0 \\ ... \\ 0 \end{bmatrix}
$$

* Each row of $$A$$ is orthogonal to $$x$$ because that row multiplied by
  $$x$$ equals 0.
  * You also have to show that $$x$$ is orthogonal to every linear combination
    of the rows of $$A$$.
  * If $$c_1\text{row}_1^Tx = 0$$ and $$c_2\text{row}_2^Tx = 0$$ then use
    distributive property to show that:

$$

(c_1\text{row}_1 + c_2\text{row}_2)^Tx = 0_{ }

$$

* The rowspace and nullspace carve $$R^n$$ into two orthogonal subspaces.  The
  columnspace and left nullspace do the same for $$R^m$$.  They are
  **orthogonal complements** (the complements contain all the vectors in the
  space they carve up).
  * The nullspace contains **all** vectors perpendicular to the row space.

* Up next: solve $$Ax=b$$ when there is no solutions.
* Consider $$A^TA$$ (where $$A$$ is $$m \times n$$):
  * It's square $$n \times n$$
  * It's symmetric: $$(A^TA)^T = A^TA^{TT} = A^TA$$

* The "good" equation used for solving $$Ax=b$$ when there is no solution is
  achieved by multiplying both sides by $$A^T$$ to get $$A^TAx=A^Tb$$.

* The nullspace of $$A^TA$$ equals the nullspace of $$A$$.
* The rank of $$A^TA$$ equals the rank of $$A$$.
* $$A^TA$$ is invertible exactly if $$A$$ has independent columns.

