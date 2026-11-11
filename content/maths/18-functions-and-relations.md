---
title: Functions and Relations
level: intermediate
---

Functions describe how input values are mapped to output values. Understanding relations, domains, ranges, function classifications, composition, and inverse functions forms the foundation of mathematical analysis and calculus.

## Relations, Functions, Domain, and Range

### Relations and Functions

- **Relation (\(R\)):** Any subset of the Cartesian product \(A \times B\), consisting of ordered pairs \((x,y)\), where \(x \in A\) and \(y \in B\).

  \[
  R \subseteq A \times B
  \]

- **Function (\(f:A \to B\)):** A special type of relation in which every element of the domain \(A\) is associated with exactly one element of the codomain \(B\).

  A function must satisfy two conditions:
  1. Every element of the domain has an assigned output.
  2. No element of the domain has more than one output.

- **Domain (\(\operatorname{Dom}(f)\)):** The set of all permissible input values for which the function is defined.

- **Codomain:** The target set \(B\) containing all possible designated output values.

- **Range (\(\operatorname{Ran}(f)\)):** The set of actual output values produced by the function.

  \[
  \operatorname{Range}(f) \subseteq \operatorname{Codomain}(f)
  \]

### Function Mapping Illustration

Consider a function \(f:A\to B\), where:

\[
A=\{1,2,3\}, \qquad B=\{a,b,c\}
\]

Suppose the mapping is:

\[
f(1)=a,\qquad f(2)=b,\qquad f(3)=b
\]

Then:

- Domain: \(\{1,2,3\}\)
- Codomain: \(\{a,b,c\}\)
- Range: \(\{a,b\}\)

The element \(c\) belongs to the codomain but not the range.

**Important:** Multiple inputs may map to the same output. However, a single input cannot map to multiple outputs in a function.

## Classification of Functions

Functions can be classified according to how their domain and codomain elements are mapped.

### 1. Injective Function (One-to-One)

A function is **injective** if distinct inputs always produce distinct outputs.

Mathematically:

\[
f(x_1)=f(x_2)\implies x_1=x_2
\]

An equivalent condition is:

\[
x_1\neq x_2\implies f(x_1)\neq f(x_2)
\]

**Example:**

\[
f(x)=2x+3
\]

If:

\[
f(x_1)=f(x_2)
\]

then:

\[
2x_1+3=2x_2+3
\]

\[
x_1=x_2
\]

Therefore, the function is injective over \(\mathbb{R}\).

### 2. Surjective Function (Onto)

A function is **surjective** if every element of its codomain is the output of at least one element from its domain.

Mathematically:

\[
\operatorname{Range}(f)=\operatorname{Codomain}(f)
\]

Equivalently, for every \(y\in B\), there exists at least one \(x\in A\) such that:

\[
f(x)=y
\]

**Example:**

\[
f:\mathbb{R}\to\mathbb{R},\qquad f(x)=x^3
\]

For every real number \(y\), we can choose:

\[
x=\sqrt[3]{y}
\]

Since \(f(x)=y\), every real number has a pre-image. Therefore, the function is surjective.

### 3. Bijective Function

A function is **bijective** if it is both injective and surjective.

It satisfies:

- Every output corresponds to exactly one input.
- Every element of the codomain is reached.

A function has an inverse function from its codomain to its domain if and only if it is bijective.

**Example:**

\[
f:\mathbb{R}\to\mathbb{R},\qquad f(x)=2x+1
\]

This function is both injective and surjective. Therefore, it is bijective.

### 4. Even and Odd Functions

**Even Function**

A function is even if:

\[
f(-x)=f(x)
\]

Its graph is symmetric about the \(y\)-axis.

Example:

\[
f(x)=x^2
\]

Because:

\[
f(-x)=(-x)^2=x^2=f(x)
\]

**Odd Function**

A function is odd if:

\[
f(-x)=-f(x)
\]

Its graph is symmetric about the origin.

Example:

\[
f(x)=x^3
\]

Because:

\[
f(-x)=(-x)^3=-x^3=-f(x)
\]

**Important:** The domain must be symmetric about zero for a function to be classified as even or odd.

A function can be neither even nor odd.

## Function Composition and Inverses

### Function Composition

Function composition combines two functions by using the output of one function as the input of another.

Suppose:

\[
g:A\to B
\]

and:

\[
f:B\to C
\]

The composite function \(f\circ g\) is defined as:

\[
f\circ g:A\to C
\]

Its algebraic expression is:

\[
\boxed{(f\circ g)(x)=f(g(x))}
\]

The function \(g\) is applied first, followed by \(f\).

