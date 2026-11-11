---
title: Linear Momentum and Collisions
level: intermediate
---

Linear momentum is a fundamental physical quantity that describes the motion of an object by combining its mass and velocity. It is especially useful in analysing collisions, explosions, recoil, and interactions between objects.

The law of conservation of momentum is one of the central conservation laws in classical mechanics.

## 1. Definition of Linear Momentum

Linear momentum is the product of the mass and velocity of an object.

\[
\vec p=m\vec v
\]

Where:
- p = linear momentum
- m = mass
- v = velocity

Momentum is a vector quantity because velocity is a vector.

Its SI unit is:

\[
kg\,m/s
\]

Its dimensional formula is:

\[
[M L T^{-1}]
\]

An object with greater mass or greater speed generally has greater momentum.

## 2. Momentum and Direction

Momentum has the same direction as velocity.

For one-dimensional motion, a direction convention must be selected.

For example:
- Rightward motion can be positive.
- Leftward motion can be negative.

A 5 kg object moving right at 4 m/s has:

\[
p=5\times4=20\,kg\,m/s
\]

If it moves left at the same speed, its momentum is:

\[
p=-20\,kg\,m/s
\]

The magnitude is unchanged, but the direction is reversed.

## 3. Impulse

Impulse measures the effect of a force acting over a time interval.

For a constant force:

\[
\vec J=\vec F\Delta t
\]

Impulse is also equal to the change in momentum:

\[
\vec J=\Delta\vec p
\]

\[
\vec J=m\vec v-m\vec u
\]

Its SI unit is N s, equivalent to kg m/s.

For a variable force:

\[
\vec J=\int_{t_1}^{t_2}\vec F(t)\,dt
\]

Impulse equals the signed area under a force-time graph.

## 4. Newton's Second Law in Momentum Form

Newton's second law can be expressed in terms of momentum:

\[
\vec F_{\text{net}}=\frac{d\vec p}{dt}
\]

For constant mass:

\[
\vec F_{\text{net}}=m\frac{d\vec v}{dt}
\]

Therefore:

\[
\vec F_{\text{net}}=m\vec a
\]

This demonstrates that the familiar form of Newton's second law is a special case of the more general momentum formulation.

## 5. Conservation of Linear Momentum

The total momentum of an isolated system remains constant if the net external force acting on the system is zero.

\[
\vec p_{\text{initial}}=\vec p_{\text{final}}
\]

For two interacting objects:

\[
m_1\vec u_1+m_2\vec u_2
=
m_1\vec v_1+m_2\vec v_2
\]

Internal forces may change the individual momenta, but the total momentum remains unchanged.

The law follows from Newton's third law because the internal forces between two interacting bodies are equal and opposite.

## 6. Types of Collisions

A collision is a short-duration interaction between objects during which large forces may act.

### Elastic Collision

In an elastic collision:
- Total momentum is conserved.
- Total kinetic energy is conserved.

\[
KE_i=KE_f
\]

An ideal collision between gas molecules is often modelled as elastic.

### Inelastic Collision

In an inelastic collision:
- Total momentum is conserved for an isolated system.
- Total kinetic energy is not conserved.

Some kinetic energy is transformed into heat, sound, deformation, or other forms.

### Perfectly Inelastic Collision

In a perfectly inelastic collision, the objects stick together after impact.

Their common final velocity is:

\[
v=\frac{m_1u_1+m_2u_2}{m_1+m_2}
\]

This collision produces the maximum loss of kinetic energy for a given isolated collision involving the same initial conditions.

## 7. Coefficient of Restitution

The coefficient of restitution measures how effectively relative speed is retained during a collision.

For a one-dimensional collision:

\[
e=\frac{\text{Relative speed of separation}}{\text{Relative speed of approach}}
\]

For two objects where object 1 approaches object 2:

\[
e=\frac{v_2-v_1}{u_1-u_2}
\]

Typical values:
- e = 1: perfectly elastic collision.
- 0 less than e less than 1: inelastic collision.
- e = 0: perfectly inelastic collision.

The coefficient is dimensionless.

## 8. One-Dimensional Elastic Collision

For an elastic collision between two objects, both momentum and kinetic energy are conserved.

