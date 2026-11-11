---
title: Permutations, Combinations and Counting
level: intermediate
---

Combinatorics is the branch of mathematics dealing with counting, arrangements, and selections. Mastering the Fundamental Counting Principle, factorials, permutations, combinations, and the Binomial Theorem forms the basis for probability theory.

## Fundamental Rules and Factorial Algebra

- **Fundamental Counting Principle (Multiplication Rule):** If an event can occur in $m$ ways and a subsequent independent event can occur in $n$ ways, both events can occur in sequence in $m \times n$ ways.
- **Addition Rule:** If two events are mutually exclusive, one occurring in $m$ ways and the other in $n$ ways, either event can occur in $m + n$ ways.
- **Factorial Notation ($n!$):** The product of all positive integers less than or equal to $n$:
$$n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1 \quad (\text{By definition, } 0! = 1)$$

## Permutations ($nPr$) vs. Combinations ($nCr$)

### Permutations (Order Matters)

A **permutation** is an arrangement of items in a specific sequence or order.

- **Arranging $r$ items from $n$ distinct items:**
$$nPr = P(n, r) = \frac{n!}{(n - r)!}$$

- **Permutations with Repetition (identical items):** Number of ways to arrange $n$ items where $n_1$ are identical, $n_2$ are identical, etc.:
$$\text{Ways} = \frac{n!}{n_1! \cdot n_2! \cdots n_k!}$$

- **Circular Permutations:** Arranging $n$ distinct items around a circle: $(n - 1)!$.

### Combinations (Order Does NOT Matter)

A **combination** is a selection of items without regard to order.

- **Selecting $r$ items from $n$ distinct items:**
$$nCr = C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!}$$

## Binomial Theorem and Pascal's Triangle

For any real numbers $a, b$ and non-negative integer $n$:

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \dots + \binom{n}{n}b^n$$

- **General Term ($T_{k+1}$):** $T_{k+1} = \binom{n}{k} a^{n-k} b^k$
- **Total Terms in Expansion:** $n + 1$ terms.

## Combinatorics Formula Master Table

| Concept | Formula | Key Characteristic |
|---|---|---|
| Permutations ($nPr$) | $\frac{n!}{(n-r)!}$ | Selections where order matters |
| Combinations ($nCr$) | $\frac{n!}{r!(n-r)!}$ | Selections where order does NOT matter |
| Identical Items Permutation | $\frac{n!}{n_1! n_2! \dots}$ | Arrangements with repeating identical objects |
| Circular Permutations | $(n - 1)!$ | Rotational symmetry eliminates 1 degree of freedom |
| Symmetry Property | $\binom{n}{r} = \binom{n}{n-r}$ | Selecting $r$ equals rejecting $n-r$ |
| Pascal's Identity | $\binom{n}{r} + \binom{n}{r-1} = \binom{n+1}{r}$ | Recursive coefficient addition rule |

## Important Formulas and Combinatorial Identities

Sum of Binomial Coefficients:

$$\sum_{k=0}^{n} \binom{n}{k} = \binom{n}{0} + \binom{n}{1} + \dots + \binom{n}{n} = 2^n$$

Alternating Sum of Binomial Coefficients:

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = \binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \dots = 0$$

## Common Exam Traps

- **Confusing Permutations and Combinations:** Using $nPr$ when order does not matter (e.g., forming a committee) or $nCr$ when order matters (e.g., forming a password).
- **Miscounting $0!$:** Assuming $0! = 0$ instead of $0! = 1$.
- **Off-by-One Index in Binomial General Term:** Writing $T_k = \binom{n}{k} a^{n-k} b^k$ instead of recognizing that the $(k+1)$-th term corresponds to index $k$.

## Quiz

1. How many distinct 4-letter codes can be formed using the letters from the word **MATH** without repeating any letter?
  - [ ] $12$
  - [x] $24$
  - [ ] $16$
  - [ ] $4$
   > Since order matters and all 4 letters are distinct: $4P4 = 4! = 4 \times 3 \times 2 \times 1 = 24$.

2. A committee of $3$ members is to be selected from a group of $8$ people. In how many different ways can this committee be chosen?
  - [ ] $336$
  - [x] $56$
  - [ ] $24$
  - [ ] $112$
   > Order does not matter, so use combinations: $\binom{8}{3} = \frac{8!}{3!(8 - 3)!} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$.

3. What is the coefficient of $x^3$ in the binomial expansion of $(x + 2)^5$?
  - [ ] $10$
  - [x] $40$
  - [ ] $80$
  - [ ] $20$
   > General term $T_{k+1} = \binom{5}{k} x^{5-k} (2)^k$. We want exponent of $x$ to be $3 \implies 5 - k = 3 \implies k = 2$. Coefficient is $\binom{5}{2} \cdot 2^2 = 10 \times 4 = 40$.