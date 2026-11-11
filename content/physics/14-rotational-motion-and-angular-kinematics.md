---
title: Rotational Motion and Angular Kinematics
level: intermediate
---

Rotational motion describes the movement of an object around an axis. It is an essential part of mechanics and is used to understand wheels, gears, turbines, motors, planets, and rotating machinery.

Many rotational quantities have direct analogies with linear motion. However, rotation introduces angular displacement, angular velocity, angular acceleration, and torque.

## 1. Angular Displacement

Angular displacement describes the change in angular position of an object.

It is represented by theta.

\[
\Delta\theta=\theta_f-\theta_i
\]

The SI unit is the radian (rad).

One complete revolution corresponds to:

\[
2\pi\,rad=360^\circ
\]

Therefore:

\[
1\,rad=\frac{180^\circ}{\pi}
\]

For a point moving along a circular path:

\[
s=r\theta
\]

Where:
- s = arc length
- r = radius
- theta = angular displacement in radians

## 2. Angular Velocity

Angular velocity measures the rate of change of angular displacement.

Average angular velocity:

\[
\omega_{\text{avg}}=\frac{\Delta\theta}{\Delta t}
\]

Instantaneous angular velocity:

\[
\omega=\frac{d\theta}{dt}
\]

The SI unit is rad/s.

For uniform circular motion:

\[
\omega=\frac{2\pi}{T}
\]

Where T is the time period.

Since frequency is the number of revolutions per second:

\[
f=\frac{1}{T}
\]

Therefore:

\[
\omega=2\pi f
\]

## 3. Angular Acceleration

Angular acceleration measures the rate of change of angular velocity.

\[
\alpha_{\text{avg}}=\frac{\Delta\omega}{\Delta t}
\]

Instantaneous angular acceleration:

\[
\alpha=\frac{d\omega}{dt}
\]

The SI unit is rad/s².

Positive or negative angular acceleration depends on the chosen rotational direction and whether angular velocity increases or decreases algebraically.

## 4. Equations of Rotational Motion

For constant angular acceleration, rotational motion follows equations analogous to linear kinematics.

\[
\omega=\omega_0+\alpha t
\]

\[
\theta=\omega_0t+\frac{1}{2}\alpha t^2
\]

\[
\omega^2=\omega_0^2+2\alpha\theta
\]

\[
\theta=\frac{\omega_0+\omega}{2}t
\]

Where:
- omega0 = initial angular velocity
- omega = final angular velocity
- alpha = angular acceleration
- theta = angular displacement

These equations apply only when angular acceleration is constant.

## 5. Relationship Between Linear and Angular Quantities

For a point at distance r from the axis:

**Tangential velocity**

\[
v=r\omega
\]

**Tangential acceleration**

\[
a_t=r\alpha
\]

**Centripetal acceleration**

\[
a_c=r\omega^2=\frac{v^2}{r}
\]

Tangential acceleration changes the magnitude of velocity, while centripetal acceleration changes its direction.

## 6. Torque

Torque is the rotational effect of a force about an axis.

\[
\vec\tau=\vec r\times\vec F
\]

Its magnitude is:

\[
\tau=rF\sin\theta
\]

Where theta is the angle between the position vector and the force.

The SI unit is N m.

Although torque and work share the same dimensional units, they represent different physical quantities.

Torque depends on:
- Force magnitude.
- Perpendicular distance from the axis.
- Angle at which the force acts.

The perpendicular distance from the axis to the force's line of action is called the moment arm.

## 7. Moment of Inertia

Moment of inertia describes an object's resistance to changes in rotational motion.

For discrete particles:

\[
I=\sum m_ir_i^2
\]

For a continuous body:

\[
I=\int r^2\,dm
\]

The SI unit is kg m².

Unlike mass in simple translational motion, moment of inertia depends on how mass is distributed relative to the axis of rotation.

Mass farther from the axis contributes more strongly because distance is squared.

## 8. Common Moments of Inertia

| Object and axis | Moment of inertia |
|---|---|
| Point mass at distance r | mr² |
| Thin ring about central perpendicular axis | MR² |
| Solid disc about central axis | (1/2)MR² |
| Solid cylinder about central axis | (1/2)MR² |
| Solid sphere about diameter | (2/5)MR² |
| Thin spherical shell about diameter | (2/3)MR² |
| Uniform rod about centre, perpendicular to length | (1/12)ML² |
| Uniform rod about one end, perpendicular to length | (1/3)ML² |

These expressions assume idealised uniform objects and the stated axes.

## 9. Newton's Second Law for Rotation

