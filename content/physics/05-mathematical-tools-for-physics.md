---
title: Mathematical Tools for Physics
level: foundation
---

Mathematics is the language of physics. Physical laws are expressed through equations, graphs, functions and mathematical relationships.

A strong mathematical foundation allows physical problems to be translated into equations, solved systematically and interpreted in terms of real phenomena.

This lesson introduces the essential mathematical tools required throughout the study of physics, including algebra, proportionality, trigonometry, coordinate geometry, differentiation and integration.

## 1. Algebraic Foundations

Algebra uses symbols to represent unknown or variable quantities.

For example:

\[
v=u+at
\]

This equation relates final velocity, initial velocity, acceleration and time.

If three quantities are known, the equation can be rearranged to determine the fourth.

### Rearranging equations

Suppose:

\[
v=u+at
\]

To make acceleration the subject:

\[
v-u=at
\]

\[
a=\frac{v-u}{t}
\]

To make time the subject:

\[
t=\frac{v-u}{a}
\]

The ability to rearrange equations is essential in numerical physics.

### Substitution

Suppose:

\[
u=5\ \text{m/s}
\]

\[
a=2\ \text{m/s}^2
\]

\[
t=4\ \text{s}
\]

Using:

\[
v=u+at
\]

\[
v=5+(2)(4)
\]

\[
v=13\ \text{m/s}
\]

Always substitute values with their units and check that the final unit is physically appropriate.

## 2. Ratios and Proportionality

Proportionality describes how one quantity changes when another quantity changes.

### Direct proportionality

Two quantities are directly proportional when one increases or decreases by the same factor as the other.

\[
y\propto x
\]

Therefore:

\[
y=kx
\]

where k is a constant.

Example:

For a constant mass:

\[
W=mg
\]

Weight is directly proportional to gravitational acceleration.

If gravitational acceleration doubles, weight doubles.

### Inverse proportionality

Two quantities are inversely proportional when one increases as the other decreases.

\[
y\propto\frac{1}{x}
\]

Therefore:

\[
y=\frac{k}{x}
\]

Example:

For a fixed distance:

\[
t=\frac{s}{v}
\]

Travel time is inversely proportional to speed.

If speed doubles, travel time becomes half, assuming the distance remains unchanged.

### Square proportionality

\[
y\propto x^2
\]

If x doubles, y becomes four times its original value.

For example, the kinetic energy of an object is:

\[
K=\frac12mv^2
\]

For constant mass, kinetic energy is proportional to the square of speed.

### Inverse-square proportionality

\[
y\propto\frac{1}{x^2}
\]

If x doubles, y becomes one-fourth.

Examples include:

- Gravitational force between two point masses.
- Electrostatic force between two point charges.
- Intensity of an ideal point source in a uniform medium.

## 3. Powers, Roots and Exponents

Powers and roots frequently appear in physics equations.

Important exponent rules:

\[
a^m\times a^n=a^{m+n}
\]

\[
\frac{a^m}{a^n}=a^{m-n}
\]

\[
(a^m)^n=a^{mn}
\]

\[
a^{-n}=\frac{1}{a^n}
\]

\[
a^0=1 \quad (a\neq0)
\]

Square roots are particularly common in equations involving energy, speed and vector magnitudes.

For example:

\[
v=\sqrt{\frac{2K}{m}}
\]

If kinetic energy and mass are known, the speed can be determined.

## 4. Coordinate Systems

A coordinate system provides a mathematical framework for specifying positions.

### Cartesian coordinates

In two dimensions, a point is represented by:

\[
(x,y)
\]

In three dimensions:

\[
(x,y,z)
\]

The coordinate axes are mutually perpendicular.

### Polar coordinates

A point in a plane can also be represented using:

- Radial distance r from the origin.
- Angle θ measured from a reference axis.

The relationships are:

\[
x=r\cos\theta
\]

\[
y=r\sin\theta
\]

And:

\[
r=\sqrt{x^2+y^2}
\]

