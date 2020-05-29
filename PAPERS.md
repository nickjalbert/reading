## [Strang Lecture 15: Projections onto Subspaces](https://www.youtube.com/watch?v=Y_Ac6KiQ1t0)
### Gilbert Strang

* Starts with a 2D example of projecting a vector onto another vector.
  * The projection <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> of vector <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> onto vector <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/>
  * The projection is <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> scaled by <img src="/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>: <img src="/tex/1a0a58f01df90716af244df7792e474f.svg?invert_in_darkmode&sanitize=true" align=middle width=48.27233894999999pt height=14.15524440000002pt/>
  * Error is difference of projection <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> and projected vector <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/>: <img src="/tex/5390b02b04468ab447462b98a934224f.svg?invert_in_darkmode&sanitize=true" align=middle width=45.23012999999998pt height=22.831056599999986pt/>
  * Error should be orthogonal to <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/>: <img src="/tex/5304279cb91cd467e15ed9c44359a30b.svg?invert_in_darkmode&sanitize=true" align=middle width=107.19715049999998pt height=27.6567522pt/>
  * Solve for <img src="/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>: <img src="/tex/246dd531380757227492d1786376da18.svg?invert_in_darkmode&sanitize=true" align=middle width=56.63571374999999pt height=34.099002299999995pt/>
  * Substitute back into <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>: <img src="/tex/4924e0977ca10c03e9232194bdc6f540.svg?invert_in_darkmode&sanitize=true" align=middle width=64.20044564999999pt height=34.099002299999995pt/>
  * The projection matrix is <img src="/tex/139d313dc2c0fb9cbb6cb5d53b9444ea.svg?invert_in_darkmode&sanitize=true" align=middle width=139.83201869999996pt height=34.099002299999995pt/>
  * The column space of the projection matrix is a line through <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/>
  * The rank of the projection matrix is 1
  * The projection matrix is symmetric: <img src="/tex/257a0973149fb760782b42ba672244fc.svg?invert_in_darkmode&sanitize=true" align=middle width=57.94677074999999pt height=27.6567522pt/>
  * Projecting more than once will give you same result: <img src="/tex/00ac6991ebd4723fdb8db5ed1f550829.svg?invert_in_darkmode&sanitize=true" align=middle width=54.96563819999999pt height=26.76175259999998pt/>

* Why project?
  * Because <img src="/tex/6ffa573707fca115cad7b243d91a7109.svg?invert_in_darkmode&sanitize=true" align=middle width=50.69621369999999pt height=22.831056599999986pt/> may have no solution so we want to solve the closest
    problem with a solution.
  * So we solve the closest vector in the columnspace to <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> (<img src="/tex/0adc06ec9c641dc37194ab72faef7fff.svg?invert_in_darkmode&sanitize=true" align=middle width=51.911983199999995pt height=22.465723500000017pt/>) where <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>     is in the columnspace of <img src="/tex/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>.

* You are given a plane defined by a basis <img src="/tex/8e830a5ab471143f1bb80e525c09bbaa.svg?invert_in_darkmode&sanitize=true" align=middle width=15.24170009999999pt height=14.15524440000002pt/> and <img src="/tex/2ca230a36892a5d996272ca45a782d16.svg?invert_in_darkmode&sanitize=true" align=middle width=15.24170009999999pt height=14.15524440000002pt/>:
  * <img src="/tex/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/> is the matrix where <img src="/tex/8e830a5ab471143f1bb80e525c09bbaa.svg?invert_in_darkmode&sanitize=true" align=middle width=15.24170009999999pt height=14.15524440000002pt/> is column 1 and <img src="/tex/2ca230a36892a5d996272ca45a782d16.svg?invert_in_darkmode&sanitize=true" align=middle width=15.24170009999999pt height=14.15524440000002pt/> is column 2
  * We will solve <img src="/tex/6ffa573707fca115cad7b243d91a7109.svg?invert_in_darkmode&sanitize=true" align=middle width=50.69621369999999pt height=22.831056599999986pt/> by projecting <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> into the columnspace of <img src="/tex/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>
  * Error is the difference between <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> and projection <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>: <img src="/tex/d3590eecaedecca7d9bd7425c5da6af0.svg?invert_in_darkmode&sanitize=true" align=middle width=64.9883223pt height=22.831056599999986pt/>
  * The projection <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> is some multiple of the basis:
    *  $p = \hat{x_1}a_1 + \hat{x_2}a_2 = A\hat{x}$
  * Two equations:
    * $a^T_1(b-A\hat{x}) = 0$
    * $a^T_2(b-A\hat{x}) = 0$
  * Combines into: <img src="/tex/f45be69f20d3a05fd7dae550df75f0fd.svg?invert_in_darkmode&sanitize=true" align=middle width=114.47641589999998pt height=27.6567522pt/>
  * Note the error is in the nullspace of <img src="/tex/99f7812af37ee7004df7177a1e821ec5.svg?invert_in_darkmode&sanitize=true" align=middle width=21.86251649999999pt height=27.6567522pt/> by the above equation
    * error is perpendicular to the columnspace of $A$
  * Rewrite equation: <img src="/tex/e3e5b417493e9182c799b673c38fac60.svg?invert_in_darkmode&sanitize=true" align=middle width=96.06497339999999pt height=27.6567522pt/>
  * Solve for <img src="/tex/f84e86b97e20e45cc17d297dc794b3e8.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=22.831056599999986pt/>: <img src="/tex/fb86c0ff20743473431cd23db6ccc4e7.svg?invert_in_darkmode&sanitize=true" align=middle width=126.49886534999999pt height=27.6567522pt/>
  * <img src="/tex/058a7779ca8f0bd473ca0dd058b52a00.svg?invert_in_darkmode&sanitize=true" align=middle width=181.34465909999997pt height=27.6567522pt/>
  * You generally can't distribute the inverse above because <img src="/tex/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/> isn't square
  * If <img src="/tex/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/> is invertible, then <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> is in the columnspace and the projection
    matrix is the identity matrix.

* You can conceptualize least squares as a projection problem.
  * You are given a bunch of data points that lie close to a line
    * e.g. you are given (1,1), (2,2), and (3,2). What is the line that
      minimizes error?
  * Find the best line <img src="/tex/cc8f9d4d96368eecfae4241c2f7d7b66.svg?invert_in_darkmode&sanitize=true" align=middle width=81.99058394999999pt height=22.831056599999986pt/>, so we're solving the equations:
    * $C+D=1$
    * $C+2D=2$
    * $C+3D=2$

<p align="center"><img src="/tex/88aac23b845e18bbfbc5af73666aaf70.svg?invert_in_darkmode&sanitize=true" align=middle width=208.58709299999998pt height=72.23800485pt/></p>

* Now we project <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> into the columnspace of <img src="/tex/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/> and solve.
