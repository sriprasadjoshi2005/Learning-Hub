---
title: Work, Energy and Power
level: foundation
---

Work, energy and power are fundamental concepts used to describe how forces transfer energy and how physical systems perform activities. They provide an alternative to solving motion problems using Newton's laws alone.

The work-energy theorem connects the net work done on an object to its change in kinetic energy. The principle of conservation of energy is one of the most important ideas in all of physics.

## 1. Meaning of Work in Physics

In everyday language, work refers to any physical or mental effort. In physics, however, work has a precise mathematical definition.

Work is done when a force produces displacement and has a component along the direction of that displacement.

The work done by a constant force is:

\[
W=Fs\cos\theta
\]

Where:
- W = work done
- F = magnitude of force
- s = displacement
- theta = angle between force and displacement

The SI unit of work is the joule (J).

\[
1\,J=1\,N\,m
\]

One joule of work is done when a force of 1 newton produces a displacement of 1 metre in its direction.

## 2. Positive, Negative and Zero Work

The sign of work depends on the angle between force and displacement.

**Positive work:** When the force has a component in the direction of displacement.

\[
W>0 \quad \text{when } 0^\circ\leq\theta<90^\circ
\]

Example: Gravity does positive work when an object falls vertically downward.

**Negative work:** When the force acts partly opposite to displacement.

\[
W<0 \quad \text{when } 90^\circ<\theta\leq180^\circ
\]

Example: Friction does negative work when an object slides across a rough surface.

**Zero work:** Work is zero when there is no displacement or when the force is perpendicular to displacement.

\[
W=0
\]

Examples:
- A person holding a stationary object does no mechanical work on it.
- The centripetal force in uniform circular motion does zero work because it is perpendicular to instantaneous displacement.

## 3. Work Done by a Variable Force

When force changes with position, the simple equation W = Fs cos(theta) cannot always be used with a single force value.

For a force acting along one dimension:

\[
W=\int_{x_1}^{x_2}F(x)\,dx
\]

The work done is equal to the signed area under the force-displacement graph.

For a constant force, the graph is a rectangle.

\[
W=F(x_2-x_1)
\]

For a spring obeying Hooke's law:

\[
F=-kx
\]

The external work required to stretch or compress the spring from zero displacement to x is:

\[
W=\frac{1}{2}kx^2
\]

Here, k is the spring constant.

## 4. Kinetic Energy

Kinetic energy is the energy possessed by an object due to its motion.

\[
KE=\frac{1}{2}mv^2
\]

Where:
- m = mass in kilograms
- v = speed in metres per second

The SI unit is the joule.

Important observations:
- Kinetic energy is always non-negative.
- It increases linearly with mass.
- It increases with the square of speed.
- Doubling speed increases kinetic energy four times.
- Tripling speed increases kinetic energy nine times.

### Derivation of Kinetic Energy

From Newton's second law:

\[
F=ma
\]

Using the kinematic equation:

\[
v^2-u^2=2as
\]

Therefore:

\[
a=\frac{v^2-u^2}{2s}
\]

Work done:

\[
W=Fs=mas
\]

Substituting acceleration:

\[
W=m\left(\frac{v^2-u^2}{2s}\right)s
\]

\[
W=\frac{1}{2}mv^2-\frac{1}{2}mu^2
\]

Thus:

\[
W=\Delta KE
\]

## 5. Work-Energy Theorem

The work-energy theorem states that the net work done on an object equals its change in kinetic energy.

\[
W_{\text{net}}=KE_f-KE_i
\]

\[
W_{\text{net}}=\frac{1}{2}mv^2-\frac{1}{2}mu^2
\]

If net work is positive, kinetic energy increases.

If net work is negative, kinetic energy decreases.

If net work is zero, kinetic energy remains unchanged.

This theorem is particularly useful when calculating speeds without directly determining acceleration and time.

## 6. Potential Energy

Potential energy is energy associated with the position or configuration of a system.

### Gravitational Potential Energy Near Earth's Surface

For an object raised through a vertical height h:

\[
PE=mgh
\]

Where:
- m = mass
- g = acceleration due to gravity
- h = height relative to a chosen reference level

The zero level of gravitational potential energy can be selected conveniently.

### Elastic Potential Energy

A stretched or compressed spring stores elastic potential energy.

\[
PE_{\text{spring}}=\frac{1}{2}kx^2
\]

The energy depends on the square of the deformation.

## 7. Conservative and Non-Conservative Forces

A conservative force performs work that depends only on the initial and final positions, not on the path taken.

Examples:
- Gravitational force
- Electrostatic force
- Ideal spring force

For a conservative force, work over a closed path is zero.

\[
\oint \vec F\cdot d\vec r=0
\]

A non-conservative force has path-dependent work.

