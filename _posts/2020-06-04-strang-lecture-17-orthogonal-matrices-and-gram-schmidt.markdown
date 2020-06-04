---
layout: post
title:  "Strang Lecture 17: Orthogonal Matrices and Gram-Schmidt"
date:   2020-06-04 12:10:00 -0700
paper-url: https://www.youtube.com/watch?v=0MtwqhIwdrI
paper-authors:
  - Gilbert Strang
author: Nick Jalbert
---

### Orthogonal basis

* Orthonormal vectors:

$$
  q^T_iq_j=
    \begin{cases}
      0 \text{ if } i \neq j \\
      1 \text{ if } i  = j \\
    \end{cases}
$$

* Each vector is a unit vector (i.e. has length one).

* A set of orthonormal vectors is also a set of independent vectors.

* Orthonormal vectors make calculations nice, a lot of linear algebra in
  practice is built around them.

### Matrix with orthonormal columns

* A matrix with an orthonormal columns (each column is independent and has
  length 1):

$$
  Q=
  \begin{bmatrix}
      \begin{array}{rcr}
            &      &      \\
        q_1 & ...  & q_n  \\
            &      &      \\
      \end{array}
  \end{bmatrix}
$$

* Note that $$Q^TQ=I$$.

* If a matrix with orthonormal columns is square, then we call it an orthogonal
  matrix:
  * Then $$Q^TQ=I$$ tells us $$Q^T=Q^{-1}$$
  * An example is a permutation matrix

* Adhemar (sp?) matrices are matrices of 1s and -1s that are orthogonal.  We
  know they exist for some sizes (e.g. 2x2, 4x4, 16x16, 64x64) but we don't
  know in general which sizes allow for this.

* "The punishing thing about Gram-Schmidt is that we always run into square
  roots"

* Why do we want orthonormal matrices?  What calculation is made easier?

* Suppose $$Q$$ has orthonormal columns.  Project onto its column space.

$$
P=Q(Q^TQ)^{-1}Q^T
$$

$$
P=Q(I)^{-1}Q^T
$$

$$
P=QQ^T
$$

* If you have a square $$Q$$, then because of the orthonormal columns, then the
  matrix is full rank and any $$b$$ will be in the column space and thus 
  $$QQ^T = I$$

* Two properties of any projection matrix:
  * It's symmetric
  * And $$(QQ^T)(QQ^T) = QQ^T$$


* Remember $$A^TA\hat{x}=A^Tb$$, with orthogonal $$Q$$:

$$Q^TQ\hat{x}=Q^Tb$$

$$I\hat{x}=Q^Tb$$

$$\hat{x}=Q^Tb$$

$$\hat{x}_i=q_i^Tb$$

### Gram-Schmidt

* Start with independent vectors and turn them into an orthonormal basis.

* Given independent vectors $$a$$, $$b$$, and $$c$$, what's an orthonormal
  basis ($$q_1$$, $$q_2$$, $$q_3$$) for the space they span?
  * First, get orthogonal vectors $$A$$, $$B$$, and $$C$$
  * Second, get orthonormal vectors
    $$q_1=\frac{A}{\lvert \lvert A\rvert\rvert}$$, 
    $$q_2=\frac{B}{\lvert \lvert B\rvert\rvert}$$, and
    $$q_2=\frac{C}{\lvert \lvert C\rvert\rvert}$$,

* Idea: keep $$a$$ and then project $$b$$ onto an orthogonal subspace and then
  do the same for $$c$$ with respect to $$a$$ and $$b$$.  Essentially we're
  interested in the error component of the projection of $$b$$ onto $$a$$.

* For $$B$$:

$$p=b-e$$

$$e=b-p$$

$$B=b-p$$

$$B=b-\frac{A^Tb}{A^TA}A$$

* For $$C$$:

$$C = c - \frac{A^Tc}{A^TA}A - \frac{B^Tc}{B^TB}B$$

* You can think of (for example) $$\frac{A^Tc}{A^TA}A$$ as the component of
  $$c$$ in the $$a$$ direction that we're subtracting off.

* Works through a numerical example starting at 38:15.

$$
a=
\begin{bmatrix}
    \begin{array}{r}
      1 \\
      1 \\
      1 \\
    \end{array}
\end{bmatrix}

b=
\begin{bmatrix}
    \begin{array}{r}
      1 \\
      0 \\
      2 \\
    \end{array}
\end{bmatrix}
$$

$$
A=a
$$

$$
B=b - \frac{A^Tb}{A^TA}A
$$

$$
B=b - \frac{3}{3}A
$$

$$
B=\begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} - 
  \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
$$

$$
B=
  \begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}
$$

$$q_1= \frac{1}{\sqrt{3}}\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$$

$$q_2= \frac{1}{\sqrt{2}}\begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}$$

* The column space of $$A$$ and its orthonormal $$Q$$ calculated via
  Gram-Schmidt is the same.

* $$A=QR$$ is the magic formula expressing Gram-Schmidt (similar to $$A=LU$$ we
  saw earlier).
  * $$R$$ is upper triangular.

$$A=QR$$

$$
\begin{bmatrix} 
      &&     \\
  a_1 && a_2 \\
      &&     \\
\end{bmatrix} =
\begin{bmatrix} 
      &&     \\
  q_1 && q_2 \\
      &&     \\
\end{bmatrix} *
 \begin{bmatrix} 
  a_1^Tq_1   && ... \\
  a_1^Tq_2   && ... \\
\end{bmatrix}
$$

* Note $$a_1^Tq_2=0$$ because the later $$q$$'s are perpendicular to all the
  earlier vectors.


{::comment}

## Matrix

$$
Q=
\begin{bmatrix}
    \begin{array}{rcr}
          &      &      \\
      q_1 & ...  & q_n  \\
          &      &      \\
    \end{array}
\end{bmatrix}
$$


## Cases

$$
q^T_iq_j=
  \begin{cases}
    0 \text{ if } i \neq j \\
    1 \text{ if } i  = j \\
  \end{cases}
$$

## Bars

$$
\lvert x\rvert^2 + \lvert y\rvert^2 = \lvert x + y\rvert^2
$$


## Fractions

$$
\frac{1}{2}
$$

{:/comment}
