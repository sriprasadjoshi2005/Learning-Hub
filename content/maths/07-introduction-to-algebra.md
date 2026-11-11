---
title: Introduction to Algebra
level: foundation
---

Algebra generalizes arithmetic by using letters (variables) to represent unknown or changing numbers. Learning to construct, manipulate, and simplify algebraic expressions provides the core language for all higher mathematics.

## Variables, Expressions, and Operations

- **Variable:** A symbol (usually a letter like $x, y, z$) standing in for an unknown numerical value.
- **Constant:** A fixed numerical value (e.g., $5, -\frac{2}{3}, \pi$).
- **Term:** A single number, variable, or product of numbers and variables (e.g., $7$, $4x$, $-3x^2y$). The numerical multiplier of a term is its **coefficient**.
- **Algebraic Expression:** A combination of terms connected by addition or subtraction operators (e.g., $3x^2 - 5x + 7$).

### Combining Like Terms

**Like terms** are terms that contain identical variable bases raised to identical exponents. Only like terms can be added or subtracted together:

$$5x^2y - 2x^2y + 4xy^2 = (5 - 2)x^2y + 4xy^2 = 3x^2y + 4xy^2$$

## Expansion of Brackets and Algebraic Multiplication

Multiplying algebraic expressions requires applying the **Distributive Property**: $a(b + c) = ab + ac$.

### Expansion Rules and Polynomial Products

1. **Single Bracket:** $a(x + y) = ax + ay$
2. **Double Brackets (FOIL: First, Outer, Inner, Last):**
$$(a + b)(c + d) = ac + ad + bc + bd$$
3. **Square of a Binomial:**
$$(a + b)^2 = a^2 + 2ab + b^2$$
$$(a - b)^2 = a^2 - 2ab + b^2$$
4. **Difference of Two Squares:**
$$(a + b)(a - b) = a^2 - b^2$$

## Standard Algebraic Identities Table

| Identity Name | Algebraic Expression | Expanded Form |
|---|---|---|
| Perfect Square (Sum) | $(a + b)^2$ | $a^2 + 2ab + b^2$ |
| Perfect Square (Difference) | $(a - b)^2$ | $a^2 - 2ab + b^2$ |
| Difference of Squares | $a^2 - b^2$ | $(a + b)(a - b)$ |
| Sum of Cubes | $a^3 + b^3$ | $(a + b)(a^2 - ab + b^2)$ |
| Difference of Cubes | $a^3 - b^3$ | $(a - b)(a^2 + ab + b^2)$ |
| Cube of a Binomial | $(a + b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |

## Important Formulas and Transformation Rules

Distributive Law across Multiple Terms:

$$a(b + c - d) = ab + ac - ad$$

Nested Bracket Expansion Order:

$$\text{Evaluate}: 2\left[3x - 4(x - 2)\right] = 2\left[3x - 4x + 8\right] = 2[-x + 8] = -2x + 16$$

Evaluation of Expressions (Substitution):

$$\text{If } f(x, y) = 2x^2 - 3xy + y^2, \quad \text{evaluating at } x = -2, y = 3 \text{ yields}:$$

$$f(-2, 3) = 2(-2)^2 - 3(-2)(3) + (3)^2 = 2(4) + 18 + 9 = 8 + 18 + 9 = 35$$

## Common Exam Traps

- **Dropping Negatives when Distributing:** Writing $-3(x - 4) = -3x - 12$ instead of correctly distributing the negative sign: $-3(x - 4) = -3x + 12$.
- **The Freshman's Dream Error:** Incorrectly writing $(a + b)^2 = a^2 + b^2$. The middle cross-term $2ab$ must always be included: $(a + b)^2 = a^2 + 2ab + b^2$.
- **Combining Unlike Terms:** Adding terms with different powers, such as writing $3x + 4x^2 = 7x^3$. $3x$ and $4x^2$ are unlike terms and cannot be combined.

## Quiz

1. Expand and simplify the expression completely: $(3x - 4)(2x + 5)$.
  - [ ] $6x^2 - 20$
  - [x] $6x^2 + 7x - 20$
  - [ ] $6x^2 - 7x - 20$
  - [ ] $6x^2 + 23x - 20$
   > Using FOIL: $(3x)(2x) + (3x)(5) + (-4)(2x) + (-4)(5) = 6x^2 + 15x - 8x - 20 = 6x^2 + 7x - 20$.

2. If $a + b = 7$ and $ab = 10$, what is the exact numerical value of $a^2 + b^2$?
  - [ ] $49$
  - [ ] $39$
  - [x] $29$
  - [ ] $19$
   > Square the sum identity: $(a + b)^2 = a^2 + 2ab + b^2 \implies 7^2 = a^2 + 2(10) + b^2 \implies 49 = a^2 + 20 + b^2 \implies a^2 + b^2 = 49 - 20 = 29$.

3. Simplify the algebraic expression by expanding brackets and combining like terms: $5 - 2[3x - (x - 4)]$.
  - [ ] $-4x - 3$
  - [x] $-4x - 3$
  - [ ] $-4x + 13$
  - [ ] $4x - 3$
   > Inner bracket: $3x - (x - 4) = 3x - x + 4 = 2x + 4$. Outer bracket: $5 - 2(2x + 4) = 5 - 4x - 8 = -4x - 3$.