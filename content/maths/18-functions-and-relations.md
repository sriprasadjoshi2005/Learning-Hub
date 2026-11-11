---
title: Functions and Relations
level: intermediate
---

Functions describe how input values are connected to output values. This lesson covers relations, types of functions, domain, range, composition, and inverse functions.

## Relations and Functions

- **Relation:** A connection between elements of two sets.
- **Function:** A relation where every input has exactly one output.
- **Domain:** All possible input values.
- **Codomain:** The set of possible output values.
- **Range:** The actual output values.

The range is always a subset of the codomain.

### Example

Let:

A = {1, 2, 3}

B = {a, b, c}

Suppose:

f(1) = a

f(2) = b

f(3) = b

Then:

- Domain = {1, 2, 3}
- Codomain = {a, b, c}
- Range = {a, b}

The element c is in the codomain but not in the range.

**Important:** Different inputs can have the same output, but one input cannot have two different outputs.

## Types of Functions

### 1. Injective Function

An injective function is also called a one-to-one function.

Different inputs produce different outputs.

Condition:

If f(x1) = f(x2), then x1 = x2.

**Example:**

f(x) = 2x + 3

If:

2x1 + 3 = 2x2 + 3

Then:

x1 = x2

Therefore, the function is injective over the real numbers.

### 2. Surjective Function

A surjective function is also called an onto function.

Every element of the codomain must be reached.

Condition:

Range = Codomain

**Example:**

f(x) = x³

For every real number y, we can choose x as the cube root of y.

Therefore, the function is surjective when its domain and codomain are both real numbers.

### 3. Bijective Function

A bijective function is both injective and surjective.

It satisfies two conditions:

- Every output comes from exactly one input.
- Every element of the codomain is reached.

A function has an inverse if and only if it is bijective.

**Example:**

f(x) = 2x + 1

When the domain and codomain are real numbers, this function is bijective.

### 4. Even and Odd Functions

**Even Function**

A function is even if:

f(-x) = f(x)

Its graph is symmetric about the y-axis.

Example:

f(x) = x²

**Odd Function**

A function is odd if:

f(-x) = -f(x)

Its graph is symmetric about the origin.

Example:

f(x) = x³

**Important:** The domain must be symmetric about zero. A function can also be neither even nor odd.

## Function Composition

Function composition means applying one function after another.

Formula:

(f o g)(x) = f(g(x))

The function g is applied first, followed by f.

### Example

Given:

f(x) = 2x + 3

g(x) = x² - 1

Find (f o g)(x).

Substitute g(x) into f(x):

(f o g)(x) = 2(x² - 1) + 3

Answer:

2x² + 1

### Properties of Composition

**Non-Commutative Property**

The order of functions usually matters.

(f o g)(x) is not necessarily equal to (g o f)(x).

For the previous example:

(g o f)(x) = (2x + 3)² - 1

= 4x² + 12x + 8

Therefore:

f o g is not equal to g o f.

**Associative Property**

Function composition is associative:

f o (g o h) = (f o g) o h

This holds whenever the compositions are defined.

## Inverse Functions

An inverse function reverses the operation of the original function.

It is written as f⁻¹.

A function has an inverse if it is bijective.

The inverse identities are:

f(f⁻¹(x)) = x

f⁻¹(f(x)) = x

### Steps to Find an Inverse

1. Write y = f(x).
2. Interchange x and y.
3. Solve for y.
4. Replace y with f⁻¹(x).
5. State the domain and range.

### Example

Find the inverse of:

f(x) = (3x - 1) / (x + 2)

Start with:

y = (3x - 1) / (x + 2)

Interchange x and y:

x = (3y - 1) / (y + 2)

Cross-multiply:

xy + 2x = 3y - 1

Collect y terms:

xy - 3y = -1 - 2x

y(x - 3) = -1 - 2x

Therefore:

f⁻¹(x) = (2x + 1) / (3 - x)

**Domain and Range:**

Original function:
- Domain: All real numbers except -2.
- Range: All real numbers except 3.

