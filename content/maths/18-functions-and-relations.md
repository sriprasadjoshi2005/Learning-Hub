---
title: Functions and Relations
level: intermediate
---

Functions describe how input values are mapped to output values. Understanding relations, domains, ranges, function classifications, composition, and inverse functions forms the foundation of mathematical analysis and calculus.

## Relations, Functions, Domain, and Range

### Relations and Functions

- **Relation:** Any subset of the Cartesian product A x B, consisting of ordered pairs (x, y).
- **Function:** A special relation in which every element of the domain has exactly one output.
- **Domain:** The set of all permissible input values.
- **Codomain:** The target set containing all designated output values.
- **Range:** The set of actual output values produced by the function.

The range is always a subset of the codomain.

### Function Mapping Example

Consider a function f from A to B, where:

A = {1, 2, 3}

B = {a, b, c}

Suppose:

f(1) = a

f(2) = b

f(3) = b

Then:

- Domain: {1, 2, 3}
- Codomain: {a, b, c}
- Range: {a, b}

The element c belongs to the codomain but not the range.

**Important:** Multiple inputs may map to the same output, but one input cannot map to multiple outputs in a function.

## Classification of Functions

### 1. Injective Function (One-to-One)

A function is injective if different inputs always produce different outputs.

Mathematically:

f(x1) = f(x2) implies x1 = x2.

**Example:**

f(x) = 2x + 3

If f(x1) = f(x2), then:

2x1 + 3 = 2x2 + 3

Therefore:

x1 = x2

Hence, the function is injective over the real numbers.

### 2. Surjective Function (Onto)

A function is surjective if every element of its codomain is reached by at least one input.

Mathematically:

Range(f) = Codomain(f)

**Example:**

f(x) = x³, where the domain and codomain are real numbers.

For every real number y, choose:

x = cube root of y.

Then f(x) = y.

Therefore, the function is surjective.

### 3. Bijective Function

A function is bijective if it is both injective and surjective.

It satisfies two conditions:

- Every output corresponds to exactly one input.
- Every element of the codomain is reached.

A function has an inverse function if and only if it is bijective.

**Example:**

f(x) = 2x + 1, where the domain and codomain are real numbers.

This function is both injective and surjective. Therefore, it is bijective.

### 4. Even and Odd Functions

**Even Function**

A function is even if:

f(-x) = f(x)

Its graph is symmetric about the y-axis.

Example:

f(x) = x²

Because:

f(-x) = (-x)² = x² = f(x)

**Odd Function**

A function is odd if:

f(-x) = -f(x)

Its graph is symmetric about the origin.

Example:

f(x) = x³

Because:

f(-x) = (-x)³ = -x³ = -f(x)

**Important:** The domain must be symmetric about zero for a function to be classified as even or odd. A function can be neither even nor odd.

## Function Composition and Inverses

### Function Composition

Function composition combines two functions by using the output of one function as the input of another.

If g maps A to B and f maps B to C, then the composite function maps A to C.

The formula is:

(f o g)(x) = f(g(x))

The function g is applied first, followed by f.

**Example:**

Given:

f(x) = 2x + 3

g(x) = x² - 1

Find (f o g)(x).

Substitute g(x) into f(x):

(f o g)(x) = 2(x² - 1) + 3

= 2x² + 1

### Properties of Function Composition

**Non-Commutative Property**

Function composition is generally non-commutative:

f o g is not necessarily equal to g o f.

For the previous functions:

(g o f)(x) = (2x + 3)² - 1

= 4x² + 12x + 8

This is different from:

(f o g)(x) = 2x² + 1

**Associative Property**

Function composition is associative whenever the compositions are defined:

f o (g o h) = (f o g) o h

### Inverse Function

An inverse function reverses the mapping performed by the original function.

If f is bijective, its inverse is written as f⁻¹.

The inverse satisfies:

f(f⁻¹(x)) = x

f⁻¹(f(x)) = x

These are called inverse function identities.

### Steps to Find an Inverse Function

1. Write the original function as y = f(x).
2. Interchange x and y.
3. Solve the equation for y.
4. Replace y with f⁻¹(x).
5. State the appropriate domain and range restrictions.

**Example:**

Find the inverse of:

f(x) = (3x - 1) / (x + 2)

Let:

y = (3x - 1) / (x + 2)

Interchange x and y:

x = (3y - 1) / (y + 2)

Cross-multiply:

x(y + 2) = 3y - 1

xy + 2x = 3y - 1

Collect the terms containing y:

xy - 3y = -1 - 2x

y(x - 3) = -(1 + 2x)

Therefore:

y = (2x + 1) / (3 - x)

Hence:

f⁻¹(x) = (2x + 1) / (3 - x)

The original function has:

- Domain: All real numbers except -2.
- Range: All real numbers except 3.

The inverse has:

