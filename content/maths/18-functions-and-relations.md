---
title: Functions and Relations
level: intermediate
---

Functions describe how input values map to output values. Defining relations, domains, ranges, function classifications (injective, surjective, bijective), and composition forms the bedrock of modern analysis and calculus.

## Relations, Functions, Domain, and Range

- **Relation ($R$):** Any subset of the Cartesian product $A \times B$, containing ordered pairs $(x, y)$ where $x \in A$ and $y \in B$.
- **Function ($f: A \to B$):** A special relation where **every** element $x$ in domain $A$ is mapped to **exactly one** element $y$ in codomain $B$.
- **Domain ($\text{Dom}(f)$):** The set of all valid input values $x \in A$ for which $f(x)$ is real and defined.
- **Codomain:** The target set $B$ into which all outputs are mapped.
- **Range ($\text{Ran}(f)$):** The subset of codomain $B$ containing all actual output values $y = f(x)$.

```text
                        Function Mapping Logic
   Domain Set A                                      Codomain Set B
   ┌──────────┐                                      ┌──────────┐
   │    x₁ ───┼─────────────────────────────────────►│   y₁     │ (Range)
   │    x₂ ───┼─────────────────────────────────────►│   y₂     │ (Range)
   │    x₃ ───┼─────────────────────────────────────►│   y₃     │ (Unused)
   └──────────┘                                      └──────────┘
```

## Classification of Functions

1. **Injective Function (One-to-One):** Distinct inputs produce distinct outputs.
$$f(x_1) = f(x_2) \implies x_1 = x_2$$

2. **Surjective Function (Onto):** Every element in codomain $B$ has at least one pre-image in domain $A$.
$$\text{Range}(f) = \text{Codomain}(B)$$

3. **Bijective Function (One-to-One and Onto):** Both injective and surjective. A function has a well-defined **inverse function** $f^{-1}(x)$ **if and only if it is bijective**.

4. **Even and Odd Functions:**
  - *Even Function:* $f(-x) = f(x)$ (Symmetric about the $y$-axis).
  - *Odd Function:* $f(-x) = -f(x)$ (Symmetric about the origin $(0, 0)$).

## Function Composition and Inverses

### Function Composition

Given $f: B \to C$ and $g: A \to B$, the composite function $(f \circ g): A \to C$ is defined as:

$$(f \circ g)(x) = f(g(x))$$

Note: Function composition is generally **non-commutative**: $(f \circ g)(x) \neq (g \circ f)(x)$.

### Inverse Function

If $f: A \to B$ is bijective, its inverse $f^{-1}: B \to A$ satisfies:

$$f(f^{-1}(y)) = y \quad \text{and} \quad f^{-1}(f(x)) = x$$

## Function Property Master Table

| Function Type | Defining Algebraic Condition | Geometric / Graphical Feature | Inverse Status |
|---|---|---|---|
| Injective (1-to-1) | $f(a) = f(b) \implies a = b$ | Passes Horizontal Line Test | Right-inverse exists |
| Surjective (Onto) | $\text{Range} = \text{Codomain}$ | Covers entire vertical codomain span | Left-inverse exists |
| Bijective | Both 1-to-1 and Onto | Passes Horizontal Line Test & Covers Codomain | Fully Invertible $f^{-1}(x)$ |
| Even | $f(-x) = f(x)$ | Symmetric with respect to $y$-axis | Non-injective |
| Odd | $f(-x) = -f(x)$ | Symmetric with respect to origin $(0,0)$ | Invertibility depends on mapping |

## Important Formulas and Domain Rules

Domain Restrictions for Real Functions $f(x)$:

$$\text{Denominator Restriction}: \frac{P(x)}{Q(x)} \implies Q(x) \neq 0$$

$$\text{Even Radical Restriction}: \sqrt[2n]{g(x)} \implies g(x) \ge 0$$

$$\text{Logarithmic Restriction}: \log_b(g(x)) \implies g(x) > 0 \quad \text{and} \quad b > 0, b \neq 1$$

Composition Domain Rule:

$$\text{Dom}(f \circ g) = \{x \in \text{Dom}(g) \mid g(x) \in \text{Dom}(f)\}$$

## Common Exam Traps

- **Vertical vs. Horizontal Line Test:** Confusing tests. The **Vertical Line Test** checks if a relation is a valid function. The **Horizontal Line Test** checks if a function is injective (one-to-one).
- **Assuming Composition Commutativity:** Writing $(f \circ g)(x) = (g \circ f)(x)$. Composite operations depend strictly on order.
- **Forgetting Domain Restrictions on Inverses:** Finding $f^{-1}(x)$ algebraically without restricting its domain to match the range of $f(x)$.

## Quiz

1. Find the domain of the real-valued function $f(x) = \frac{\sqrt{x - 3}}{x - 5}$.
  - [ ] $[3, \infty)$
  - [x] $[3, 5) \cup (5, \infty)$
  - [ ] $(5, \infty)$
  - [ ] $(-\infty, 3] \cup (5, \infty)$
   > Radicand requires $x - 3 \ge 0 \implies x \ge 3$. Denominator requires $x - 5 \neq 0 \implies x \neq 5$. Combining both restrictions gives domain $[3, 5) \cup (5, \infty)$.

2. Given $f(x) = 2x + 3$ and $g(x) = x^2 - 1$, evaluate the composite value $(f \circ g)(4)$.
  - [ ] $33$
  - [x] $33$
  - [ ] $120$
  - [ ] $35$
   > First evaluate $g(4) = 4^2 - 1 = 16 - 1 = 15$. Then evaluate $f(g(4)) = f(15) = 2(15) + 3 = 30 + 3 = 33$.

3. What is the algebraic inverse function $f^{-1}(x)$ for the bijective function $f(x) = \frac{3x - 1}{x + 2}$?
  - [ ] $f^{-1}(x) = \frac{x + 2}{3x - 1}$
  - [x] $f^{-1}(x) = \frac{2x + 1}{3 - x}$
  - [ ] $f^{-1}(x) = \frac{2x - 1}{3 + x}$
  - [ ] $f^{-1}(x) = \frac{3x + 1}{x - 2}$
   > Set $y = \frac{3x - 1}{x + 2} \implies y(x + 2) = 3x - 1 \implies yx + 2y = 3x - 1 \implies 2y + 1 = 3x - yx = x(3 - y) \implies x = \frac{2y + 1}{3 - y}$. Swap variables: $f^{-1}(x) = \frac{2x + 1}{3 - x}$.