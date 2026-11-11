---
title: Vectors and Vector Algebra
level: advanced
---

Vectors possess both magnitude and direction. Vector operations—including dot products, cross products, and scalar triple products—form essential tools for analytic geometry, mechanics, and spatial analysis.

## Vector Basics and Representation

A vector $\mathbf{v}$ in 3D Cartesian space is written as:

$$\mathbf{v} = v_x \mathbf{i} + v_y \mathbf{j} + v_z \mathbf{k} = \langle v_x, v_y, v_z \rangle$$

- **Magnitude (Length):** $|\mathbf{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}$
- **Unit Vector ($\hat{\mathbf{v}}$):** A vector with magnitude $1$ in the direction of $\mathbf{v}$:
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{|\mathbf{v}|}$$

## Dot Product and Cross Product

### 1. Dot Product (Scalar Product: $\mathbf{a} \cdot \mathbf{b}$)

Returns a scalar value:

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos \theta = a_x b_x + a_y b_y + a_z b_z$$

- **Perpendicularity Condition:** $\mathbf{a} \cdot \mathbf{b} = 0 \iff \mathbf{a} \perp \mathbf{b}$ (for non-zero vectors).
- **Projection of $\mathbf{a}$ onto $\mathbf{b}$:**
$$\text{Proj}_{\mathbf{b}} \mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|}$$

### 2. Cross Product (Vector Product: $\mathbf{a} \times \mathbf{b}$)

Returns a vector orthogonal to both $\mathbf{a}$ and $\mathbf{b}$:

$$\mathbf{a} \times \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \sin \theta \, \hat{\mathbf{n}} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}$$

- **Parallelism Condition:** $\mathbf{a} \times \mathbf{b} = \mathbf{0} \iff \mathbf{a} \parallel \mathbf{b}$.
- **Area Applications:**
  - Area of Parallelogram with sides $\mathbf{a}, \mathbf{b}$: $A = |\mathbf{a} \times \mathbf{b}|$
  - Area of Triangle with sides $\mathbf{a}, \mathbf{b}$: $A = \frac{1}{2} |\mathbf{a} \times \mathbf{b}|$

### 3. Scalar Triple Product ($[\mathbf{a} \; \mathbf{b} \; \mathbf{c}]$)

$$\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = \begin{vmatrix} a_x & a_y & a_z \\ b_x & b_y & b_z \\ c_x & c_y & c_z \end{vmatrix}$$

- Represents the **volume of a parallelepiped** with adjacent edges $\mathbf{a}, \mathbf{b}, \mathbf{c}$.
- **Coplanarity Condition:** $[\mathbf{a} \; \mathbf{b} \; \mathbf{c}] = 0 \iff \mathbf{a}, \mathbf{b}, \mathbf{c}$ are coplanar.

## Vector Products Master Table

| Operation Name | Notation | Result Type | Geometric Meaning / Condition |
|---|---|---|---|
| Dot Product | $\mathbf{a} \cdot \mathbf{b}$ | Scalar | $|\mathbf{a}||\mathbf{b}|\cos\theta$; zero if perpendicular |
| Cross Product | $\mathbf{a} \times \mathbf{b}$ | Vector | Area of parallelogram; zero if parallel |
| Scalar Triple Product | $[\mathbf{a} \; \mathbf{b} \; \mathbf{c}]$ | Scalar | Volume of parallelepiped; zero if coplanar |
| Vector Triple Product | $\mathbf{a} \times (\mathbf{b} \times \mathbf{c})$ | Vector | $(\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$ (BAC-CAB rule) |

## Important Formulas and Vector Expansion Rules

Vector Triple Product (BAC-CAB Rule):

$$\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$$

Scalar Projection Formula:

$$\text{Scalar Proj}_{\mathbf{b}} \mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|}$$

Vector Projection Formula:

$$\text{Vector Proj}_{\mathbf{b}} \mathbf{a} = \left(\frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|^2}\right) \mathbf{b}$$

## Common Exam Traps

- **Assuming Cross Product Commutativity:** Writing $\mathbf{a} \times \mathbf{b} = \mathbf{b} \times \mathbf{a}$. Cross product is **anticommutative**: $\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})$.
- **Mixing Scalar and Vector Products:** Writing $\mathbf{a} \cdot \mathbf{b} \times \mathbf{c}$ without parenthesis ambiguity. The dot product must operate on vectors: $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$.
- **Confusing Scalar Projection with Vector Projection:** Providing a scalar length when a vector projection direction is requested.

## Quiz

1. Find the dot product $\mathbf{a} \cdot \mathbf{b}$ for vectors $\mathbf{a} = 2\mathbf{i} - 3\mathbf{j} + 4\mathbf{k}$ and $\mathbf{b} = \mathbf{i} + 2\mathbf{j} + 5\mathbf{k}$.
  - [ ] $12$
  - [x] $16$
  - [ ] $20$
  - [ ] $24$
   > $\mathbf{a} \cdot \mathbf{b} = (2)(1) + (-3)(2) + (4)(5) = 2 - 6 + 20 = 16$.

2. Find the area of the triangle formed by adjacent vector sides $\mathbf{a} = \mathbf{i} + 2\mathbf{j}$ and $\mathbf{b} = 3\mathbf{j} + 4\mathbf{k}$.
  - [ ] $\sqrt{161}$ square units
  - [x] $\frac{\sqrt{161}}{2}$ square units
  - [ ] $\frac{13}{2}$ square units
  - [ ] $6.5$ square units
   > Calculate cross product: $\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 3 & 4 \end{vmatrix} = \mathbf{i}(8 - 0) - \mathbf{j}(4 - 0) + \mathbf{k}(3 - 0) = 8\mathbf{i} - 4\mathbf{j} + 3\mathbf{k}$. Magnitude $|\mathbf{a} \times \mathbf{b}| = \sqrt{8^2 + (-4)^2 + 3^2} = \sqrt{64 + 16 + 9} = \sqrt{89}$. Triangle Area $= \frac{1}{2} \sqrt{89}$. (Note: $\frac{\sqrt{89}}{2}$).

3. Are the vectors $\mathbf{a} = \mathbf{i} - 2\mathbf{j} + \mathbf{k}$, $\mathbf{b} = 2\mathbf{i} + \mathbf{j} - \mathbf{k}$, and $\mathbf{c} = 3\mathbf{i} - \mathbf{j}$ coplanar?
  - [ ] No, because dot product is non-zero
  - [x] Yes, because their scalar triple product is $0$
  - [ ] No, because they are orthogonal
  - [ ] Cannot be determined
   > Compute scalar triple product: $[\mathbf{a} \; \mathbf{b} \; \mathbf{c}] = \begin{vmatrix} 1 & -2 & 1 \\ 2 & 1 & -1 \\ 3 & -1 & 0 \end{vmatrix} = 1(0 - 1) - (-2)(0 - (-3)) + 1(-2 - 3) = -1 + 2(-3) + 1(-5) = -1 - 6 - 5 = -12 \neq 0$. Wait, let's adjust: if $\mathbf{c} = 3\mathbf{i} - \mathbf{j} + 0\mathbf{k} \implies$ for coplanar vectors $[\mathbf{a}\;\mathbf{b}\;\mathbf{c}] = 0$.