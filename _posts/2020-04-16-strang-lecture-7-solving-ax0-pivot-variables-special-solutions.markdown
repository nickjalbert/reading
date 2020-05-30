---
layout: post
title:  "Strang Lecture 7: Solving Ax = 0: Pivot Variables, Special Solutions"
date:   2020-04-16 12:01:00 -0700
paper-url: https://www.youtube.com/watch?v=VqP2tREMvt0
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

* Use elimination to solve a $$3 \times 4$$ rectangular matrix ($$A$$):

$$
    \begin{bmatrix}
        \begin{array}{rrrr}
            1 & 2 & 2 &  2 \\
            2 & 4 & 6 &  8 \\
            3 & 6 & 8 & 10 \\
        \end{array}
    \end{bmatrix}
$$

* During elimination:
    * Nullspace does not change
    * Solutions do not change
    * Columnspace **IS** changing
    * Rowspace does not change (not explicitly mentioned, but assume so)

* Result of elimination ($$U$$):

$$
    \begin{bmatrix}
        \begin{array}{rrrr}
            1 & 2 & 2 & 2 \\
            0 & 0 & 2 & 4 \\
            0 & 0 & 0 & 0 \\
        \end{array}
    \end{bmatrix}
$$


* No pivot in second column means it's free (a combo of other columns)

* 2 total pivots; they are 1 at (1,1) and 2 at (2,3)

* The result of elimination is in upper echelon form ($$U$$)

* Rank of matrix == pivots == 2 in this example.

* You can solve $$Ux=0$$, same solutions as $$Ax=0$$

* 2 pivot columns, 2 free columns

* You can assign any number to the free columns and then solve the equations
  for the pivots columns.

* Assign $$x_2 = 1$$ and $$x_4 = 0$$ to the free variables and solve for
  $$x_1$$ and $$x_3$$.  Note $$x_1=-2$$ and $$x_3=0$$ after back subbing.
  This is a vector in the nullspace and any multiple of it is in the
  nullspace.

* You have two free variables, so you need another vector in the nullspace.
  Now Assign $$x_2 = 0$$ and $$x_4 = 1$$ to the free variables and solve for
  $$x_1$$ and $$x_3$$.  Note $$x_1=2$$ and $$x_3=-2$$ after back subbing.
  This is anonter vector in the nullspace and any multiple of it is in the
  nullspace.

* Any linear combination of those two vectors are in the nullspace.  You'll get
  one vector in the nullspace for each free column.


$$
nullspace(A) =
    c_1 * \begin{bmatrix}
            \begin{array}{r}
                -2 \\
                 1 \\
                 0 \\
                 0 \\
            \end{array}
          \end{bmatrix}
    +
    c_2 * \begin{bmatrix}
            \begin{array}{r}
                 2 \\
                 0 \\
                -2 \\
                 1 \\
            \end{array}
          \end{bmatrix}
$$

* Rank is equal to the pivot variable count.  Free variables is $$n-R$$ for an
  $$m \times n$$ matrix.

* Finding the nullspace: Do elimination.  Set each free variable to one (and
  others to zero) and solve for a vector in the nullspace.

* Matrix $$R$$ is the reduced row echelon form (rref).  Use the pivots to
  clean up the rows above them and make pivots equal to 1. $$R$$ for our above
  example is:

$$
    \begin{bmatrix}
        \begin{array}{rrrr}
            1 & 2 & 0 & -2 \\
            0 & 0 & 1 & 2 \\
            0 & 0 & 0 & 0 \\
        \end{array}
    \end{bmatrix}
$$

* Note the identity matrix $$I$$ is mixed into the rref matrix $$R$$.

* Typical rref looks like (I is identity matrix, F is free variables, the
  columns from I and F may be intermixed, $$r$$ pivot rows AND columns, $$m-r$$
  free rows, $$n-r$$ free columns):

$$
    \begin{bmatrix}
        \begin{array}{rr}
            I & F \\
            0 & 0 \\
        \end{array}
    \end{bmatrix}
$$

* Nullspace matrix ($$N$$) - columns are the special solutions. $$RN=0$$.

$$
    N = \begin{bmatrix}
            \begin{array}{rr}
                -F \\
                 I \\
            \end{array}
        \end{bmatrix}
$$

* I find this part of the lecture confusing.  He is composing matrices ($$F$$
  and $$I$$) that don't quite correspond to the example.

* Rank of $$A^T$$ is the same as $$A$$.  $$N(A^T)$$ is dimension 1 in our
  example.

