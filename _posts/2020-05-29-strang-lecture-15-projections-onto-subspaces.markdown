---
layout: post
title:  "Strang Lecture 15: Projections onto Subspaces"
date:   2020-05-29 12:07:00 -0700
paper-url: https://www.youtube.com/watch?v=Y_Ac6KiQ1t0
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

### Summary

One can imagine least squares regression as solving $$Ax=b$$ where $$b$$ is
(generally) not in the columnspace of $$A$$.  To handle this, one projects
$$b$$ into the columnspace of $$A$$ and solves $$Ax=p$$. Note the error of the
projection ($$e=b-p$$) is orthogonal to $$A^T$$ and is thus in the nullspace of
$$A^T$$.

### Notes

* Starts with a 2D example of projecting a vector onto another vector.
  * The projection $$p$$ of vector $$b$$ onto vector $$a$$
  * The projection is $$a$$ scaled by $$x$$: $$p=xa$$
  * Error is difference of projection $$p$$ and projected vector $$b$$:
    $$b-xa$$
  * Error should be orthogonal to $$a$$: $$a^T(b-xa) = 0$$
  * Solve for $$x$$: $$x = \frac{a^Tb}{a^Ta}$$
  * Substitute back into $$p$$: $$p=a\frac{a^Tb}{a^Ta}$$
  * The projection matrix is $$\text{proj}(p)=Pb=\frac{aa^T}{a^Ta}$$
  * The column space of the projection matrix is a line through $$a$$
  * The rank of the projection matrix is 1
  * The projection matrix is symmetric: $$P^T=P$$
  * Projecting more than once will give you same result: $$P^2=P$$

* Why project?
  * Because $$Ax=b$$ may have no solution so we want to solve the closest
    problem with a solution.
  * So we solve the closest vector in the columnspace to $$b$$ ($$Ax=p$$)
    where $$p$$ is in the columnspace of $$A$$.

* You are given a plane defined by a basis $$a_1$$ and $$a_2$$:
  * $$A$$ is the matrix where $$a_1$$ is column 1 and $$a_2$$ is column 2
  * We will solve $$Ax=b$$ by projecting $$b$$ into the columnspace of $$A$$
  * Error is the difference between $$b$$ and projection $$p$$: $$e=b-p$$
  * The projection $$p$$ is some multiple of the basis:

    $$p = \hat{x}_1a_1 + \hat{x}_2a_2 = A\hat{x}$$

  * The above projection defines two equations:

$$a^T_1(b-A\hat{x}) = 0$$

$$a^T_2(b-A\hat{x}) = 0$$

  * Combines into: $$A^T(b-A\hat{x}) = 0$$
  * Note the error is in the nullspace of $$A^T$$ by the above equation
    * error is perpendicular to the columnspace of $$A$$
  * Rewrite equation: $$A^TA\hat{x} = A^Tb$$
  * Solve for $$\hat{x}$$: $$\hat{x} = (A^TA)^{-1}A^Tb$$

    $$p = A\hat{x} = A(A^TA)^{-1}A^Tb$$

  * You generally can't distribute the inverse above because $$A$$ isn't square
  * If $$A$$ is invertible, then $$b$$ is in the columnspace and the projection
    matrix is the identity matrix.

* You can conceptualize least squares as a projection problem.
  * You are given a bunch of data points that lie close to a line
    * e.g. you are given (1,1), (2,2), and (3,2). What is the line that
      minimizes error?
  * Find the best line $$b=C+Dt$$, so we're solving the equations:

    $$C+D=1$$

    $$C+2D=2$$

    $$C+3D=2$$

  * In matrix form, this is:

$$
Ax = b
$$

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

* Now we project $$b$$ into the columnspace of $$A$$ and solve.