Polar coordinates are particularly useful in circular motion and problems involving radial symmetry.

## 5. Trigonometric Functions

Trigonometry studies relationships between angles and sides of triangles.

For a right-angled triangle:

\[
\sin\theta=\frac{\text{Opposite}}{\text{Hypotenuse}}
\]

\[
\cos\theta=\frac{\text{Adjacent}}{\text{Hypotenuse}}
\]

\[
\tan\theta=\frac{\text{Opposite}}{\text{Adjacent}}
\]

Important relationships:

\[
\tan\theta=\frac{\sin\theta}{\cos\theta}
\]

\[
\sin^2\theta+\cos^2\theta=1
\]

\[
1+\tan^2\theta=\sec^2\theta
\]

### Important trigonometric values

| Angle | sin | cos | tan |
|---|---|---|---|
| 0° | 0 | 1 | 0 |
| 30° | 1/2 | sqrt(3)/2 | 1/sqrt(3) |
| 45° | 1/sqrt(2) | 1/sqrt(2) | 1 |
| 60° | sqrt(3)/2 | 1/2 | sqrt(3) |
| 90° | 1 | 0 | Undefined |

These values are frequently used in vector resolution, inclined-plane problems and projectile motion.

## 6. Trigonometric Identities and Applications

Trigonometric identities simplify equations involving angles.

Examples:

\[
\sin(90^\circ-\theta)=\cos\theta
\]

\[
\cos(90^\circ-\theta)=\sin\theta
\]

\[
\sin2\theta=2\sin\theta\cos\theta
\]

\[
\cos2\theta=\cos^2\theta-\sin^2\theta
\]

### Application: Resolving an inclined force

A force F acts at an angle θ above the horizontal.

Its horizontal component is:

\[
F_x=F\cos\theta
\]

Its vertical component is:

\[
F_y=F\sin\theta
\]

This allows a two-dimensional force problem to be separated into two simpler one-dimensional equations.

## 7. Graphs and Their Physical Meaning

Graphs help represent relationships between physical quantities.

A graph can reveal whether a relationship is linear, quadratic, inverse or periodic.

### Straight-line graph

\[
y=mx+c
\]

Where:

- m = gradient.
- c = vertical intercept.

Gradient:

\[
m=\frac{y_2-y_1}{x_2-x_1}
\]

If the graph represents displacement against time, the gradient represents velocity.

### Curved graph

A curved graph indicates that the relationship is not linear.

For example:

\[
y=x^2
\]

produces a parabolic curve.

The gradient changes from point to point.

### Area under a graph

In physics, the area under a graph may represent a meaningful physical quantity.

Examples:

- Area under a velocity-time graph = displacement.
- Area under a force-displacement graph = work.
- Area under a power-time graph = energy transferred.

The physical meaning depends on the axes.

## 8. Functions and Variables

A function describes how one quantity depends on another.

For example:

\[
s(t)=5t+2
\]

This describes position as a function of time.

Here:

- t is the independent variable.
- s is the dependent variable.

Physical quantities may be functions of:

- Time.
- Position.
- Temperature.
- Frequency.
- Electric field.
- Other physical variables.

Understanding functions is necessary for studying motion, waves, electric fields and thermodynamics.

## 9. Introduction to Differentiation

Differentiation measures how rapidly one quantity changes with respect to another.

The derivative of a function f(x) is written:

\[
\frac{df}{dx}
\]

It represents the instantaneous rate of change of f with respect to x.

### Basic differentiation rules

For:

\[
f(x)=x^n
\]

The derivative is:

\[
\frac{df}{dx}=nx^{n-1}
\]

Examples:

\[
\frac{d}{dx}(x^2)=2x
\]

\[
\frac{d}{dx}(x^3)=3x^2
\]

\[
\frac{d}{dx}(5x)=5
\]

\[
\frac{d}{dx}(7)=0
\]

The derivative of a constant is zero.

### Physical application: Velocity

