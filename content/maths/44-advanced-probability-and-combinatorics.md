---
title: Advanced Probability and Combinatorics
level: exam
---

Advanced exam items combine counting principles, inclusion-exclusion, derangements, geometric probability, and Bayes' Theorem into complex multi-step scenarios.

## Derangements, Multinomial Theorem, and Grid Paths

### Derangements ($D_n$ or $!n$)

A **derangement** is a permutation of $n$ items such that no item appears in its original position:

$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} = n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + \frac{(-1)^n}{n!} \right)$$

Values: $D_1 = 0, D_2 = 1, D_3 = 2, D_4 = 9, D_5 = 44$.
As $n \to \infty$, the probability that a random permutation is a derangement approaches $\frac{1}{e} \approx 0.3678$.

### Grid Path Counting

Number of shortest paths on a 2D grid from $(0, 0)$ to $(m, n)$ moving only Right and Up:

$$\text{Paths} = \binom{m + n}{m} = \frac{(m + n)!}{m! n!}$$

## Expected Value and Advanced Conditional Scenarios

### Expected Value Properties

For random variables $X$ and $Y$ and constants $a, b$:

- **Linearity of Expectation (Holds ALWAYS, regardless of independence!):**
  $$E[a X + b Y] = a E[X] + b E[Y]$$
- **Product Expectation (Holds ONLY for independent $X, Y$):**
  $$E[X \cdot Y] = E[X] \cdot E[Y]$$

## Combinatorics & Probability Master Table

| Concept | Mathematical Formula | Key Application |
|---|---|---|
| Derangements ($D_n$) | $n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$ | No item in original position |
| Grid Paths | $\binom{m+n}{m}$ | Shortest lattice paths |
| Linearity of Expectation | $E[X+Y] = E[X] + E[Y]$ | Valid even for dependent variables |
| Inclusion-Exclusion | $|A \cup B \cup C| = \sum |A| - \sum |A \cap B| + |A \cap B \cap C|$ | Counting overlapping sets |
| Derangement Probability | $P(\text{Derangement}) \approx \frac{1}{e}$ | Large $n$ approximation |

## Important Formulas and Combinatorial Identities

Derangement Recursive Formula:

$$D_n = (n - 1)(D_{n-1} + D_{n-2})$$

Multinomial Expansion Term Count:

$$\text{Number of terms in } (x_1 + x_2 + \dots + x_r)^n = \binom{n + r - 1}{r - 1}$$

## Common Exam Traps

- **Assuming Independence for Product Expectation:** Applying $E[XY] = E[X]E[Y]$ when $X$ and $Y$ are dependent variables. Linearity $E[X+Y] = E[X]+E[Y]$ holds generally, but product equality requires independence.
- **Off-by-One in Derangement Index:** Confusing $D_4 = 9$ with $D_5 = 44$.
- **Ignoring Obstacles in Grid Paths:** Using $\binom{m+n}{m}$ directly without subtracting paths passing through forbidden grid points.

## Quiz

1. Four letters addressed to four different individuals are placed randomly into four stamped envelopes. What is the probability that **no letter** reaches its correct recipient?
  - [ ] $\frac{1}{24}$
  - [ ] $\frac{1}{4}$
  - [x] $\frac{3}{8}$
  - [ ] $\frac{9}{16}$
   > Total permutations $= 4! = 24$. Number of derangements $D_4 = 9$. Probability $= \frac{D_4}{4!} = \frac{9}{24} = \frac{3}{8}$.

2. How many shortest paths exist on a grid from point $(0, 0)$ to point $(4, 3)$ moving only right or up?
  - [ ] $12$
  - [x] $35$
  - [ ] $70$
  - [ ] $144$
   > Grid steps required: $m = 4$ (Right), $n = 3$ (Up). Total paths $= \binom{4 + 3}{4} = \binom{7}{4} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$.

3. What is the total number of terms in the expansion of $(a + b + c + d)^6$?
  - [ ] $28$
  - [x] $84$
  - [ ] $120$
  - [ ] $210$
   > Use multinomial term count formula $\binom{n + r - 1}{r - 1}$ with $n = 6$ and $r = 4$ variables: $\binom{6 + 4 - 1}{4 - 1} = \binom{9}{3} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84$.