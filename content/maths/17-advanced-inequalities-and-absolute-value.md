---
title: Advanced Inequalities and Absolute Value
level: intermediate
---

This lesson covers absolute value inequalities, rational inequalities, sign analysis, the Wavy Curve Method, AM-GM inequality, and triangle inequalities.

## 1. Absolute Value

Absolute value represents the non-negative distance of a number from zero.

\[
|x| =
\begin{cases}
x & x \geq 0 \\
-x & x < 0
\end{cases}
\]

Examples: \(|5|=5\), \(|-5|=5\).

### Absolute Value Properties

For \(a>0\):

| Expression | Equivalent form |
|---|---|
| \(|x|=a\) | \(x=a\) or \(x=-a\) |
| \(|x|<a\) | \(-a<x<a\) |
| \(|x|\leq a\) | \(-a\leq x\leq a\) |
| \(|x|>a\) | \(x<-a\) or \(x>a\) |
| \(|x|\geq a\) | \(x\leq-a\) or \(x\geq a\) |

For two expressions:

\[
|f(x)|=|g(x)|
\]

Therefore:

\[
f(x)=g(x)\quad\text{or}\quad f(x)=-g(x)
\]

### Shifted Absolute Values

For \(r\geq0\):

\[
|x-c|\leq r
\iff c-r\leq x\leq c+r
\]

\[
|x-c|\geq r
\iff x\leq c-r\text{ or }x\geq c+r
\]

## 2. Rational Inequalities

A rational inequality contains a fraction involving polynomial expressions.

Examples:

\[
\frac{x-2}{x+3}>0
\]

\[
\frac{x^2-4}{x-1}\leq0
\]

The denominator must never equal zero.

### Wavy Curve Method

The Wavy Curve Method determines where a polynomial or rational expression is positive or negative.

**Procedure:**

1. Move all terms to one side.
2. Factorize the expression.
3. Find the zeros of the numerator and denominator.
4. Arrange the critical points in increasing order.
5. Divide the number line into intervals.
6. Determine the sign in each interval.
7. Select the intervals satisfying the inequality.

**Rules:**

- Numerator roots may be included when equality is allowed.
- Denominator roots are always excluded.
- Odd-multiplicity roots change the sign.
- Even-multiplicity roots do not change the sign.

### Worked Example

Solve:

\[
\frac{x-3}{x+1}\leq0
\]

**Step 1: Find critical points.**

\[
x-3=0\implies x=3
\]

\[
x+1=0\implies x=-1
\]

**Step 2: Divide the number line.**

\[
(-\infty,-1),\quad(-1,3),\quad(3,\infty)
\]

**Step 3: Analyze signs.**

| Interval | Expression sign |
|---|---|
| \((-\infty,-1)\) | Positive |
| \((-1,3)\) | Negative |
| \((3,\infty)\) | Positive |

**Step 4: Write the solution.**

The expression must be negative or zero.

- Include \(x=3\), where the numerator is zero.
- Exclude \(x=-1\), where the denominator is zero.

\[
\boxed{x\in(-1,3]}
\]

## 3. Important Inequality Formulas

### Absolute Value

| Inequality | Solution |
|---|---|
| \(|x-c|<r\) | \(c-r<x<c+r\) |
| \(|x-c|\leq r\) | \(c-r\leq x\leq c+r\) |
| \(|x-c|>r\) | \(x<c-r\) or \(x>c+r\) |
| \(|x-c|\geq r\) | \(x\leq c-r\) or \(x\geq c+r\) |

### Quadratic Expressions

For \(a<b\):

\[
(x-a)(x-b)<0
\]

\[
\boxed{a<x<b}
\]

Similarly:

\[
(x-a)(x-b)>0
\]

\[
\boxed{x<a\text{ or }x>b}
\]

### Rational Expressions

For \(a<b\):

\[
\frac{x-a}{x-b}\leq0
\]

\[
\boxed{x\in[a,b)}
\]

The numerator root is included, but the denominator root is excluded.

## 4. AM-GM Inequality

The Arithmetic Mean-Geometric Mean inequality states that the arithmetic mean of two non-negative numbers is greater than or equal to their geometric mean.

For \(a,b\geq0\):

\[
\frac{a+b}{2}\geq\sqrt{ab}
\]

Equivalently:

\[
\boxed{a+b\geq2\sqrt{ab}}
\]

Equality occurs when:

\[
a=b
\]

### Application: Finding a Minimum

Find the minimum value of:

\[
f(x)=x+\frac{9}{x},\qquad x>0
\]

Applying AM-GM:

\[
x+\frac{9}{x}
\geq2\sqrt{x\cdot\frac{9}{x}}
\]

\[
x+\frac{9}{x}\geq6
\]

Equality occurs when:

\[
x=\frac{9}{x}
\]

\[
x^2=9
\]

Since \(x>0\), \(x=3\).

Therefore:

\[
\boxed{\text{Minimum value}=6}
\]

## 5. Triangle Inequality

For real numbers \(a\) and \(b\):

\[
|a+b|\leq|a|+|b|
\]

\[
|a-b|\leq|a|+|b|
\]

The reverse triangle inequality is:

\[
\boxed{\left||a|-|b|\right|\leq|a\pm b|}
\]

Another important property is:

\[
\boxed{|x|^2=x^2}
\]

## 6. Common Exam Traps

- **Denominator roots:** Never include values that make the denominator zero.
- **Absolute value splitting:** \(|x|>5\) means \(x<-5\) or \(x>5\), not a double inequality.
- **Negative multiplication:** Reverse the inequality sign when multiplying or dividing by a negative number.
- **Boundary points:** Strict inequalities exclude endpoints; inclusive inequalities include valid endpoints.
- **AM-GM conditions:** Check that both quantities are non-negative.
- **Repeated roots:** Even-multiplicity roots do not change the sign.

## Quiz

1. Solve:

   \[
   |2x-3|\leq7
   \]

   - [x] \([-2,5]\)
   - [ ] \((-\infty,-2]\cup[5,\infty)\)
   - [ ] \([-5,2]\)
   - [ ] \((-2,5)\)

   > \[
   > -7\leq2x-3\leq7
   > \]
   >
   > \[
   > -4\leq2x\leq10
   > \]
   >
   > \[
   > \boxed{-2\leq x\leq5}
   > \]

2. Solve:

   \[
   \frac{x-3}{x+1}\leq0
   \]

   - [ ] \([-1,3]\)
   - [x] \((-1,3]\)
   - [ ] \((-\infty,-1)\cup[3,\infty)\)
   - [ ] \([-1,3)\)

   > The critical points are \(-1\) and \(3\). The expression is negative between them. Include \(3\), because the numerator becomes zero, and exclude \(-1\), because the denominator becomes zero.
   >
   > \[
   > \boxed{(-1,3]}
   > \]

3. Find the minimum value:

   \[
   f(x)=x+\frac{9}{x},\qquad x>0
   \]

   - [ ] \(3\)
   - [x] \(6\)
   - [ ] \(9\)
   - [ ] \(12\)

   > Applying AM-GM:
   >
   > \[
   > x+\frac{9}{x}
   > \geq2\sqrt{x\cdot\frac{9}{x}}=6
   > \]
   >
   > Equality occurs at \(x=3\).
   >
   > \[
   > \boxed{\text{Minimum value}=6}
   > \]
