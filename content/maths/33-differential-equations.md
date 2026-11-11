---
title: Differential Equations
level: advanced
---

A differential equation relates an unknown function to its derivatives. Solving first-order differential equations provides tools for modeling physical, biological, and economic systems.

## Order, Degree, and Solution Types

A **differential equation (DE)** involves variables $x, y$ and derivatives of $y$ with respect to $x$.

- **Order:** The order of the highest derivative present in the equation.
- **Degree:** The power to which the highest-order derivative is raised, after the equation has been made rational and integral with respect to its derivatives.
- **General Solution:** Contains as many arbitrary constants as the order of the differential equation.
- **Particular Solution:** Obtained by assigning specific values to the arbitrary constants using initial conditions.

## Solution Methods for First-Order DEs

A first-order DE takes the general form $\frac{dy}{dx} = f(x, y)$.

### 1. Variable Separable Method

If the equation can be factored into functions of $x$ and $y$ separately:

$$\frac{dy}{dx} = g(x) h(y) \implies \int \frac{1}{h(y)} \, dy = \int g(x) \, dx + C$$

### 2. Homogeneous Differential Equations

An equation $\frac{dy}{dx} = F(x, y)$ is homogeneous if $F(\lambda x, \lambda y) = F(x, y)$. Substitute $y = v x \implies \frac{dy}{dx} = v + x \frac{dv}{dx}$ to separate variables in $v$ and $x$.

### 3. Linear First-Order Differential Equations

A first-order linear DE has standard form:

$$\frac{dy}{dx} + P(x) y = Q(x)$$

Solve using an **Integrating Factor ($\text{IF}$)**:

$$\text{IF} = e^{\int P(x) \, dx}$$

$$\text{General Solution}: y \cdot (\text{IF}) = \int \Big( Q(x) \cdot (\text{IF}) \Big) \, dx + C$$

## First-Order DE Classification Table

| DE Type | Standard Equation Form | Solution Strategy / Formula |
|---|---|---|
| Variable Separable | $\frac{dy}{dx} = f(x)g(y)$ | Integrate $\int \frac{dy}{g(y)} = \int f(x)dx$ |
| Homogeneous | $\frac{dy}{dx} = f\left(\frac{y}{x}\right)$ | Substitute $y = vx, \frac{dy}{dx} = v + x\frac{dv}{dx}$ |
| First-Order Linear | $\frac{dy}{dx} + P(x)y = Q(x)$ | $y \cdot e^{\int P dx} = \int Q e^{\int P dx} dx + C$ |
| Bernoulli Equation | $\frac{dy}{dx} + P(x)y = Q(x)y^n$ | Substitute $u = y^{1-n}$ to linearize |

## Important Formulas and Integrating Factor Identities

Linear DE Integrating Factor:

$$\text{IF} = e^{\int P(x) \, dx}$$

General Solution Formula for Linear DE:

$$y \cdot e^{\int P(x) \, dx} = \int \left( Q(x) \cdot e^{\int P(x) \, dx} \right) dx + C$$

Exponential Decay / Growth Law:

$$\frac{dy}{dt} = k y \implies y(t) = y_0 e^{k t}$$

## Common Exam Traps

- **Finding Degree of Non-Polynomial Derivatives:** Attempting to define the degree of a DE containing terms like $\sin\left(\frac{dy}{dx}\right)$ or $e^{y'}$. The degree of such DEs is **undefined**.
- **Forgetting Absolute Sign in $\text{IF}$ Logarithm:** Writing $\text{IF} = e^{\int \frac{1}{x} dx} = e^{\ln x} = x$ without verifying $x > 0$.
- **Not Converting to Standard Linear Form First:** Calculating $\text{IF}$ from $x \frac{dy}{dx} + 2y = x^2$ as $e^{\int 2 dx}$ without first dividing by $x$ to get $\frac{dy}{dx} + \frac{2}{x}y = x$.

## Quiz

1. Determine the order and degree of the differential equation: $\left(\frac{d^2y}{dx^2}\right)^3 + \left(\frac{dy}{dx}\right)^4 + y = 0$.
  - [ ] Order $3$, Degree $2$
  - [x] Order $2$, Degree $3$
  - [ ] Order $2$, Degree $4$
  - [ ] Order $4$, Degree $3$
   > The highest derivative present is $\frac{d^2y}{dx^2}$, so the order is $2$. Its exponent is $3$, so the degree is $3$.

2. Find the integrating factor ($\text{IF}$) for the linear differential equation: $\frac{dy}{dx} + \frac{3}{x} y = x^2 \quad (x > 0)$.
  - [ ] $3x$
  - [ ] $e^{3x}$
  - [x] $x^3$
  - [ ] $\ln(x^3)$
   > Here $P(x) = \frac{3}{x}$. Compute $\text{IF} = e^{\int \frac{3}{x} \, dx} = e^{3 \ln x} = e^{\ln(x^3)} = x^3$.

3. Solve the variable separable differential equation: $\frac{dy}{dx} = 2x y$ for $y > 0$.
  - [ ] $y = x^2 + C$
  - [x] $y = C e^{x^2}$
  - [ ] $y = e^{2x} + C$
  - [ ] $y = C x^2$
   > Separate variables: $\frac{1}{y} \, dy = 2x \, dx$. Integrate both sides: $\int \frac{1}{y} \, dy = \int 2x \, dx \implies \ln y = x^2 + c_1 \implies y = e^{x^2 + c_1} = e^{c_1} e^{x^2} = C e^{x^2}$.