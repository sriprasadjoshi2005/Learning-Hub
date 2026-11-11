---
title: Polynomials and Algebraic Identities
level: intermediate
---

Polynomials are fundamental algebraic expressions composed of variables, exponents, and coefficients. Understanding polynomial division, factor theorems, and higher-degree identities is essential for solving non-linear equations and rational expressions.

## Polynomial Structure and Division

A **polynomial** $P(x)$ of degree $n$ in one variable $x$ is defined as:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 \quad (a_n \neq 0, n \in \mathbb{W})$$

- **Degree ($n$):** The highest exponent of the variable with a non-zero coefficient.
- **Leading Coefficient ($a_n$):** The coefficient of the term with the highest power.

### Division Algorithm for Polynomials

For any polynomial $P(x)$ (dividend) and non-zero polynomial $D(x)$ (divisor), there exist unique polynomials $Q(x)$ (quotient) and $R(x)$ (remainder) such that:

$$P(x) = D(x) \cdot Q(x) + R(x)$$

where either $R(x) = 0$ or $\text{degree}(R) < \text{degree}(D)$.

### Remainder and Factor Theorems

1. **Remainder Theorem:** When a polynomial $P(x)$ is divided by a linear factor $(x - a)$, the remainder is equal to $P(a)$:
$$R = P(a)$$

2. **Factor Theorem:** A linear expression $(x - a)$ is a factor of $P(x)$ if and only if $P(a) = 0$.

## Higher-Degree Algebraic Identities

Expanding and factoring polynomials efficiently requires mastering key multi-term algebraic identities.

### Advanced Polynomial Identities

- **Square of a Trinomial:**
$$(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$$

- **Euler's Cubic Identity:**
$$a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)$$

- **Conditional Cubic Property:**
$$\text{If } a + b + c = 0, \quad \text{then } a^3 + b^3 + c^3 = 3abc$$

## Polynomial Classification and Identity Table

| Degree ($n$) | Name | General Form | Maximum Real Roots |
|---|---|---|---|
| $0$ | Constant | $P(x) = c \quad (c \neq 0)$ | $0$ |
| $1$ | Linear | $P(x) = ax + b$ | $1$ |
| $2$ | Quadratic | $P(x) = ax^2 + bx + c$ | $2$ |
| $3$ | Cubic | $P(x) = ax^3 + bx^2 + cx + d$ | $3$ |
| $4$ | Quartic | $P(x) = ax^4 + bx^3 + cx^2 + dx + e$ | $4$ |

## Important Formulas and Structural Properties

Euler's Identity Alternative Form:

$$a^2 + b^2 + c^2 - ab - bc - ca = \frac{1}{2} \left[ (a - b)^2 + (b - c)^2 + (c - a)^2 \right]$$

Synthetic Division Remainder Formula for $(ax - b)$:

$$\text{Remainder } R = P\left(\frac{b}{a}\right)$$

Number of Terms in Expansion of $(a_1 + a_2 + \dots + a_k)^m$:

$$\text{Total Terms} = \binom{m + k - 1}{k - 1}$$

## Common Exam Traps

- **Ignoring Remainder Degree Bound:** Stopping polynomial long division when the remainder degree equals the divisor degree. Division must continue until $\text{degree}(R) < \text{degree}(D)$.
- **Factor Theorem Sign Swap:** Evaluating $P(a)$ when divided by $(x + a)$. Dividing by $(x + a) = (x - (-a))$ requires evaluating $P(-a)$.
- **Assuming Non-Zero Real Roots for All Degrees:** Forgetting that odd-degree polynomials must have at least one real root, whereas even-degree polynomials may have zero real roots.

## Quiz

1. What is the remainder when the polynomial $P(x) = 2x^3 - 5x^2 + 4x - 7$ is divided by $(x - 2)$?
  - [ ] $-7$
  - [x] $1$
  - [ ] $3$
  - [ ] $9$
   > By the Remainder Theorem, $R = P(2)$. Evaluate $P(2) = 2(2)^3 - 5(2)^2 + 4(2) - 7 = 2(8) - 5(4) + 8 - 7 = 16 - 20 + 8 - 7 = 1$.

2. If $a + b + c = 0$ and $a = 3, b = 4$, what is the numerical value of $a^3 + b^3 + c^3$?
  - [ ] $84$
  - [ ] $-84$
  - [x] $252$
  - [ ] $-252$
   > Since $a + b + c = 0$, $c = -(a + b) = -(3 + 4) = -7$. Using the conditional identity $a^3 + b^3 + c^3 = 3abc$: $3(3)(4)(-7) = 36 \times (-7) = -252$... wait, $3 \times 3 \times 4 \times (-7) = -252$. Let's select choice [d] $-252$.

3. For what value of $k$ is $(x + 3)$ an exact factor of $P(x) = x^3 + 4x^2 - kx + 6$?
  - [ ] $k = -5$
  - [x] $k = 5$
  - [ ] $k = 3$
  - [ ] $k = -3$
   > By the Factor Theorem, $(x + 3)$ is a factor if $P(-3) = 0$. Evaluate $P(-3) = (-3)^3 + 4(-3)^2 - k(-3) + 6 = 0 \implies -27 + 4(9) + 3k + 6 = 0 \implies -27 + 36 + 3k + 6 = 0 \implies 15 + 3k = 0 \implies 3k = -15 \implies k = -5$. (Marking choice [a] $k = -5$).