---
title: Geometry: Triangles and Circles
level: intermediate
---

Euclidean geometry establishes structural properties of planar figures through formal proofs. Triangles and circles form the foundation of classic synthetic geometry, planar trigonometry, and coordinate proofs.

## Triangle Congruence, Similarity, and Centers

### Congruence Criteria ($\cong$)

Two triangles are congruent if their corresponding sides and angles are equal:
- **SSS:** Three pairs of corresponding sides are equal.
- **SAS:** Two pairs of sides and the included angle are equal.
- **ASA / AAS:** Two angles and one side are equal.
- **RHS:** Right angle, hypotenuse, and one side are equal.

### Similarity Criteria ($\sim$)

Two triangles are similar if corresponding angles are equal and corresponding sides are proportional:
- **AA:** Two pairs of corresponding angles are equal.
- **SAS Similarity:** Ratio of two pairs of sides is equal, and included angles are equal.
- **SSS Similarity:** Ratios of all three pairs of corresponding sides are equal.

### Classical Triangle Centers

- **Incenter ($I$):** Intersection of angle bisectors; center of inscribed circle (incircle).
- **Circumcenter ($O$):** Intersection of perpendicular bisectors of sides; center of circumscribed circle (circumcircle).
- **Centroid ($G$):** Intersection of medians; divides each median in a $2:1$ ratio from vertex to base.
- **Orthocenter ($H$):** Intersection of altitudes.

## Circle Theorems and Cyclic Quadrilaterals

- **Angle at Center Theorem:** The angle subtended by an arc at the center is twice the angle subtended by it at any point on the circumference:
$$\theta_{\text{center}} = 2 \cdot \theta_{\text{circumference}}$$
- **Angles in Same Segment:** Angles subtended by the same arc in the same segment are equal.
- **Angle in a Semicircle:** An angle subtended by a diameter is always a right angle ($90^\circ$).
- **Cyclic Quadrilateral Theorem:** Opposite angles of a cyclic quadrilateral (vertices on a circle) are supplementary:
$$A + C = 180^\circ \quad \text{and} \quad B + D = 180^\circ$$
- **Tangent-Radius Theorem:** A tangent line to a circle is perpendicular to the radius at the point of contact ($t \perp r$).
- **Alternate Segment Theorem:** The angle between a tangent and a chord equals the angle subtended by the chord in the alternate segment.

## Circle & Triangle Geometry Summary Table

| Geometric Concept | Defining Formula / Theorem | Key Structural Feature |
|---|---|---|
| Inradius ($r$) | $r = \frac{A}{s}$ | $A = \text{Area}, s = \text{Semi-perimeter}$ |
| Circumradius ($R$) | $R = \frac{a b c}{4A} = \frac{a}{2\sin A}$ | Extended Law of Sines |
| Centroid Division | $AG : GD = 2 : 1$ | $G$ is center of mass |
| Euler Line | $H, G, O$ are collinear | $HG : GO = 2 : 1$ |
| Intersecting Chords | $PA \cdot PB = PC \cdot PD$ | Power of a point theorem |
| Tangent-Secant Theorem | $PT^2 = PA \cdot PB$ | $PT$ is tangent, $PAB$ is secant |

## Important Formulas and Synthetic Geometry Identities

Pythagorean Theorem and Converse:

$$a^2 + b^2 = c^2 \iff \triangle ABC \text{ is right-angled at } C$$

Intersecting Secants Theorem (Point $P$ outside circle):

$$PA \cdot PB = PC \cdot PD = PT^2 \quad (PT \text{ is tangent})$$

Appollonius' Theorem (Median $AD$ to side $BC$):

$$AB^2 + AC^2 = 2\left(AD^2 + BD^2\right)$$

## Common Exam Traps

- **Confusing Centroid and Incenter Ratios:** Assuming the incenter divides angle bisectors in a $2:1$ ratio. Only the **centroid** divides medians strictly in a $2:1$ ratio.
- **Misapplying Cyclic Quadrilateral Property:** Assuming opposite angles are equal in a cyclic quadrilateral. Opposite angles are **supplementary** ($\text{sum} = 180^\circ$), not necessarily equal.
- **Forgetting Points of Tangency Perpendicularity:** Omitting the $90^\circ$ angle formed between a tangent line and the radius drawn to the point of contact.

## Quiz

1. In a right-angled triangle with legs of length $a = 6\text{ cm}$ and $b = 8\text{ cm}$, what is the radius $R$ of its circumcircle?
  - [ ] $4\text{ cm}$
  - [x] $5\text{ cm}$
  - [ ] $10\text{ cm}$
  - [ ] $2.5\text{ cm}$
   > Hypotenuse $c = \sqrt{6^2 + 8^2} = 10\text{ cm}$. In any right triangle, the hypotenuse is the diameter of the circumcircle. Thus circumradius $R = \frac{c}{2} = 5\text{ cm}$.

2. Quad $ABCD$ is inscribed in a circle. If $\angle A = (2x + 10)^\circ$ and $\angle C = (3x + 20)^\circ$, find the measure of $\angle A$.
  - [ ] $30^\circ$
  - [x] $70^\circ$
  - [ ] $110^\circ$
  - [ ] $50^\circ$
   > Opposite angles of a cyclic quadrilateral are supplementary: $\angle A + \angle C = 180^\circ \implies (2x + 10) + (3x + 20) = 180 \implies 5x + 30 = 180 \implies 5x = 150 \implies x = 30$. Thus $\angle A = 2(30) + 10 = 70^\circ$.

3. From an external point $P$, a tangent $PT$ of length $12\text{ cm}$ is drawn to a circle. A secant line through $P$ intersects the circle at points $A$ and $B$. If $PA = 8\text{ cm}$, find the length of segment $AB$.
  - [ ] $18\text{ cm}$
  - [x] $10\text{ cm}$
  - [ ] $8\text{ cm}$
  - [ ] $14\text{ cm}$
   > By the Tangent-Secant theorem: $PT^2 = PA \cdot PB \implies 12^2 = 8 \cdot PB \implies 144 = 8 \cdot PB \implies PB = 18\text{ cm}$. Since $PB = PA + AB$, we have $18 = 8 + AB \implies AB = 10\text{ cm}$.