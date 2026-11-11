---
title: Factors, Multiples and Number Properties
level: foundation
---

Number theory focuses on the properties of integers. Understanding prime factorization, Greatest Common Divisors ($\text{GCD}$), Least Common Multiples ($\text{LCM}$), modular arithmetic, and the Euclidean algorithm forms the core of discrete mathematics and competitive quantitative analysis.

## GCD, LCM, and Fundamental Number Relations

- **Factor (Divisor):** An integer $d$ is a factor of $a$ if there exists an integer $k$ such that $a = d \cdot k$.
- **Multiple:** An integer $m$ is a multiple of $a$ if $m = a \cdot k$ for some integer $k$.
- **Greatest Common Divisor ($\text{GCD}$ or $\text{HCF}$):** The largest positive integer that divides two or more integers without a remainder.
- **Least Common Multiple ($\text{LCM}$):** The smallest positive integer that is a multiple of two or more integers.

### Calculating GCD and LCM using Prime Factorization

Given prime factorizations of two integers $a$ and $b$:

$$a = p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}, \qquad b = p_1^{f_1} \cdot p_2^{f_2} \cdots p_k^{f_k}$$

- **$\text{GCD}(a, b)$:** Product of the minimum powers of all common prime factors:
$$\text{GCD}(a, b) = p_1^{\min(e_1, f_1)} \cdot p_2^{\min(e_2, f_2)} \cdots p_k^{\min(e_k, f_k)}$$

- **$\text{LCM}(a, b)$:** Product of the maximum powers of all prime factors present:
$$\text{LCM}(a, b) = p_1^{\max(e_1, f_1)} \cdot p_2^{\max(e_2, f_2)} \cdots p_k^{\max(e_k, f_k)}$$

## The Euclidean Algorithm and Modular Arithmetic

### The Euclidean Algorithm for GCD

The Euclidean algorithm computes the $\text{GCD}$ of two integers efficiently without factorizing them, using the Division Algorithm property: $\text{GCD}(a, b) = \text{GCD}(b, a \bmod b)$.

$$\begin{aligned}
a &= b \cdot q_1 + r_1 \quad (0 \le r_1 < b) \\
b &= r_1 \cdot q_2 + r_2 \quad (0 \le r_2 < r_1) \\
r_1 &= r_2 \cdot q_3 + r_3 \\
&\;\;\vdots \\
r_{k-1} &= r_k \cdot q_{k+1} + 0
\end{aligned}$$

The last non-zero remainder $r_k$ is equal to $\text{GCD}(a, b)$.

### Basics of Modular Arithmetic

For a positive integer $m$ (the *modulus*), two integers $a$ and $b$ are **congruent modulo $m$**, written as $a \equiv b \pmod m$, if their difference $(a - b)$ is a multiple of $m$ (i.e., $m \mid (a - b)$). Equivalently, $a$ and $b$ leave the same remainder when divided by $m$.

## GCD vs. LCM Comparison Table

| Property | Greatest Common Divisor ($\text{GCD}$) | Least Common Multiple ($\text{LCM}$) |
|---|---|---|
| Definition | Largest integer dividing all numbers | Smallest integer divisible by all numbers |
| Prime Power Rule | Takes $\min(e_i, f_i)$ of prime powers | Takes $\max(e_i, f_i)$ of prime powers |
| Bound | $\text{GCD}(a, b) \le \min(a, b)$ | $\text{LCM}(a, b) \ge \max(a, b)$ |
| Fraction Application | Used for reducing fractions to lowest terms | Used for finding Least Common Denominator |
| Product Identity | $\text{GCD}(a, b) \times \text{LCM}(a, b) = a \times b$ | $\text{GCD}(a, b) \times \text{LCM}(a, b) = a \times b$ |

## Important Formulas and Number Theory Identities

Fundamental Product Relation for Two Integers:

$$\text{GCD}(a, b) \times \text{LCM}(a, b) = a \times b$$

Number of Divisors of an Integer $n = p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}$:

$$d(n) = (e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$$

Sum of Divisors of $n$:

$$\sigma(n) = \left(\frac{p_1^{e_1 + 1} - 1}{p_1 - 1}\right) \left(\frac{p_2^{e_2 + 1} - 1}{p_2 - 1}\right) \cdots \left(\frac{p_k^{e_k + 1} - 1}{p_k - 1}\right)$$

## Common Exam Traps

- **Extrapolating Product Identity to Three Numbers:** Assuming $\text{GCD}(a, b, c) \times \text{LCM}(a, b, c) = a \cdot b \cdot c$. This product relation holds **strictly for two numbers only**.
- **Confusing Divisors and Multiples:** Setting up LCM when GCD is required in practical word problems (e.g., dividing items into equal groups requires GCD; recurring events timing requires LCM).
- **Miscounting Total Divisors:** Forgetting to add $1$ to exponents when calculating the number of divisors (e.g., for $12 = 2^2 \times 3^1$, total divisors are $(2+1)(1+1) = 6$, not $2 \times 1 = 2$).

## Quiz

1. What is the total number of positive divisors of the integer $n = 360$?
  - [ ] $12$
  - [ ] $18$
  - [x] $24$
  - [ ] $36$
   > Prime factorization of $360 = 2^3 \times 3^2 \times 5^1$. The total number of divisors $d(360) = (3+1)(2+1)(1+1) = 4 \times 3 \times 2 = 24$.

2. The $\text{GCD}$ of two numbers is $12$ and their $\text{LCM}$ is $420$. If one of the numbers is $60$, what is the other number?
  - [ ] $70$
  - [x] $84$
  - [ ] $96$
  - [ ] $105$
   > Using $\text{GCD}(a,b) \times \text{LCM}(a,b) = a \times b$: $12 \times 420 = 60 \times b \implies 5040 = 60b \implies b = \frac{5040}{60} = 84$.

3. Find the remainder when $2^{50}$ is divided by $7$.
  - [ ] $1$
  - [ ] $2$
  - [x] $4$
  - [ ] $5$
   > Note that $2^3 = 8 \equiv 1 \pmod 7$. We express exponent $50 = 3 \times 16 + 2$. Thus, $2^{50} = (2^3)^{16} \cdot 2^2 \equiv (1)^{16} \cdot 4 \equiv 4 \pmod 7$.