---
title: Advanced Inequalities and Absolute Value
level: intermediate
---

Advanced inequalities involve absolute values, polynomial expressions, rational expressions, and radicals. This lesson covers absolute value properties, sign analysis, the Wavy Curve Method, and the AM-GM inequality.

## 1. Absolute Value

The absolute value of a real number is its non-negative distance from zero.

\[
|x| =
\begin{cases}
x, & x \geq 0 \\
-x, & x < 0
\end{cases}
\]

Examples:

\[
|5|=5,\qquad |-5|=5
\]

### 1.1 Absolute Value Equations

For \(a>0\):

\[
|x|=a \iff x=a \text{ or } x=-a
\]

For two expressions:

\[
|f(x)|=|g(x)|
\]

Therefore:

\[
f(x)=g(x) \text{ or } f(x)=-g(x)
\]

### 1.2 Absolute Value Inequalities

For \(a>0\):

**Less than:**

\[
|x|<a \iff -a<x<a
\]

**Less than or equal to:**

\[
|x|\leq a \iff -a\leq x\leq a
\]

**Greater than:**

\[
|x|>a \iff x<-a \text{ or } x>a
\]

**Greater than or equal to:**

\[
|x|\geq a \iff x\leq-a \text{ or } x\geq a
\]

### 1.3 Shifted Absolute Value

For \(r\geq0\):

\[
|x-c|\leq r
\]

gives:

\[
c-r\leq x\leq c+r
\]

Similarly:

\[
|x-c|\geq r
\]

gives:

\[
x\leq c-r \text{ or } x\geq c+r
\]

## 2. Rational Inequalities

Rational inequalities contain polynomial expressions in the numerator and denominator.

Examples:

\[
\frac{x-2}{x+3}>0
\]

\[
\frac{x^2-4}{x-1}\leq0
\]

The denominator must never equal zero.

### 2.1 Wavy Curve Method

The Wavy Curve Method is a technique for determining where a factored polynomial or rational expression is positive or negative.

**Procedure:**

1. Move all terms to one side.
2. Factorize the numerator and denominator.
3. Find the real zeros of all factors.
4. Arrange the critical points in increasing order.
5. Divide the number line into intervals.
6. Determine the sign in each interval.
7. Select the intervals satisfying the inequality.

**Important rules:**

- Numerator roots can be included when equality is allowed.
- Denominator roots must always be excluded.
- Odd-multiplicity roots change the sign.
- Even-multiplicity roots do not change the sign.

### 2.2 Worked Example

Solve:

\[
\frac{x-3}{x+1}\leq0
\]

**Step 1: Find the critical points.**

Numerator:

\[
x-3=0\implies x=3
\]

Denominator:

\[
x+1=0\implies x=-1
\]

**Step 2: Divide the number line.**

The intervals are:

\[
(-\infty,-1),\quad(-1,3),\quad(3,\infty)
\]

**Step 3: Determine the signs.**

| Interval | Numerator | Denominator | Expression |
|---|---|---|---|
| \((-\infty,-1)\) | Negative | Negative | Positive |
| \((-1,3)\) | Negative | Positive | Negative |
| \((3,\infty)\) | Positive | Positive | Positive |

**Step 4: Select the solution.**

The expression must be less than or equal to zero.

- Select \((-1,3)\), where the expression is negative.
- Include \(x=3\), where the numerator is zero.
- Exclude \(x=-1\), where the denominator is zero.

Final answer:

\[
\boxed{x\in(-1,3]}
\]

## 3. Important Inequality Formulas

### 3.1 Absolute Value Rules

| Inequality | Solution |
|---|---|
| \(|x-c|<r\) | \(c-r<x<c+r\) |
| \(|x-c|\leq r\) | \(c-r\leq x\leq c+r\) |
| \(|x-c|>r\) | \(x<c-r\) or \(x>c+r\) |
| \(|x-c|\geq r\) | \(x\leq c-r\) or \(x\geq c+r\) |

