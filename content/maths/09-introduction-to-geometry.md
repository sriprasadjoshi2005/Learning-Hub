---
title: Introduction to Geometry
level: foundation
---

Geometry is the mathematical study of shapes, sizes, positions, angles, and dimensions of objects. Mastering fundamental geometric axioms, parallel line relationships, and polygon properties establishes the basis for spatial reasoning and formal mathematical proofs.

## Points, Lines, Angles, and Parallel Line Theorems

- **Point, Line, and Plane:** Undefined foundational terms. A line extends infinitely in two directions; a ray has one endpoint and extends infinitely in one direction; a line segment has two fixed endpoints.
- **Angle Classifications:**
  - *Acute Angle:* $0^\circ < \theta < 90^\circ$
  - *Right Angle:* $\theta = 90^\circ$
  - *Obtuse Angle:* $90^\circ < \theta < 180^\circ$
  - *Straight Angle:* $\theta = 180^\circ$
  - *Reflex Angle:* $180^\circ < \theta < 360^\circ$
- **Angle Relationships:**
  - *Complementary Angles:* Two angles whose sum is $90^\circ$.
  - *Supplementary Angles:* Two angles whose sum is $180^\circ$.
  - *Vertically Opposite Angles:* Formed by intersecting lines; they are equal ($\theta_1 = \theta_2$).

### Angles Formed by Parallel Lines and a Transversal

When two parallel lines ($L_1 \parallel L_2$) are intersected by a transversal line $T$:

1. **Corresponding Angles are Equal:** $\angle 1 = \angle 5$.
2. **Alternate Interior Angles are Equal:** $\angle 3 = \angle 6$ and $\angle 4 = \angle 5$.
3. **Alternate Exterior Angles are Equal:** $\angle 1 = \angle 8$ and $\angle 2 = \angle 7$.
4. **Consecutive Interior Angles are Supplementary:** $\angle 3 + \angle 5 = 180^\circ$ and $\angle 4 + \angle 6 = 180^\circ$.

## Polygon Properties and Angle Sum Theorems

A **polygon** is a closed 2D shape bounded by straight line segments. A **regular polygon** has all sides equal (equilateral) and all interior angles equal (equiangular).

### Polygon Formulas for an $n$-sided Polygon

- **Sum of Interior Angles ($S_{\text{int}}$):**
$$S_{\text{int}} = (n - 2) \times 180^\circ$$

- **Each Interior Angle of a Regular $n$-gon ($\theta_{\text{int}}$):**
$$\theta_{\text{int}} = \frac{(n - 2) \times 180^\circ}{n}$$

- **Sum of Exterior Angles ($S_{\text{ext}}$):** For any convex polygon, the sum of exterior angles is always:
$$S_{\text{ext}} = 360^\circ$$

- **Number of Diagonals in an $n$-sided Polygon ($D$):**
$$D = \frac{n(n - 3)}{2}$$

## Polygon Angle Summary Table

| Polygon Name | Sides ($n$) | Sum of Interior Angles | Single Interior Angle (Regular) | Number of Diagonals |
|---|---|---|---|---|
| Triangle | $3$ | $180^\circ$ | $60^\circ$ | $0$ |
| Quadrilateral | $4$ | $360^\circ$ | $90^\circ$ | $2$ |
| Pentagon | $5$ | $540^\circ$ | $108^\circ$ | $5$ |
| Hexagon | $6$ | $720^\circ$ | $120^\circ$ | $9$ |
| Octagon | $8$ | $1080^\circ$ | $135^\circ$ | $20$ |
| Decagon | $10$ | $1440^\circ$ | $144^\circ$ | $35$ |

## Important Formulas and Geometric Axioms

Triangle Angle Sum Theorem:

$$\alpha + \beta + \gamma = 180^\circ$$

Exterior Angle Theorem of a Triangle:

$$\theta_{\text{ext}} = \alpha + \beta \quad (\text{Sum of two interior opposite angles})$$

Exterior and Interior Angle Relationship at any Vertex:

$$\theta_{\text{int}} + \theta_{\text{ext}} = 180^\circ$$

## Common Exam Traps

- **Confusing Consecutive Interior and Alternate Angles:** Assuming consecutive interior angles are equal. They are **supplementary** ($\text{sum} = 180^\circ$), whereas alternate interior angles are equal.
- **Applying Regular Polygon Formulas to Irregular Polygons:** Using $\frac{(n-2) \times 180^\circ}{n}$ to find an individual interior angle of a polygon that is not equiangular.
- **Misidentifying Exterior Angles:** An exterior angle is formed by extending **one** side of a polygon, not by extending both sides (which forms vertically opposite interior angles).

## Quiz

1. If two parallel lines are cut by a transversal and one consecutive interior angle measures $75^\circ$, what is the measure of the other consecutive interior angle?
  - [ ] $75^\circ$
  - [x] $105^\circ$
  - [ ] $15^\circ$
  - [ ] $285^\circ$
   > Consecutive interior angles along parallel lines are supplementary: $\theta + 75^\circ = 180^\circ \implies \theta = 180^\circ - 75^\circ = 105^\circ$.

2. What is the measure of each interior angle of a regular octagon ($8$-sided polygon)?
  - [ ] $108^\circ$
  - [ ] $120^\circ$
  - [x] $135^\circ$
  - [ ] $140^\circ$
   > Using the interior angle formula for $n = 8$: $\theta_{\text{int}} = \frac{(8 - 2) \times 180^\circ}{8} = \frac{6 \times 180^\circ}{8} = \frac{1080^\circ}{8} = 135^\circ$.

3. How many distinct diagonals can be drawn inside a convex hexagon ($6$-sided polygon)?
  - [ ] $6$
  - [x] $9$
  - [ ] $12$
  - [ ] $15$
   > Using the diagonal formula $D = \frac{n(n - 3)}{2}$ for $n = 6$: $D = \frac{6(6 - 3)}{2} = \frac{6 \times 3}{2} = 9$.