The rotational equivalent of Newton's second law is:

\[
\tau_{\text{net}}=I\alpha
\]

This applies to rotation about a fixed axis when the moment of inertia is constant.

A greater net torque produces greater angular acceleration.

A greater moment of inertia produces smaller angular acceleration for the same torque.

## 10. Angular Momentum

Angular momentum is the rotational analogue of linear momentum.

For a rigid body rotating about a fixed principal axis:

\[
L=I\omega
\]

The SI unit is kg m²/s.

The more general definition for a particle is:

\[
\vec L=\vec r\times\vec p
\]

For a system, angular momentum is the vector sum of the angular momenta of its particles.

## 11. Conservation of Angular Momentum

If the net external torque on a system is zero, its total angular momentum remains constant.

\[
L_i=L_f
\]

For a rotating body with changing moment of inertia:

\[
I_i\omega_i=I_f\omega_f
\]

Example: A spinning person rotates faster when pulling their arms closer to the body because their moment of inertia decreases.

## 12. Rotational Kinetic Energy

A rotating rigid body possesses rotational kinetic energy.

\[
KE_{\text{rot}}=\frac{1}{2}I\omega^2
\]

For an object undergoing both translation and rotation:

\[
KE_{\text{total}}=
\frac{1}{2}Mv_{CM}^2+\frac{1}{2}I_{CM}\omega^2
\]

This expression separates the kinetic energy of centre-of-mass motion from the energy of rotation about the centre of mass.

## 13. Rolling Motion Without Slipping

For pure rolling:

\[
v_{CM}=R\omega
\]

And:

\[
a_{CM}=R\alpha
\]

For a rolling object:

\[
KE=\frac{1}{2}Mv_{CM}^2+\frac{1}{2}I_{CM}\omega^2
\]

Static friction can provide the torque required for rolling without slipping.

In ideal pure rolling on a stationary surface, the point of contact has zero instantaneous velocity relative to the surface.

## 14. Worked Numerical Examples

**Example 1: Angular velocity**

A wheel completes 10 revolutions in 5 seconds.

\[
f=\frac{10}{5}=2\,Hz
\]

\[
\omega=2\pi f
\]

\[
\boxed{\omega=4\pi\,rad/s}
\]

**Example 2: Tangential speed**

A point on a wheel of radius 0.5 m rotates at 4 rad/s.

\[
v=r\omega
\]

\[
v=0.5\times4
\]

\[
\boxed{v=2\,m/s}
\]

**Example 3: Torque**

A perpendicular force of 20 N acts at a distance of 0.4 m from an axis.

\[
\tau=rF
\]

\[
\tau=0.4\times20
\]

\[
\boxed{\tau=8\,N\,m}
\]

**Example 4: Rotational kinetic energy**

A body has a moment of inertia of 2 kg m² and angular velocity of 3 rad/s.

\[
KE=\frac{1}{2}I\omega^2
\]

\[
KE=\frac{1}{2}\times2\times9
\]

\[
\boxed{KE=9\,J}
\]

## 15. Applications

- Wheels and gears in vehicles.
- Turbines and electric motors.
- Rotating machinery.
- Planetary and satellite motion.
- Gyroscopes and stabilisation systems.
- Sports involving spinning objects.
- Flywheels used for energy storage.

## Common Exam Traps

- Angular displacement should be in radians when using s = r theta.
- Angular velocity is measured in rad/s, not revolutions per second.
- Moment of inertia depends on the selected axis.
- Torque is not the same as work, even though both use N m.
- Centripetal acceleration and tangential acceleration have different roles.
- Angular momentum is conserved only when net external torque is zero.
- Rolling without slipping requires v = R omega.

## Quiz

1. A wheel rotates through 2 complete revolutions. Its angular displacement magnitude is:

- [ ] pi rad
- [ ] 2 rad
- [x] 4 pi rad
- [ ] 360 rad

> One revolution is 2 pi radians. Two revolutions correspond to 4 pi radians.

2. A point is 0.5 m from the axis of a wheel rotating at 6 rad/s. Its tangential speed is:

- [ ] 12 m/s
- [x] 3 m/s
- [ ] 6.5 m/s
- [ ] 0.083 m/s

> Tangential speed = r omega = 0.5 × 6 = 3 m/s.

3. If the net external torque on a system is zero, which quantity is conserved?

- [ ] Angular acceleration
- [ ] Moment of inertia
- [x] Angular momentum
- [ ] Angular velocity in every situation

> Zero net external torque implies conservation of total angular momentum. Angular velocity can change if the moment of inertia changes.