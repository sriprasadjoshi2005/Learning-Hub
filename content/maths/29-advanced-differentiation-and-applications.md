---
title: Advanced Differentiation and Applications
level: advanced
---

Advanced differentiation encompasses implicit functions, logarithmic differentiation, parametric curves, higher-order derivatives, and inverse trigonometric rates of change.

## Implicit, Logarithmic, and Parametric Differentiation

### Implicit Differentiation

When an equation defines $y$ implicitly as a function of $x$ ($F(x, y) = 0$), differentiate both sides with respect to $x$, applying the Chain Rule to all terms containing $y$ ($\frac{d}{dx}[g(y)] = g'(y) \frac{dy}{dx}$), then solve for $\frac{dy}{dx}$.

$$\text{Example}: x^2 + y^2 = r^2 \implies 2x + 2y \frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}$$

### Logarithmic Differentiation

Used for functions containing variable exponents ($y = [f(x)]^{g(x)}$) or complicated products/quotients:

1. Take natural logarithm of both sides: $\ln y = g(x) \ln[f(x)]$.
2. Differentiate implicitly: $\frac{1}{y} \frac{dy}{dx} = \frac{d}{dx}\left\{g(x) \ln[f(x)]\right\}$.
3. Multiply by $y$ to solve for $\frac{dy}{dx}$.

### Parametric Differentiation

When $x$ and $y$ are both expressed in terms of a parameter $t$ ($x = f(t), y = g(t)$):

- **First Derivative:**
$$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} \quad \left(\frac{dx}{dt} \neq 0\right)$$

- **Second Derivative:**
$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}$$

## Inverse Trigonometric Derivatives and Higher Orders

### Inverse Trigonometric Derivatives

- $\frac{d}{dx}(\arcsin x) = \frac{1}{\sqrt{1 - x^2}} \quad (|x| < 1)$
- $\frac{d}{dx}(\arccos x) = -\frac{1}{\sqrt{1 - x^2}} \quad (|x| < 1)$
- $\frac{d}{dx}(\arctan x) = \frac{1}{1 + x^2}$

## Advanced Derivatives Master Table

| Expression Form | Differentiation Strategy | Output Derivative Formula |
|---|---|---|
| $y = f(x)^g(x)$ | Logarithmic Differentiation | $y' = f(x)^g(x) \left[ g'(x)\ln f(x) + \frac{g(x)f'(x)}{f(x)} \right]$ |
| $x = f(t), y = g(t)$ | Parametric Rule | $\frac{dy}{dx} = \frac{g'(t)}{f'(t)}$ |
| $F(x, y) = 0$ | Implicit Differentiation | $\frac{dy}{dx} = -\frac{F_x}{F_y}$ |
| $y = \arctan(u)$ | Chain Rule + Inv. Trig | $\frac{dy}{dx} = \frac{1}{1 + u^2} \cdot \frac{du}{dx}$ |
| $y = a^x \quad (a > 0)$ | General Exponential | $\frac{dy}{dx} = a^x \ln a$ |
| $y = \log_a x$ | General Logarithm | $\frac{dy}{dx} = \frac{1}{x \ln a}$ |

## Important Formulas and Parametric Identities

Parametric Second Derivative Formula:

$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}} \neq \frac{\frac{d^2y}{dt^2}}{\frac{d^2x}{dt^2}}$$

N-th Derivative Power Rule:

$$\frac{d^n}{dx^n}(x^m) = \begin{cases} \frac{m!}{(m-n)!} x^{m-n} & \text{if } n \le m \\ 0 & \text{if } n > m \end{cases}$$

## Common Exam Traps

- **Parametric Second Derivative Error:** Calculating $\frac{d^2y}{dx^2}$ as $\frac{y''(t)}{x''(t)}$. You must differentiate $\frac{dy}{dx}$ with respect to $t$, then divide by $\frac{dx}{dt}$.
- **Forgetting $\frac{dy}{dx}$ during Implicit Steps:** Differentiating $y^3$ with respect to $x$ as $3y^2$ instead of $3y^2 \frac{dy}{dx}$.
- **Applying Power Rule to Variable Exponents:** Differentiating $x^x$ as $x \cdot x^{x-1} = x^x$. The correct derivative using logarithmic differentiation is $x^x(1 + \ln x)$.

## Quiz

1. Find $\frac{dy}{dx}$ for the curve defined implicitly by $x^3 + y^3 = 6xy$.
  - [ ] $\frac{2y - x^2}{y^2 - 2x}$
  - [x] $\frac{2y - x^2}{y^2 - 2x}$
  - [ ] $\frac{x^2 - 2y}{2x - y^2}$
  - [ ] $\frac{3x^2 - 6y}{6x - 3y^2}$
   > Differentiate implicitly with respect to $x$: $3x^2 + 3y^2 \frac{dy}{dx} = 6y + 6x \frac{dy}{dx} \implies 3y^2 \frac{dy}{dx} - 6x \frac{dy}{dx} = 6y - 3x^2 \implies 3(y^2 - 2x)\frac{dy}{dx} = 3(2y - x^2) \implies \frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}$.

2. Find the derivative $\frac{dy}{dx}$ of $y = x^x$ for $x > 0$.
  - [ ] $x^x$
  - [ ] $x \cdot x^{x-1}$
  - [x] $x^x (1 + \ln x)$
  - [ ] $x^x \ln x$
   > Take natural log: $\ln y = x \ln x$. Differentiate implicitly: $\frac{1}{y} \frac{dy}{dx} = (1)(\ln x) + x\left(\frac{1}{x}\right) = \ln x + 1$. Multiply by $y$: $\frac{dy}{dx} = y (1 + \ln x) = x^x (1 + \ln x)$.

3. Find the slope of the tangent line $\frac{dy}{dx}$ to the parametric curve $x = 2t^2, y = t^3 - t$ at parameter $t = 2$.
  - [ ] $\frac{11}{8}$
  - [x] $\frac{11}{8}$
  - [ ] $\frac{12}{8}$
  - [ ] $\frac{8}{11}$
   > $\frac{dx}{dt} = 4t$ and $\frac{dy}{dt} = 3t^2 - 1$. So $\frac{dy}{dx} = \frac{3t^2 - 1}{4t}$. At $t = 2$: $\frac{dy}{dx} = \frac{3(2)^2 - 1}{4(2)} = \frac{12 - 1}{8} = \frac{11}{8}$.