**Example:**

Given:

\[
f(x)=2x+3
\]

\[
g(x)=x^2-1
\]

Find \((f\circ g)(x)\).

Substitute \(g(x)\) into \(f(x)\):

\[
(f\circ g)(x)=2(x^2-1)+3
\]

\[
=2x^2-2+3
\]

\[
\boxed{(f\circ g)(x)=2x^2+1}
\]

**Non-Commutative Property**

Function composition is generally non-commutative:

\[
f\circ g\neq g\circ f
\]

For the previous functions:

\[
(g\circ f)(x)=(2x+3)^2-1
\]

\[
=4x^2+12x+8
\]

This is different from:

\[
(f\circ g)(x)=2x^2+1
\]

**Associative Property**

Function composition is associative whenever the compositions are defined:

\[
f\circ(g\circ h)=(f\circ g)\circ h
\]

### Inverse Function

An **inverse function** reverses the mapping performed by the original function.

If \(f:A\to B\) is bijective, its inverse is:

\[
f^{-1}:B\to A
\]

The inverse satisfies:

\[
f(f^{-1}(y))=y
\]

and:

\[
f^{-1}(f(x))=x
\]

These are called the inverse function identities.

### Steps to Find an Inverse Function

1. Write the original function as \(y=f(x)\).
2. Interchange \(x\) and \(y\).
3. Solve the resulting equation for \(y\).
4. Replace \(y\) with \(f^{-1}(x)\).
5. State the appropriate domain and range restrictions.

**Example:**

Find the inverse of:

\[
f(x)=\frac{3x-1}{x+2}
\]

Let:

\[
y=\frac{3x-1}{x+2}
\]

Interchange \(x\) and \(y\):

\[
x=\frac{3y-1}{y+2}
\]

Cross-multiply:

\[
x(y+2)=3y-1
\]

\[
xy+2x=3y-1
\]

Collect the terms containing \(y\):

\[
xy-3y=-1-2x
\]

\[
y(x-3)=-(1+2x)
\]

Therefore:

\[
y=\frac{2x+1}{3-x}
\]

Hence:

\[
\boxed{f^{-1}(x)=\frac{2x+1}{3-x}}
\]

The original function has domain \(\mathbb{R}\setminus\{-2\}\) and range \(\mathbb{R}\setminus\{3\}\).

Consequently, the inverse has:

- Domain: \(\mathbb{R}\setminus\{3\}\)
- Range: \(\mathbb{R}\setminus\{-2\}\)

## Function Property Master Table

| Function Type | Defining Algebraic Condition | Geometric / Graphical Feature | Inverse Status |
|---|---|---|---|
| Injective | \(f(a)=f(b)\implies a=b\) | Passes the Horizontal Line Test | Has a left inverse |
| Surjective | \(\operatorname{Range}(f)=\operatorname{Codomain}(f)\) | Every codomain value is attained | Has a right inverse |
| Bijective | Both injective and surjective | Passes the Horizontal Line Test and covers the codomain | Has a two-sided inverse |
| Even | \(f(-x)=f(x)\) | Symmetric about the \(y\)-axis | Not necessarily injective |
| Odd | \(f(-x)=-f(x)\) | Symmetric about the origin | Invertibility depends on the mapping |

**Note:** The inverse-status statements for injective and surjective functions assume the usual set-theoretic setting with the appropriate domains and codomains. An injective function has a left inverse, while a surjective function has a right inverse.

## Important Formulas and Domain Rules

### Domain Restrictions for Real-Valued Functions

The domain of a real-valued function must satisfy all algebraic restrictions imposed by its expression.

**1. Denominator Restriction**

For a rational expression:

\[
f(x)=\frac{P(x)}{Q(x)}
\]

the denominator must not be zero:

\[
\boxed{Q(x)\neq 0}
\]

**2. Even-Root Restriction**

For an even root:

\[
f(x)=\sqrt[2n]{g(x)}
\]

the radicand must be non-negative:

\[
\boxed{g(x)\geq 0}
\]

Odd roots, such as cube roots, are defined for all real radicands.

**3. Logarithmic Restriction**

For a logarithmic expression:

\[
f(x)=\log_b(g(x))
\]

the restrictions are:

\[
\boxed{g(x)>0,\qquad b>0,\qquad b\neq 1}
\]

**4. Combined Domain Restrictions**

When a function contains multiple operations, all restrictions must be satisfied simultaneously.

For example:

\[
f(x)=\frac{\sqrt{x-3}}{x-5}
\]

The square root requires:

\[
x-3\geq 0\implies x\geq 3
\]