The final velocities can be obtained using:

\[
v_1=
\frac{m_1-m_2}{m_1+m_2}u_1+
\frac{2m_2}{m_1+m_2}u_2
\]

\[
v_2=
\frac{2m_1}{m_1+m_2}u_1+
\frac{m_2-m_1}{m_1+m_2}u_2
\]

For equal masses, a one-dimensional elastic collision causes the objects to exchange velocities.

## 9. Explosion and Recoil

An explosion involves an object or system separating into multiple parts due to internal forces.

If the system initially has zero momentum:

\[
\sum m_i\vec v_i=0
\]

For a gun and bullet initially at rest:

\[
m_bv_b+m_gv_g=0
\]

The gun moves backward because the bullet moves forward.

This backward motion is called recoil.

## 10. Centre of Mass and Momentum

For a system of particles, the total momentum is equal to the total mass multiplied by the velocity of the centre of mass.

\[
\vec P=M\vec V_{CM}
\]

Where M is the total mass.

The centre of mass moves as if the entire mass of the system were concentrated there and the net external force acted on it.

\[
\vec F_{\text{external}}=M\vec a_{CM}
\]

## 11. Worked Numerical Examples

**Example 1: Momentum**

A 3 kg object moves at 6 m/s. Find its momentum.

\[
p=mv
\]

\[
p=3\times6
\]

\[
\boxed{p=18\,kg\,m/s}
\]

**Example 2: Impulse**

A force of 50 N acts on an object for 0.2 seconds.

\[
J=F\Delta t
\]

\[
J=50\times0.2
\]

\[
\boxed{J=10\,N\,s}
\]

**Example 3: Perfectly inelastic collision**

A 2 kg object moving at 6 m/s collides with a stationary 4 kg object. They stick together. Find their common velocity.

Using conservation of momentum:

\[
m_1u_1+m_2u_2=(m_1+m_2)v
\]

\[
2(6)+4(0)=6v
\]

\[
12=6v
\]

\[
\boxed{v=2\,m/s}
\]

**Example 4: Recoil**

A 0.02 kg bullet is fired forward at 300 m/s from a 3 kg gun initially at rest.

\[
m_bv_b+m_gv_g=0
\]

\[
0.02(300)+3v_g=0
\]

\[
6+3v_g=0
\]

\[
\boxed{v_g=-2\,m/s}
\]

The negative sign indicates backward motion.

## 12. Applications

- Airbags increase collision time and reduce average impact force.
- Rocket propulsion uses conservation of momentum.
- Recoil occurs when firearms discharge projectiles.
- Sports involve momentum transfer during impacts.
- Vehicle crash analysis uses impulse and momentum.
- Explosions and fragmentation are analysed using momentum conservation.

## Common Exam Traps

- Momentum is a vector; kinetic energy is a scalar.
- Momentum is conserved in an isolated collision even when kinetic energy is not.
- A perfectly inelastic collision does not conserve kinetic energy.
- Impulse is equal to change in momentum, not necessarily the final momentum.
- Direction must be included when solving one-dimensional collision problems.
- Conservation of momentum requires zero net external impulse, not necessarily zero internal forces.
- Negative velocity indicates direction, not negative mass or negative speed.

## Quiz

1. A 4 kg object moves at 5 m/s. Its momentum is:

- [ ] 0.8 kg m/s
- [ ] 9 kg m/s
- [x] 20 kg m/s
- [ ] 25 kg m/s

> Momentum = mass × velocity = 4 × 5 = 20 kg m/s.

2. Which quantity is conserved in every collision of an isolated system?

- [ ] Kinetic energy
- [x] Linear momentum
- [ ] Speed of each object
- [ ] Mechanical energy in every form

> Total linear momentum is conserved in an isolated system. Kinetic energy may be transformed into other forms during an inelastic collision.

3. A 2 kg object moving at 8 m/s sticks to a stationary 2 kg object. Their common final speed is:

- [ ] 8 m/s
- [x] 4 m/s
- [ ] 2 m/s
- [ ] 16 m/s

> Initial momentum = 2 × 8 = 16 kg m/s. Combined mass = 4 kg. Final velocity = 16/4 = 4 m/s.