Inverse function:
- Domain: All real numbers except 3.
- Range: All real numbers except -2.

## Function Properties Summary

| Type | Condition | Graph Feature |
|---|---|---|
| Injective | Different inputs have different outputs | Passes the Horizontal Line Test |
| Surjective | Range equals codomain | Every codomain value is reached |
| Bijective | Both injective and surjective | Has an inverse |
| Even | f(-x) = f(x) | Symmetric about y-axis |
| Odd | f(-x) = -f(x) | Symmetric about origin |

**Inverse Properties:**

- Injective functions have a left inverse.
- Surjective functions have a right inverse.
- Bijective functions have a two-sided inverse.

## Domain Rules

The domain contains all values for which a function is defined.

### 1. Fractions

The denominator cannot be zero.

Example:

f(x) = 1 / (x - 2)

Here, x cannot equal 2.

### 2. Square Roots

The expression inside an even root must be zero or positive.

Example:

f(x) = square root of (x - 3)

Here:

x >= 3

Cube roots can accept any real number.

### 3. Logarithms

For log base b of x:

- x must be greater than zero.
- b must be greater than zero.
- b cannot equal 1.

### 4. Combined Restrictions

Example:

f(x) = square root of (x - 3) / (x - 5)

The square root requires x >= 3.

The denominator cannot equal zero, so x cannot equal 5.

Therefore:

Domain = [3, 5) union (5, infinity).

## Composition and Inverse Domain Rules

### Composition Domain

For (f o g)(x), both conditions must be satisfied:

- x must belong to the domain of g.
- g(x) must belong to the domain of f.

### Inverse Domain and Range

For a bijective function:

- Domain of f⁻¹ = Range of f.
- Range of f⁻¹ = Domain of f.

Also:

f⁻¹(f(x)) = x

f(f⁻¹(x)) = x

## Common Exam Traps

- **Function definition:** One input cannot have multiple outputs.
- **Range and codomain:** The range contains only actual outputs.
- **Injective and surjective:** These are different properties.
- **Bijective functions:** A function must be both injective and surjective to have an inverse.
- **Line tests:** The Vertical Line Test checks functions. The Horizontal Line Test checks injectivity.
- **Composition order:** Apply the inner function first.
- **Inverse functions:** Interchange x and y before solving.
- **Even and odd functions:** Check the defining equations and domain.
- **Domain restrictions:** Never allow a zero denominator or a negative value inside an even root.
- **Composition domain:** The output of the inner function must be valid for the outer function.

## Quiz

1. Find the domain of:

f(x) = square root of (x - 3) / (x - 5)

- [ ] [3, infinity)
- [x] [3, 5) union (5, infinity)
- [ ] (5, infinity)
- [ ] (-infinity, 3] union (5, infinity)

> The square root requires x >= 3.
>
> The denominator cannot equal zero, so x cannot equal 5.
>
> Therefore, the domain is [3, 5) union (5, infinity).

2. Given:

f(x) = 2x + 3

g(x) = x² - 1

Find (f o g)(4).

- [x] 33
- [ ] 31
- [ ] 120
- [ ] 35

> First, calculate g(4):
>
> g(4) = 4² - 1 = 15.
>
> Now calculate f(15):
>
> f(15) = 2(15) + 3 = 33.
>
> Answer: 33.

3. Find the inverse of:

f(x) = (3x - 1) / (x + 2)

- [ ] (x + 2) / (3x - 1)
- [x] (2x + 1) / (3 - x)
- [ ] (2x - 1) / (3 + x)
- [ ] (3x + 1) / (x - 2)

> Start with:
>
> y = (3x - 1) / (x + 2)
>
> Interchange x and y:
>
> x = (3y - 1) / (y + 2)
>
> Cross-multiply and collect the y terms:
>
> xy + 2x = 3y - 1
>
> y(x - 3) = -1 - 2x
>
> Therefore:
>
> f⁻¹(x) = (2x + 1) / (3 - x).