The denominator requires:

\[
x-5\neq 0\implies x\neq 5
\]

Therefore:

\[
\boxed{\operatorname{Dom}(f)=[3,5)\cup(5,\infty)}
\]

### Composition Domain Rule

For two composable functions \(f\) and \(g\):

\[
\boxed{
\operatorname{Dom}(f\circ g)
=
\{x\in\operatorname{Dom}(g)\mid g(x)\in\operatorname{Dom}(f)\}
}
\]

This means that an input must first belong to the domain of \(g\), and its output must then belong to the domain of \(f\).

### Inverse Function Properties

For a bijective function \(f\):

\[
f^{-1}(f(x))=x
\]

\[
f(f^{-1}(x))=x
\]

The domain and range are interchanged:

\[
\operatorname{Dom}(f^{-1})=\operatorname{Range}(f)
\]

\[
\operatorname{Range}(f^{-1})=\operatorname{Dom}(f)
\]

## Common Exam Traps

- **Confusing relations with functions:** A relation may assign multiple outputs to one input. A function must assign exactly one output to every element of its domain.

- **Confusing domain, codomain, and range:** The domain contains inputs, the codomain is the designated target set, and the range contains actual outputs.

- **Vertical vs. Horizontal Line Test:** The Vertical Line Test determines whether a graph represents a function. The Horizontal Line Test determines whether a function is injective.

- **Assuming every function is bijective:** A function must be both injective and surjective to be bijective.

- **Assuming composition is commutative:** In general, \(f\circ g\neq g\circ f\). Always follow the order of operations in the composite function.

- **Incorrectly finding an inverse:** Remember to interchange \(x\) and \(y\) before solving for the new \(y\).

- **Ignoring domain restrictions on inverses:** The domain of an inverse function is the range of the original function. Excluded values must remain excluded.

- **Misclassifying even and odd functions:** Check the defining equations and ensure that the domain is symmetric about zero.

- **Ignoring domain restrictions during composition:** The output of the inner function must belong to the domain of the outer function.

## Quiz

1. Find the domain of the real-valued function:

   \[
   f(x)=\frac{\sqrt{x-3}}{x-5}
   \]

   - [ ] \([3,\infty)\)
   - [x] \([3,5)\cup(5,\infty)\)
   - [ ] \((5,\infty)\)
   - [ ] \((-\infty,3]\cup(5,\infty)\)

   > The square root requires:
   >
   > \[
   > x-3\geq 0\implies x\geq 3
   > \]
   >
   > The denominator requires:
   >
   > \[
   > x-5\neq 0\implies x\neq 5
   > \]
   >
   > Combining both restrictions gives:
   >
   > \[
   > \boxed{[3,5)\cup(5,\infty)}
   > \]

2. Given:

   \[
   f(x)=2x+3,\qquad g(x)=x^2-1
   \]

   evaluate the composite value \((f\circ g)(4)\).

   - [x] \(33\)
   - [ ] \(31\)
   - [ ] \(120\)
   - [ ] \(35\)

   > First, evaluate the inner function:
   >
   > \[
   > g(4)=4^2-1=16-1=15
   > \]
   >
   > Then substitute this result into \(f\):
   >
   > \[
   > f(g(4))=f(15)
   > \]
   >
   > \[
   > =2(15)+3=33
   > \]
   >
   > Therefore:
   >
   > \[
   > \boxed{(f\circ g)(4)=33}
   > \]

3. What is the algebraic inverse function \(f^{-1}(x)\) for the bijective function:

   \[
   f(x)=\frac{3x-1}{x+2}
   \]

   - [ ] \(f^{-1}(x)=\frac{x+2}{3x-1}\)
   - [x] \(f^{-1}(x)=\frac{2x+1}{3-x}\)
   - [ ] \(f^{-1}(x)=\frac{2x-1}{3+x}\)
   - [ ] \(f^{-1}(x)=\frac{3x+1}{x-2}\)

   > Let:
   >
   > \[
   > y=\frac{3x-1}{x+2}
   > \]
   >
   > Cross-multiply:
   >
   > \[
   > y(x+2)=3x-1
   > \]
   >
   > Expand:
   >
   > \[
   > yx+2y=3x-1
   > \]
   >
   > Collect the terms containing \(x\):
   >
   > \[
   > 2y+1=x(3-y)
   > \]
   >
   > Therefore:
   >
   > \[
   > x=\frac{2y+1}{3-y}
   > \]
   >
   > Interchange the variables:
   >
   > \[
   > \boxed{f^{-1}(x)=\frac{2x+1}{3-x}}
   > \]
