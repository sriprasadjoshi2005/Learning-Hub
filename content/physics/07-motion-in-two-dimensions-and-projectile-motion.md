---
title: Motion in Two Dimensions and Projectile Motion
level: foundation
---

Motion in two dimensions occurs when an object moves in a plane rather than along a single straight line.

Examples include:

- A ball thrown into the air.
- A stone released from a moving vehicle.
- A car travelling around a curved road.
- A satellite moving in an orbital plane.
- Water flowing from a fountain.

Two-dimensional motion requires vector mathematics because position, velocity and acceleration may have components along two perpendicular directions.

Projectile motion is one of the most important applications of two-dimensional kinematics.

## 1. Position and Displacement in Two Dimensions

In a Cartesian coordinate system, the position of an object is represented by:

\[
\vec{r}=x\hat{i}+y\hat{j}
\]

Where:

- x is the horizontal coordinate.
- y is the vertical coordinate.
- \(\hat{i}\) is the unit vector along the x-axis.
- \(\hat{j}\) is the unit vector along the y-axis.

If an object moves from position:

\[
\vec{r}_1=x_1\hat{i}+y_1\hat{j}
\]

to:

\[
\vec{r}_2=x_2\hat{i}+y_2\hat{j}
\]

Its displacement is:

\[
\Delta\vec{r}
=(x_2-x_1)\hat{i}+(y_2-y_1)\hat{j}
\]

The magnitude of displacement is:

