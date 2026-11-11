---
title: Number Systems and Mathematical Fundamentals
level: foundation
---

Mathematics is built upon the foundational structure of numbers. Understanding how different sets of numbers interact, their algebraic properties, and how they map onto the real number line provides the essential groundwork for algebra, calculus, and advanced problem-solving.

## Classification of Real Numbers

The set of real numbers, denoted by $\mathbb{R}$, comprises all numbers that can represent a distance along a continuous line. Real numbers are divided into nested sub-sets based on their structural properties.

- **Natural Numbers ($\mathbb{N}$):** The counting numbers starting from $1$: $\mathbb{N} = \{1, 2, 3, 4, \dots\}$.
- **Whole Numbers ($\mathbb{W}$):** Natural numbers combined with zero: $\mathbb{W} = \{0, 1, 2, 3, \dots\}$.
- **Integers ($\mathbb{Z}$):** Whole numbers alongside their negative opposites: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$.
- **Rational Numbers ($\mathbb{Q}$):** Numbers that can be expressed as a ratio of two integers $\frac{p}{q}$, where $p, q \in \mathbb{Z}$ and $q \neq 0$. Their decimal representations either terminate (e.g., $0.75 = \frac{3}{4}$) or repeat periodically (e.g., $0.\overline{3} = \frac{1}{3}$).
- **Irrational Numbers ($\mathbb{I}$ or $\mathbb{R} \setminus \mathbb{Q}$):** Numbers that cannot be written as a fraction of two integers. Their decimal expansions are non-terminating and non-repeating (e.g., $\sqrt{2} \approx 1.41421356\dots$, $\pi \approx 3.14159265\dots$, $e \approx 2.71828182\dots$).

## Properties of Real Numbers and Absolute Value

### Algebraic Field Axioms

For all real numbers $a, b, c \in \mathbb{R}$, the following fundamental axioms govern addition and multiplication:

1. **Closure Property:** $a + b \in \mathbb{R}$ and $a \cdot b \in \mathbb{R}$.
2. **Commutative Property:** $a + b = b + a$ and $a \cdot b = b \cdot a$.
3. **Associative Property:** $(a + b) + c = a + (b + c)$ and $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
4. **Distributive Property:** $a \cdot (b + c) = a \cdot b + a \cdot c$.
5. **Identity Elements:** Additive identity is $0$ ($a + 0 = a$); Multiplicative identity is $1$ ($a \cdot 1 = a$).
6. **Inverse Elements:** Additive inverse of $a$ is $-a$ ($a + (-a) = 0$); Multiplicative inverse of $a \neq 0$ is $\frac{1}{a}$ ($a \cdot \frac{1}{a} = 1$).

### Absolute Value and Distance

The **absolute value** of a real number $x$, written as $|x|$, represents its magnitude or non-negative distance from zero on the number line.

$$|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$

For any real numbers $a$ and $b$, the distance between them on the number line is given by $d(a, b) = |a - b|$.

## Number Set Classifications

| Set Symbol | Name | Formal Set-Builder Definition | Representative Examples |
|---|---|---|---|
| $\mathbb{N}$ | Natural Numbers | $\{x \mid x \text{ is a counting integer}\} = \{1, 2, 3, \dots\}$ | $1, 42, 10^6$ |
| $\mathbb{Z}$ | Integers | $\{x \mid x \text{ is a whole number or its negative}\}$ | $-105, -1, 0, 17$ |
| $\mathbb{Q}$ | Rational Numbers | $\left\{\frac{p}{q} \mathrel{\Big|} p, q \in \mathbb{Z}, q \neq 0\right\}$ | $-\frac{7}{2}, 0.25, 0.\overline{6}, 5$ |
| $\mathbb{I}$ | Irrational Numbers | $\{x \in \mathbb{R} \mid x \notin \mathbb{Q}\}$ | $\sqrt{3}, \pi, e, \sqrt[3]{5}$ |
| $\mathbb{R}$ | Real Numbers | $\mathbb{Q} \cup \mathbb{I}$ | All points on the number line |

## Important Formulas and Axiomatic Relationships

Principal Property of Square Roots and Absolute Value:

$$\sqrt{x^2} = |x| \quad (\text{Note: } \sqrt{x^2} \neq x \text{ if } x < 0)$$

Triangle Inequality for Real Numbers:

$$|a + b| \le |a| + |b| \quad \text{for all } a, b \in \mathbb{R}$$

Distance Between Points $a$ and $b$:

$$d(a, b) = |b - a| = |a - b|$$

## Common Exam Traps

- **Equating $\sqrt{x^2}$ directly to $x$:** Writing $\sqrt{(-5)^2} = -5$ instead of $|-5| = 5$. Principal square roots are always non-negative.
- **Assuming $\pi$ or $\sqrt{2}$ can be represented as exact fractions:** Approximations like $\frac{22}{7}$ for $\pi$ are rational approximations, but $\pi$ itself is strictly irrational.
- **Dividing by Zero:** Attempting to evaluate $\frac{a}{0}$. Division by zero is undefined within the real number system $\mathbb{R}$.

## Quiz

1. Which of the following sets correctly classifies the number $-\sqrt{16}$?
  - [ ] Irrational number ($\mathbb{I}$)
  - [ ] Natural number ($\mathbb{N}$)
  - [x] Integer ($\mathbb{Z}$) and Rational number ($\mathbb{Q}$)
  - [ ] Non-real complex number
   > Since $\sqrt{16} = 4$, we have $-\sqrt{16} = -4$, which is an integer ($\mathbb{Z}$) and therefore also a rational number ($\mathbb{Q}$).

2. What is the simplified numerical value of the expression $|3 - \pi| + |1 - \pi|$?
  - [ ] $2$
  - [x] $2\pi - 4$
  - [ ] $4 - 2\pi$
  - [ ] $-2$
   > Since $\pi \approx 3.14159$, $3 - \pi < 0 \implies |3 - \pi| = -(3 - \pi) = \pi - 3$. Similarly, $1 - \pi < 0 \implies |1 - \pi| = \pi - 1$. Adding them yields $(\pi - 3) + (\pi - 1) = 2\pi - 4$.

3. Which property of real numbers justifies the algebraic step $3(x + 4) = 3x + 12$?
  - [ ] Associative Property of Addition
  - [ ] Commutative Property of Multiplication
  - [x] Distributive Property of Multiplication over Addition
  - [ ] Additive Inverse Property
   > The Distributive Property dictates that $a(b + c) = ab + ac$. Here, $3(x + 4) = 3x + 3(4) = 3x + 12$.