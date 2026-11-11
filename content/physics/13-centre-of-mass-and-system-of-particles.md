---
title: Centre of Mass and Systems of Particles
level: intermediate
---

Many physical systems contain multiple particles or extended bodies. Instead of analysing every particle independently, physics often uses the concept of the centre of mass.

The centre of mass provides a convenient way to describe the overall translational motion of a system. It is important in collision analysis, rotational mechanics, planetary motion, and the study of extended objects.

## 1. What Is the Centre of Mass?

The centre of mass is the weighted average position of the mass distribution of a system.

It is the point that represents the average position of the system's mass.

For a system of particles:

\[
\vec r_{CM}=
\frac{\sum m_i\vec r_i}{\sum m_i}
\]

Where:
- m_i = mass of each particle
- r_i = position vector of each particle
- M = total mass

\[
M=\sum m_i
\]

The centre of mass need not be located inside the physical material of an object.

For example, the centre of mass of a uniform ring is at its geometrical centre, which contains no material.

## 2. Centre of Mass in One Dimension

For particles positioned along the x-axis:

\[
x_{CM}=\frac{\sum m_ix_i}{\sum m_i}
\]

For two particles:

\[
x_{CM}=\frac{m_1x_1+m_2x_2}{m_1+m_2}
\]

The centre of mass lies closer to the heavier object.

### Example

Two particles of masses 2 kg and 6 kg are located at x = 0 m and x = 4 m.

\[
x_{CM}=\frac{2(0)+6(4)}{2+6}
\]

\[
x_{CM}=\frac{24}{8}
\]

\[
\boxed{x_{CM}=3\,m}
\]

The centre of mass is closer to the 6 kg particle.

## 3. Centre of Mass in Two and Three Dimensions

In two dimensions:

\[
x_{CM}=\frac{\sum m_ix_i}{M}
\]

\[
y_{CM}=\frac{\sum m_iy_i}{M}
\]

In three dimensions:

\[
z_{CM}=\frac{\sum m_iz_i}{M}
\]

The complete position vector is:

\[
\vec r_{CM}=x_{CM}\hat i+y_{CM}\hat j+z_{CM}\hat k
\]

Each coordinate is calculated independently using the same mass-weighted average principle.

## 4. Centre of Mass of Continuous Bodies

For continuous mass distributions, summations are replaced by integration.

\[
\vec r_{CM}=\frac{1}{M}\int\vec r\,dm
\]

In one dimension:

\[
x_{CM}=\frac{1}{M}\int x\,dm
\]

For a uniform rod of length L and mass M, the centre of mass is at its midpoint:

\[
x_{CM}=\frac{L}{2}
\]

For uniform symmetric objects, symmetry often makes the centre of mass easy to determine.

Examples:
- Uniform disc: geometric centre.
- Uniform sphere: geometric centre.
- Uniform rectangular plate: intersection of its diagonals.
- Uniform circular ring: centre of the ring.

## 5. Motion of the Centre of Mass

The velocity of the centre of mass is:

\[
\vec V_{CM}=\frac{d\vec r_{CM}}{dt}
\]

For a system of particles:

\[
\vec V_{CM}=\frac{\sum m_i\vec v_i}{M}
\]

The total momentum is:

\[
\vec P=M\vec V_{CM}
\]

The acceleration of the centre of mass is:

\[
\vec a_{CM}=\frac{\sum m_i\vec a_i}{M}
\]

Using Newton's second law:

\[
\vec F_{\text{external}}=M\vec a_{CM}
\]

This equation shows that internal forces cannot change the motion of the centre of mass of an isolated system.

## 6. Internal and External Forces

Internal forces act between particles belonging to the same system.

External forces are exerted on the system by objects outside it.

According to Newton's third law, internal forces occur in equal and opposite pairs.

Therefore, the total internal force of the system cancels when considering its overall motion.

Only the resultant external force determines the acceleration of the centre of mass.

## 7. Centre of Mass and Explosions

Suppose an object initially at rest explodes into several fragments.

If external forces are negligible during the explosion:

