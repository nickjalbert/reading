---
layout: post
title:  "Strang Lecture 16: Projection Matrices and Least Squares"
date:   2020-06-01 12:07:00 -0700
paper-url: https://www.youtube.com/watch?v=osh80YCg_GM
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

* The projection matrix is $$P=A(A^TA)^{-1}A^T$$
* If you project $$b$$ and $$b$$ is in the column space, then $$Pb=b$$:

  $$
    Pb=A(A^TA)^{-1}A^Tb
  $$

  $$
    \text{note: }b = Ax
  $$

  $$
    Pb=A(A^TA)^{-1}A^TAx
  $$

  $$
    Pb=A\frac{A^TA}{A^TA}x
  $$

  $$
    Pb=Ax
  $$

  $$
    Pb=b
  $$

* If you project $$b$$ and $$b$$ is perpendicular to the column space, then
  $$Pb=0$$ (note, $$b$$ is in the nullspace of $$A^T$$ because it is
  perpendicular to each column of $$A$$):

  $$
    Pb=A(A^TA)^{-1}A^Tb
  $$

  $$
    \text{note: }A^Tb = 0
  $$

  $$
    Pb=A(A^TA)^{-1}0
  $$

  $$
    Pb=0
  $$

*  When we project $$b$$ into the columnspace of $$A$$, the projection $$p=Pb$$
   plus the error $$e$$ results in $$b$$ ($$p+e=b$$).  Note that we are also
   projecting $$b$$ into the left nullspace to find $$e$$.  Thus $$e=(I-P)b$$.
   It is not clear to me why the $$I-P$$ appears other than:

   $$
     p+e = Pb + (I-P)b = Pb + Ib - Pb = Ib = b
   $$

### Least squares


* Find the best straight line $$y=C+Dt$$ through the points
  (1,1), (2,2), and (3,2).

* Each point defines a linear equation:

  $$
    C + D = 1
  $$

  $$
    C + 2D = 2
  $$

  $$
    C + 3D = 2
  $$

* This translates to matrix form:

  $$
    \begin{bmatrix}
        \begin{array}{rr}
        1 & 1 \\
        1 & 2 \\
        1 & 3 \\
        \end{array}
    \end{bmatrix} *
    \begin{bmatrix}
        \begin{array}{r}
        C \\
        D \\
        \end{array}
    \end{bmatrix}  =
    \begin{bmatrix}
        \begin{array}{r}
        1 \\
        2 \\
        2 \\
        \end{array}
    \end{bmatrix}

  $$

* What are we minimizing when we try to find the best possible projection of
  $$b$$ into the columnspace.  Minimize
  $$\lvert Ax-b\rvert^2=\lvert e\rvert^2$$.  The error is how far each
  point lies from the line.

* For the least squares method of calculating the error, outliers can unduly
  influence the result.

* Pretty good discussion of the projections vs the original points at 17:15.
  Essentially we project all the points in our dataset onto a line. We choose
  the line  such that the line minimizes the total error squared.

* The goal of least squares: Find
  $$\hat{x} = \begin{bmatrix} \hat{C} \\ \hat{D} \end{bmatrix}$$ and $$P$$

  $$
    A^TA\hat{x} = A^Tb
  $$

  $$
    A^TA =
    \begin{bmatrix}
        \begin{array}{rrr}
        1 & 1 & 1\\
        1 & 2 & 3\\
        \end{array}
    \end{bmatrix} *
    \begin{bmatrix}
        \begin{array}{rr}
        1 & 1 \\
        1 & 2 \\
        1 & 3 \\
        \end{array}
    \end{bmatrix} =
    \begin{bmatrix}
        \begin{array}{rr}
        3 & 6 \\
        6 & 14 \\
        \end{array}
    \end{bmatrix}
  $$

  $$
    A^TAb =
    \begin{bmatrix}
        \begin{array}{rrr}
        1 & 1 & 1\\
        1 & 2 & 3\\
        \end{array}
    \end{bmatrix} *
    \begin{bmatrix}
        \begin{array}{rrr}
        1 & 1 & 1\\
        1 & 2 & 2\\
        1 & 3 & 2\\
        \end{array}
    \end{bmatrix} =
    \begin{bmatrix}
        \begin{array}{rrr}
        3 & 6 & 5\\
        6 & 14 & 11\\
        \end{array}
    \end{bmatrix}
  $$

* Normal equations:

  $$
    3C + 6D = 5
  $$

  $$
    6C + 14D = 11
  $$

* Solution: $$D=\frac{1}{2}$$ and $$C=\frac{2}{3}$$.

* 30:00 - good discussion of the error vector and how it relates to the matrix
  world.  He shows how $$b=p+e$$ in this example.

  $$
  b = p+e
  $$

  $$
    \begin{bmatrix}
        \begin{array}{r}
        1 \\
        2 \\
        2 \\
        \end{array}
    \end{bmatrix} =
    \begin{bmatrix}
        \begin{array}{r}
        \frac{7}{6} \\
        \frac{10}{6} \\
        \frac{13}{6} \\
        \end{array}
    \end{bmatrix} +
    \begin{bmatrix}
        \begin{array}{r}
        \frac{-1}{6} \\
        \frac{2}{6} \\
        \frac{-1}{6} \\
        \end{array}
    \end{bmatrix}
  $$

* Note $$e$$ is perpendicular to all vectors in the columnspace.


### Back to Linear Algebra

* If $$A$$ has independent columns, then $$A^TA$$ is invertible.

* How to prove?

  $$
    \text{Suppose } A^TAx=0 \text{ then prove } x=0
  $$

  $$
    x^TA^TAx=0
  $$

  $$
    (Ax)^T(Ax) = 0
  $$

  $$
    Ax=0
  $$

  $$
    A \text{ has independent columns and } Ax=0 \text{ then } x=0
  $$

* Columns are definitely independent if they are perpendicular unit vectors
  (orthonormal vectors).
