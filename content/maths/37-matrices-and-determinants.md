---
title: Matrices and Determinants
level: advanced
---

Matrices organize data into rectangular arrays of rows and columns, while determinants provide scalar metrics characterizing square linear transformations. Mastering matrix algebra, determinants, and inverses allows for solving complex systems of linear equations.

## Matrix Operations and Classifications

A matrix $A$ of order $m \times n$ consists of $m$ rows and $n$ columns.

### Matrix Operations

1. **Addition & Subtraction:** Matrix sizes must be identical: $(A \pm B)_{ij} = A_{ij} \pm B_{ij}$.
2. **Scalar Multiplication:** $(k A)_{ij} = k \cdot A_{ij}$.
3. **Matrix Multiplication ($A_{m \times p} \cdot B_{p \times n} = C_{m \times n}$):** Inner dimensions must match.
   $$C_{ij} = \sum_{k=1}^{p} A_{ik} B_{kj}$$
   Note: Matrix multiplication is **non-commutative**: $A B \neq B A$ in general.

### Special Matrix Types

- **Symmetric Matrix:** $A^T = A$
- **Skew-Symmetric Matrix:** $A^T = -A$ (Diagonal entries are always $0$).
- **Orthogonal Matrix:** $A^T A = A A^T = I \implies A^{-1} = A^T$.

## Determinants and Matrix Inversion

The **determinant** $\det(A)$ or $|A|$ is a scalar defined for square matrices ($n \times n$).

### Properties of Determinants

1. $\det(A^T) = \det(A)$
2. $\det(A B) = \det(A) \cdot \det(B)$
3. $\det(k A_{n \times n}) = k^n \det(A)$
4. Swapping two rows or columns flips the determinant sign ($\det \to -\det$).
5. If any two rows or columns are identical or proportional, $\det(A) = 0$.

### Matrix Inversion

A square matrix $A$ is **invertible (non-singular)** if and only if $\det(A) \neq 0$:

$$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

where $\text{adj}(A) = (C_{ij})^T$ is the transpose of the cofactor matrix.

## Matrix Algebra Master Table

| Matrix Property | Algebraic Identity / Definition | Condition / Constraint |
|---|---|---|
| Invertibility | $\det(A) \neq 0$ | Non-singular matrix requirement |
| Inverse Formula | $A^{-1} = \frac{1}{|A|} \text{adj}(A)$ | $|A| \neq 0$ |
| Adjoint Identity | $A \cdot \text{adj}(A) = |A| I_n$ | Holds for all square matrices |
| Adjoint Determinant | $|\text{adj}(A)| = |A|^{n-1}$ | $n \times n$ matrix order |
| Reversal Law | $(A B)^{-1} = B^{-1} A^{-1}$ | Order flips upon inverse |
| Transpose Reversal | $(A B)^T = B^T A^T$ | Order flips upon transpose |

## Important Formulas and Linear System Solution Theorems

Cramer's Rule for $3 \times 3$ Linear Systems:

$$x = \frac{D_x}{D}, \qquad y = \frac{D_y}{D}, \qquad z = \frac{D_z}{D} \quad (D \neq 0)$$

Determinant of Adjoint Matrix ($n \times n$):

$$|\text{adj}(A)| = |A|^{n-1} \implies |\text{adj}(\text{adj}(A))| = |A|^{(n-1)^2}$$

## Common Exam Traps

- **Assuming Matrix Multiplication Commutativity:** Writing $A B = B A$. In general, matrix multiplication does not commute.
- **Scaling Determinant Error:** Evaluating $\det(3 A)$ for a $3 \times 3$ matrix as $3 \det(A)$ instead of $3^3 \det(A) = 27 \det(A)$.
- **Reversal Law Neglect:** Expanding $(A B)^{-1}$ as $A^{-1} B^{-1}$ instead of correctly flipping order: $B^{-1} A^{-1}$.

## Quiz

1. If $A$ is a $3 \times 3$ square matrix with determinant $|A| = 5$, what is the numerical value of $|2 A|$?
  - [ ] $10$
  - [ ] $30$
  - [x] $40$
  - [ ] $125$
   > For an $n \times n$ matrix, $|k A| = k^n |A|$. Here $n = 3, k = 2$, so $|2 A| = 2^3 |A| = 8 \times 5 = 40$.

2. Compute the determinant of the matrix $A = \begin{pmatrix} 2 & 5 \\ 3 & 1 \end{pmatrix}$.
  - [ ] $17$
  - [x] $-13$
  - [ ] $13$
  - [ ] $-17$
   > $|A| = (2)(1) - (5)(3) = 2 - 15 = -13$.

3. If matrix $A$ has order $3 \times 3$ and $|A| = 4$, find the determinant of its adjoint matrix $|\text{adj}(A)|$.
  - [ ] $4$
  - [ ] $8$
  - [x] $16$
  - [ ] $64$
   > Use formula $|\text{adj}(A)| = |A|^{n-1}$. For $n = 3$, $|\text{adj}(A)| = |A|^{3-1} = |A|^2 = 4^2 = 16$.