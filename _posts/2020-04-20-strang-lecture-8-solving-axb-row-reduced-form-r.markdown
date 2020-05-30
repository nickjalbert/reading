---
layout: post
title:  "Strang Lecture 8: Solving Ax = b: Row Reduced Form R"
date:   2020-04-20 12:05:00 -0700
paper-url: https://www.youtube.com/watch?v=9Q1q7s1jTzU
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

* We'll reuse our example matrix to explore $$Ax=b$$:

$$
    \begin{bmatrix}
        \begin{array}{rrrr}
            1 & 2 & 2 &  2 \\
            2 & 4 & 6 &  8 \\
            3 & 6 & 8 & 10 \\
        \end{array}
    \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}
$$

* Let's use an augmented matrix to deal with the right hand side and do
  elimination:

$$
    \begin{bmatrix}
        \begin{array}{rrrrr}
            1 & 2 & 2 &  2 & b_1 \\
            2 & 4 & 6 &  8 & b_2 \\
            3 & 6 & 8 & 10 & b_3 \\
        \end{array}
    \end{bmatrix}
$$

* End up with, the condition for a solution is $$0 = -b_1 - b_2 + b_3$$
  (e.g. $$b = (1, 5, 6)$$):

$$
    \begin{bmatrix}
        \begin{array}{rrrrr}
            1 & 2 & 2 & 2 &   b_1             \\
            0 & 0 & 2 & 4 & -2b_1 + b_2       \\
            0 & 0 & 0 & 0 &  -b_1 - b_2 + b_3 \\
        \end{array}
    \end{bmatrix}
$$

* Solvability: a condition on $$b$$.  $$Ax=b$$ is solvable when $$b$$ is in
  the columnspace of $$A$$, $$C(A)$$. Alternatively, if a combination of the
  rows of $$A$$ give the zero row, then the same combination of the components
  of $$b$$ have to give a zero.

* To find complete solution to $$Ax=b$$:

  * Find a particular solution. One way to find a particular solution: set all
    free variables to zero and then solve for pivot variables.

  $$
    x_p = \begin{bmatrix}
          \begin{array}{r}
                       -2  \\
                        0  \\
               \frac{3}{2} \\
                        0  \\
          \end{array}
          \end{bmatrix}
  $$

  * Add in the nullspace $$x_n$$ (aka special solutions).

* The complete solution to $$Ax=b$$ is $$ x_{complete} = x_p + x_n $$

$$

x_{complete} =
    \begin{bmatrix}
    \begin{array}{r}
              -2  \\
               0  \\
      \frac{3}{2} \\
               0  \\
    \end{array}
    \end{bmatrix}  +
    c_1 *
    \begin{bmatrix}
    \begin{array}{r}
      -2 \\
       1 \\
       0 \\
       0 \\
    \end{array}
    \end{bmatrix}  +
    c_2 *
    \begin{bmatrix}
    \begin{array}{r}
        2 \\
        0 \\
       -2 \\
        1 \\
    \end{array}
    \end{bmatrix}
$$

* Note $$ A * (x_p + x_n) = A * x_p + A * x_n = A * x_p + 0 = A * x_p = b$$.

* $$ x_c $$ in this case is a subspace (the nullspace) shifted by the
  $$x_p$$.  Instead of going through zero, the subspace goes through
  $$x_p$$.

* Relations between rank $$r$$ in a $$m \times n$$ matrix:

  * $$ r \leq m$$
  * $$ r \leq n$$

* Full column rank $$r = n$$: no free variables, nullspace is only the zero
  vector, one or zero solutions to $$Ax=b$$.  Matrix will look tall and thin.
  Each zero row will be an additional condition on $$b$$.

* Full row rank $$r = m$$: One or many solutions for every $$b$$ (depending if
  there are free variables.  There will be $$n-r = n-m$$ free variables).
  Matrix will be short and fat.  $$m > n$$ results in free variables.

* Full row and column rank $$r = m = n$$.  Square matrix and invertible, one
  solution for every b. Row reduced echelon form is the identity matrix.

* If $$r < m$$ and $$r < n$$, then you will have 0 solutions (if the
  conditions of the zero row are not satisifed) or infinite solutions if the
  conditions of the zero row are satisfied.
