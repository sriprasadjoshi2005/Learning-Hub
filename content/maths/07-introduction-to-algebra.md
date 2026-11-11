---
title: Introduction to Algebra
level: foundation
---

Algebra generalizes arithmetic by using letters (variables) to represent unknown or changing numerical values. Learning to construct, manipulate, expand, and simplify algebraic expressions provides the foundation for higher mathematics.

## Main Concept 1: Variables, Expressions, and Operations

Algebraic expressions are mathematical combinations of numbers, variables, and operations.

- **Variable:** A symbol, usually a letter such as \(x\), \(y\), or \(z\), representing an unknown or changing numerical value.
- **Constant:** A fixed numerical value that does not change (e.g., \(5\), \(-\frac{2}{3}\), \(\pi\)).
- **Term:** A single number, variable, or product of numbers and variables (e.g., \(7\), \(4x\), \(-3x^2y\)). The numerical multiplier of a term is called its **coefficient**.
- **Algebraic Expression:** A combination of terms connected by mathematical operations such as addition, subtraction, and multiplication (e.g., \(3x^2 - 5x + 7\)).

### Subtopic 1: Combining Like Terms

**Like terms** contain identical variable parts, meaning the same variables raised to the same exponents. Only like terms can be added or subtracted.

**Example:**

$$
5x^2y - 2x^2y + 4xy^2
$$

Combining the like terms:

$$
= (5-2)x^2y + 4xy^2
$$

$$
= 3x^2y + 4xy^2
$$

The terms \(3x^2y\) and \(4xy^2\) cannot be combined because their variable parts are different.

## Main Concept 2: Expansion of Brackets and Algebraic Multiplication

Expanding algebraic expressions involves removing brackets by multiplying each term inside a bracket by the term outside it. This follows the **Distributive Property**.

$$
a(b+c)=ab+ac
$$

### Subtopic 1: Expansion Rules and Polynomial Products

1. **Single Bracket:**

   $$a(x+y)=ax+ay$$

2. **Double Brackets (FOIL Method):**

   FOIL stands for First, Outer, Inner, and Last. It helps multiply two binomials by ensuring that every term in the first bracket is multiplied by every term in the second bracket.

   $$
   (a+b)(c+d)=ac+ad+bc+bd
   $$

3. **Square of a Binomial:**

   $$
   (a+b)^2=a^2+2ab+b^2
   $$

   $$
   (a-b)^2=a^2-2ab+b^2
   $$

4. **Difference of Two Squares:**

   $$
   (a+b)(a-b)=a^2-b^2
   $$

## Important Classifications / Structures / Processes

### Standard Algebraic Identities Table

| Identity Name | Algebraic Expression | Expanded / Factorised Form |
|---|---|---|
| Perfect Square (Sum) | \((a+b)^2\) | \(a^2+2ab+b^2\) |
| Perfect Square (Difference) | \((a-b)^2\) | \(a^2-2ab+b^2\) |
| Difference of Squares | \(a^2-b^2\) | \((a+b)(a-b)\) |
| Sum of Cubes | \(a^3+b^3\) | \((a+b)(a^2-ab+b^2)\) |
| Difference of Cubes | \(a^3-b^3\) | \((a-b)(a^2+ab+b^2)\) |
| Cube of a Binomial (Sum) | \((a+b)^3\) | \(a^3+3a^2b+3ab^2+b^3\) |

## Important Formulas / Rules / Relationships

### 1. Distributive Law Across Multiple Terms

A factor outside a bracket must be multiplied by every term inside it.

$$
a(b+c-d)=ab+ac-ad
$$

### 2. Nested Bracket Expansion Order

When an expression contains multiple levels of brackets, simplify the innermost brackets first, followed by the outer brackets.

**Example:**

$$
2[3x-4(x-2)]
$$

First, expand the inner bracket:

$$
=2[3x-4x+8]
$$

Combine like terms:

$$
=2[-x+8]
$$

Multiply by the outer factor:

$$
=-2x+16
$$

### 3. Evaluation of Expressions (Substitution)

Substitution involves replacing variables with their given numerical values and simplifying the resulting expression.

**Example:**

If

$$
f(x,y)=2x^2-3xy+y^2
$$

evaluate the expression at \(x=-2\) and \(y=3\).

Substitute the values:

$$
f(-2,3)=2(-2)^2-3(-2)(3)+(3)^2
$$

Simplify:

$$
=2(4)+18+9
$$

$$
=8+18+9
$$

$$
=35
$$

## Common Exam Traps

- **Dropping Negative Signs During Distribution:** Writing \(-3(x-4)=-3x-12\) instead of correctly distributing the negative factor:

  $$
  -3(x-4)=-3x+12
  $$

- **The Freshman's Dream Error:** Incorrectly assuming that \((a+b)^2=a^2+b^2\). The middle cross-term \(2ab\) must be included:

  $$
  (a+b)^2=a^2+2ab+b^2
  $$

- **Combining Unlike Terms:** Adding terms with different powers, such as writing \(3x+4x^2=7x^3\). These are unlike terms and cannot be combined.

- **Incorrect FOIL Expansion:** Forgetting one of the four products when multiplying two binomials. Every term in the first bracket must multiply every term in the second bracket.

## Quiz

1. Expand and simplify the expression completely: \((3x-4)(2x+5)\).

   - [ ] \(6x^2-20\)
   - [x] \(6x^2+7x-20\)
   - [ ] \(6x^2-7x-20\)
   - [ ] \(6x^2+23x-20\)

   > Using FOIL: \((3x)(2x)+(3x)(5)+(-4)(2x)+(-4)(5)=6x^2+15x-8x-20=6x^2+7x-20\).

2. If \(a+b=7\) and \(ab=10\), what is the exact numerical value of \(a^2+b^2\)?

   - [ ] \(49\)
   - [ ] \(39\)
   - [x] \(29\)
   - [ ] \(19\)

   > Using the square of a sum identity: \((a+b)^2=a^2+2ab+b^2\). Substituting the given values: \(7^2=a^2+2(10)+b^2\). Therefore, \(49=a^2+20+b^2\), giving \(a^2+b^2=49-20=29\).

3. Simplify the algebraic expression by expanding brackets and combining like terms: \(5-2[3x-(x-4)]\).

   - [x] \(-4x-3\)
   - [ ] \(-4x+3\)
   - [ ] \(-4x+13\)
   - [ ] \(4x-3\)

   > First simplify the inner bracket: \(3x-(x-4)=3x-x+4=2x+4\). Then expand the outer bracket: \(5-2(2x+4)=5-4x-8=-4x-3\).
