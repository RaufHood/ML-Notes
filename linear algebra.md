# Linear Algebra refresher
A **scalar** is a quantity that is represented by a single number and is uneffected by vector space changes.  
A **vector** is a quantity that need to be expressed in magnitude and direction.
A **tuple** is an order list of numbers.
A **matrix** is an array of numbers or symbols. In geometry they represent a geometric transformations, such as rotations, translation, reflections (rigid transformations), affine transformations (preserving lines and parallelism, but not necessarily Euclidean distances and angles. ), stretching, shearing and projections. 

## Inner or Dot product
The inner product of 2 vectors is a scalar and consist of the norm of the 2 vectors scaled by the cos of the relative angle $\theta$.
$$ x^T y = \sum_i x_i y_i = |x| |y| \cos(\theta) $$

## Cross product 
The cross product is a vector multiplication leading to a new vector orthogonal to the 2 vectors and with length of $|x| |y|  \sin(\theta)$,
$$ x \times y = \ = |x| |y| cos(\theta) $$
For 3 dimensional vectors the cross product is  
$${\displaystyle x ={\begin{bmatrix}x_{2}y_{3}-x_{3}y_{2}\\x_{3}y_{1}-x_{1}y_{3}\\x_{1}y_{2}-x_{2}y_{1}\end{bmatrix}}}$$

## Matrix Multiplication
MAtrix $A$ and vector $x$
$$ y = A x$$
$${\displaystyle {\begin{pmatrix}\color {OliveGreen}3&\color {OliveGreen}2&\color {OliveGreen}1\\1&0&2\end{pmatrix}}\cdot {\begin{pmatrix}\color {BrickRed}1&2\\\color {BrickRed}0&1\\\color {BrickRed}4&0\end{pmatrix}}={\begin{pmatrix}{\color {OliveGreen}3}\cdot {\color {BrickRed}1}+{\color {OliveGreen}2}\cdot {\color {BrickRed}0}+{\color {OliveGreen}1}\cdot {\color {BrickRed}4}&\ast \\\ast &\ast \end{pmatrix}}={\begin{pmatrix}{\color {Blue}7}&\ast \\\ast &\ast \end{pmatrix}}}$$

Inverse of a matrix $A{^-1}$ fullfills the following condition 
$$A \cdot A^{-1} = \mathbb{1}$$