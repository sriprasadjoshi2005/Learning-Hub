---
title: Graphs of Functions
level: intermediate
---

Graphing functions provides visual insight into their operational behaviors, roots, extrema, asymptotic boundaries, and symmetries. Learning transformation techniques allows for rapid sketching of complex functions from basic parent curves.

## Parent Functions and Their Graphs

Understanding fundamental parent function shapes establishes a toolkit for graphing:

1. **Linear Function:** $f(x) = x$ (Straight line through origin with slope $1$).
2. **Quadratic Function:** $f(x) = x^2$ (Parabola opening upwards with vertex at $(0, 0)$).
3. **Cubic Function:** $f(x) = x^3$ (S-shaped inflection curve through origin).
4. **Absolute Value Function:** $f(x) = |x|$ (V-shaped graph with corner at $(0, 0)$).
5. **Reciprocal Function:** $f(x) = \frac{1}{x}$ (Rectangular hyperbola with asymptotes along $x=0$ and $y=0$).
6. **Square Root Function:** $f(x) = \sqrt{x}$ (Half-parabola starting at origin for $x \ge 0$).

## Graph Transformations

Any function $g(x)$ derived from parent function $f(x)$ can be analyzed using rigid and non-rigid transformations:

### Transformation Rules ($c > 0$)

- **Vertical Shifts:**
  - $y = f(x) + c$: Shift UP by $c$ units.
  - $y = f(x) - c$: Shift DOWN by $c$ units.
- **Horizontal Shifts:**
  - $y = f(x + c)$: Shift LEFT by $c$ units.
  - $y = f(x - c)$: Shift RIGHT by $c$ units.
- **Reflections:**
  - $y = -f(x)$: Reflection across the $x$-axis (Vertical flip).
  - $y = f(-x)$: Reflection across the $y$-axis (Horizontal flip).
- **Stretching and Compressing ($a > 0$):**
  - $y = a \cdot f(x)$: Vertical stretch by factor $a$ if $a > 1$; vertical compression if $0 < a < 1$.
  - $y = f(a \cdot x)$: Horizontal compression by factor $\frac{1}{a}$ if $a > 1$; horizontal stretch if $0 < a < 1$.

## Transformation Mapping Master Table

| Equation Transformation | Graphic Effect on Parent Point $(x, y)$ | Asymptote / Feature Shift |
|---|---|---|
| $y = f(x - h) + k$ | $(x, y) \longrightarrow (x + h, y + k)$ | Vertex/Center shifts to $(h, k)$ |
| $y = -f(x)$ | $(x, y) \longrightarrow (x, -y)$ | Inverts vertical orientation |
| $y = f(-x)$ | $(x, y) \longrightarrow (-x, y)$ | Inverts horizontal orientation |
| $y = a \cdot f(x)$ | $(x, y) \longrightarrow (x, a \cdot y)$ | Vertical distance scaled by $a$ |
| $y = f(a \cdot x)$ | $(x, y) \longrightarrow \left(\frac{x}{a}, y\right)$ | Horizontal distance scaled by $\frac{1}{a}$ |

## Important Formulas and Quadratic Vertex Transformations

Quadratic Vertex Form Graphing:

$$y = a(x - h)^2 + k$$

$$\text{Vertex} = (h, k), \quad \text{Axis of Symmetry}: x = h, \quad \text{Direction}: \begin{cases} \text{Upward} & \text{if } a > 0 \\ \text{Downward} & \text{if } a < 0 \end{cases}$$

Horizontal Asymptote Rule for Rational Functions $f(x) = \frac{P(x)}{Q(x)}$:

$$\text{Horizontal Asymptote } y = \begin{cases} 0 & \text{if } \text{deg}(P) < \text{deg}(Q) \\ \frac{\text{Leading Coeff}(P)}{\text{Leading Coeff}(Q)} & \text{if } \text{deg}(P) = \text{deg}(Q) \\ \text{None (Oblique asymptote exists)} & \text{if } \text{deg}(P) = \text{deg}(Q) + 1 \end{cases}$$

## Common Exam Traps

- **Horizontal Shift Direction Error:** Assuming $f(x + 3)$ shifts right by $3$. Adding inside the function $f(x + c)$ shifts the graph **LEFT** by $c$ units.
- **Order of Multiple Transformations:** Applying shifts before stretches when transformations are written in un-factored form $f(ax + b)$. Always factor horizontal coefficients first: $f\left(a\left(x + \frac{b}{a}\right)\right)$.
- **Graphing Absolute Value of Functions:** Misinterpreting $y = |f(x)|$. The graph of $|f(x)|$ reflects all negative parts below the $x$-axis **upward** above the $x$-axis.

## Quiz

1. Describe the precise graph transformation from parent $f(x) = x^2$ to $g(x) = -(x - 4)^2 + 3$.
  - [ ] Shifted right 4, up 3, no reflection
  - [x] Shifted right 4, reflected over $x$-axis, shifted up 3
  - [ ] Shifted left 4, reflected over $y$-axis, shifted up 3
  - [ ] Shifted right 4, reflected over $y$-axis, shifted down 3
   > The term $(x - 4)^2$ shifts right by 4 units; the negative sign $-$ reflects the graph vertically across the $x$-axis; $+ 3$ shifts it up by 3 units.

2. What are the vertical and horizontal asymptotes for the rational function $f(x) = \frac{4x + 1}{2x - 6}$?
  - [ ] Vertical: $x = 6$, Horizontal: $y = 4$
  - [x] Vertical: $x = 3$, Horizontal: $y = 2$
  - [ ] Vertical: $x = 3$, Horizontal: $y = 4$
  - [ ] Vertical: $x = -3$, Horizontal: $y = 2$
   > Vertical asymptote occurs where denominator equals zero: $2x - 6 = 0 \implies x = 3$. Horizontal asymptote is the ratio of leading coefficients since degrees are equal: $y = \frac{4}{2} = 2$.

3. If point $(3, -6)$ lies on the graph of $y = f(x)$, what point must lie on the transformed graph $y = 2 f(x + 1)$?
  - [ ] $(4, -12)$
  - [x] $(2, -12)$
  - [ ] $(2, -3)$
  - [ ] $(4, -3)$
   > Transformation $f(x + 1)$ shifts $x$-coordinates left by $1$: $x' = 3 - 1 = 2$. Multiplier $2 f(x)$ doubles $y$-coordinates: $y' = 2 \times (-6) = -12$. Transformed point is $(2, -12)$.