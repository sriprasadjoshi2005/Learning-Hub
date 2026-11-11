---
title: Advanced Inequalities and Absolute Value
level: intermediate
---

This lesson covers absolute value inequalities, rational inequalities, sign analysis, the Wavy Curve Method, AM-GM inequality, and triangle inequalities.

## Absolute Value

Absolute value represents the non-negative distance of a number from zero.

For any real number x:

- If x is positive or zero, |x| = x.
- If x is negative, |x| = -x.

Examples: |5| = 5 and |-5| = 5.

### Absolute Value Properties

For a positive number a:

| Expression | Equivalent form |
|---|---|
| |x| = a | x = a or x = -a |
| |x| < a | -a < x < a |
| |x| <= a | -a <= x <= a |
| |x| > a | x < -a or x > a |
| |x| >= a | x <= -a or x >= a |

For two expressions:

|f(x)| = |g(x)|

Therefore:

f(x) = g(x) or f(x) = -g(x).

### Shifted Absolute Values

For r >= 0:

- |x - c| <= r means c - r <= x <= c + r.
- |x - c| >= r means x <= c - r or x >= c + r.

## Rational Inequalities

A rational inequality contains a fraction involving polynomial expressions.

Examples:

(x - 2) / (x + 3) > 0

(x² - 4) / (x - 1) <= 0

The denominator must never equal zero.

### Wavy Curve Method

The Wavy Curve Method helps determine where a polynomial or rational expression is positive or negative.

**Steps:**

1. Move all terms to one side.
2. Factorize the expression.
3. Find the zeros of the numerator and denominator.
4. Arrange the critical points in increasing order.
5. Divide the number line into intervals.
6. Determine the sign in each interval.
7. Select the intervals that satisfy the inequality.

**Important Rules:**

- Numerator roots may be included when equality is allowed.
- Denominator roots are always excluded.
- Odd-multiplicity roots change the sign.
- Even-multiplicity roots do not change the sign.

### Worked Example

Solve:

(x - 3) / (x + 1) <= 0

**Step 1: Find critical points.**

Numerator root: x = 3.

Denominator root: x = -1.

**Step 2: Divide the number line.**

Intervals:

- (-infinity, -1)
- (-1, 3)
- (3, infinity)

**Step 3: Analyze signs.**

| Interval | Sign |
|---|---|
| (-infinity, -1) | Positive |
| (-1, 3) | Negative |
| (3, infinity) | Positive |

**Step 4: Write the solution.**

The expression must be negative or zero.

Include x = 3 because the numerator is zero.

Exclude x = -1 because the denominator is zero.

**Answer:** (-1, 3]

## Important Inequality Formulas

### Absolute Value

| Inequality | Solution |
|---|---|
| |x - c| < r | c - r < x < c + r |
| |x - c| <= r | c - r <= x <= c + r |
| |x - c| > r | x < c - r or x > c + r |
| |x - c| >= r | x <= c - r or x >= c + r |

### Quadratic Expressions

For a < b:

- (x - a)(x - b) < 0 gives a < x < b.
- (x - a)(x - b) > 0 gives x < a or x > b.

### Rational Expressions

For a < b:

(x - a) / (x - b) <= 0

Solution: [a, b).

The numerator root is included, but the denominator root is excluded.

## AM-GM Inequality

The Arithmetic Mean-Geometric Mean inequality states that the arithmetic mean of two non-negative numbers is greater than or equal to their geometric mean.

For a >= 0 and b >= 0:

(a + b) / 2 >= sqrt(ab)

Equivalently:

a + b >= 2sqrt(ab)

Equality occurs when a = b.

### Application: Finding a Minimum

Find the minimum value of:

f(x) = x + 9/x, where x > 0.

Applying AM-GM:

x + 9/x >= 2sqrt(x * 9/x)

Therefore:

x + 9/x >= 6

Equality occurs when:

x = 9/x

x² = 9

Since x is positive, x = 3.

**Minimum value = 6.**

## Triangle Inequality

For real numbers a and b:

- |a + b| <= |a| + |b|
- |a - b| <= |a| + |b|

The reverse triangle inequality is:

||a| - |b|| <= |a + b|

Also:

|x|² = x²

## Common Exam Traps

- **Denominator roots:** Never include values that make the denominator zero.
- **Absolute value splitting:** |x| > 5 means x < -5 or x > 5.
- **Negative multiplication:** Reverse the inequality sign when multiplying or dividing by a negative number.
- **Boundary points:** Strict inequalities exclude endpoints. Inclusive inequalities include valid endpoints.
- **AM-GM conditions:** Both quantities must be non-negative.
- **Repeated roots:** Even-multiplicity roots do not change the sign.

## Quiz

1. Solve |2x - 3| <= 7.

- [x] [-2, 5]
- [ ] (-infinity, -2] or [5, infinity)
- [ ] [-5, 2]
- [ ] (-2, 5)

> -7 <= 2x - 3 <= 7.
>
> Adding 3 gives -4 <= 2x <= 10.
>
> Dividing by 2 gives -2 <= x <= 5.
>
> Answer: [-2, 5].

2. Solve (x - 3) / (x + 1) <= 0.

- [ ] [-1, 3]
- [x] (-1, 3]
- [ ] (-infinity, -1) or [3, infinity)
- [ ] [-1, 3)

> The critical points are -1 and 3. The expression is negative between these points. Include 3 because the numerator becomes zero. Exclude -1 because the denominator becomes zero.
>
> Answer: (-1, 3].

3. Find the minimum value of f(x) = x + 9/x, where x > 0.

- [ ] 3
- [x] 6
- [ ] 9
- [ ] 12

> Applying AM-GM:
>
> x + 9/x >= 2sqrt(x * 9/x) = 6.
>
> Equality occurs when x = 3.
>
> Minimum value = 6.
