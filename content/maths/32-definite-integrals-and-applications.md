---
title: Definite Integrals and Applications
level: advanced
---

Definite integrals compute net accumulated quantities over an interval $[a, b]$, enabling the calculation of planar areas, volumes of solids of revolution, and mean values of continuous functions.

## The Fundamental Theorem of Calculus and Properties

The **definite integral** of $f(x)$ from $a$ to $b$ represents the net signed area bounded by $y = f(x)$ and the $x$-axis:

$$\int_{a}^{b} f(x) \, dx$$

### Fundamental Theorem of Calculus (FTC)

1. **Part 1 (Area Function Derivative):** If $F(x) = \int_{a}^{x} f(t) \, dt$, then $F'(x) = f(x)$.
2. **Part 2 (Evaluation Theorem):** If $F'(x) = f(x)$, then:
$$\int_{a}^{b} f(x) \, dx = F(b) - F(a) = \Big[ F(x) \Big]_{a}^{b}$$

### Key Properties of Definite Integrals

- **Reversal of Limits:** $\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$
- **Interval Additivity:** $\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx$
- **Symmetry Properties:**
  - If $f(x)$ is **even** ($f(-x) = f(x)$): $\int_{-a}^{a} f(x) \, dx = 2 \int_{0}^{a} f(x) \, dx$
  - If $f(x)$ is **odd** ($f(-x) = -f(x)$): $\int_{-a}^{a} f(x) \, dx = 0$

## Area and Volume of Revolution

### Area Between Curves

The area $A$ enclosed between $y = f(x)$ and $y = g(x)$ where $f(x) \ge g(x)$ over $[a, b]$ is:

$$A = \int_{a}^{b} \Big[ f(x) - g(x) \Big] \, dx$$

### Volume of Solids of Revolution (Disk Method)

Revolving a region bounded by $y = f(x)$ around the $x$-axis from $x = a$ to $x = b$ creates a solid of volume $V$:

$$V = \pi \int_{a}^{b} \Big[ f(x) \Big]^2 \, dx$$

## Definite Integral Applications Table

| Geometric Application | Integral Formula | Integration Axis / Variable |
|---|---|---|
| Net Signed Area | $\int_{a}^{b} f(x) \, dx$ | $x$-axis |
| Total Enclosed Area | $\int_{a}^{b} |f(x)| \, dx$ | Absolute positive area |
| Area Between Curves | $\int_{a}^{b} [f(x) - g(x)] \, dx$ | Top curve minus bottom curve |
| Volume (Disk Method) | $\pi \int_{a}^{b} [f(x)]^2 \, dx$ | Revolution around $x$-axis |
| Average Value of $f(x)$ | $f_{\text{avg}} = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx$ | Mean function height |

## Important Formulas and Kings' Property Theorem

King's Property of Definite Integrals:

$$\int_{a}^{b} f(x) \, dx = \int_{a}^{b} f(a + b - x) \, dx$$

Average Value Formula:

$$f_{\text{avg}} = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx$$

## Common Exam Traps

- **Computing Area Without Absolute Value:** Integrating $f(x)$ directly over an interval where it dips below the $x$-axis, causing positive and negative areas to cancel out.
- **Forgetting $\pi$ in Volume Formulas:** Leaving out the factor of $\pi$ in disk method calculations: $\int_{a}^{b} y^2 \, dx$ instead of $\pi \int_{a}^{b} y^2 \, dx$.
- **Not Changing Limits during $u$-Substitution:** Substituting $u = g(x)$ without converting the limits of integration from $x = a, b$ to $u = g(a), g(b)$.

## Quiz

1. Evaluate the definite integral: $\int_{-3}^{3} (x^3 - 4x) \, dx$.
  - [ ] $18$
  - [x] $0$
  - [ ] $36$
  - [ ] $-12$
   > The integrand $f(x) = x^3 - 4x$ is an odd function because $f(-x) = (-x)^3 - 4(-x) = -x^3 + 4x = -f(x)$. The integral of an odd function over a symmetric interval $[-a, a]$ is identically $0$.

2. Calculate the exact area bounded by the curve $y = x^2$ and the line $y = 4$.
  - [ ] $\frac{16}{3}$
  - [x] $\frac{32}{3}$
  - [ ] $\frac{8}{3}$
  - [ ] $16$
   > Intersection points: $x^2 = 4 \implies x = \pm 2$. Area $A = \int_{-2}^{2} (4 - x^2) \, dx = 2 \int_{0}^{2} (4 - x^2) \, dx = 2 \Big[ 4x - \frac{x^3}{3} \Big]_{0}^{2} = 2 \left( 8 - \frac{8}{3} \right) = 2 \left( \frac{16}{3} \right) = \frac{32}{3}$.

3. Find the average value of $f(x) = 3x^2$ over the interval $[1, 3]$.
  - [ ] $9$
  - [x] $13$
  - [ ] $26$
  - [ ] $12$
   > $f_{\text{avg}} = \frac{1}{3 - 1} \int_{1}^{3} 3x^2 \, dx = \frac{1}{2} \Big[ x^3 \Big]_{1}^{3} = \frac{1}{2} (27 - 1) = \frac{26}{2} = 13$.