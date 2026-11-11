---
title: Advanced Inequalities and Absolute Value
level: intermediate
---

Advanced inequalities involve absolute values, quadratic expressions, rational functions, and radical terms. Solving them requires analyzing critical points, sign schemes (the Wavy Curve Method), and absolute value properties.

## Absolute Value Equations and Inequalities

The **absolute value** $|x|$ represents the non-negative distance of $x$ from origin:

$$|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$

### Fundamental Absolute Value Theorems ($a > 0$)

1. **Absolute Value Equation:**
$$|x| = a \iff x = a \quad \text{or} \quad x = -a$$

2. **"Less Than" Absolute Inequality (Bounded Interval):**
$$|x| < a \iff -a < x < a \iff x \in (-a, a)$$

3. **"Greater Than" Absolute Inequality (Unbounded Union):**
$$|x| > a \iff x < -a \quad \text{or} \quad x > a \iff x \in (-\infty, -a) \cup (a, \infty)$$

4. **Two Absolute Values:**
$$|f(x)| = |g(x)| \iff f(x) = g(x) \quad \text{or} \quad f(x) = -g(x)$$

## Rational Inequalities and the Wavy Curve Method

The **Wavy Curve Method (Sign Scheme)** solves polynomial and rational inequalities of the form $\frac{P(x)}{Q(x)} > 0$ or $\le 0$.

```text
                     Wavy Curve Method Algorithm
                                  │
  1. Move all terms to one side so the right side is 0.
                                  │
  2. Factor numerator P(x) and denominator Q(x) into linear factors (x - c_i).
                                  │
  3. Find all Critical Points (roots of numerator & denominator).
                                  │
  4. Plot critical points on a number line (Open circles for denominator roots!).
                                  │
  5. Test sign in rightmost interval; alternate signs at odd-power roots.
                                  │
  6. Select intervals matching the inequality sign (> 0 for +, < 0 for -).
```

## Absolute Value & Inequality Theorem Table

| Form / Condition | Solution Set / Transformation | Interval Notation |
|---|---|---|
| $|x - c| \le r$ | $c - r \le x \le c + r$ | $[c - r, c + r]$ |
| $|x - c| \ge r$ | $x \le c - r \quad \text{or} \quad x \ge c + r$ | $(-\infty, c - r] \cup [c + r, \infty)$ |
| $(x - a)(x - b) < 0 \quad (a < b)$ | $a < x < b$ | $(a, b)$ |
| $(x - a)(x - b) > 0 \quad (a < b)$ | $x < a \quad \text{or} \quad x > b$ | $(-\infty, a) \cup (b, \infty)$ |
| $\frac{x - a}{x - b} \le 0 \quad (a < b)$ | $a \le x < b$ | $[a, b) \quad \text{(Exclude denominator root } b\text{!)}$ |

## Important Formulas and AM-GM Inequality

Arithmetic Mean - Geometric Mean (AM-GM) Inequality (for $a, b \ge 0$):

$$\text{AM} \ge \text{GM} \implies \frac{a + b}{2} \ge \sqrt{a \cdot b} \quad (\text{Equality holds } \iff a = b)$$

Triangle Inequality Properties:

$$||a| - |b|| \le |a \pm b| \le |a| + |b|$$

Square of Absolute Value:

$$|x|^2 = x^2$$

## Common Exam Traps

- **Including Denominator Roots in Closed Intervals:** Including denominator critical points in the solution set when given $\le$ or $\ge$. Denominator roots **must always be excluded** (open intervals) to prevent division by zero.
- **Splitting Inequalities incorrectly:** Writing $|x| > 5 \implies -5 > x > 5$, which is logically impossible. The correct split is $x < -5$ OR $x > 5$.
- **Canceling Terms with Variables without checking signs:** Multiplying an inequality by $(x - 2)$ without considering if $(x - 2) < 0$ (which flips the sign).

## Quiz

1. Solve the absolute value inequality for $x$: $|2x - 3| \le 7$.
  - [ ] $[-2, 5]$
  - [x] $[-2, 5]$
  - [ ] $(-\infty, -2] \cup [5, \infty)$
  - [ ] $[-5, 2]$
   > Rewrite as double inequality: $-7 \le 2x - 3 \le 7$. Add $3$ across all parts: $-4 \le 2x \le 10$. Divide by $2$: $-2 \le x \le 5$, which is interval $[-2, 5]$.

2. Find the solution set for the rational inequality: $\frac{x - 3}{x + 1} \le 0$.
  - [ ] $[-1, 3]$
  - [x] $(-1, 3]$
  - [ ] $(-\infty, -1) \cup [3, \infty)$
  - [ ] $[-1, 3)$
   > Critical points are $x = 3$ (numerator) and $x = -1$ (denominator). Denominator root $x = -1$ must be excluded (open parenthesis). Numerator root $x = 3$ is included (closed bracket). Testing intervals gives negative region in $(-1, 3]$.

3. Using the AM-GM inequality, what is the minimum value of $f(x) = x + \frac{9}{x}$ for $x > 0$?
  - [ ] $3$
  - [x] $6$
  - [ ] $9$
  - [ ] $12$
   > By AM-GM for $a = x$ and $b = \frac{9}{x}$: $\frac{x + \frac{9}{x}}{2} \ge \sqrt{x \cdot \frac{9}{x}} = \sqrt{9} = 3 \implies x + \frac{9}{x} \ge 2 \times 3 = 6$. Minimum value is $6$.