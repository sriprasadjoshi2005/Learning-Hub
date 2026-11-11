---
title: Sequences and Series
level: intermediate
---

A sequence is an ordered list of numbers governed by a mathematical rule, while a series is the sum of terms in a sequence. Arithmetic progressions, geometric progressions, and infinite series play crucial roles in financial mathematics, calculus, and discrete analysis.

## Arithmetic Progressions (AP)

An **Arithmetic Progression** is a sequence where the difference between consecutive terms is constant.

- **Common Difference ($d$):** $d = a_{k+1} - a_k$.
- **General $n$-th Term ($a_n$):**
$$a_n = a_1 + (n - 1)d$$

- **Sum of First $n$ Terms ($S_n$):**
$$S_n = \frac{n}{2} \left[ 2a_1 + (n - 1)d \right] = \frac{n}{2} (a_1 + a_n)$$

- **Arithmetic Mean (AM):** The arithmetic mean of two numbers $a$ and $b$ is:
$$\text{AM} = \frac{a + b}{2}$$

## Geometric Progressions (GP) and Infinite Series

A **Geometric Progression** is a sequence where each term after the first is found by multiplying the previous term by a fixed non-zero ratio.

- **Common Ratio ($r$):** $r = \frac{a_{k+1}}{a_k}$.
- **General $n$-th Term ($a_n$):**
$$a_n = a_1 \cdot r^{n-1}$$

- **Sum of First $n$ Terms ($S_n$):**
$$S_n = \begin{cases} a_1 \left( \frac{1 - r^n}{1 - r} \right) & \text{if } r \neq 1 \\ n \cdot a_1 & \text{if } r = 1 \end{cases}$$

- **Sum of Infinite Geometric Series ($S_\infty$):** An infinite geometric series converges if and only if $|r| < 1$:
$$S_\infty = \frac{a_1}{1 - r} \quad (|r| < 1)$$

- **Geometric Mean (GM):** The geometric mean of two positive numbers $a$ and $b$ is:
$$\text{GM} = \sqrt{a \cdot b}$$

## Sequence & Series Formula Master Table

| Sequence Type | $n$-th Term ($a_n$) | Sum of $n$ Terms ($S_n$) | Infinite Sum ($S_\infty$) | Mean Property |
|---|---|---|---|---|
| Arithmetic (AP) | $a_1 + (n-1)d$ | $\frac{n}{2}[2a_1 + (n-1)d]$ | Diverges ($\pm \infty$) | $\text{AM} = \frac{a + b}{2}$ |
| Geometric (GP) | $a_1 r^{n-1}$ | $a_1 \left(\frac{1 - r^n}{1 - r}\right)$ | $\frac{a_1}{1 - r} \quad (|r| < 1)$ | $\text{GM} = \sqrt{ab}$ |
| Harmonic (HP) | $\frac{1}{a_1 + (n-1)d}$ | No simple general formula | Diverges | $\text{HM} = \frac{2ab}{a + b}$ |

## Important Formulas and Special Sum Identities

Relation Between Mean Properties ($\text{AM}, \text{GM}, \text{HM}$ for positive $a, b$):

$$\text{AM} \ge \text{GM} \ge \text{HM} \quad \text{and} \quad (\text{GM})^2 = \text{AM} \times \text{HM}$$

Standard Sigma ($\sum$) Summation Formulas:

$$\sum_{k=1}^{n} k = \frac{n(n + 1)}{2}$$

$$\sum_{k=1}^{n} k^2 = \frac{n(n + 1)(2n + 1)}{6}$$

$$\sum_{k=1}^{n} k^3 = \left[ \frac{n(n + 1)}{2} \right]^2 = \left( \sum_{k=1}^{n} k \right)^2$$

## Common Exam Traps

- **Off-by-One Exponent Error in GP:** Writing $a_n = a_1 r^n$ instead of $a_1 r^{n-1}$. The exponent for the $n$-th term is $n - 1$.
- **Applying $S_\infty$ Formula when $|r| \ge 1$:** Using $\frac{a}{1 - r}$ for an infinite series with $r = 2$ or $r = -1.5$. The infinite series **diverges** when $|r| \ge 1$.
- **Finding $a_n$ from Sum $S_n$:** Forgetting that $a_n = S_n - S_{n-1}$ for $n \ge 2$, with $a_1 = S_1$.

## Quiz

1. Find the $15$-th term of the arithmetic progression: $5, 9, 13, 17, \dots$.
  - [ ] $57$
  - [x] $61$
  - [ ] $65$
  - [ ] $60$
   > Here $a_1 = 5$ and common difference $d = 9 - 5 = 4$. Using $a_n = a_1 + (n - 1)d$: $a_{15} = 5 + (15 - 1)(4) = 5 + 14(4) = 5 + 56 = 61$.

2. What is the sum of the infinite geometric series: $12 + 4 + \frac{4}{3} + \frac{4}{9} + \dots$?
  - [ ] $16$
  - [x] $18$
  - [ ] $20$
  - [ ] $24$
   > First term $a_1 = 12$, common ratio $r = \frac{4}{12} = \frac{1}{3}$. Since $|r| = \frac{1}{3} < 1$, the series converges: $S_\infty = \frac{a_1}{1 - r} = \frac{12}{1 - 1/3} = \frac{12}{2/3} = 12 \times \frac{3}{2} = 18$.

3. Calculate the sum of the squares of the first $10$ positive integers ($\sum_{k=1}^{10} k^2$).
  - [ ] $302$
  - [ ] $340$
  - [x] $385$
  - [ ] $505$
   > Apply the sum of squares formula $\sum_{k=1}^{n} k^2 = \frac{n(n + 1)(2n + 1)}{6}$ for $n = 10$: $\frac{10(11)(21)}{6} = \frac{2310}{6} = 385$.