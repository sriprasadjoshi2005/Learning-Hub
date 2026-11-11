---
title: Motion in One Dimension
level: foundation
---

Mechanics is the branch of physics that studies the motion of objects and the forces responsible for changing their motion.

Kinematics is the part of mechanics that describes motion without initially considering the forces causing it.

Motion in one dimension occurs when an object moves along a straight line. Examples include a car travelling along a straight road, a stone falling vertically and a train moving along a straight track.

This lesson develops the fundamental quantities used to describe motion, including position, distance, displacement, speed, velocity and acceleration.

## 1. Rest and Motion

An object is said to be at rest if its position does not change with time relative to a chosen reference frame.

An object is said to be in motion if its position changes with time relative to that reference frame.

Motion and rest are relative concepts.

For example, a passenger sitting inside a moving train is at rest relative to the train but is moving relative to an observer standing beside the railway track.

Therefore, describing motion requires specifying a reference frame.

## 2. Position and Reference Point

Position describes the location of an object relative to an origin.

In one-dimensional motion, a coordinate axis is commonly selected.

For example:

- Positive direction: Right.
- Negative direction: Left.
- Origin: x = 0.

An object located 5 m to the right of the origin has:

\[
x=+5\ \text{m}
\]

An object located 3 m to the left has:

\[
x=-3\ \text{m}
\]

The sign indicates direction, while the magnitude indicates distance from the origin.

## 3. Distance and Displacement

Distance is the total length of the actual path travelled by an object.

Displacement is the change in position.

\[
\Delta x=x_f-x_i
\]

Where:

- \(x_f\) is final position.
- \(x_i\) is initial position.

Distance is a scalar quantity, whereas displacement is a vector quantity.

### Example

A person walks 10 m east and then 4 m west.

Total distance:

\[
10+4=14\ \text{m}
\]

Displacement:

\[
10-4=6\ \text{m east}
\]

Distance is 14 m, while displacement is 6 m east.

### Important properties

- Distance is always non-negative.
- Displacement can be positive, negative or zero.
- Distance is always greater than or equal to the magnitude of displacement.
- Displacement depends only on initial and final positions.
- Distance depends on the actual path followed.

If an object completes a round trip and returns to its starting point, its displacement is zero even though the distance travelled is non-zero.

## 4. Speed

Speed is the rate at which distance is covered.

Average speed is:

\[
\text{Average speed}=
\frac{\text{Total distance}}{\text{Total time}}
\]

SI unit:

\[
\text{m/s}
\]

Speed is a scalar quantity.

### Example

A vehicle travels 150 m in 10 s.

\[
\text{Average speed}=\frac{150}{10}
\]

\[
=15\ \text{m/s}
\]

### Instantaneous speed

Instantaneous speed is the speed of an object at a particular instant.

A speedometer displays the approximate instantaneous speed of a vehicle.

## 5. Velocity

Velocity is the rate of change of displacement with time.

Average velocity:

\[
v_{\text{avg}}=\frac{\Delta x}{\Delta t}
\]

Instantaneous velocity:

\[
v=\frac{dx}{dt}
\]

Velocity is a vector quantity.

Its sign indicates the direction of motion relative to the selected coordinate axis.

### Example

An object moves from x = 2 m to x = 12 m in 5 s.

Displacement:

\[
\Delta x=12-2=10\ \text{m}
\]

Average velocity:

\[
v_{\text{avg}}=\frac{10}{5}
\]

\[
=2\ \text{m/s}
\]

The positive sign indicates motion in the positive direction.

### Speed and velocity comparison

| Speed | Velocity |
|---|---|
| Scalar quantity | Vector quantity |
| Based on distance | Based on displacement |
| Cannot be negative | Can be positive, negative or zero in 1D |
| Describes how fast an object moves | Describes how fast and in which direction it moves |

## 6. Average and Instantaneous Velocity

Average velocity describes displacement over a time interval.

Instantaneous velocity describes velocity at a specific moment.

Mathematically:

\[
v_{\text{avg}}=\frac{\Delta x}{\Delta t}
\]

\[
v=\lim_{\Delta t\to0}\frac{\Delta x}{\Delta t}
\]

