---
title: Advanced Inequalities and Absolute Value
level: intermediate
---

Advanced inequalities involve absolute values, quadratic expressions, rational functions, and radical expressions. Solving them requires understanding inequality properties, identifying critical points, analyzing signs across intervals, and applying techniques such as the **Wavy Curve Method** and **AM-GM inequality**.

## Absolute Value Equations and Inequalities

The **absolute value** of a real number \(x\), denoted by \(|x|\), represents its non-negative distance from zero on the number line.

\[
|x| =
\begin{cases}
x & \text{if } x \geq 0 \\
-x & \text{if } x < 0
\end{cases}
\]

For example:

\[
|5| = 5, \qquad |-5| = 5
\]

### Fundamental Absolute Value Theorems

For \(a > 0\), the following properties are essential:

1. **Absolute Value Equation**

   \[
   |x| = a \iff x = a \text{ or } x = -a
   \]

2. **Less-Than Absolute Value Inequality**

   \[
   |x| < a \iff -a < x < a
   \]

   This represents a bounded interval:

   \[
   x \in (-a,a)
   \]

3. **Greater-Than Absolute Value Inequality**

   \[
   |x| > a \iff x < -a \text{ or } x > a
   \]

   This represents two unbounded intervals:

   \[
   x \in (-\infty,-a) \cup (a,\infty)
   \]

4. **Absolute Values of Two Expressions**

   \[
   |f(x)| = |g(x)|
   \]

   is equivalent to:

   \[
   f(x) = g(x) \quad \text{or} \quad f(x) = -g(x)
   \]

### Inclusive Inequalities

When the inequality contains equality, the boundary points must also be included.

\[
|x| \leq a \iff -a \leq x \leq a
\]

\[
|x| \geq a \iff x \leq -a \text{ or } x \geq a
\]

For a shifted absolute value expression:

\[
|x-c| \leq r
\]

the solution is:

\[
c-r \leq x \leq c+r
\]

Similarly:

\[
|x-c| \geq r
\]

gives:

\[
x \leq c-r \quad \text{or} \quad x \geq c+r
\]

where \(r \geq 0\).

## Rational Inequalities and the Wavy Curve Method

The **Wavy Curve Method**, also called the **Sign Scheme**, is used to solve polynomial and rational inequalities by analyzing the signs of their factors across intervals.

It is particularly useful for inequalities of the form:

\[
\frac{P(x)}{Q(x)} > 0
\]

or

\[
\frac{P(x)}{Q(x)} \leq 0
\]

where \(P(x)\) and \(Q(x)\) are polynomials and \(Q(x) \neq 0\).

### Steps of the Wavy Curve Method

1. **Move all terms to one side:** Rewrite the inequality so that the other side is zero.

2. **Factorize:** Express the numerator and denominator as products of linear factors, wherever possible.

3. **Identify critical points:** Find the real roots of the numerator and denominator.

4. **Mark the number line:** Arrange all distinct critical points in increasing order.
   - Numerator roots are included only when the inequality permits equality.
   - Denominator roots are always excluded because division by zero is undefined.

5. **Determine the signs:** Start with the sign in the rightmost interval and move across the critical points.
   - At a root with odd multiplicity, the sign changes.
   - At a root with even multiplicity, the sign remains unchanged.

6. **Select the required intervals:** Choose the intervals where the expression satisfies the given inequality.

### Example: Solving a Rational Inequality

Solve:

\[
\frac{x-3}{x+1} \leq 0
\]

**Step 1: Identify the critical points.**

Numerator:

\[
x-3=0 \implies x=3
\]

Denominator:

\[
x+1=0 \implies x=-1
\]

**Step 2: Arrange the critical points.**

\[
-1 < 3
\]

These points divide the number line into three intervals:

\[
(-\infty,-1), \quad (-1,3), \quad (3,\infty)
\]

**Step 3: Analyze the signs.**

| Interval | Sign of \(x-3\) | Sign of \(x+1\) | Overall sign |
|---|---|---|---|
| \((-\infty,-1)\) | \(-\) | \(-\) | \(+\) |
| \((-1,3)\) | \(-\) | \(+\) | \(-\) |
| \((3,\infty)\) | \(+\) | \(+\) | \(+\) |

**Step 4: Select the required intervals.**

Since the inequality is \(\leq 0\), select the negative interval and include the numerator root \(x=3\).

The denominator root \(x=-1\) must be excluded.

Therefore:

\[
\boxed{x \in (-1,3]}
\]

## Absolute Value and Inequality Theorem Table

| Form / Condition | Solution Set / Transformation | Interval Notation |
|---|---|---|
| \(|x-c| \leq r\) | \(c-r \leq x \leq c+r\) | \([c-r,c+r]\) |
| \(|x-c| < r\) | \(c-r < x < c+r\) | \((c-r,c+r)\) |
| \(|x-c| \geq r\) | \(x \leq c-r\) or \(x \geq c+r\) | \((-\infty,c-r] \cup [c+r,\infty)\) |
| \(|x-c| > r\) | \(x < c-r\) or \(x > c+r\) | \((-\infty,c-r) \cup (c+r,\infty)\) |
| \((x-a)(x-b) < 0,\ a<b\) | \(a < x < b\) | \((a,b)\) |
| \((x-a)(x-b) > 0,\ a<b\) | \(x < a\) or \(x > b\) | \((-\infty,a) \cup (b,\infty)\) |
| \(\frac{x-a}{x-b} \leq 0,\ a<b\) | \(a \leq x < b\) | \([a,b)\) |