\[
\vec P_i=\vec P_f
\]

Since initial momentum is zero:

\[
\sum m_i\vec v_i=0
\]

The fragments move in different directions, but their combined centre of mass remains at rest.

This explains why the centre of mass follows its original trajectory even when the object breaks apart.

## 8. Centre of Mass and Collisions

During a collision, the objects exert large internal forces on one another.

However, if external impulses are negligible, the centre-of-mass velocity remains constant.

\[
\vec V_{CM}=\frac{\vec P}{M}
\]

This simplifies complicated collision problems because the centre of mass can be treated as a single system-level quantity.

## 9. Centre of Mass and Stability

The position of the centre of mass influences the stability of an object.

An object is more likely to remain stable when:
- Its centre of mass is relatively low.
- Its base of support is wide.
- The vertical projection of its centre of mass remains within its support area.

When the vertical projection falls outside the base of support, the object tends to topple.

Examples include:
- Racing cars designed with low centres of mass.
- Wide-bottomed structures.
- Gymnasts adjusting body positions to maintain balance.

## 10. Centre of Mass Versus Centre of Gravity

The centre of mass is determined by the distribution of mass.

The centre of gravity is the point through which the resultant gravitational force effectively acts.

In a uniform gravitational field, the centre of gravity coincides with the centre of mass.

In a non-uniform gravitational field, they may differ.

## 11. Worked Numerical Examples

**Example 1: Two-particle system**

A 3 kg particle is at x = 2 m, and a 5 kg particle is at x = 6 m.

\[
x_{CM}=\frac{3(2)+5(6)}{3+5}
\]

\[
x_{CM}=\frac{6+30}{8}
\]

\[
\boxed{x_{CM}=4.5\,m}
\]

**Example 2: Two-dimensional system**

A 2 kg particle is at (0, 0), and a 3 kg particle is at (4, 2).

\[
x_{CM}=\frac{2(0)+3(4)}{5}=2.4\,m
\]

\[
y_{CM}=\frac{2(0)+3(2)}{5}=1.2\,m
\]

Therefore:

\[
\boxed{(x_{CM},y_{CM})=(2.4,1.2)}
\]

**Example 3: Centre-of-mass velocity**

A 2 kg object moves at 5 m/s rightward, while a 3 kg object moves at 1 m/s leftward.

Taking rightward as positive:

\[
V_{CM}=\frac{2(5)+3(-1)}{2+3}
\]

\[
V_{CM}=\frac{10-3}{5}
\]

\[
\boxed{V_{CM}=1.4\,m/s}
\]

The centre of mass moves rightward.

## 12. Applications

- Collision and explosion analysis.
- Spacecraft and planetary motion.
- Balance and stability of structures.
- Human body movement and sports biomechanics.
- Robotic motion planning.
- Analysis of extended mechanical systems.

## Common Exam Traps

- The centre of mass is a mass-weighted average, not always the geometric centre.
- The centre of mass can lie outside an object's material.
- Internal forces cannot change the total momentum of an isolated system.
- Centre of mass and centre of gravity coincide only under a uniform gravitational field.
- Coordinates must be calculated using consistent reference axes.
- Direction must be included when calculating centre-of-mass velocity.

## Quiz

1. Two masses of 2 kg and 6 kg are placed at x = 0 m and x = 4 m. The centre of mass is located at:

- [ ] 1 m
- [ ] 2 m
- [x] 3 m
- [ ] 4 m

> xCM = [2(0) + 6(4)]/8 = 3 m.

2. Which force determines the acceleration of the centre of mass of a system?

- [ ] Total internal force
- [x] Net external force
- [ ] Gravitational force in every possible situation
- [ ] Friction alone

> The equation Fexternal = M aCM shows that the net external force determines centre-of-mass acceleration.

3. The centre of mass of a uniform circular ring is:

- [ ] On its circumference
- [ ] At an arbitrary point
- [x] At its geometrical centre
- [ ] Outside the plane of the ring

> Symmetry places the centre of mass at the geometrical centre of a uniform ring.