The second expression is the derivative of position with respect to time.

An object's instantaneous velocity can change even if its average velocity over a particular interval remains constant.

## 7. Acceleration

Acceleration is the rate of change of velocity with time.

Average acceleration:

\[
a_{\text{avg}}=\frac{v-u}{t}
\]

Where:

- u = initial velocity.
- v = final velocity.
- t = elapsed time.

Instantaneous acceleration:

\[
a=\frac{dv}{dt}
\]

Since velocity has dimensions [LT^-1] and time has dimensions [T]:

\[
[a]=[LT^{-2}]
\]

SI unit:

\[
\text{m/s}^2
\]

### Example

A car increases its velocity from 10 m/s to 30 m/s in 5 s.

\[
a=\frac{30-10}{5}
\]

\[
a=4\ \text{m/s}^2
\]

This means velocity increases by 4 m/s every second, assuming constant acceleration.

## 8. Positive and Negative Acceleration

Positive acceleration means acceleration acts in the positive direction of the chosen coordinate axis.

Negative acceleration means acceleration acts in the negative direction.

Negative acceleration does not always mean that an object is slowing down.

Consider the relationship between velocity and acceleration:

| Velocity | Acceleration | Behaviour |
|---|---|---|
| Positive | Positive | Speed increases |
| Positive | Negative | Speed decreases |
| Negative | Negative | Speed increases |
| Negative | Positive | Speed decreases |

An object speeds up when velocity and acceleration have the same direction.

It slows down when velocity and acceleration have opposite directions.

The term retardation is commonly used for acceleration opposite to the direction of velocity.

## 9. Uniform and Non-Uniform Motion

**Uniform motion:**

An object undergoes uniform motion when it covers equal displacements in equal intervals of time along a straight line.

Its velocity remains constant.

\[
a=0
\]

**Non-uniform motion:**

An object undergoes non-uniform motion when its velocity changes with time.

This may occur due to a change in speed, direction or both.

Acceleration is non-zero when velocity changes.

## 10. Equations of Motion for Constant Acceleration

For motion in one dimension with constant acceleration, three important equations are used.

Let:

- u = initial velocity.
- v = final velocity.
- a = constant acceleration.
- t = elapsed time.
- s = displacement.

### First equation

\[
v=u+at
\]

Derivation:

Acceleration is:

\[
a=\frac{v-u}{t}
\]

Rearranging:

\[
v=u+at
\]

### Second equation

\[
s=ut+\frac12at^2
\]

For constant acceleration, average velocity is:

\[
v_{\text{avg}}=\frac{u+v}{2}
\]

Therefore:

\[
s=\frac{u+v}{2}t
\]

Substituting \(v=u+at\):

\[
s=\frac{u+(u+at)}{2}t
\]

\[
s=ut+\frac12at^2
\]

### Third equation

\[
v^2=u^2+2as
\]

Using:

\[
s=\frac{u+v}{2}t
\]

and:

\[
t=\frac{v-u}{a}
\]

Substituting and simplifying gives:

\[
v^2-u^2=2as
\]

Therefore:

\[
v^2=u^2+2as
\]

### Important condition

These equations are valid when acceleration remains constant.

They should not be applied directly to arbitrary non-uniform acceleration without further analysis.

## 11. Solved Numerical Problems

### Example 1: Finding final velocity

A vehicle starts with an initial velocity of 5 m/s and accelerates uniformly at 3 m/s² for 4 s.

Find its final velocity.

Given:

\[
u=5\ \text{m/s}
\]

\[
a=3\ \text{m/s}^2
\]

\[
t=4\ \text{s}
\]

Using:

\[
v=u+at
\]

\[
v=5+(3)(4)
\]

\[
v=17\ \text{m/s}
\]

### Example 2: Finding displacement

A body starts from rest and accelerates at 2 m/s² for 6 s.

Given:

\[
u=0,\quad a=2,\quad t=6
\]

Using:

\[
s=ut+\frac12at^2
\]

\[
s=0+\frac12(2)(6^2)
\]

\[
s=36\ \text{m}
\]

### Example 3: Finding acceleration without time

