---
title: Differential Equations
level: advanced
---

## Learning objective

Introduce differential equations, order, general solutions and elementary separable methods.

## Core concepts

- A differential equation relates an unknown function to one or more of its derivatives. Its order is the highest derivative present.
- A solution is a function that satisfies the equation on an interval. A general solution usually contains arbitrary constants.
- For dy/dx=g(x), integrate: y=∫g(x)dx+C.
- For a separable equation dy/dx=f(x)g(y), rearrange dy/g(y)=f(x)dx and integrate, while respecting points where division by g(y) is invalid.
- An initial condition such as y(0)=2 determines the arbitrary constant when the solution is unique.

## Essential formulae and results

For separable dy/dx=f(x)g(y), write dy/g(y)=f(x)dx where valid.

## Worked examples

**Example 1.** Solve dy/dx=3x²: y=x³+C.
**Example 2.** Solve dy/dx=ky: dy/y=k dx, so ln|y|=kx+C and y=Ae^(kx), including the zero solution when A=0.

## Common mistakes to avoid

- State the interval and domain where a solution is valid.
- Dividing by a function can lose constant solutions where that function is zero.
- Apply the initial condition after finding the general solution.

## Exam approach

1. Identify the topic and write down the relevant definition or formula.
2. Check the conditions: domain, non-zero denominators, interval, sign and units where applicable.
3. Show the essential algebraic steps instead of jumping to an answer.
4. Substitute the result into the original condition whenever extraneous solutions are possible.
5. Keep exact values (fractions, radicals and π) until a decimal approximation is requested.

## Quiz

1. The order of d²y/dx²+dy/dx+y=0 is:
- [ ] 0
- [ ] 1
- [x] 2
- [ ] 3
> The highest derivative is the second derivative.

2. A solution of dy/dx=2x is:
- [ ] y=x+C
- [x] y=x²+C
- [ ] y=2x²+C
- [ ] y=e^(2x)
> Integrating 2x gives x²+C.

3. For dy/dx=3y, the general solution is:
- [ ] 3x+C
- [x] Ce^(3x)
- [ ] 3e^x
- [ ] C+3y
> Separate variables: dy/y=3dx, then exponentiate.

