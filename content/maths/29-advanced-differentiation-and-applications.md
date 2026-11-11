---
title: Advanced Differentiation and Applications
level: advanced
---

Advanced differentiation includes implicit differentiation, logarithmic differentiation, parametric differentiation, inverse trigonometric derivatives, and higher-order derivatives.

## Implicit Differentiation

Implicit differentiation is used when an equation contains both x and y without expressing y directly in terms of x.

Differentiate both sides with respect to x. Whenever differentiating a term containing y, multiply by dy/dx.

**Example:**

x² + y² = r²

2x + 2y(dy/dx) = 0

Therefore,

dy/dx = -x/y

## Logarithmic Differentiation

Logarithmic differentiation is useful for functions with variable exponents or complicated products and quotients.

**Steps:**

1. Take the natural logarithm of both sides.
2. Differentiate both sides with respect to x.
3. Multiply by y to find dy/dx.

**Example:**

y = xˣ

Taking logarithms:

ln y = x ln x

Differentiating:

(1/y)(dy/dx) = ln x + 1

Therefore,

dy/dx = xˣ(1 + ln x)

## Parametric Differentiation

In parametric equations, both x and y are expressed in terms of another variable called a parameter t.

**First Derivative:**

dy/dx = (dy/dt) / (dx/dt)

**Second Derivative:**

d²y/dx² = [d/dt(dy/dx)] / (dx/dt)

The second derivative must be calculated by differentiating dy/dx with respect to t and then dividing by dx/dt.

## Inverse Trigonometric Derivatives

The important inverse trigonometric derivatives are:

| Function | Derivative |
|---|---|
| sin⁻¹ x | 1 / √(1 - x²) |
| cos⁻¹ x | -1 / √(1 - x²) |
| tan⁻¹ x | 1 / (1 + x²) |

For a function containing u instead of x, apply the Chain Rule.

**Example:**

If y = tan⁻¹(u), then

dy/dx = (1 / (1 + u²)) × (du/dx)

## Important Differentiation Formulas

| Function | Derivative |
|---|---|
| f(x)^g(x) | f(x)^g(x) [g'(x) ln f(x) + g(x)f'(x)/f(x)] |
| aˣ | aˣ ln a |
| logₐ x | 1 / (x ln a) |
| xᵐ | mxᵐ⁻¹ |

For an implicitly defined equation F(x, y) = 0:

dy/dx = -Fₓ / Fᵧ

This formula applies when Fᵧ is nonzero.

## Higher-Order Derivatives

Higher-order derivatives are obtained by differentiating a function repeatedly.

- First derivative: dy/dx
- Second derivative: d²y/dx²
- Third derivative: d³y/dx³
- Nth derivative: dⁿy/dxⁿ

For a power function:

dⁿ(xᵐ)/dxⁿ = [m! / (m - n)!] xᵐ⁻ⁿ

When n is greater than m for a non-negative integer power m, the derivative is zero.

## Common Exam Traps

- **Forgetting the Chain Rule:** The derivative of y³ with respect to x is 3y²(dy/dx), not just 3y².
- **Incorrect Parametric Second Derivative:** Do not calculate d²y/dx² as (d²y/dt²) / (d²x/dt²).
- **Variable Exponents:** Do not apply the ordinary power rule directly to xˣ. Use logarithmic differentiation.
- **Inverse Trigonometric Signs:** The derivative of cos⁻¹ x is negative, unlike the derivative of sin⁻¹ x.
- **Missing Logarithmic Conditions:** For real-valued logarithmic differentiation, ensure the logarithm is defined.

## Quiz

1. Find dy/dx for the curve x³ + y³ = 6xy.

- [ ] (2y - x²) / (y² - 2x)
- [x] (2y - x²) / (y² - 2x)
- [ ] (x² - 2y) / (2x - y²)
- [ ] (3x² - 6y) / (6x - 3y²)

> Differentiating implicitly gives 3x² + 3y²(dy/dx) = 6y + 6x(dy/dx). Rearranging gives 3(y² - 2x)(dy/dx) = 3(2y - x²). Therefore, dy/dx = (2y - x²)/(y² - 2x).

2. Find the derivative of y = xˣ, where x is positive.

- [ ] xˣ
- [ ] x × xˣ⁻¹
- [x] xˣ(1 + ln x)
- [ ] xˣ ln x

> Taking logarithms gives ln y = x ln x. Differentiating gives (1/y)(dy/dx) = ln x + 1. Therefore, dy/dx = xˣ(1 + ln x).

3. Find the slope of the tangent to the parametric curve x = 2t² and y = t³ - t at t = 2.

- [ ] 3/2
- [x] 11/8
- [ ] 12/8
- [ ] 8/11

> dx/dt = 4t and dy/dt = 3t² - 1. Therefore, dy/dx = (3t² - 1)/(4t). Substituting t = 2 gives (12 - 1)/8 = 11/8.
