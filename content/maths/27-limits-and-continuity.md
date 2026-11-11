---
title: Limits and Continuity
level: advanced
---

Limits examine the behavior of a function as its input approaches a specific value. Establishing limits, evaluating indeterminate forms, and defining continuity forms the foundation for calculus.

## Definition of a Limit and One-Sided Limits

The **limit of a function** $f(x)$ as $x$ approaches $c$ is $L$, written as:

$$\lim_{x \to c} f(x) = L$$

if $f(x)$ gets arbitrarily close to $L$ as $x$ gets sufficiently close to $c$ from both sides ($x \neq c$).

- **Left-Hand Limit (LHL):** $\lim_{x \to c^-} f(x) = L_1$ (Approaching $c$ from values $x < c$).
- **Right-Hand Limit (RHL):** $\lim_{x \to c^+} f(x) = L_2$ (Approaching $c$ from values $x > c$).
- **Existence of Limit Theorem:**
$$\lim_{x \to c} f(x) = L \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L$$

## Indeterminate Forms and L'Hôpital's Rule

When direct substitution yields an indeterminate form like $\left[\frac{0}{0}\right]$ or $\left[\frac{\infty}{\infty}\right]$, algebraic techniques or L'Hôpital's Rule must be used.

### Algebraic Limit Evaluation Techniques

1. **Factoring and Canceling:** Factor out common zero-producing terms $(x - c)$.
2. **Rationalization:** Multiply numerator and denominator by conjugate radicals.
3. **Standard Trigonometric Limits:**
$$\lim_{x \to 0} \frac{\sin x}{x} = 1 \qquad \text{and} \qquad \lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

### L'Hôpital's Rule

If $\lim_{x \to c} f(x) = 0$ and $\lim_{x \to c} g(x) = 0$ (or both $\pm \infty$), then:

$$\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$$

provided the limit of derivatives exists.

## Formal Definition of Continuity

A function $f(x)$ is **continuous at a point $x = c$** if and only if all three conditions are satisfied:

1. $f(c)$ is defined ($c$ is in the domain of $f$).
2. $\lim_{x \to c} f(x)$ exists.
3. $\lim_{x \to c} f(x) = f(c)$.

### Types of Discontinuities

- **Removable Discontinuity:** Limit exists, but $\lim_{x \to c} f(x) \neq f(c)$ (or $f(c)$ is undefined).
- **Jump Discontinuity:** LHL and RHL both exist as finite numbers, but $\lim_{x \to c^-} f(x) \neq \lim_{x \to c^+} f(x)$.
- **Essential / Infinite Discontinuity:** At least one of the one-sided limits is $\pm \infty$ or does not exist.

## Limits & Continuity Master Table

| Standard Limit Form | Exact Limit Value | Operational Condition |
|---|---|---|
| $\lim_{x \to 0} \frac{\sin(ax)}{x}$ | $a$ | Angle $ax$ in radians |
| $\lim_{x \to 0} \frac{e^x - 1}{x}$ | $1$ | Natural exponential base |
| $\lim_{x \to 0} \frac{\ln(1 + x)}{x}$ | $1$ | Natural logarithm base |
| $\lim_{x \to \infty} \left(1 + \frac{a}{x}\right)^x$ | $e^a$ | Compound interest limit form |
| $\lim_{x \to a} \frac{x^n - a^n}{x - a}$ | $n a^{n-1}$ | Algebraic power limit rule |

## Important Formulas and Theorems

The Squeeze (Sandwich) Theorem:

$$\text{If } g(x) \le f(x) \le h(x) \text{ near } c, \text{ and } \lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L \implies \lim_{x \to c} f(x) = L$$

Intermediate Value Theorem (IVT):

$$\text{If } f \text{ is continuous on } [a, b] \text{ and } k \text{ is between } f(a) \text{ and } f(b) \implies \exists c \in (a, b) \text{ s.t. } f(c) = k$$

## Common Exam Traps

- **Applying L'Hôpital's Rule to Non-Indeterminate Forms:** Differentiating numerator and denominator when direct substitution yields a valid number (e.g., $\frac{2}{3}$). L'Hôpital's rule **only** applies to $\frac{0}{0}$ or $\frac{\infty}{\infty}$.
- **Applying Quotient Rule during L'Hôpital's Rule:** Differentiating $\frac{f(x)}{g(x)}$ using $\frac{f'g - fg'}{g^2}$ instead of simply differentiating numerator and denominator separately: $\frac{f'(x)}{g'(x)}$.
- **Confusing Limit Existence with Continuity:** Assuming that if $\lim_{x \to c} f(x) = 5$, then $f(c)$ must equal $5$. The function could be undefined or redefined at $x = c$ (removable discontinuity).

## Quiz

1. Evaluate the limit: $\lim_{x \to 2} \frac{x^2 - 4}{x^2 + x - 6}$.
  - [ ] $0$
  - [x] $\frac{4}{5}$
  - [ ] $1$
  - [ ] Undefined
   > Direct substitution yields $\frac{0}{0}$. Factor numerator and denominator: $\lim_{x \to 2} \frac{(x - 2)(x + 2)}{(x - 2)(x + 3)} = \lim_{x \to 2} \frac{x + 2}{x + 3} = \frac{2 + 2}{2 + 3} = \frac{4}{5}$.

2. Evaluate the trigonometric limit: $\lim_{x \to 0} \frac{1 - \cos(4x)}{x^2}$.
  - [ ] $2$
  - [ ] $4$
  - [x] $8$
  - [ ] $16$
   > Use identity $1 - \cos(4x) = 2\sin^2(2x)$. Limit becomes $\lim_{x \to 0} \frac{2\sin^2(2x)}{x^2} = 2 \lim_{x \to 0} \left(\frac{\sin(2x)}{x}\right)^2 = 2 (2)^2 = 2 \times 4 = 8$. (Alternatively by L'Hôpital twice: $\frac{4\sin 4x}{2x} \to \frac{16\cos 4x}{2} = 8$).

3. Find the value of constant $k$ such that the piecewise function is continuous at $x = 3$:
   $$f(x) = \begin{cases} k x^2 - 2 & \text{if } x \le 3 \\ 2x + 10 & \text{if } x > 3 \end{cases}$$
  - [ ] $k = 1$
  - [x] $k = 2$
  - [ ] $k = 3$
  - [ ] $k = 4$
   > For continuity at $x = 3$, LHL must equal RHL: LHL $= f(3) = k(3)^2 - 2 = 9k - 2$. RHL $= \lim_{x \to 3^+} (2x + 10) = 2(3) + 10 = 16$. Equating: $9k - 2 = 16 \implies 9k = 18 \implies k = 2$.