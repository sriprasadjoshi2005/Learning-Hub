---
title: Advanced Trigonometry and Coordinate Geometry
level: exam
---

Competitive examination items in trigonometry and coordinate geometry demand high-speed elimination, auxiliary parameter substitutions, locus determination, and advanced conic tangents.

## Advanced Inverse Trigonometric Identities and Conditional Sums

### Inverse Trigonometric Identities

- **Principal Domain Definitions:**
  - $\arcsin(x) \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
  - $\arccos(x) \in [0, \pi]$
  - $\arctan(x) \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
- **Complementary Sum Identity:**
  $$\arcsin(x) + \arccos(x) = \frac{\pi}{2} \quad (|x| \le 1)$$
- **Addition Formula for Arctangent ($x y < 1$):**
  $$\arctan(x) + \arctan(y) = \arctan\left(\frac{x + y}{1 - x y}\right)$$

## Locus Problems and Advanced Conic Tangents

### Locus Solving Methodology

1. Assume the moving point whose locus is required to be $(h, k)$.
2. Write down given geometric conditions involving $(h, k)$ and auxiliary parameters.
3. Eliminate all auxiliary parameters algebraically to obtain an equation in $h$ and $k$.
4. Replace $h \to x$ and $k \to y$ to state the final locus equation.

### Director Circle

The locus of the point of intersection of two **perpendicular tangents** to a conic:

- **Circle ($x^2 + y^2 = r^2$):** Director circle is $x^2 + y^2 = 2r^2$.
- **Ellipse ($\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$):** Director circle is $x^2 + y^2 = a^2 + b^2$.
- **Hyperbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$):** Director circle is $x^2 + y^2 = a^2 - b^2 \quad (a > b)$.

## Advanced Trig & Conic Formula Master Table

| Conic Section | Director Circle Equation | Tangent Condition ($y = mx + c$) | Parametric Coordinates |
|---|---|---|---|
| Parabola $y^2 = 4ax$ | Directrix $x = -a$ | $c = \frac{a}{m}$ | $(a t^2, 2 a t)$ |
| Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $x^2 + y^2 = a^2 + b^2$ | $c = \pm \sqrt{a^2 m^2 + b^2}$ | $(a \cos \theta, b \sin \theta)$ |
| Hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | $x^2 + y^2 = a^2 - b^2$ | $c = \pm \sqrt{a^2 m^2 - b^2}$ | $(a \sec \theta, b \tan \theta)$ |

## Important Formulas and Conditional Identities

Conditional Trigonometric Product Identity ($A + B + C = \pi$):

$$\sin(2A) + \sin(2B) + \sin(2C) = 4 \sin A \sin B \sin C$$

$$\tan A + \tan B + \tan C = \tan A \tan B \tan C$$

Director Circle Radius Ratio for Standard Circle:

$$R_{\text{director}} = \sqrt{2} \cdot R_{\text{original}}$$

## Common Exam Traps

- **Ignoring Domain Restrictions in Arctan Sum:** Applying $\arctan x + \arctan y = \arctan\left(\frac{x+y}{1-xy}\right)$ when $xy > 1$. If $x > 0, y > 0$ and $xy > 1$, the formula requires adding $\pi$: $\pi + \arctan\left(\frac{x+y}{1-xy}\right)$.
- **Principal Value Range Violation:** Evaluating $\arcsin\left(\sin\frac{3\pi}{4}\right)$ as $\frac{3\pi}{4}$. Since range of $\arcsin$ is $[-\frac{\pi}{2}, \frac{\pi}{2}]$, the correct answer is $\frac{\pi}{4}$.
- **Confusing Parabola Director Circle:** Looking for a circular equation for parabola perpendicular tangents. Perpendicular tangents to a parabola intersect on its **directrix line** $x = -a$.

## Quiz

1. Evaluate the exact principal value of $\arctan(1) + \arctan(2) + \arctan(3)$.
  - [ ] $\frac{\pi}{2}$
  - [x] $\pi$
  - [ ] $\frac{3\pi}{4}$
  - [ ] $2\pi$
   > $\arctan(1) = \frac{\pi}{4}$. For $\arctan(2) + \arctan(3)$, since $xy = 2 \times 3 = 6 > 1$, use formula $\pi + \arctan\left(\frac{2+3}{1 - 6}\right) = \pi + \arctan(-1) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$. Adding $\frac{\pi}{4} + \frac{3\pi}{4} = \pi$.

2. Find the equation of the director circle of the ellipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$.
  - [ ] $x^2 + y^2 = 7$
  - [x] $x^2 + y^2 = 25$
  - [ ] $x^2 + y^2 = 144$
  - [ ] $x^2 + y^2 = 5$
   > Director circle of ellipse is $x^2 + y^2 = a^2 + b^2$. Here $a^2 = 16$ and $b^2 = 9 \implies x^2 + y^2 = 16 + 9 = 25$.

3. What is the locus of the point of intersection of perpendicular tangents to the parabola $y^2 = 8x$?
  - [ ] $x^2 + y^2 = 16$
  - [x] $x = -2$
  - [ ] $x = -4$
  - [ ] $y = -2$
   > Perpendicular tangents to parabola $y^2 = 4ax$ intersect on its directrix $x = -a$. Here $4a = 8 \implies a = 2$, so directrix is $x = -2$.