Examples:
- Friction
- Air resistance
- Viscous resistance

These forces commonly transform mechanical energy into thermal energy or other forms.

## 8. Conservation of Mechanical Energy

Mechanical energy is the sum of kinetic and potential energy.

\[
E=KE+PE
\]

When only conservative forces act:

\[
KE_i+PE_i=KE_f+PE_f
\]

For an object falling freely without air resistance:

\[
mgh+\frac{1}{2}mu^2
=
\frac{1}{2}mv^2
\]

If it starts from rest:

\[
mgh=\frac{1}{2}mv^2
\]

Therefore:

\[
v=\sqrt{2gh}
\]

Mechanical energy remains constant, although kinetic and potential energy continuously change.

## 9. Power

Power measures the rate at which work is performed or energy is transferred.

\[
P=\frac{W}{t}
\]

The SI unit is the watt (W).

\[
1\,W=1\,J/s
\]

Instantaneous power is:

\[
P=\frac{dW}{dt}
\]

For a constant force and velocity:

\[
P=\vec F\cdot\vec v
\]

\[
P=Fv\cos\theta
\]

Power is not the same as work. Two machines can perform the same work but require different amounts of time.

## 10. Efficiency

Efficiency measures how effectively input energy is converted into useful output energy.

\[
\eta=\frac{\text{Useful output energy}}{\text{Input energy}}\times100\%
\]

For power:

\[
\eta=\frac{\text{Useful output power}}{\text{Input power}}\times100\%
\]

Efficiency of a real energy-conversion system is generally less than 100% because some energy is transferred into unwanted forms, such as heat and sound.

## 11. Worked Numerical Examples

**Example 1: Work done by an inclined force**

A force of 20 N moves an object through 5 m. The angle between force and displacement is 60 degrees. Calculate work.

Given:

F = 20 N, s = 5 m, theta = 60 degrees.

\[
W=Fs\cos\theta
\]

\[
W=20\times5\times\cos60^\circ
\]

\[
W=100\times0.5
\]

\[
\boxed{W=50\,J}
\]

**Example 2: Kinetic energy**

Calculate the kinetic energy of a 4 kg object moving at 3 m/s.

\[
KE=\frac{1}{2}mv^2
\]

\[
KE=\frac{1}{2}\times4\times3^2
\]

\[
KE=2\times9
\]

\[
\boxed{KE=18\,J}
\]

**Example 3: Speed acquired during free fall**

An object falls from rest through a height of 20 m. Ignore air resistance and take g = 9.8 m/s².

Using conservation of mechanical energy:

\[
mgh=\frac{1}{2}mv^2
\]

Cancel mass:

\[
gh=\frac{v^2}{2}
\]

\[
v=\sqrt{2gh}
\]

\[
v=\sqrt{2\times9.8\times20}
\]

\[
\boxed{v\approx19.8\,m/s}
\]

**Example 4: Power**

A machine performs 6000 J of work in 20 seconds.

\[
P=\frac{W}{t}
\]

\[
P=\frac{6000}{20}
\]

\[
\boxed{P=300\,W}
\]

## 12. Applications

- Electric motors convert electrical energy into mechanical energy.
- Hydroelectric plants convert gravitational potential energy into electrical energy.
- Braking systems transform kinetic energy into thermal energy.
- Roller coasters demonstrate the exchange between kinetic and potential energy.
- Engines are compared using power and efficiency.
- Renewable energy systems rely on energy conversion and conservation.

## Common Exam Traps

- Work is zero when force is perpendicular to displacement.
- Negative work does not mean that the magnitude of work is negative; it indicates energy is removed from the object's kinetic energy through that force.
- Kinetic energy depends on speed squared, not speed.
- Gravitational potential energy near Earth's surface depends on the chosen reference height.
- The work-energy theorem uses net work, not the work done by only one force.
- Power measures the rate of energy transfer, not the total amount of energy.
- Mechanical energy is conserved only when non-conservative work is absent or properly accounted for.

## Quiz

1. A 10 N force acts on an object and moves it 4 m in the same direction. What is the work done?

- [ ] 2.5 J
- [x] 40 J
- [ ] 14 J
- [ ] 0 J

> Work = Fs = 10 × 4 = 40 J because the force and displacement are in the same direction.

2. If the speed of an object is doubled while its mass remains constant, its kinetic energy becomes:

- [ ] Twice its original value
- [ ] Three times its original value
- [x] Four times its original value
- [ ] Eight times its original value

> Kinetic energy is proportional to v squared. Doubling speed multiplies kinetic energy by 2 squared, which equals 4.

3. A machine performs 1200 J of work in 6 seconds. Its power is:

- [ ] 7200 W
- [ ] 120 W
- [x] 200 W
- [ ] 6 W

> Power = work/time = 1200/6 = 200 W.