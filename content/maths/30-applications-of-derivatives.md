---
title: Applications of Derivatives
level: advanced
---

Applications of derivatives include geometric analysis of curves, finding rates of change, determining intervals of monotonicity, locating extrema, solving optimization problems, and sketching graphs.

## Tangents, Normals, and Monotonicity

### Equations of Tangent and Normal Lines

For a curve y = f(x) at point P(x0, y0):

- **Tangent Line Slope:** mt = f'(x0)
- **Tangent Line Equation:** y - y0 = f'(x0)(x - x0)
- **Normal Line Slope:** mn = -1 / f'(x0), provided f'(x0) is not zero.
- **Normal Line Equation:** y - y0 = -1 / f'(x0) * (x - x0)

### Monotonicity (Increasing / Decreasing Intervals)

Let f be continuous on [a, b] and differentiable on (a, b):

- **Strictly Increasing:** f'(x) > 0 for all x in (a, b).
- **Strictly Decreasing:** f'(x) < 0 for all x in (a, b).
- **Constant:** f'(x) = 0 for all x in (a, b).

## Extrema and Concavity

### Critical Points and Local Extrema

A **critical point** occurs where f'(c) = 0 or f'(c) is undefined.

1. **First Derivative Test:**
   - Local Maximum: f'(x) changes sign from positive (+) to negative (-) at c.
   - Local Minimum: f'(x) changes sign from negative (-) to positive (+) at c.
   - No Extrema: f'(x) does not change sign at c.

2. **Second Derivative Test:** Let f'(c) = 0:
   - f''(c) < 0 means a local maximum at x = c.
   - f''(c) > 0 means a local minimum at x = c.
   - f''(c) = 0 means the test is inconclusive. Use the First Derivative Test.

### Concavity and Inflection Points

- **Concave Upwards:** f''(x) > 0. The graph lies above its tangent lines locally.
- **Concave Downwards:** f''(x) < 0. The graph lies below its tangent lines locally.
- **Point of Inflection:** A point where concavity changes sign. This may occur where f''(c) = 0 or is undefined, provided the sign of f'' changes.

## Derivative Applications Master Table

| Problem Type | Derivative Criterion | Geometric / Physical Meaning |
|---|---|---|
| Slope of Tangent | m = f'(x0) | Direction of tangent line |
| Slope of Normal | m = -1/f'(x0) | Perpendicular line to curve |
| Increasing Function | f'(x) > 0 | Positive curve gradient |
| Local Maximum | f'(c) = 0, f''(c) < 0 | Peak point of curve |
| Local Minimum | f'(c) = 0, f''(c) > 0 | Trough point of curve |
| Inflection Point | f''(c) = 0 with sign change | Transition in concavity |

## Important Formulas and Optimization Theorem

### Rolle's Theorem

If f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there exists at least one c in (a, b) such that:

f'(c) = 0

### Mean Value Theorem (MVT)

If f is continuous on [a, b] and differentiable on (a, b), then there exists at least one c in (a, b) such that:

f'(c) = [f(b) - f(a)] / (b - a)

## Common Exam Traps

- **Assuming f'(c) = 0 Guarantees an Extremum:** Every stationary point is not necessarily a maximum or minimum. For example, f(x) = x³ at x = 0 has f'(0) = 0, but it is an inflection point, not an extremum.
- **Normal Line Slope Sign Error:** Remember the negative reciprocal: mn = -1/f'(x0).
- **Inconclusive Second Derivative Test:** Assuming f''(c) = 0 means there are no extrema is incorrect. The test is inconclusive and requires checking the First Derivative Test.
- **Increasing and Decreasing Intervals:** Use the sign of the first derivative, not the sign of the function itself.
- **Inflection Points:** A point where f''(x) = 0 is not automatically an inflection point. Concavity must actually change.

## Quiz

1. Find the equation of the tangent line to the curve y = x³ - 3x + 2 at the point (2, 4).
- [ ] y = 9x - 12
- [x] y = 9x - 14
- [ ] y = 9x + 4
- [ ] y = 3x - 2

> Derivative f'(x) = 3x² - 3. At x = 2, slope m = f'(2) = 3(2)² - 3 = 12 - 3 = 9.
>
> Equation of tangent:
>
> y - 4 = 9(x - 2)
>
> y - 4 = 9x - 18
>
> y = 9x - 14.

2. Find the local minimum value of the function f(x) = x² - 6x + 13.
- [ ] x = 3
- [x] f(3) = 4
- [ ] f(3) = 13
- [ ] f(0) = 13

> f'(x) = 2x - 6 = 0 gives x = 3.
>
> Second derivative f''(x) = 2 > 0, so x = 3 is a local minimum.
>
> The minimum value is:
>
> f(3) = 3² - 6(3) + 13 = 9 - 18 + 13 = 4.

3. For what values of x is the function f(x) = 2x³ - 9x² + 12x - 5 strictly increasing?
- [ ] (1, 2)
- [x] (-infinity, 1) union (2, infinity)
- [ ] (1, infinity)
- [ ] (-infinity, 2)

> Differentiate:
>
> f'(x) = 6x² - 18x + 12
>
> f'(x) = 6(x² - 3x + 2)
>
> f'(x) = 6(x - 1)(x - 2)
>
> The function is strictly increasing when f'(x) > 0.
>
> Therefore, x < 1 or x > 2.
>
> Answer: (-infinity, 1) union (2, infinity).
