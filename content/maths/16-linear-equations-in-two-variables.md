---
title: Linear Equations in Two Variables
level: intermediate
---

A system of linear equations in two variables consists of two or more equations sharing common variables. Analyzing their geometric intersections and algebraic solutions forms the core of linear algebra.

## Systems of Two Linear Equations

A general system of two linear equations in two variables $x$ and $y$ is represented as:

$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

### Algebraic Methods of Solution

1. **Substitution Method:** Express one variable in terms of the other from one equation, then substitute it into the second equation.
2. **Elimination Method:** Multiply equations by suitable scalars so that coefficients of one variable are equal or opposite, then add or subtract to eliminate that variable.
3. **Cramer's Rule (Determinant Method):**
$$x = \frac{D_x}{D}, \qquad y = \frac{D_y}{D} \quad (D \neq 0)$$
where $D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}$, $D_x = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}$, $D_y = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}$.

## Consistency and Graphical Interpretation

Geometrically, each linear equation represents a straight line in the Cartesian plane. The system's solution corresponds to the point(s) of intersection.

- **Consistent & Independent (Unique Solution):** Lines intersect at exactly one point.
$$\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$$

- **Consistent & Dependent (Infinitely Many Solutions):** Lines are coincident (identical lines).
$$\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$$

- **Inconsistent (No Solution):** Lines are parallel and distinct.
$$\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$$

## System Classification Master Table

| Coefficient Ratio Condition | Graphical Behavior | Algebraic Classification | Number of Solutions | Determinant Condition |
|---|---|---|---|---|
| $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ | Intersecting lines | Consistent & Independent | Exactly One $(x, y)$ | $D \neq 0$ |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Coincident lines | Consistent & Dependent | Infinitely Many | $D = 0, D_x = 0, D_y = 0$ |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ | Parallel lines | Inconsistent | Zero (No Solution) | $D = 0, D_x \neq 0 \text{ or } D_y \neq 0$ |

## Important Formulas and Matrix Identities

$2 \times 2$ Determinant Calculation:

$$D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1$$

Matrix Inversion Solution Form ($A \mathbf{x} = \mathbf{b}$):

$$\begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} \implies \begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{a_1 b_2 - a_2 b_1} \begin{pmatrix} b_2 & -b_1 \\ -a_2 & a_1 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

## Common Exam Traps

- **Division by Zero in Cramer's Rule:** Applying Cramer's rule formulas $x = \frac{D_x}{D}$ when $D = 0$. When $D = 0$, Cramer's rule fails, and you must check if $D_x = D_y = 0$ (infinitely many solutions) or non-zero (no solution).
- **Rearranging Constants Incorrectly:** Mixing up standard form $Ax + By = C$ with $Ax + By + C = 0$ when applying ratio tests or Cramer's determinant.
- **Signs in $2 \times 2$ Determinant:** Subtracting in the wrong order: writing $a_2 b_1 - a_1 b_2$ instead of $a_1 b_2 - a_2 b_1$.

## Quiz

1. Solve the system of equations for $x$ and $y$:
   $$\begin{cases} 2x + 3y = 12 \\ 5x - 2y = 11 \end{cases}$$
  - [ ] $(x, y) = (2, 3)$
  - [x] $(x, y) = (3, 2)$
  - [ ] $(x, y) = (4, 1)$
  - [ ] $(x, y) = (1, 3)$
   > Multiply first equation by $2$: $4x + 6y = 24$. Multiply second equation by $3$: $15x - 6y = 33$. Add the equations: $19x = 57 \implies x = 3$. Substitute $x = 3$ into first equation: $2(3) + 3y = 12 \implies 6 + 3y = 12 \implies 3y = 6 \implies y = 2$.

2. For what value of $k$ will the system of equations have no solution (inconsistent)?
   $$\begin{cases} 4x + 6y = 9 \\ k x + 9y = 15 \end{cases}$$
  - [ ] $k = 4$
  - [x] $k = 6$
  - [ ] $k = 8$
  - [ ] $k = 12$
   > For no solution, slopes must be equal but intercepts different: $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2} \implies \frac{4}{k} = \frac{6}{9} \neq \frac{9}{15}$. Cross-multiplying: $6k = 36 \implies k = 6$. Check constants: $\frac{4}{6} = \frac{2}{3}$ while $\frac{9}{15} = \frac{3}{5} \neq \frac{2}{3}$. Thus $k = 6$.

3. Calculate the determinant value $D_x$ for the linear system:
   $$\begin{cases} 3x - y = 7 \\ 2x + 4y = 14 \end{cases}$$
  - [ ] $D_x = 14$
  - [ ] $D_x = 28$
  - [x] $D_x = 42$
  - [ ] $D_x = 56$
   > Replace $x$-column with constants $(7, 14)$: $D_x = \begin{vmatrix} 7 & -1 \\ 14 & 4 \end{vmatrix} = (7)(4) - (-1)(14) = 28 + 14 = 42$.