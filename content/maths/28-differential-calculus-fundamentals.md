---
title: Differential Calculus: Fundamentals
level: advanced
---

Differential calculus studies rates of change and slopes of curves. Defining the derivative from first principles provides the groundwork for differentiation rules used across science and engineering.

## Derivative Definition and Geometric Meaning

The **derivative** of a function $y = f(x)$ at $x$ measures the instantaneous rate of change of $y$ with respect to $x$.

### Derivative from First Principles (Difference Quotient)

$$f'(x) = \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

- **Geometric Interpretation:** $f'(a)$ is the exact **slope of the tangent line** to the curve $y = f(x)$ at point $(a, f(a))$.
- **Secant to Tangent:** As $h \to 0$, the secant line connecting $(x, f(x))$ and $(x+h, f(x+h))$ approaches the tangent line.

```text
                     Geometric Meaning of Derivative
         y
         │                                       / Tangent Line (Slope = f'(a))
         │                                      /
         │                                ┌───*  (a+h, f(a+h))
         │                               /   /│
         │                        ┌─────*───/─┼─ Secant Line
         │                       /     (a, f(a))│
         │               ───────┘             │
         └────────────────────────────────────┴─────────── x
                                        a    a+h
```

## Fundamental Differentiation Rules

Let $u(x)$ and $v(x)$ be differentiable functions, and $c$ be a constant:

1. **Constant Rule:** $\frac{d}{dx}(c) = 0$
2. **Power Rule:** $\frac{d}{dx}(x^n) = n x^{n-1} \quad (n \in \mathbb{R})$
3. **Constant Multiple Rule:** $\frac{d}{dx}[c \cdot u(x)] = c \cdot u'(x)$
4. **Sum and Difference Rule:** $\frac{d}{dx}[u(x) \pm v(x)] = u'(x) \pm v'(x)$
5. **Product Rule:**
$$\frac{d}{dx}[u(x) \cdot v(x)] = u'(x)v(x) + u(x)v'(x)$$

6. **Quotient Rule:**
$$\frac{d}{dx}\left[\frac{u(x)}{v(x)}\right] = \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2} \quad (v(x) \neq 0)$$

7. **Chain Rule (Composite Functions):** If $y = f(g(x))$, let $u = g(x)$:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = f'(g(x)) \cdot g'(x)$$

## Basic Derivatives Master Table

| Function $f(x)$ | Derivative $f'(x) = \frac{d}{dx}[f(x)]$ | Rule Name / Notes |
|---|---|---|
| $x^n$ | $n x^{n-1}$ | Power Rule |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ | Power Rule ($n = 1/2$) |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ | Power Rule ($n = -1$) |
| $\sin x$ | $\cos x$ | Standard Trig Derivative |
| $\cos x$ | $-\sin x$ | Standard Trig Derivative |
| $\tan x$ | $\sec^2 x$ | Derived via Quotient Rule |
| $e^x$ | $e^x$ | Natural Exponential |
| $\ln x$ | $\frac{1}{x} \quad (x > 0)$ | Natural Logarithm |

## Important Formulas and Differentiability Theorem

Differentiability Implies Continuity:

$$\text{If } f(x) \text{ is differentiable at } x = c \implies f(x) \text{ is continuous at } x = c$$

$$\text{(Note: The converse is FALSE! } f(x) = |x| \text{ is continuous at } x = 0 \text{ but NOT differentiable at } x = 0\text{)}$$

Chain Rule Leibniz Form:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx}$$

## Common Exam Traps

- **Product Rule Mistake:** Writing $\frac{d}{dx}[u \cdot v] = u' \cdot v'$. The correct rule requires two terms: $u'v + uv'$.
- **Quotient Rule Order & Sign Error:** Writing $\frac{d}{dx}[\frac{u}{v}] = \frac{u v' - u' v}{v^2}$. The numerator **must start** with $u' v$: $\frac{u' v - u v'}{v^2}$.
- **Forgetting the Inner Derivative in Chain Rule:** Differentiating $\sin(3x^2)$ as $\cos(3x^2)$ without multiplying by the inner derivative $\frac{d}{dx}(3x^2) = 6x$. Correct answer is $6x \cos(3x^2)$.

## Quiz

1. Using first principles or differentiation rules, find $\frac{dy}{dx}$ for $y = 4x^3 - 5x^2 + 7x - 9$.
  - [ ] $12x^2 - 10x$
  - [x] $12x^2 - 10x + 7$
  - [ ] $4x^2 - 5x + 7$
  - [ ] $12x^3 - 10x^2 + 7$
   > Apply Power Rule term by term: $\frac{dy}{dx} = 4(3x^2) - 5(2x) + 7(1) - 0 = 12x^2 - 10x + 7$.

2. Differentiate the product function $f(x) = x^2 \sin x$ with respect to $x$.
  - [ ] $2x \cos x$
  - [ ] $x^2 \cos x$
  - [x] $2x \sin x + x^2 \cos x$
  - [ ] $2x \sin x - x^2 \cos x$
   > Apply Product Rule $u'v + uv'$ with $u = x^2$ and $v = \sin x$: $f'(x) = (2x)(\sin x) + (x^2)(\cos x) = 2x \sin x + x^2 \cos x$.

3. Find the derivative of the composite function $y = (3x^2 + 5)^4$.
  - [ ] $4(3x^2 + 5)^3$
  - [ ] $12x(3x^2 + 5)^4$
  - [x] $24x(3x^2 + 5)^3$
  - [ ] $6x(3x^2 + 5)^3$
   > Apply Chain Rule: let $u = 3x^2 + 5 \implies y = u^4$. $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = 4 u^3 \cdot (6x) = 4(3x^2 + 5)^3 \cdot (6x) = 24x(3x^2 + 5)^3$.