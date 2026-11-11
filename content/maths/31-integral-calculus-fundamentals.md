---
title: Integral Calculus - Fundamentals
level: advanced
---

Integral calculus reverses the process of differentiation. Indefinite integration finds antiderivatives of functions, representing the family of curves whose rate of change matches a given function.

## Antiderivatives and Indefinite Integration

An **antiderivative** of a function f(x) is a function F(x) such that F'(x) = f(x).

The **indefinite integral** of f(x) is expressed as:

integral f(x) dx = F(x) + C

where C is the **constant of integration**, representing an arbitrary vertical shift.

### Basic Integration Rules

1. **Power Rule:** integral x^n dx = x^(n+1)/(n+1) + C, where n is not equal to -1.
2. **Logarithmic Rule:** integral (1/x) dx = ln(abs(x)) + C, where x is not zero.
3. **Exponential Rule:** integral e^(kx) dx = e^(kx)/k + C, where k is not zero.
4. **Trigonometric Integrals:**
   - integral sin(x) dx = -cos(x) + C
   - integral cos(x) dx = sin(x) + C
   - integral sec²(x) dx = tan(x) + C

## Primary Integration Techniques

### Integration by Substitution (u-Substitution)

Used when an integral contains a function and its derivative:

integral f(g(x))g'(x) dx

Set:

u = g(x)

du = g'(x) dx

Therefore:

integral f(g(x))g'(x) dx = integral f(u) du

### Integration by Parts

Derived from the product rule of differentiation:

integral u dv = uv - integral v du

**LIATE Priority Rule for Choosing u:**

1. **L**ogarithmic (ln x)
2. **I**nverse Trigonometric (arctan x)
3. **A**lgebraic (x², 3x)
4. **T**rigonometric (sin x)
5. **E**xponential (e^x)

## Standard Integration Master Table

| Integrand f(x) | Indefinite Integral | Strategy / Technique |
|---|---|---|
| x^n, where n is not -1 | x^(n+1)/(n+1) + C | Power rule |
| 1/(a² + x²) | (1/a) arctan(x/a) + C | Standard inverse trig |
| 1/sqrt(a² - x²) | arcsin(x/a) + C | Standard radical form |
| tan(x) | ln(abs(sec x)) + C | Rewritten as sin(x)/cos(x) |
| x e^x | (x - 1)e^x + C | Integration by parts |

## Important Formulas and Standard Forms

### Inverse Trigonometric Primitive Integrals

integral 1/(a² + x²) dx = (1/a) arctan(x/a) + C

integral 1/sqrt(a² - x²) dx = arcsin(x/a) + C

### Integration by Parts Formula

integral u dv = uv - integral v du

## Common Exam Traps

- **Forgetting the Constant of Integration (C):** Omitting +C in indefinite integrals.
- **Incorrect Sign in Trigonometric Integrals:** Writing integral sin(x) dx = cos(x) + C instead of -cos(x) + C.
- **Power Rule Failure at n = -1:** Attempting to apply x^0/0 to integral (1/x) dx. The correct integral is ln(abs(x)) + C.
- **Integration by Parts:** Remember the negative sign in uv - integral v du.
- **Substitution:** Do not forget to replace dx using the substitution.

## Quiz

1. Evaluate the indefinite integral: integral (6x² - 4x + 5) dx.
- [ ] 12x - 4 + C
- [x] 2x³ - 2x² + 5x + C
- [ ] 6x³ - 4x² + 5x + C
- [ ] 2x³ - 4x² + 5x + C

> Integrate term by term:
>
> integral 6x² dx - integral 4x dx + integral 5 dx
>
> = 6(x³/3) - 4(x²/2) + 5x + C
>
> = 2x³ - 2x² + 5x + C.

2. Evaluate integral x cos(x) dx using integration by parts.
- [ ] x sin(x) - cos(x) + C
- [x] x sin(x) + cos(x) + C
- [ ] x sin(x) + 2cos(x) + C
- [ ] -x sin(x) + cos(x) + C

> Let u = x, so du = dx.
>
> Let dv = cos(x) dx, so v = sin(x).
>
> Apply the formula:
>
> integral u dv = uv - integral v du
>
> = x sin(x) - integral sin(x) dx
>
> = x sin(x) - (-cos(x)) + C
>
> = x sin(x) + cos(x) + C.

3. Find integral [2x/(x² + 9)] dx.
- [ ] arctan(x/3) + C
- [x] ln(x² + 9) + C
- [ ] 1/(x² + 9) + C
- [ ] 2ln(x² + 9) + C

> Substitute u = x² + 9.
>
> Then du = 2x dx.
>
> The integral becomes:
>
> integral (1/u) du = ln(abs(u)) + C
>
> Substituting back:
>
> ln(x² + 9) + C.
