---
title: Factorization and Algebraic Fractions
level: intermediate
---

Factorization transforms algebraic sums into products of simpler factors. Mastering factorization techniques allows for the simplification of complex rational expressions and partial fraction decomposition.

## Fundamental Methods of Factorization

Factorization is the reverse process of bracket expansion. The principal methods include:

1. **Taking Out Common Factors:**
$$ab + ac = a(b + c)$$

2. **Grouping Terms:**
$$ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)$$

3. **Splitting the Middle Term (Trinomials $ax^2 + bx + c$):** Find two numbers $p$ and $q$ such that $p \cdot q = a \cdot c$ and $p + q = b$.
$$ax^2 + px + qx + c = (x \dots)$$

4. **Difference of Two Squares:**
$$a^2 - b^2 = (a - b)(a + b)$$

5. **Sum and Difference of Two Cubes:**
$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

## Rational Expressions and Partial Fractions

A **rational expression** is a ratio of two polynomials $\frac{P(x)}{Q(x)}$, where $Q(x) \neq 0$.

### Simplification of Algebraic Fractions

Simplify by factorizing numerator and denominator completely and canceling common non-zero factors:

$$\frac{x^2 - 9}{x^2 + 5x + 6} = \frac{(x - 3)(x + 3)}{(x + 2)(x + 3)} = \frac{x - 3}{x + 2} \quad (x \neq -3, x \neq -2)$$

### Partial Fraction Decomposition

Partial fractions break a proper rational function $\frac{P(x)}{Q(x)}$ ($\text{degree}(P) < \text{degree}(Q)$) into simpler component fractions based on the factors of $Q(x)$:

- **Distinct Linear Factors:**
$$\frac{p x + q}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}$$

- **Repeated Linear Factors:**
$$\frac{p x + q}{(x - a)^2} = \frac{A}{x - a} + \frac{B}{(x - a)^2}$$

- **Irreducible Quadratic Factor:**
$$\frac{p x^2 + q x + r}{(x - a)(x^2 + bx + c)} = \frac{A}{x - a} + \frac{B x + C}{x^2 + bx + c}$$

## Partial Fraction Template Summary Table

| Factor Structure in Denominator $Q(x)$ | Partial Fraction Setup Form |
|---|---|
| $(x - a)(x - b)$ | $\frac{A}{x - a} + \frac{B}{x - b}$ |
| $(x - a)^3$ | $\frac{A}{x - a} + \frac{B}{(x - a)^2} + \frac{C}{(x - a)^3}$ |
| $(x - a)(x^2 + k)$ | $\frac{A}{x - a} + \frac{Bx + C}{x^2 + k}$ |
| $(x^2 + a)(x^2 + b)$ | $\frac{Ax + B}{x^2 + a} + \frac{Cx + D}{x^2 + b}$ |

## Important Formulas and Algebraic Theorems

Cover-Up Rule for Distinct Linear Factors:

$$\text{For } \frac{P(x)}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}: \quad A = \left. \frac{P(x)}{x - b} \right|_{x = a}, \quad B = \left. \frac{P(x)}{x - a} \right|_{x = b}$$

Sum and Difference of Cubes Signs:

$$a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2) \quad [\text{Middle term sign is OPPOSITE to binom sign}]$$

## Common Exam Traps

- **Factoring Sum of Squares over Reals:** Writing $a^2 + b^2 = (a + b)(a + b)$. Sum of squares $a^2 + b^2$ cannot be factorized over real numbers $\mathbb{R}$.
- **Applying Partial Fractions to Improper Expressions:** Attempting partial fraction setup when $\text{degree}(P) \ge \text{degree}(Q)$. Polynomial long division must be performed first to isolate a polynomial quotient.
- **Incorrect Sign in Cube Trinomial Factor:** Writing $a^3 - b^3 = (a - b)(a^2 - ab + b^2)$. The quadratic factor takes a positive middle term: $(a^2 + ab + b^2)$.

## Quiz

1. Factorize the expression completely: $8x^3 - 27y^3$.
  - [ ] $(2x - 3y)(4x^2 - 6xy + 9y^2)$
  - [x] $(2x - 3y)(4x^2 + 6xy + 9y^2)$
  - [ ] $(2x + 3y)(4x^2 - 6xy + 9y^2)$
  - [ ] $(2x - 3y)^3$
   > Use difference of cubes $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ with $a = 2x$ and $b = 3y$: $(2x - 3y)((2x)^2 + (2x)(3y) + (3y)^2) = (2x - 3y)(4x^2 + 6xy + 9y^2)$.

2. Decompose the rational expression into partial fractions: $\frac{5x - 1}{(x - 1)(x + 2)}$.
  - [ ] $\frac{2}{x - 1} + \frac{3}{x + 2}$
  - [x] $\frac{4}{3(x - 1)} + \frac{11}{3(x + 2)}$
  - [ ] $\frac{1}{x - 1} + \frac{4}{x + 2}$
  - [ ] $\frac{3}{x - 1} + \frac{2}{x + 2}$
   > Setup $\frac{A}{x - 1} + \frac{B}{x + 2}$. Cover-up rule: $A = \frac{5(1) - 1}{1 + 2} = \frac{4}{3}$. $B = \frac{5(-2) - 1}{-2 - 1} = \frac{-11}{-3} = \frac{11}{3}$. So result is $\frac{4/3}{x - 1} + \frac{11/3}{x + 2}$.

3. Simplify the rational fraction completely: $\frac{2x^2 - 8}{x^2 - x - 6}$.
  - [ ] $\frac{2(x - 2)}{x + 3}$
  - [x] $\frac{2(x - 2)}{x - 3}$
  - [ ] $\frac{2(x + 2)}{x - 3}$
  - [ ] $\frac{x - 2}{x - 3}$
   > Factor numerator: $2(x^2 - 4) = 2(x - 2)(x + 2)$. Factor denominator: $(x - 3)(x + 2)$. Canceling $(x + 2)$ leaves $\frac{2(x - 2)}{x - 3}$.