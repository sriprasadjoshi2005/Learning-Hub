---
title: Integral Calculus- Fundamentals
level: advanced
---

Integral calculus reverses the process of differentiation. Indefinite integration finds antiderivatives of functions, representing the family of curves whose rate of change matches a given function.

## Antiderivatives and Indefinite Integration

An **antiderivative** of a function $f(x)$ is a function $F(x)$ such that $F'(x) = f(x)$.

The **indefinite integral** of $f(x)$ is expressed as:

$$\int f(x) \, dx = F(x) + C$$

where $C$ is the **constant of integration**, representing an arbitrary vertical shift.

### Basic Integration Rules

1. **Power Rule:** $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)$
2. **Logarithmic Rule:** $\int \frac{1}{x} \, dx = \ln|x| + C \quad (x \neq 0)$
3. **Exponential Rule:** $\int e^{kx} \, dx = \frac{1}{k} e^{kx} + C$
4. **Trigonometric Integrals:**
   - $\int \sin(x) \, dx = -\cos(x) + C$
   - $\int \cos(x) \, dx = \sin(x) + C$
   - $\int \sec^2(x) \, dx = \tan(x) + C$

## Primary Integration Techniques

### Integration by Substitution ($u$-Substitution)

Used when an integral contains a function and its derivative: $\int f(g(x)) g'(x) \, dx$. Set $u = g(x) \implies du = g'(x) \, dx$:

$$\int f(g(x)) g'(x) \, dx = \int f(u) \, du$$

### Integration by Parts

Derived from the product rule of differentiation:

$$\int u \, dv = u v - \int v \, du$$

- **LIATE Priority Rule for Choosing $u$:**
  1. **L**ogarithmic ($\ln x$)
  2. **I**nverse Trigonometric ($\arctan x$)
  3. **A**lgebraic ($x^2, 3x$)
  4. **T**rigonometric ($\sin x$)
  5. **E**xponential ($e^x$)

## Standard Integration Master Table

| Integrand $f(x)$ | Indefinite Integral $\int f(x) \, dx$ | Strategy / Technique |
|---|---|---|
| $x^n \quad (n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ | Power rule |
| $\frac{1}{a^2 + x^2}$ | $\frac{1}{a} \arctan\left(\frac{x}{a}\right) + C$ | Standard inverse trig |
| $\frac{1}{\sqrt{a^2 - x^2}}$ | $\arcsin\left(\frac{x}{a}\right) + C$ | Standard radical form |
| $\tan(x)$ | $\ln|\sec x| + C = -\ln|\cos x| + C$ | Rewritten as $\frac{\sin x}{\cos x}$ |
| $x e^x$ | $(x - 1)e^x + C$ | Integration by parts |

## Important Formulas and Standard Forms

Inverse Trigonometric Primitive Integrals:

$$\int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C$$

$$\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C$$

Integration by Parts Formula:

$$\int u \, dv = u v - \int v \, du$$

## Common Exam Traps

- **Forgetting the Constant of Integration ($C$):** Omitting $+C$ in indefinite integrals.
- **Incorrect Sign in Trigonometric Integrals:** Writing $\int \sin x \, dx = \cos x + C$ instead of $-\cos x + C$.
- **Power Rule Failure at $n = -1$:** Attempting to apply $\frac{x^{0}}{0}$ to $\int \frac{1}{x} \, dx$. The correct integral is $\ln|x| + C$.

## Quiz

1. Evaluate the indefinite integral: $\int (6x^2 - 4x + 5) \, dx$.
  - [ ] $12x - 4 + C$
  - [x] $2x^3 - 2x^2 + 5x + C$
  - [ ] $6x^3 - 4x^2 + 5x + C$
  - [ ] $2x^3 - 4x^2 + 5x + C$
   > Integrate term by term: $\int 6x^2 \, dx - \int 4x \, dx + \int 5 \, dx = 6\left(\frac{x^3}{3}\right) - 4\left(\frac{x^2}{2}\right) + 5x + C = 2x^3 - 2x^2 + 5x + C$.

2. Evaluate $\int x \cos(x) \, dx$ using integration by parts.
  - [ ] $x \sin x + \cos x + C$
  - [x] $x \sin x + \cos x + C$
  - [ ] $x \sin x - \cos x + C$
  - [ ] $-x \sin x + \cos x + C$
   > Let $u = x \implies du = dx$, and $dv = \cos x \, dx \implies v = \sin x$. Apply formula: $uv - \int v \, du = x \sin x - \int \sin x \, dx = x \sin x - (-\cos x) + C = x \sin x + \cos x + C$.

3. Find $\int \frac{2x}{x^2 + 9} \, dx$.
  - [ ] $\arctan\left(\frac{x}{3}\right) + C$
  - [x] $\ln(x^2 + 9) + C$
  - [ ] $\frac{1}{x^2 + 9} + C$
  - [ ] $2\ln(x^2 + 9) + C$
   > Substitute $u = x^2 + 9 \implies du = 2x \, dx$. The integral becomes $\int \frac{du}{u} = \ln|u| + C = \ln(x^2 + 9) + C$.