### 3.2 Quadratic Sign Rules

For \(a<b\):

\[
(x-a)(x-b)<0
\]

Solution:

\[
a<x<b
\]

Similarly:

\[
(x-a)(x-b)>0
\]

Solution:

\[
x<a \text{ or } x>b
\]

### 3.3 Rational Sign Rule

For \(a<b\):

\[
\frac{x-a}{x-b}\leq0
\]

Solution:

\[
\boxed{x\in[a,b)}
\]

The numerator root \(a\) is included, but the denominator root \(b\) is excluded.

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

Equality holds when:

\[
a=b
\]

### 4.1 Finding Minimum Values

Consider:

\[
f(x)=x+\frac{9}{x},\qquad x>0
\]

Applying AM-GM:

\[
x+\frac{9}{x}
\geq2\sqrt{x\cdot\frac{9}{x}}
\]

\[
x+\frac{9}{x}\geq2\sqrt{9}
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

Since \(x>0\):

\[
x=3
\]

Therefore, the minimum value is:

\[
\boxed{6}
\]

## 5. Triangle Inequality

For any real numbers \(a\) and \(b\):

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

These properties are useful when simplifying and estimating absolute value expressions.

### Square of Absolute Value

For every real number \(x\):

\[
\boxed{|x|^2=x^2}
\]

## 6. Common Exam Traps

- **Including denominator roots:** Denominator roots are always excluded because division by zero is undefined.
- **Incorrect absolute value splitting:** The inequality \(|x|>5\) gives \(x<-5\) or \(x>5\), not a double inequality.
- **Ignoring negative multiplication:** Multiplying or dividing by a negative number reverses the inequality sign.
- **Confusing strict and inclusive inequalities:** Strict inequalities exclude boundary points; inclusive inequalities include valid boundary points.
- **Incorrect AM-GM application:** The quantities must be non-negative.
- **Ignoring multiplicity:** Odd-multiplicity roots change signs, while even-multiplicity roots do not.

## Quiz

1. Solve the inequality:

   \[
   |2x-3|\leq7
   \]

   - [x] \([-2,5]\)
   - [ ] \((-\infty,-2]\cup[5,\infty)\)
   - [ ] \([-5,2]\)
   - [ ] \((-2,5)\)

   > Remove the absolute value:
   >
   > \[
   > -7\leq2x-3\leq7
   > \]
   >
   > Add 3:
   >
   > \[
   > -4\leq2x\leq10
   > \]
   >
   > Divide by 2:
   >
   > \[
   > \boxed{-2\leq x\leq5}
   > \]

2. Solve the rational inequality:

   \[
   \frac{x-3}{x+1}\leq0
   \]

   - [ ] \([-1,3]\)
   - [x] \((-1,3]\)
   - [ ] \((-\infty,-1)\cup[3,\infty)\)
   - [ ] \([-1,3)\)

   > The critical points are \(x=-1\) and \(x=3\).
   >
   > Sign analysis shows that the expression is negative between these points.
   >
   > Include \(x=3\) because it makes the numerator zero. Exclude \(x=-1\) because it makes the denominator zero.
   >
   > Therefore:
   >
   > \[
   > \boxed{(-1,3]}
   > \]

3. Find the minimum value using AM-GM:

   \[
   f(x)=x+\frac{9}{x},\qquad x>0
   \]

   - [ ] \(3\)
   - [x] \(6\)
   - [ ] \(9\)
   - [ ] \(12\)

   > By AM-GM:
   >
   > \[
   > x+\frac{9}{x}
   > \geq2\sqrt{x\cdot\frac{9}{x}}
   > \]
   >
   > \[
   > x+\frac{9}{x}\geq6
   > \]
   >
   > Equality occurs when:
   >
   > \[
   > x=\frac{9}{x}\implies x=3
   > \]
   >
   > Therefore, the minimum value is:
   >
   > \[
   > \boxed{6}
   > \]
