---
title: Basic Mensuration
level: foundation
---

Mensuration is the branch of mathematics dealing with the measurement of geometric magnitudes such as lengths, perimeters, areas, surface areas, and volumes. Mastering standard formulas for 2D plane figures and 3D solid figures is essential for geometry and applied calculus.

## 2D Geometric Figures: Perimeter and Area

- **Perimeter ($P$):** Total boundary length enclosing a 2D shape.
- **Area ($A$):** Total 2D surface enclosed within a boundary, measured in square units.

### Primary 2D Area Formulas

1. **Triangle:**
   - Base and Height: $A = \frac{1}{2} \cdot b \cdot h$
   - Heron's Formula (given sides $a, b, c$ and semi-perimeter $s = \frac{a+b+c}{2}$):
$$A = \sqrt{s(s - a)(s - b)(s - c)}$$
   - Equilateral Triangle (side $a$): $A = \frac{\sqrt{3}}{4} a^2$

2. **Rectangle and Square:**
   - Rectangle: $P = 2(l + w), \quad A = l \cdot w$
   - Square: $P = 4a, \quad A = a^2, \quad \text{Diagonal } d = a\sqrt{2}$

3. **Parallelogram and Trapezium:**
   - Parallelogram: $A = b \cdot h$
   - Trapezium (parallel sides $a, b$, height $h$): $A = \frac{1}{2}(a + b) \cdot h$

4. **Circle:**
   - Circumference: $C = 2\pi r = \pi d$
   - Area: $A = \pi r^2$
   - Arc Length ($L$) and Sector Area ($A_{\text{sec}}$) for angle $\theta$ in degrees:
$$L = \frac{\theta}{360^\circ} \cdot 2\pi r, \qquad A_{\text{sec}} = \frac{\theta}{360^\circ} \cdot \pi r^2$$

## 3D Solid Geometry: Surface Area and Volume

- **Lateral / Curved Surface Area (LSA/CSA):** Area of outer surfaces excluding top and bottom bases.
- **Total Surface Area (TSA):** Combined area of all enclosing boundary surfaces.
- **Volume ($V$):** Total 3D space occupied by a solid, measured in cubic units.

## Mensuration Formulas Master Table

| 3D Solid Shape | Lateral/Curved Surface Area (LSA) | Total Surface Area (TSA) | Volume ($V$) |
|---|---|---|---|
| Cube (side $a$) | $4a^2$ | $6a^2$ | $a^3$ |
| Cuboid ($l, w, h$) | $2h(l + w)$ | $2(lw + wh + hl)$ | $l \cdot w \cdot h$ |
| Right Cylinder ($r, h$) | $2\pi r h$ | $2\pi r h + 2\pi r^2 = 2\pi r(r + h)$ | $\pi r^2 h$ |
| Right Cone ($r, h, l=\sqrt{r^2+h^2}$) | $\pi r l$ | $\pi r l + \pi r^2 = \pi r(l + r)$ | $\frac{1}{3}\pi r^2 h$ |
| Sphere (radius $r$) | $4\pi r^2$ | $4\pi r^2$ | $\frac{4}{3}\pi r^3$ |
| Hemisphere (radius $r$) | $2\pi r^2$ | $3\pi r^2$ | $\frac{2}{3}\pi r^3$ |

## Important Formulas and Scaling Laws

Scaling Effect on Similar Geometrical Figures (Scale Factor $k$):

$$\text{Linear Dimensions}: \frac{L_2}{L_1} = k$$

$$\text{Surface Area}: \frac{A_2}{A_1} = k^2$$

$$\text{Volume}: \frac{V_2}{V_1} = k^3$$

Heron's Formula Semi-Perimeter:

$$s = \frac{a + b + c}{2}$$

## Common Exam Traps

- **Confusing CSA and TSA of a Hemisphere:** Using $2\pi r^2$ for total surface area instead of $3\pi r^2$ (which includes the flat circular base).
- **Linear vs. Volumetric Scaling Error:** Assuming that doubling the radius of a sphere ($k=2$) doubles its volume. Volume increases by a factor of $k^3 = 2^3 = 8$.
- **Incompatible Units in Volume Calculations:** Multiplying dimensions in meters by dimensions in centimeters without converting to a common unit first.

## Quiz

1. What is the total surface area of a solid hemisphere of radius $r = 7\text{ cm}$? (Use $\pi \approx \frac{22}{7}$)
  - [ ] $308\text{ cm}^2$
  - [x] $462\text{ cm}^2$
  - [ ] $616\text{ cm}^2$
  - [ ] $718.67\text{ cm}^2$
   > $\text{TSA of solid hemisphere} = 3\pi r^2 = 3 \times \frac{22}{7} \times 7^2 = 3 \times 22 \times 7 = 462\text{ cm}^2$.

2. A right circular cone has a base radius of $6\text{ cm}$ and a vertical height of $8\text{ cm}$. What is its curved surface area (CSA)?
  - [ ] $48\pi\text{ cm}^2$
  - [x] $60\pi\text{ cm}^2$
  - [ ] $96\pi\text{ cm}^2$
  - [ ] $100\pi\text{ cm}^2$
   > Slant height $l = \sqrt{r^2 + h^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ cm}$. $\text{CSA} = \pi r l = \pi \times 6 \times 10 = 60\pi\text{ cm}^2$.

3. If the side length of a cube is increased by $50\%$, by what percentage does its total volume increase?
  - [ ] $125\%$
  - [ ] $150\%$
  - [x] $237.5\%$
  - [ ] $337.5\%$
   > New side length $a' = 1.5 a$. New volume $V' = (1.5 a)^3 = 3.375 a^3 = 3.375 V$. Percentage increase $= (3.375 - 1) \times 100\% = 2.375 \times 100\% = 237.5\%$.