\[
|\Delta\vec{r}|=
\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

## 2. Velocity in Two Dimensions

Average velocity is:

\[
\vec{v}_{avg}=\frac{\Delta\vec{r}}{\Delta t}
\]

Instantaneous velocity is:

\[
\vec{v}=\frac{d\vec{r}}{dt}
\]

Since:

\[
\vec{r}=x\hat{i}+y\hat{j}
\]

Differentiating:

\[
\vec{v}=\frac{dx}{dt}\hat{i}
+\frac{dy}{dt}\hat{j}
\]

Therefore:

\[
\vec{v}=v_x\hat{i}+v_y\hat{j}
\]

The magnitude is:

\[
v=\sqrt{v_x^2+v_y^2}
\]

The direction relative to the positive x-axis is:

\[
\theta=\tan^{-1}\left(\frac{v_y}{v_x}\right)
\]

The correct quadrant must be considered when determining the direction.

## 3. Acceleration in Two Dimensions

Acceleration is the rate of change of velocity.

\[
\vec{a}=\frac{d\vec{v}}{dt}
\]

Therefore:

\[
\vec{a}=a_x\hat{i}+a_y\hat{j}
\]

Where:

\[
a_x=\frac{dv_x}{dt}
\]

\[
a_y=\frac{dv_y}{dt}
\]

The magnitude is:

\[
a=\sqrt{a_x^2+a_y^2}
\]

In two-dimensional motion, acceleration may change the speed, the direction of velocity, or both.

## 4. Independence of Perpendicular Motion

A central principle of two-dimensional kinematics is that motion along perpendicular axes can be analysed independently.

For example, consider a projectile launched horizontally or at an angle.

Ignoring air resistance:

- Horizontal acceleration is zero.
- Vertical acceleration is due to gravity.

Therefore:

\[
a_x=0
\]

\[
a_y=-g
\]

if upward is chosen as positive.

Horizontal and vertical motions occur simultaneously, but their equations can be solved separately using the same time variable.

## 5. Projectile Motion

Projectile motion occurs when an object is launched into the air and subsequently moves under the influence of gravity alone.

Examples include:

- A ball thrown at an angle.
- A stone projected from a cliff.
- A football kicked into the air.
- A water jet emerging from a nozzle.

Assumptions of ideal projectile motion:

1. Air resistance is neglected.
2. Gravitational acceleration is constant.
3. Earth's curvature is negligible over the trajectory.
4. The projectile is treated as a point object.

Under these assumptions, the trajectory is parabolic.

## 6. Initial Velocity Components

Suppose a projectile is launched with initial speed u at an angle θ above the horizontal.

The initial velocity has two components.

Horizontal:

\[
u_x=u\cos\theta
\]

Vertical:

\[
u_y=u\sin\theta
\]

These components determine the subsequent motion.

Horizontal velocity remains constant:

\[
v_x=u\cos\theta
\]

Vertical velocity changes due to gravity:

\[
v_y=u\sin\theta-gt
\]

The signs assume upward is positive.

## 7. Horizontal Motion of a Projectile

Since horizontal acceleration is zero:

\[
a_x=0
\]

The horizontal displacement after time t is:

\[
x=u_x t
\]

Therefore:

\[
x=u\cos\theta\ t
\]

Horizontal velocity remains:

\[
v_x=u\cos\theta
\]

This means the projectile covers equal horizontal distances in equal time intervals under ideal conditions.

## 8. Vertical Motion of a Projectile

Vertical motion is uniformly accelerated motion with acceleration -g.

Vertical displacement:

\[
y=u\sin\theta\ t-\frac12gt^2
\]

Vertical velocity:

\[
v_y=u\sin\theta-gt
\]

At the highest point of the trajectory:

\[
v_y=0
\]

However, horizontal velocity remains non-zero unless the projectile was launched vertically.

The total velocity at the highest point is therefore horizontal.

## 9. Equation of the Projectile Trajectory

The horizontal equation is:

\[
x=u\cos\theta\ t
\]

Therefore:

\[
t=\frac{x}{u\cos\theta}
\]

The vertical equation is:

\[
y=u\sin\theta\ t-\frac12gt^2
\]

Substituting for time:

\[
y=x\tan\theta-
\frac{gx^2}{2u^2\cos^2\theta}
\]

This is the equation of a parabola.

Therefore, the ideal projectile trajectory is parabolic.

## 10. Time of Flight

Time of flight is the total time taken by a projectile to return to its launch height.

At the final point, vertical displacement is zero:

\[
0=u\sin\theta\ T-\frac12gT^2
\]

Taking the non-zero solution:

\[
T=\frac{2u\sin\theta}{g}
\]

This is valid when launch and landing heights are equal.

Time of flight depends on:

- Initial speed.
- Launch angle.
- Gravitational acceleration.

## 11. Maximum Height

Maximum height is reached when vertical velocity becomes zero.

\[
v_y=u\sin\theta-gt
\]

At the highest point:

\[
v_y=0
\]

Therefore:

\[
t=\frac{u\sin\theta}{g}
\]

Using:

\[
H=u\sin\theta\ t-\frac12gt^2
\]

Substituting:

\[
H=\frac{u^2\sin^2\theta}{2g}
\]

This is the maximum vertical height above the launch point.

## 12. Horizontal Range

Horizontal range is the horizontal distance covered when the projectile returns to its launch height.

\[
R=u\cos\theta\ T
\]

Substituting time of flight:

\[
R=u\cos\theta
\left(\frac{2u\sin\theta}{g}\right)
\]

Using:

\[
2\sin\theta\cos\theta=\sin2\theta
\]

Therefore:

\[
R=\frac{u^2\sin2\theta}{g}
\]

### Maximum range

For fixed initial speed and equal launch and landing heights:

\[
R_{max}=\frac{u^2}{g}
\]

This occurs when:

\[
\sin2\theta=1
\]

Therefore:

\[
2\theta=90^\circ
\]

\[
\theta=45^\circ
\]

The maximum horizontal range occurs at a launch angle of 45 degrees under ideal conditions.

## 13. Complementary Projection Angles

Two projectiles launched with the same initial speed at complementary angles have equal horizontal ranges, provided their launch and landing heights are equal.

For angles θ and (90° - θ):

\[
R_1=\frac{u^2\sin2\theta}{g}
\]

\[
R_2=
\frac{u^2\sin(180^\circ-2\theta)}{g}
\]

Since:

\[
\sin(180^\circ-2\theta)=\sin2\theta
\]

Therefore:

\[
R_1=R_2
\]

However, their maximum heights and times of flight are generally different.

## 14. Horizontal Projection from a Height

Consider an object projected horizontally from a height h with initial horizontal velocity u.

Initial vertical velocity is zero.

Vertical displacement:

\[
h=\frac12gt^2
\]

Therefore, time to reach the ground:

\[
t=\sqrt{\frac{2h}{g}}
\]

Horizontal range:

\[
R=ut
\]

Therefore:

\[
R=u\sqrt{\frac{2h}{g}}
\]

The horizontal and vertical motions are independent.

## 15. Solved Numerical Problems

### Example 1: Projectile launched at an angle

A projectile is launched at 20 m/s at 30 degrees above the horizontal. Take g = 10 m/s².

Find its time of flight, maximum height and horizontal range.

Given:

\[
u=20,\quad\theta=30^\circ,\quad g=10
\]

Time of flight:

\[
T=\frac{2u\sin\theta}{g}
\]

\[
T=\frac{2(20)(0.5)}{10}
\]

\[
T=2\ \text{s}
\]

Maximum height:

\[
H=\frac{u^2\sin^2\theta}{2g}
\]

\[
H=\frac{400(0.25)}{20}
\]

\[
H=5\ \text{m}
\]

Horizontal range:

\[
R=\frac{u^2\sin2\theta}{g}
\]

\[
R=\frac{400\sin60^\circ}{10}
\]

\[
R=20\sqrt{3}\ \text{m}
\]

\[
R\approx34.64\ \text{m}
\]

### Example 2: Horizontal projection

A stone is projected horizontally at 15 m/s from a cliff 20 m high. Take g = 10 m/s².

Find the time taken to reach the ground and horizontal distance travelled.

Vertical motion:

\[
h=\frac12gt^2
\]

\[
20=5t^2
\]

\[
t=2\ \text{s}
\]

Horizontal distance:

\[
R=ut
\]

\[
R=15(2)
\]

\[
R=30\ \text{m}
\]

## 16. Relative Motion in Two Dimensions

Relative motion describes the motion of one object as observed from another moving object.

The relative velocity of A with respect to B is:

\[
\vec{v}_{AB}=\vec{v}_A-\vec{v}_B
\]

For example, two vehicles travelling in the same direction have relative speed equal to the difference between their speeds.

If they travel in opposite directions, their relative speed is the sum of their speeds.

Two-dimensional relative motion will be explored further in the next lesson.

## Common Exam Traps

- Horizontal and vertical motions must use the same elapsed time.
- Horizontal acceleration is zero only when air resistance is neglected and no other horizontal force acts.
- At the highest point, vertical velocity is zero but acceleration is still downward.
- Horizontal velocity remains constant during ideal projectile motion.
- The 45-degree maximum-range result assumes equal launch and landing heights.
- Complementary angles produce equal ranges only under the appropriate equal-height and equal-speed conditions.
- The time-of-flight formula for an angled projectile assumes the projectile lands at its launch height.
- A projectile launched horizontally has zero initial vertical velocity.
- The trajectory is parabolic only under the standard constant-gravity, negligible-air-resistance model.

## Quiz

1. A projectile is launched at 20 m/s at 30 degrees above the horizontal. What is its initial vertical velocity component?

- [ ] 20 m/s
- [x] 10 m/s
- [ ] 10sqrt(3) m/s
- [ ] 5 m/s

> The vertical component is u sin(theta) = 20 sin(30 degrees) = 20 × 0.5 = 10 m/s.

2. At the highest point of ideal projectile motion, which statement is correct?

- [ ] Both horizontal and vertical velocities are zero.
- [ ] Acceleration becomes zero.
- [x] Vertical velocity is zero while acceleration remains downward.
- [ ] Horizontal velocity reverses direction.

> At maximum height, the vertical component of velocity becomes zero. Gravity continues acting downward, so acceleration remains equal to g downward.

3. For a projectile launched and landing at the same height, at what angle is horizontal range maximum for a fixed initial speed?

- [ ] 30 degrees
- [ ] 60 degrees
- [x] 45 degrees
- [ ] 90 degrees

> Range is R = (u² sin(2theta))/g. Its maximum occurs when sin(2theta) = 1, giving theta = 45 degrees.
