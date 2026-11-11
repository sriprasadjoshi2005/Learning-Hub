---
title: Previous-Year Questions and Examination Analysis
level: exam
---

Analyzing authentic previous-year questions (PYQs) reveals high-yield question patterns, recurring distractor traps, and time-saving techniques.

## High-Yield Topic Taxonomy and Pattern Analysis

Standardized entrance exams (such as SAT Math, ACT, CUET, and JEE) allocate question distributions predictably across core mathematical domains.

```text
                    Exam Topic Weightage Distribution
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
Calculus & DEs (30-35%)         Algebra & Matrices (25-30%)     Geometry & Vectors (25%)
- Derivatives & Applications    - Quadratic & Polynomials       - 3D Geometry & Vectors
- Integration & Area            - Sequences & Combinatorics     - Conics & Lines
```

## Deconstructing Typical PYQ Distractors

- **The Partial Calculation Trap:** An option matching an intermediate step of a multi-step problem (e.g., stopping after finding $x = 3$ when the question asks for $2x + 5$).
- **The Sign Flip Distractor:** An option identical to the correct answer except for an inverted sign ($+13$ vs $-13$).
- **The Reciprocal Trap:** An option containing the reciprocal of the target ratio.

## PYQ Pattern Strategy Table

| Domain | High-Yield PYQ Subtopic | Fast-Solving Shortcut |
|---|---|---|
| Calculus | Area bounded by curves | Use $\int (y_1 - y_2) dx$; check symmetry |
| Algebra | Roots of quadratic equations | Use Vieta's formulas ($\alpha+\beta, \alpha\beta$) |
| Vectors | Shortest distance between lines | Apply formula $d = \frac{|(\mathbf{a}_2-\mathbf{a}_1)\cdot(\mathbf{b}_1\times\mathbf{b}_2)|}{|\mathbf{b}_1\times\mathbf{b}_2|}$ |
| Matrices | Value of $|\text{adj}(A)|$ | Use property $|A|^{n-1}$ without computing adjoint |

## Important Formulas and Analysis Identities

Matrix Adjoint Shortcut:

$$|\text{adj}(A)| = |A|^{n-1}$$

Shortest Distance Between Parallel Lines:

$$d = \frac{|(\mathbf{a}_2 - \mathbf{a}_1) \times \mathbf{b}|}{|\mathbf{b}|}$$

## Common Exam Traps

- **Stopping Mid-Calculation:** Selecting an option matching an intermediate variable instead of completing the requested target quantity.
- **Forgetting Domain Restrictions in Log/Trig PYQs:** Failing to check if solutions lie within valid domain bounds.
- **Misreading Negative Modifiers:** Missing words like *NOT, EXCEPT*, or *LEAST* in question stems.

## Quiz

1. [PYQ Style] If $A$ is a $3 \times 3$ matrix such that $|A| = 3$, find the value of $|2 \text{adj}(A)|$.
  - [ ] $18$
  - [ ] $36$
  - [x] $72$
  - [ ] $108$
   > First evaluate $|\text{adj}(A)| = |A|^{3-1} = 3^2 = 9$. Next, for a $3 \times 3$ matrix, $|2 M| = 2^3 |M| = 8 |M|$. Thus $|2 \text{adj}(A)| = 8 \times 9 = 72$.

2. [PYQ Style] What is the area of the region bounded by the parabola $y^2 = 4x$ and its latus rectum $x = 1$?
  - [ ] $\frac{4}{3}$
  - [x] $\frac{8}{3}$
  - [ ] $\frac{16}{3}$
  - [ ] $4$
   > By symmetry, Area $= 2 \int_{0}^{1} 2\sqrt{x} \, dx = 4 \Big[ \frac{2}{3} x^{3/2} \Big]_{0}^{1} = 4 \times \frac{2}{3} = \frac{8}{3}$.

3. [PYQ Style] Evaluate the sum of all roots of the equation $|x^2 - 3x + 2| = 2$.
  - [ ] $9$
  - [x] $3$
  - [ ] $6$
  - [ ] $0$
   > Case 1: $x^2 - 3x + 2 = 2 \implies x^2 - 3x = 0 \implies x = 0$ or $x = 3$. Case 2: $x^2 - 3x + 2 = -2 \implies x^2 - 3x + 4 = 0$ (discriminant $\Delta = 9 - 16 = -7 < 0$, no real roots). The real roots are $x = 0$ and $x = 3$. Sum of real roots $= 0 + 3 = 3$.
