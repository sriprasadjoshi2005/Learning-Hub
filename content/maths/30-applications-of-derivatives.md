---
title: Applications of Derivatives
level: advanced
---

Applications of derivatives include geometric analysis of curves, finding rates of change, determining intervals of monotonicity, locating extrema, solving optimization problems, and sketching graphs.

## Tangents, Normals, and Monotonicity

### Equations of Tangent and Normal Lines

For a curve $y = f(x)$ at point $P(x_0, y_0)$:

- **Tangent Line Slope:** $m_t = f'(x_0)$
- **Tangent Line Equation:**
$$y - y_0 = f'(x_0)(x - x_0)$$
- **Normal Line Slope:** $m_n = -\frac{1}{f'(x_0)} \quad (f'(x_0) \neq 0)$
- **Normal Line Equation:**
$$y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)$$

### Monotonicity (Increasing / Decreasing Intervals)

Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$:

- **Strictly Increasing:** $f'(x) > 0$ for all $x \in (a, b)$.
- **Strictly Decreasing:** $f'(x) < 0$ for all $x \in (a, b)$.
- **Constant:** $f'(x) = 0$ for all $x \in (a, b)$.

## Extrema and Concavity

### Critical Points and Local Extrema

A **critical point** occurs where $f'(c) = 0$ or $f'(c)$ is undefined.

1. **First Derivative Test:**
  - Local Maximum: $f'(x)$ changes sign from positive ($+$) to negative ($-$) at $c$.
  - Local Minimum: $f'(x)$ changes sign from negative ($-$) to positive ($+$) at $c$.
  - No Extrema: $f'(x)$ does not change sign at $c$.

2. **Second Derivative Test:** Let $f'(c) = 0$:
  - $f''(c) < 0 \implies$ Local Maximum at $x = c$.
  - $f''(c) > 0 \implies$ Local Minimum at $x = c$.
  - $f''(c) = 0 \implies$ Inconclusive (must use First Derivative Test).

### Concavity and Inflection Points

- **Concave Upwards:** $f''(x) > 0$ (Graph lies above tangent lines).
- **Concave Downwards:** $f''(x) < 0$ (Graph lies below tangent lines).
- **Point of Inflection:** Point where concavity changes sign ($f''(c) = 0$ or undefined, with sign change in $f''$).

## Derivative Applications Master Table

| Problem Type | Derivative Criterion | Geometric / Physical Meaning |
|---|---|---|
| Slope of Tangent | $m = f'(x_0)$ | Direction of tangent vector |
| Slope of Normal | $m = -1/f'(x_0)$ | Perpendicular line to curve |
| Increasing Function | $f'(x) > 0$ | Positive curve gradient |
| Local Maximum | $f'(c) = 0, f''(c) < 0$ | Peak point of curve |
| Local Minimum | $f'(c) = 0, f''(c) > 0$ | Trough point of curve |
| Inflection Point | $f''(c) = 0$ (with sign change) | Transition in concavity |

## Important Formulas and Optimization Theorem

Rolle's Theorem:

$$\text{If } f \text{ continuous on } [a, b], \text{ diff. on } (a, b), \text{ and } f(a) = f(b) \implies \exists c \in (a, b) \text{ s.t. } f'(c) = 0$$

Mean Value Theorem (MVT):

$$\text{If } f \text{ continuous on } [a, b] \text{ and diff. on } (a, b) \implies \exists c \in (a, b) \text{ s.t. } f'(c) = \frac{f(b) - f(a)}{b - a}$$

## Common Exam Traps

- **Assuming $f'(c) = 0$ Guarantees an Extremum:** Treating every stationary point as a max/min (e.g., $f(x) = x^3$ at $x = 0$ has $f'(0) = 0$, but it is an inflection point, not an extremum).
- **Normal Line Slope Sign Error:** Forgetting the negative sign when taking the reciprocal slope: writing $m_n = \frac{1}{f'(x_0)}$ instead of $-\frac{1}{f'(x_0)}$.
- **Inconclusive Second Derivative Test:** Assuming $f''(c) = 0$ means there are no extrema. When $f''(c) = 0$, the test is **inconclusive** and requires checking the First Derivative Test.

## Quiz

1. Find the equation of the tangent line to the curve $y = x^3 - 3x + 2$ at the point $(2, 4)$.
  - [ ] $y = 9x - 14$
  - [x] $y = 9x - 14$
  - [ ] $y = 9x + 4$
  - [ ] $y = 3x - 2$
   > Derivative $f'(x) = 3x^2 - 3$. At $x = 2$, slope $m = f'(2) = 3(2)^2 - 3 = 12 - 3 = 9$. Equation of tangent: $y - 4 = 9(x - 2) \implies y - 4 = 9x - 18 \implies y = 9x - 14$.

2. Find the local minimum value of the function $f(x) = x^2 - 6x + 13$.
  - [ ] $x = 3$
  - [x] $f(3) = 4$
  - [ ] $f(3) = 13$
  - [ ] $f(0) = 13$
   > $f'(x) = 2x - 6 = 0 \implies x = 3$. Second derivative $f''(x) = 2 > 0$, so $x = 3$ is a local minimum. The minimum **value** is $f(3) = (3)^2 - 6(3) + 13 = 9 - 18 + 13 = 4$.

3. For what values of $x$ is the function $f(x) = 2x^3 - 9x^2 + 12x - 5$ strictly increasing?
  - [ ] $(1, 2)$
  - [x] $(-\infty, 1) \cup (2, \infty)$
  - [ ] $(1, \infty)$
  - [ ] $(-\infty, 2)$
   > Differentiate: $f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x - 1)(x - 2)$. $f'(x) > 0$ when $(x - 1)(x - 2) > 0 \implies x < 1$ or $x > 2$, which is $(-\infty, 1) \cup (2, \infty)$.