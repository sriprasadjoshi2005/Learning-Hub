---
title: Quadratic Equations
level: intermediate
---

Quadratic equations are second-degree polynomial equations. Analyzing their roots, discriminants, graphical parabolas, and Vieta's formulas provides foundational tools for algebra, optimization, and calculus.

## Standard Form and Solution Methods

A **quadratic equation** in standard form is written as:

$$ax^2 + bx + c = 0 \quad (a \neq 0, a, b, c \in \mathbb{R})$$

### Solving Methods

1. **Factoring Method:** If $ax^2 + bx + c = (px + q)(rx + s) = 0$, set each factor to zero: $x = -\frac{q}{p}$ or $x = -\frac{s}{r}$.
2. **Completing the Square:** Transform $ax^2 + bx + c = 0$ into $(x + h)^2 = k$.
3. **The Quadratic Formula:** Derived by completing the square for general coefficients:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

## The Discriminant and Vieta's Formulas

### The Discriminant ($\Delta$) and Nature of Roots

The term under the radical in the quadratic formula, $\Delta = b^2 - 4ac$, dictates the nature of the roots:

- **$\Delta > 0$:** Two distinct real roots. (If $\Delta$ is a perfect square, roots are rational; otherwise, irrational conjugate surds).
- **$\Delta = 0$:** Exactly one real root (a repeated/double root: $x = -\frac{b}{2a}$).
- **$\Delta < 0$:** No real roots (two complex conjugate roots: $x = \alpha \pm i \beta$).

### Vieta's Formulas for Quadratic Equations

If $\alpha$ and $\beta$ are the roots of $ax^2 + bx + c = 0$:

- **Sum of Roots:**
$$\alpha + \beta = -\frac{b}{a}$$

- **Product of Roots:**
$$\alpha \cdot \beta = \frac{c}{a}$$

- **Reconstructing Equation from Roots:** Given roots $\alpha$ and $\beta$, the quadratic equation is:
$$x^2 - (\alpha + \beta)x + (\alpha \cdot \beta) = 0$$

## Discriminant & Root Classification Table

| Discriminant Value ($\Delta = b^2 - 4ac$) | Nature of Roots | Graph Intercepts ($y = ax^2+bx+c$) |
|---|---|---|
| $\Delta > 0$ (Perfect Square) | Two distinct rational roots | Intersects $x$-axis at two distinct rational points |
| $\Delta > 0$ (Non-Square) | Two distinct irrational conjugate roots | Intersects $x$-axis at two distinct irrational points |
| $\Delta = 0$ | One real repeated root | Touches $x$-axis tangentially at one vertex point |
| $\Delta < 0$ | Two complex conjugate roots | Does not intersect $x$-axis at all |

## Important Formulas and Identity Relations

Difference of Roots Formula:

$$|\alpha - \beta| = \frac{\sqrt{b^2 - 4ac}}{|a|} = \frac{\sqrt{\Delta}}{|a|}$$

Sum of Squares of Roots:

$$\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta = \left(-\frac{b}{a}\right)^2 - 2\left(\frac{c}{a}\right) = \frac{b^2 - 2ac}{a^2}$$

Vertex Form of Quadratic Function $y = ax^2 + bx + c$:

$$y = a\left(x - h\right)^2 + k \quad \text{where } h = -\frac{b}{2a}, \quad k = c - \frac{b^2}{4a} = -\frac{\Delta}{4a}$$

## Common Exam Traps

- **Denominator Error in Quadratic Formula:** Writing $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{a}$ instead of $2a$.
- **Sign Error in Sum of Roots:** Writing $\alpha + \beta = \frac{b}{a}$ instead of $-\frac{b}{a}$.
- **Ignoring Non-Zero Coefficient Constraint $a \neq 0$:** Treating $ax^2 + bx + c = 0$ as a quadratic when $a = 0$ (which reduces it to a linear equation).

## Quiz

1. Determine the nature of the roots for the quadratic equation $3x^2 - 5x + 4 = 0$.
  - [ ] Two distinct rational roots
  - [ ] Two distinct irrational roots
  - [ ] One repeated real root
  - [x] Two complex conjugate roots (no real roots)
   > Calculate discriminant $\Delta = b^2 - 4ac = (-5)^2 - 4(3)(4) = 25 - 48 = -23$. Since $\Delta < 0$, the equation has no real roots (two complex conjugate roots).

2. If $\alpha$ and $\beta$ are roots of $2x^2 - 6x + 3 = 0$, what is the exact numerical value of $\frac{1}{\alpha} + \frac{1}{\beta}$?
  - [ ] $1$
  - [x] $2$
  - [ ] $3$
  - [ ] $\frac{1}{2}$
   > By Vieta's formulas: $\alpha + \beta = -\frac{-6}{2} = 3$ and $\alpha \beta = \frac{3}{2}$. Now, $\frac{1}{\alpha} + \frac{1}{\beta} = \frac{\alpha + \beta}{\alpha \beta} = \frac{3}{3/2} = 3 \times \frac{2}{3} = 2$.

3. Construct the quadratic equation whose roots are $\alpha = 4$ and $\beta = -2$.
  - [ ] $x^2 + 2x - 8 = 0$
  - [x] $x^2 - 2x - 8 = 0$
  - [ ] $x^2 - 6x + 8 = 0$
  - [ ] $x^2 + 2x + 8 = 0$
   > Sum of roots $= 4 + (-2) = 2$. Product of roots $= 4 \times (-2) = -8$. The quadratic equation form is $x^2 - (\text{Sum})x + (\text{Product}) = 0 \implies x^2 - 2x - 8 = 0$.