---
title: Advanced Problem-Solving Strategies
level: exam
---

Mastering high-stakes competitive examinations requires general problem-solving heuristics—including symmetry, extreme principle, invariance, and strategic option elimination.

## Core Problem-Solving Heuristics

High-scoring test-takers use structured heuristics when faced with unfamiliar or novel problems.

- **Symmetry Principle:** If a problem is symmetric with respect to its variables, the optimum or critical state usually occurs when all variables are equal ($x = y = z$).
- **Extremal Principle:** Consider the extreme elements of a system (the smallest or largest value, the closest pair, the maximum angle).
- **Invariance Principle:** Identify quantities that remain unchanged under specified operational transformations.
- **Dimensional & Unit Analysis:** Verify formulas by checking that physical or geometric dimensions match across both sides of an equation.

## Strategic Process of Elimination (POE)

```text
                     Option Elimination Matrix
                                  │
  1. Dimensional Check ──> Eliminate options with wrong units/dimensions
                                  │
  2. Boundary Value Test ──> Test x = 0, x = 1, or x -> infinity
                                  │
  3. Parity & Sign Audit ──> Check even/odd properties & positive bounds
```

## Strategy Master Table

| Strategy Name | Core Principle | Primary Exam Application |
|---|---|---|
| Extremal Principle | Focus on max/min elements | Graph theory, inequalities, geometry |
| Symmetry Assumption | Equate symmetric variables | Constrained optimization, algebraic systems |
| Invariance | Track conserved properties | Iterative operations, game theory |
| Dimensional Analysis | Match units across sides | Physical/geometric formula checking |
| Boundary Testing | Substitute $0, 1, \infty$ | Instant distractor elimination |

## Important Formulas and Heuristic Rules

Symmetric Variable Equality Heuristic:

$$\text{If } f(x, y, z) \text{ is symmetric and } x + y + z = k \implies \text{Extremum occurs at } x = y = z = \frac{k}{3}$$

Boundary Testing Rule:

$$\text{If an identity holds } \forall x \in \mathbb{R} \implies \text{Test simple values } x = 0, x = 1, x = -1 \text{ to eliminate wrong options!}$$

## Common Exam Traps

- **Over-looking Boundary Cases:** Testing only interior values and missing endpoint constraints.
- **Assuming Symmetry Without Proof:** Assuming $x=y=z$ yields a maximum when it actually yields a local minimum.
- **Misapplying Dimensional Elimination:** Eliminating a valid dimensionless option because it lacks expected variable powers.

## Quiz

1. Find the maximum value of $f(x, y, z) = x y z$ subject to $x + y + z = 12$ for positive real numbers $x, y, z > 0$.
  - [ ] $36$
  - [x] $64$
  - [ ] $48$
  - [ ] $256$
   > By the Symmetry Principle / AM-GM inequality, maximum of symmetric product $xyz$ subject to fixed sum occurs when variables are equal: $x = y = z = \frac{12}{3} = 4$. Maximum product is $4 \times 4 \times 4 = 64$.

2. Which option could represent the exact area of an ellipse with semi-axes $a$ and $b$?
  - [ ] $A = 2\pi(a + b)$
  - [ ] $A = \pi(a^2 + b^2)$
  - [x] $A = \pi a b$
  - [ ] $A = \frac{4}{3}\pi a^2 b$
   > By Dimensional Analysis: area must have dimensions of $[\text{Length}]^2$. Option A is length ($[\text{L}]$). Option D is volume ($[\text{L}]^3$). Option C gives $\pi a b \to [\text{L}]^2$. Furthermore, when $a = b = r$, area must reduce to circle area $\pi r^2$, which holds strictly for $\pi a b$.

3. Solve for the sum of the infinite series $S = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots$ using boundary bounds.
  - [ ] $1.5$
  - [x] $2.0$
  - [ ] $2.5$
  - [ ] $\infty$
   > The first two terms sum to $1 + 0.5 = 1.5$. Since all subsequent terms are positive, $S > 1.5$. Using infinite GP sum formula $S = \frac{1}{1 - 1/2} = 2.0$.