A car increases its speed from 10 m/s to 20 m/s over a displacement of 75 m.

Find its constant acceleration.

Given:

\[
u=10,\quad v=20,\quad s=75
\]

Using:

\[
v^2=u^2+2as
\]

\[
400=100+150a
\]

\[
300=150a
\]

\[
a=2\ \text{m/s}^2
\]

## 12. Displacement-Time Graphs

A displacement-time graph represents the position of an object as a function of time.

The gradient represents velocity.

\[
v=\frac{\Delta x}{\Delta t}
\]

### Important graph patterns

**Horizontal straight line:**

The object's position is constant.

Velocity is zero.

**Straight line with positive slope:**

The object moves in the positive direction with constant velocity.

**Straight line with negative slope:**

The object moves in the negative direction with constant velocity.

**Curved line:**

Velocity changes with time.

The gradient at a particular point represents instantaneous velocity.

## 13. Velocity-Time Graphs

A velocity-time graph represents velocity as a function of time.

The gradient represents acceleration.

\[
a=\frac{\Delta v}{\Delta t}
\]

The signed area under the graph represents displacement.

### Important graph patterns

**Horizontal line:**

Constant velocity and zero acceleration.

**Straight line with positive slope:**

Constant positive acceleration.

**Straight line with negative slope:**

Constant negative acceleration.

**Curved line:**

Non-uniform acceleration.

### Area under the graph

For constant velocity:

\[
s=vt
\]

For constant acceleration:

\[
s=\frac12(u+v)t
\]

These expressions correspond to rectangular and trapezoidal areas under a velocity-time graph.

## 14. Acceleration-Time Graphs

An acceleration-time graph represents acceleration as a function of time.

The area under the graph represents the change in velocity.

\[
\Delta v=\int a(t)\,dt
\]

For constant acceleration:

\[
\Delta v=at
\]

A horizontal acceleration-time graph represents constant acceleration.

A zero acceleration-time graph represents constant velocity.

## 15. Free Fall as a Special Case of One-Dimensional Motion

Free fall is motion under the influence of gravity alone.

Near Earth's surface, gravitational acceleration is approximately:

\[
g=9.8\ \text{m/s}^2
\]

Ignoring air resistance, all objects in free fall experience the same gravitational acceleration regardless of mass.

If upward is selected as positive:

\[
a=-g
\]

If downward is selected as positive:

\[
a=+g
\]

The sign depends on the coordinate convention.

For an object released from rest:

\[
u=0
\]

\[
v=gt
\]

for downward-positive coordinates.

Displacement after time t:

\[
s=\frac12gt^2
\]

The equations of constant acceleration can be applied to free-fall problems by substituting the appropriate acceleration.

## Common Exam Traps

- Distance and displacement are not interchangeable.
- Average speed uses total distance, while average velocity uses displacement.
- An object can have zero displacement but non-zero distance.
- Negative acceleration does not always indicate decreasing speed.
- Velocity is zero at an instant when an object changes direction, but acceleration need not be zero.
- The equations of motion require constant acceleration.
- The gradient of a displacement-time graph represents velocity.
- The gradient of a velocity-time graph represents acceleration.
- The signed area under a velocity-time graph represents displacement, not necessarily total distance.
- Free-fall acceleration is independent of mass when air resistance is neglected.

## Quiz

1. A person walks 8 m east and then 3 m west. What is the magnitude of displacement?

- [ ] 11 m
- [x] 5 m
- [ ] 8 m
- [ ] 3 m

> Displacement is the net change in position: 8 - 3 = 5 m east. Its magnitude is 5 m.

2. A car increases its velocity from 5 m/s to 25 m/s in 4 seconds with uniform acceleration. What is its acceleration?

- [ ] 4 m/s²
- [x] 5 m/s²
- [ ] 6 m/s²
- [ ] 8 m/s²

> Acceleration = (final velocity - initial velocity)/time = (25 - 5)/4 = 5 m/s².

3. What does the area under a velocity-time graph represent?

- [ ] Acceleration
- [ ] Average speed
- [x] Displacement
- [ ] Force

> Integrating velocity with respect to time gives displacement. The signed area represents net displacement.
