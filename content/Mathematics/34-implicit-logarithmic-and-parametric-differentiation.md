---
title: Implicit, Logarithmic and Parametric Differentiation
level: advanced
---

## Learning objective

Differentiate relations where y is not isolated, products of variable powers, and curves described parametrically.

## Core concepts

- For an implicit relation F(x,y)=0, differentiate both sides with respect to x, treating y as a function of x; thus d(y^n)/dx=ny^(n−1)dy/dx.
- Logarithmic differentiation is useful for products, quotients and variable exponents. Take logarithms first, differentiate, then solve for y'.
- For y=u(x)^{v(x)} with positive u, take ln y=v ln u, giving y'/y=v'ln u+v u'/u.
- For parametric equations x=x(t), y=y(t), dy/dx=(dy/dt)/(dx/dt), when dx/dt≠0.
- The second derivative in parametric form is d²y/dx²=[d/dt(dy/dx)]/(dx/dt).

## Essential formulae and results

Implicit: differentiate y as a function of x; parametric: dy/dx=(dy/dt)/(dx/dt).

## Worked examples

**Example 1.** Differentiate x²+y²=25: 2x+2y y'=0, so y'=−x/y where y≠0.
**Example 2.** For y=x^x (x>0), ln y=x ln x; y'/y=ln x+1, so y'=x^x(ln x+1).

## Common mistakes to avoid

- When differentiating y, include dy/dx.
- Logarithms require positive arguments in real-variable work.
- For parametric curves, divide by dx/dt only where it is non-zero.

## Exam approach

1. Identify the topic and write down the relevant definition or formula.
2. Check the conditions: domain, non-zero denominators, interval, sign and units where applicable.
3. Show the essential algebraic steps instead of jumping to an answer.
4. Substitute the result into the original condition whenever extraneous solutions are possible.
5. Keep exact values (fractions, radicals and π) until a decimal approximation is requested.

## Quiz

1. Differentiating x²+y²=1 gives:
- [ ] 2x+2y=0
- [x] 2x+2y y'=0
- [ ] 2x y'+2y=0
- [ ] x+y'=0
> Differentiate y² using the chain rule.

2. For x=t² and y=t³, dy/dx is:
- [ ] 2t/3
- [x] 3t/2
- [ ] t
- [ ] 6t
> dy/dt=3t² and dx/dt=2t; ratio=3t/2.

3. The logarithmic derivative of x^x for x>0 is:
- [ ] x
- [ ] 1/x
- [x] ln x+1
- [ ] x ln x
> ln y=x ln x; differentiating gives y'/y=ln x+1.
