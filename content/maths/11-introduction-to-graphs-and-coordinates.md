---
title: Introduction to Graphs and Coordinates
level: foundation
---

Coordinate geometry connects algebra and geometry by representing geometric shapes on a numerical grid. The Cartesian coordinate plane enables the analysis of geometric relationships using algebraic equations.

## The Cartesian Coordinate System

The 2D Cartesian plane is formed by two perpendicular number lines: the horizontal $x$-axis and the vertical $y$-axis. Their intersection point $(0, 0)$ is called the **origin** ($O$).

- **Coordinates $(x, y)$:** An ordered pair specifying position. $x$ represents the horizontal distance (abscissa) and $y$ represents the vertical distance (ordinate).
- **Quadrants:** The axes divide the plane into four quadrants:
  - Quadrant I: $x > 0, y > 0$
  - Quadrant II: $x < 0, y > 0$
  - Quadrant III: $x < 0, y < 0$
  - Quadrant IV: $x > 0, y < 0$

### Fundamental Distance and Midpoint Formulas

For any two points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ in the Cartesian plane:

1. **Distance Formula:** Derived from the Pythagorean theorem:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

2. **Midpoint Formula:** Calculates the coordinates of the midpoint $M$ of the segment $P_1P_2$:
$$M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$$

3. **Section Formula (Internal Division):** Coordinates of point $R$ dividing $P_1P_2$ in the ratio $m : n$:
$$R = \left( \frac{m x_2 + n x_1}{m + n}, \frac{m y_2 + n y_1}{m + n} \right)$$

## Line Slope and Linear Equations

### Slope (Gradient) of a Straight Line

The **slope** $m$ measures the steepness and direction of a line connecting $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$:

$$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} \quad (x_1 \neq x_2)$$

Alternatively, if $\theta$ is the angle of inclination with the positive $x$-axis: $m = \tan \theta$.

### Forms of Linear Equations

- **Slope-Intercept Form:** $y = mx + c$, where $m$ is the slope and $c$ is the $y$-intercept.
- **Point-Slope Form:** $y - y_1 = m(x - x_1)$.
- **Two-Point Form:** $y - y_1 = \left( \frac{y_2 - y_1}{x_2 - x_1} \right) (x - x_1)$.
- **Intercept Form:** $\frac{x}{a} + \frac{y}{b} = 1$, where $a$ is the $x$-intercept and $b$ is the $y$-intercept.
- **General Form:** $Ax + By + C = 0$, with slope $m = -\frac{A}{B}$.

## Coordinate Geometry Formula Master Table

| Concept | Formula / Relation | Conditions / Notes |
|---|---|---|
| Distance | $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ | Always non-negative ($d \ge 0$) |
| Midpoint | $M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$ | Equidistant from both endpoints |
| Parallel Lines Slope | $m_1 = m_2$ | Same steepness, non-intersecting |
| Perpendicular Lines Slope | $m_1 \cdot m_2 = -1 \implies m_2 = -\frac{1}{m_1}$ | Lines intersect at $90^\circ$ |
| Area of Triangle | $A = \frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$ | Vertices $(x_1, y_1), (x_2, y_2), (x_3, y_3)$ |

## Important Formulas and Geometric Conditions

Condition for Collinearity of Three Points $A, B, C$:

$$\text{Area}(\triangle ABC) = 0 \iff \frac{y_2 - y_1}{x_2 - x_1} = \frac{y_3 - y_2}{x_3 - x_2}$$

Distance from Point $(x_0, y_0)$ to Line $Ax + By + C = 0$:

$$d = \frac{|A x_0 + B y_0 + C|}{\sqrt{A^2 + B^2}}$$

## Common Exam Traps

- **Perpendicular Slope Sign Error:** Forgetting to change the sign when taking the negative reciprocal. If $m_1 = 3$, $m_2 = -\frac{1}{3}$, not $+\frac{1}{3}$.
- **Order Inconsistency in Slope:** Computing $\frac{y_2 - y_1}{x_1 - x_2}$. The point order must match in numerator and denominator: $\frac{y_2 - y_1}{x_2 - x_1}$.
- **Confusing $x$- and $y$-Intercepts:** Setting $x = 0$ to find the $x$-intercept. The $x$-intercept occurs when $y = 0$, and the $y$-intercept occurs when $x = 0$.

## Quiz

1. Find the distance between the points $A(-2, 5)$ and $B(4, -3)$ in the Cartesian plane.
  - [ ] $8$ units
  - [x] $10$ units
  - [ ] $\sqrt{52}$ units
  - [ ] $14$ units
   > Apply the distance formula: $d = \sqrt{(4 - (-2))^2 + (-3 - 5)^2} = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.

2. What is the equation of the line passing through point $(2, -1)$ and perpendicular to the line $3x - 4y + 8 = 0$?
  - [ ] $3x - 4y - 10 = 0$
  - [ ] $4x + 3y - 11 = 0$
  - [x] $4x + 3y - 5 = 0$
  - [ ] $4x - 3y - 11 = 0$
   > Slope of given line is $m_1 = \frac{3}{4}$. Perpendicular slope is $m_2 = -\frac{4}{3}$. Point-slope equation: $y - (-1) = -\frac{4}{3}(x - 2) \implies 3(y + 1) = -4(x - 2) \implies 3y + 3 = -4x + 8 \implies 4x + 3y - 5 = 0$.

3. In which quadrant does the midpoint of the line segment joining $(-5, 8)$ and $(-1, -2)$ lie?
  - [ ] Quadrant I
  - [x] Quadrant II
  - [ ] Quadrant III
  - [ ] Quadrant IV
   > Midpoint $M = \left( \frac{-5 + (-1)}{2}, \frac{8 + (-2)}{2} \right) = \left( \frac{-6}{2}, \frac{6}{2} \right) = (-3, 3)$. Since $x < 0$ and $y > 0$, it lies in Quadrant II.