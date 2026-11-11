---
title: Powers, Exponents and Roots
level: foundation
---

Exponents and radicals represent repeated multiplication and root extraction. Mastering the laws of indices, fractional exponents, and surd manipulations allows for efficient simplification of algebraic and calculus expressions.

## Laws of Exponents

For a base $a \neq 0$ and integer or rational exponents $m, n$:

- **Product Rule:** $a^m \cdot a^n = a^{m+n}$
- **Quotient Rule:** $\frac{a^m}{a^n} = a^{m-n}$
- **Power of a Power Rule:** $(a^m)^n = a^{m \cdot n}$
- **Power of a Product:** $(a \cdot b)^n = a^n \cdot b^n$
- **Power of a Quotient:** $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n} \quad (b \neq 0)$
- **Zero Exponent:** $a^0 = 1 \quad (a \neq 0)$
- **Negative Exponents:** $a^{-n} = \frac{1}{a^n} \quad \text{and} \quad \left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n$

## Radical Expressions and Fractional Exponents

### Fractional Exponents Definition

A fractional exponent connects powers with radicals:

$$a^{\frac{m}{n}} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$$

where $n \in \mathbb{N}$ is the **index** of the radical, and $a \ge 0$ whenever $n$ is an even integer.

### Operations on Surds (Radicals)

A **surd** is an irrational radical expression involving roots of integers (e.g., $\sqrt{3}, \sqrt[3]{5}$).

- **Simplifying Radicals:** Factor out perfect $n$-th powers: $\sqrt{a^2 b} = |a|\sqrt{b}$.
- **Addition and Subtraction:** Combine *like surds* (same radicand and index):
$$3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}$$
- **Rationalizing the Denominator:** Eliminating radicals from the denominator of a fraction using conjugate pairs:
$$\frac{1}{\sqrt{a} + \sqrt{b}} = \frac{1 \cdot (\sqrt{a} - \sqrt{b})}{(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b})} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$$

## Exponent Laws Summary Table

| Law Name | Algebraic Formula | Concrete Example |
|---|---|---|
| Product of Powers | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7 = 128$ |
| Quotient of Powers | $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{5^6}{5^2} = 5^4 = 625$ |
| Power to Power | $(a^m)^n = a^{m \cdot n}$ | $(3^2)^3 = 3^6 = 729$ |
| Fractional Exponent | $a^{m/n} = \sqrt[n]{a^m}$ | $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4$ |
| Negative Exponent | $a^{-n} = \frac{1}{a^n}$ | $4^{-2} = \frac{1}{4^2} = \frac{1}{16}$ |
| Radical Product | $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$ | $\sqrt{3} \cdot \sqrt{12} = \sqrt{36} = 6$ |

## Important Formulas and Rationalization Identities

Conjugate Radical Rationalization:

$$\frac{k}{\sqrt{x} + \sqrt{y}} = \frac{k(\sqrt{x} - \sqrt{y})}{x - y} \quad (x \neq y)$$

$$\frac{k}{a + b\sqrt{c}} = \frac{k(a - b\sqrt{c})}{a^2 - b^2 c}$$

Nested Square Root Simplification:

$$\sqrt{x \pm 2\sqrt{y}} = \sqrt{a} \pm \sqrt{b} \quad \text{where } a+b = x \text{ and } a \cdot b = y$$

## Common Exam Traps

- **Distributing Exponents Over Addition:** Incorrectly writing $(a + b)^n = a^n + b^n$. $(a + b)^2 = a^2 + 2ab + b^2 \neq a^2 + b^2$.
- **Confusing Power of Powers:** Assuming $(a^m)^n = a^{m^n}$. Note that $(2^3)^2 = 2^{3 \times 2} = 2^6 = 64$, whereas $2^{3^2} = 2^9 = 512$.
- **Forgetting Absolute Values on Even Roots:** Writing $\sqrt{x^2} = x$ for real numbers. Correct formulation is $\sqrt{x^2} = |x|$.

## Quiz

1. Evaluate the numerical expression: $\left(\frac{16}{81}\right)^{-\frac{3}{4}}$.
  - [ ] $\frac{8}{27}$
  - [ ] $-\frac{27}{8}$
  - [x] $\frac{27}{8}$
  - [ ] $\frac{64}{243}$
   > First invert the base due to negative exponent: $\left(\frac{81}{16}\right)^{\frac{3}{4}}$. Take the $4$-th root: $\sqrt[4]{81} = 3$ and $\sqrt[4]{16} = 2$. Cube the result: $\left(\frac{3}{2}\right)^3 = \frac{27}{8}$.

2. Simplify the radical expression completely: $\frac{6}{\sqrt{5} - \sqrt{2}}$.
  - [ ] $2(\sqrt{5} - \sqrt{2})$
  - [x] $2(\sqrt{5} + \sqrt{2})$
  - [ ] $3(\sqrt{5} + \sqrt{2})$
  - [ ] $\sqrt{5} + \sqrt{2}$
   > Multiply numerator and denominator by conjugate $(\sqrt{5} + \sqrt{2})$: $\frac{6(\sqrt{5} + \sqrt{2})}{(\sqrt{5})^2 - (\sqrt{2})^2} = \frac{6(\sqrt{5} + \sqrt{2})}{5 - 2} = \frac{6(\sqrt{5} + \sqrt{2})}{3} = 2(\sqrt{5} + \sqrt{2})$.

3. Solve for $x$ in the exponential equation: $9^{x+1} = 27^{2x-1}$.
  - [ ] $x = 1$
  - [x] $x = \frac{5}{4}$
  - [ ] $x = \frac{3}{2}$
  - [ ] $x = 2$
   > Express both sides using base $3$: $(3^2)^{x+1} = (3^3)^{2x-1} \implies 3^{2x+2} = 3^{6x-3}$. Equating exponents: $2x + 2 = 6x - 3 \implies 4x = 5 \implies x = \frac{5}{4}$.