**Important:** In the last row, \(x=a\) is included because it makes the numerator zero, whereas \(x=b\) is excluded because it makes the denominator zero.

## Important Formulas and AM-GM Inequality

### Arithmetic Mean-Geometric Mean Inequality

The **AM-GM inequality** states that the arithmetic mean of two non-negative real numbers is greater than or equal to their geometric mean.

For \(a,b \geq 0\):

\[
\frac{a+b}{2} \geq \sqrt{ab}
\]

Equivalently:

\[
a+b \geq 2\sqrt{ab}
\]

Equality holds if and only if:

\[
a=b
\]

**Application: Finding a Minimum Value**

Consider:

\[
f(x)=x+\frac{9}{x}, \qquad x>0
\]

Applying AM-GM:

\[
x+\frac{9}{x}
\geq 2\sqrt{x\cdot\frac{9}{x}}
\]

\[
=2\sqrt{9}=6
\]

Therefore:

\[
f(x)\geq 6
\]

Equality occurs when:

\[
x=\frac{9}{x}
\]

\[
x^2=9
\]

Since \(x>0\):

\[
x=3
\]

Hence, the minimum value is:

\[
\boxed{6}
\]

### Triangle Inequality

For any real numbers \(a\) and \(b\):

\[
|a+b| \leq |a|+|b|
\]

\[
|a-b| \leq |a|+|b|
\]

The reverse triangle inequality is:

\[
\boxed{\left||a|-|b|\right| \leq |a\pm b|}
\]

These inequalities are useful for estimating absolute values without evaluating them directly.

### Square of Absolute Value

For every real number \(x\):

\[
\boxed{|x|^2=x^2}
\]

This follows because squaring eliminates the sign of a real number.

## Common Exam Traps

- **Including denominator roots:** A denominator root must always be excluded from the solution set, even when the inequality contains \(\leq\) or \(\geq\). Equality cannot make division by zero valid.

- **Incorrectly splitting absolute value inequalities:** Writing \(|x|>5\) as \(-5>x>5\) is incorrect. The correct interpretation is:

  \[
  x<-5 \quad \text{or} \quad x>5
  \]

- **Ignoring sign changes when multiplying inequalities:** Multiplying or dividing an inequality by a negative expression reverses its direction. If the sign of a variable expression is unknown, analyze its sign before multiplying.

- **Confusing strict and inclusive inequalities:** The symbols \(<\) and \(>\) exclude boundary points, whereas \(\leq\) and \(\geq\) include valid boundary points.

- **Applying AM-GM without checking non-negativity:** The standard AM-GM inequality requires non-negative quantities. Check the domain before applying it.

- **Assuming every critical point changes the sign:** Sign changes occur at roots of odd multiplicity. Roots of even multiplicity do not change the sign.

## Quiz

1. Solve the absolute value inequality for \(x\):

   \[
   |2x-3| \leq 7
   \]

   - [x] \([-2,5]\)
   - [ ] \((-\infty,-2] \cup [5,\infty)\)
   - [ ] \([-5,2]\)
   - [ ] \((-2,5)\)

   > Rewrite the inequality as a double inequality:
   >
   > \[
   > -7 \leq 2x-3 \leq 7
   > \]
   >
   > Add \(3\) to all three parts:
   >
   > \[
   > -4 \leq 2x \leq 10
   > \]
   >
   > Divide by \(2\):
   >
   > \[
   > -2 \leq x \leq 5
   > \]
   >
   > Therefore, the solution interval is \([-2,5]\).

2. Find the solution set for the rational inequality:

   \[
   \frac{x-3}{x+1} \leq 0
   \]

   - [ ] \([-1,3]\)
   - [x] \((-1,3]\)
   - [ ] \((-\infty,-1) \cup [3,\infty)\)
   - [ ] \([-1,3)\)

   > The critical points are \(x=3\), obtained from the numerator, and \(x=-1\), obtained from the denominator.
   >
   > These points divide the number line into three intervals:
   >
   > \[
   > (-\infty,-1),\quad (-1,3),\quad (3,\infty)
   > \]
   >
   > Sign analysis shows that the expression is negative in \((-1,3)\). The numerator becomes zero at \(x=3\), so this point is included. However, \(x=-1\) makes the denominator zero and must be excluded.
   >
   > Therefore:
   >
   > \[
   > \boxed{(-1,3]}
   > \]

3. Using the AM-GM inequality, what is the minimum value of the function?

   \[
   f(x)=x+\frac{9}{x}, \qquad x>0
   \]

   - [ ] \(3\)
   - [x] \(6\)
   - [ ] \(9\)
   - [ ] \(12\)

   > By AM-GM, for two non-negative quantities \(a=x\) and \(b=\frac{9}{x}\):
   >
   > \[
   > \frac{x+\frac{9}{x}}{2}
   > \geq \sqrt{x\cdot\frac{9}{x}}
   > \]
   >
   > Simplifying:
   >
   > \[
   > \frac{x+\frac{9}{x}}{2}\geq 3
   > \]
   >
   > Therefore:
   >
   > \[
   > x+\frac{9}{x}\geq 6
   > \]
   >
   > Equality occurs when \(x=\frac{9}{x}\), giving \(x=3\) because \(x>0\).
   >
   > Hence, the minimum value is \(\boxed{6}\).