- Domain: All real numbers except 3.
- Range: All real numbers except -2.

## Function Property Master Table

| Function Type | Defining Condition | Graphical Feature | Inverse Status |
|---|---|---|---|
| Injective | f(a) = f(b) implies a = b | Passes the Horizontal Line Test | Has a left inverse |
| Surjective | Range equals codomain | Every codomain value is reached | Has a right inverse |
| Bijective | Both injective and surjective | Passes the Horizontal Line Test and covers the codomain | Has a two-sided inverse |
| Even | f(-x) = f(x) | Symmetric about the y-axis | Not necessarily injective |
| Odd | f(-x) = -f(x) | Symmetric about the origin | Invertibility depends on the mapping |

**Note:** An injective function has a left inverse, while a surjective function has a right inverse, under the usual set-theoretic conditions.

## Important Formulas and Domain Rules

### Domain Restrictions

The domain of a real-valued function must satisfy all restrictions imposed by its expression.

**1. Denominator Restriction**

For a rational function:

f(x) = P(x) / Q(x)

The denominator must not be zero:

Q(x) is not equal to zero.

**2. Even-Root Restriction**

For an even root:

f(x) = square root of g(x)

The expression inside the root must be non-negative:

g(x) >= 0

Odd roots, such as cube roots, are defined for all real numbers.

**3. Logarithmic Restriction**

For a logarithmic function:

f(x) = log base b of g(x)

The restrictions are:

- g(x) > 0
- b > 0
- b is not equal to 1

**4. Combined Domain Restrictions**

When a function contains multiple operations, all restrictions must be satisfied simultaneously.

Example:

f(x) = square root of (x - 3) / (x - 5)

The square root requires x >= 3.

The denominator requires x is not equal to 5.

Therefore:

Domain = [3, 5) union (5, infinity).

### Composition Domain Rule

For two composable functions f and g:

The domain of (f o g) contains all values of x that satisfy both conditions:

- x belongs to the domain of g.
- g(x) belongs to the domain of f.

### Inverse Function Properties

For a bijective function f:

f⁻¹(f(x)) = x

f(f⁻¹(x)) = x

The domain and range are interchanged:

- Domain of f⁻¹ = Range of f.
- Range of f⁻¹ = Domain of f.

## Common Exam Traps

- **Confusing relations with functions:** A relation may assign multiple outputs to one input. A function must assign exactly one output to every element of its domain.
- **Confusing domain, codomain, and range:** The domain contains inputs, the codomain is the target set, and the range contains actual outputs.
- **Vertical and Horizontal Line Tests:** The Vertical Line Test determines whether a graph represents a function. The Horizontal Line Test determines whether a function is injective.
- **Assuming every function is bijective:** A function must be both injective and surjective to be bijective.
- **Assuming composition is commutative:** In general, f o g is not equal to g o f.
- **Incorrectly finding an inverse:** Interchange x and y before solving for the new y.
- **Ignoring inverse domain restrictions:** The domain of an inverse is the range of the original function.
- **Misclassifying even and odd functions:** Check the defining equations and ensure that the domain is symmetric about zero.
- **Ignoring composition restrictions:** The output of the inner function must belong to the domain of the outer function.

## Quiz

1. Find the domain of the function:

f(x) = square root of (x - 3) / (x - 5)

- [ ] [3, infinity)
- [x] [3, 5) union (5, infinity)
- [ ] (5, infinity)
- [ ] (-infinity, 3] union (5, infinity)

> The square root requires x - 3 >= 0, so x >= 3.
>
> The denominator requires x - 5 is not equal to zero, so x cannot equal 5.
>
> Combining both restrictions gives:
>
> [3, 5) union (5, infinity).

2. Given:

f(x) = 2x + 3

g(x) = x² - 1

Evaluate (f o g)(4).

- [x] 33
- [ ] 31
- [ ] 120
- [ ] 35

> First, evaluate the inner function:
>
> g(4) = 4² - 1 = 15.
>
> Then substitute the result into f:
>
> f(15) = 2(15) + 3 = 33.
>
> Therefore, (f o g)(4) = 33.

3. Find the inverse function of:

f(x) = (3x - 1) / (x + 2)

- [ ] (x + 2) / (3x - 1)
- [x] (2x + 1) / (3 - x)
- [ ] (2x - 1) / (3 + x)
- [ ] (3x + 1) / (x - 2)

> Let y = (3x - 1) / (x + 2).
>
> Interchange x and y:
>
> x = (3y - 1) / (y + 2).
>
> Cross-multiply:
>
> xy + 2x = 3y - 1.
>
> Collect the terms containing y:
>
> xy - 3y = -1 - 2x.
>
> y(x - 3) = -(1 + 2x).
>
> Therefore:
>
> y = (2x + 1) / (3 - x).
>
> Hence, the inverse function is (2x + 1) / (3 - x).