Velocity is the rate of change of displacement with time.

\[
v=\frac{ds}{dt}
\]

More precisely, instantaneous velocity is:

\[
v=\frac{ds}{dt}
\]

Acceleration is the rate of change of velocity:

\[
a=\frac{dv}{dt}
\]

Therefore:

\[
a=\frac{d^2s}{dt^2}
\]

Differentiation is essential for understanding instantaneous physical quantities.

## 10. Introduction to Integration

Integration is the mathematical process used to determine accumulated quantities.

It is closely related to differentiation.

The indefinite integral is written:

\[
\int f(x)\,dx
\]

For powers:

\[
\int x^n dx=\frac{x^{n+1}}{n+1}+C
\]

provided n is not equal to -1.

Examples:

\[
\int x^2dx=\frac{x^3}{3}+C
\]

\[
\int 5dx=5x+C
\]

The constant C represents an arbitrary constant of integration.

### Physical application: Displacement

Since:

\[
v=\frac{ds}{dt}
\]

We can write:

\[
ds=v\,dt
\]

Integrating between two times:

\[
\Delta s=\int_{t_1}^{t_2}v(t)\,dt
\]

Thus, displacement is obtained by integrating velocity with respect to time.

Similarly:

\[
\Delta v=\int_{t_1}^{t_2}a(t)\,dt
\]

This means the change in velocity is obtained by integrating acceleration over time.

## 11. Differential Equations in Physics

A differential equation contains an unknown function and one or more of its derivatives.

Many physical laws are expressed using differential equations.

For example, Newton's second law:

\[
F=m\frac{d^2x}{dt^2}
\]

This relates force to the second derivative of position.

For a spring undergoing simple harmonic motion:

\[
F=-kx
\]

Using Newton's second law:

\[
m\frac{d^2x}{dt^2}=-kx
\]

Therefore:

\[
\frac{d^2x}{dt^2}+\frac{k}{m}x=0
\]

This differential equation describes ideal spring oscillations.

Differential equations become increasingly important in advanced mechanics, electromagnetism, waves and quantum physics.

## 12. Estimation and Mathematical Reasoning

Physics problems often require estimation and sensible approximations.

Useful strategies include:

- Identify the quantities that are known.
- Identify the quantity being calculated.
- Convert all values into consistent units.
- Select the relevant physical equation.
- Check whether the mathematical assumptions are valid.
- Estimate the expected order of magnitude.
- Check whether the final answer is physically reasonable.

A mathematically correct result can still be physically unreasonable if the model or assumptions are incorrect.

## Common Exam Traps

- Direct proportionality means y = kx, not y = k/x.
- Inverse-square relationships change by a factor of four when distance doubles.
- The sine component of a vector is not always vertical; it depends on how the angle is defined.
- Differentiation gives an instantaneous rate of change.
- Integration gives an accumulated quantity.
- The area under a graph has meaning determined by its axes.
- The gradient of a curved graph varies from point to point.
- The constant of integration must be included in indefinite integrals.
- A derivative of a constant is zero.
- Units must remain consistent when substituting into physical equations.

## Quiz

1. If kinetic energy is proportional to the square of speed, what happens to kinetic energy when speed doubles while mass remains constant?

- [ ] It doubles
- [ ] It triples
- [x] It becomes four times as large
- [ ] It becomes eight times as large

> Kinetic energy is K = (1/2)mv². Doubling speed multiplies kinetic energy by 2² = 4.

2. What is the derivative of x³ with respect to x?

- [ ] x²
- [ ] 2x
- [x] 3x²
- [ ] 3x

> Using the power rule, d(x^n)/dx = nx^(n-1). Therefore, d(x³)/dx = 3x².

3. What physical quantity is represented by the area under a velocity-time graph?

- [ ] Acceleration
- [ ] Speed
- [x] Displacement
- [ ] Force

> The area under a velocity-time graph is the integral of velocity with respect to time, which gives displacement.
