---
title: Advanced Coordinate Geometry- Conic Sections
level: advanced
---

Conic sections are curves formed by intersecting a double-napped cone with a plane. Analyzing parabolas, ellipses, and hyperbolas through focus-directrix definitions and standard equations provides vital tools for celestial mechanics, optics, and geometry.

## Unified Definition and Eccentricity

A **conic section** is the locus of a point $P$ moving such that its distance from a fixed point (the **focus** $F$) divided by its perpendicular distance from a fixed line (the **directrix** $D$) equals a constant **eccentricity ($e$)**:

$$e = \frac{PF}{PD}$$

- **Circle:** $e = 0$
- **Parabola:** $e = 1$
- **Ellipse:** $0 < e < 1$
- **Hyperbola:** $e > 1$

## Standard Equations and Structural Features

### 1. Parabola ($y^2 = 4ax$)

- **Focus:** $(a, 0)$, **Directrix:** $x = -a$
- **Vertex:** $(0, 0)$, **Latus Rectum Length:** $4a$

### 2. Ellipse ($\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, a > b$)

- **Foci:** $(\pm ae, 0)$, **Directrices:** $x = \pm \frac{a}{e}$
- **Eccentricity Relation:** $b^2 = a^2(1 - e^2) \implies e = \sqrt{1 - \frac{b^2}{a^2}}$
- **Latus Rectum Length:** $\frac{2b^2}{a}$

### 3. Hyperbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$)

- **Foci:** $(\pm ae, 0)$, **Directrices:** $x = \pm \frac{a}{e}$
- **Eccentricity Relation:** $b^2 = a^2(e^2 - 1) \implies e = \sqrt{1 + \frac{b^2}{a^2}}$
- **Asymptotes:** $y = \pm \frac{b}{a} x$
- **Rectangular Hyperbola:** $x^2 - y^2 = a^2$ (when $a = b$, $e = \sqrt{2}$).

## Conic Section Comparison Table

| Conic Type | Standard Equation | Eccentricity ($e$) | Focal Distance / Foci | Latus Rectum Length |
|---|---|---|---|---|
| Parabola | $y^2 = 4ax$ | $e = 1$ | Focus $(a, 0)$ | $4a$ |
| Ellipse ($a > b$) | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $e = \sqrt{1 - \frac{b^2}{a^2}} < 1$ | Foci $(\pm ae, 0)$ | $\frac{2b^2}{a}$ |
| Hyperbola | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | $e = \sqrt{1 + \frac{b^2}{a^2}} > 1$ | Foci $(\pm ae, 0)$ | $\frac{2b^2}{a}$ |
| Rectangular Hyperbola | $x y = c^2$ | $e = \sqrt{2}$ | Foci $(\pm c\sqrt{2}, \pm c\sqrt{2})$ | $2\sqrt{2}c$ |

## Important Formulas and Tangency Conditions

Condition for Line $y = mx + c$ to be Tangent to Conics:

$$\text{Parabola } (y^2 = 4ax): c = \frac{a}{m}$$

$$\text{Ellipse } \left(\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1\right): c = \pm \sqrt{a^2 m^2 + b^2}$$

$$\text{Hyperbola } \left(\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1\right): c = \pm \sqrt{a^2 m^2 - b^2}$$

## Common Exam Traps

- **Confusing Major Axis Orientation:** Using $e = \sqrt{1 - b^2/a^2}$ when $b > a$. If $b > a$, the major axis is vertical, so $e = \sqrt{1 - a^2/b^2}$ and latus rectum is $\frac{2a^2}{b}$.
- **Mixing Up Ellipse and Hyperbola Eccentricity Formulas:** Forgetting that ellipse uses $(1 - e^2)$ while hyperbola uses $(e^2 - 1)$.
- **Sign Error in Hyperbola Asymptotes:** Writing asymptotes as $y = \pm \frac{a}{b} x$ instead of $y = \pm \frac{b}{a} x$ for horizontal hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$.

## Quiz

1. What is the eccentricity of the ellipse given by the equation $9x^2 + 25y^2 = 225$?
  - [ ] $e = \frac{3}{5}$
  - [x] $e = \frac{4}{5}$
  - [ ] $e = \frac{16}{25}$
  - [ ] $e = \frac{5}{4}$
   > Divide by $225$: $\frac{x^2}{25} + \frac{y^2}{9} = 1 \implies a^2 = 25, b^2 = 9$. Compute $e = \sqrt{1 - \frac{9}{25}} = \sqrt{\frac{16}{25}} = \frac{4}{5}$.

2. Find the focus and directrix of the parabola $y^2 = -12x$.
  - [ ] Focus $(3, 0)$, Directrix $x = -3$
  - [x] Focus $(-3, 0)$, Directrix $x = 3$
  - [ ] Focus $(0, -3)$, Directrix $y = 3$
  - [ ] Focus $(-6, 0)$, Directrix $x = 6$
   > Compare $y^2 = 4ax$ with $y^2 = -12x \implies 4a = -12 \implies a = -3$. Focus is $(a, 0) = (-3, 0)$, and directrix is $x = -a \implies x = 3$.

3. Calculate the length of the latus rectum of the hyperbola $\frac{x^2}{16} - \frac{y^2}{9} = 1$.
  - [ ] $\frac{9}{4}$
  - [ ] $\frac{9}{6}$
  - [x] $\frac{9}{2}$
  - [ ] $\frac{8}{3}$
   > Here $a^2 = 16 \implies a = 4$, and $b^2 = 9$. Latus rectum length $= \frac{2b^2}{a} = \frac{2(9)}{4} = \frac{18}{4} = \frac{9}{2}$.
