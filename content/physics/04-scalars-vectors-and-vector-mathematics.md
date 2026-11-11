---
title: Scalars, Vectors and Vector Mathematics
level: foundation
---

Physics involves quantities that describe both magnitude and direction. Understanding the difference between scalar and vector quantities is essential for studying motion, forces, momentum, electric fields and magnetic fields.

A scalar is described by magnitude alone, whereas a vector requires both magnitude and direction.

Vector mathematics provides a systematic way to combine physical quantities while accounting for their directions.

## 1. Scalar Quantities

A scalar quantity is a physical quantity that is completely described by its magnitude and unit.

Scalars do not have a direction associated with them.

Examples include:

- Mass
- Time
- Temperature
- Distance
- Speed
- Energy
- Work
- Power
- Density
- Pressure
- Electric charge

For example:

A mass of 5 kg is completely described by its numerical value and unit.

There is no need to specify a direction.

Scalar quantities are generally combined using ordinary algebra, subject to the physical meaning of the quantity.

## 2. Vector Quantities

A vector quantity has both magnitude and direction.

Examples include:

- Displacement
- Velocity
- Acceleration
- Force
- Momentum
- Impulse
- Torque
- Angular momentum
- Electric field
- Magnetic field

For example:

A displacement of 5 metres east is different from a displacement of 5 metres west.

Although their magnitudes are equal, their directions differ.

### Vector representation

A vector is commonly represented by an arrow.

- Length of the arrow represents magnitude.
- Arrowhead represents direction.
- The symbol above a letter indicates a vector.

For example:

\[
\vec{A}
\]

The magnitude of a vector is written as:

\[
|\vec{A}| \quad \text{or simply } A
\]

The magnitude is always non-negative.

## 3. Difference Between Scalars and Vectors

| Scalar | Vector |
|---|---|
| Has magnitude only | Has magnitude and direction |
| Combined using scalar algebra | Combined using vector rules |
| Does not require directional representation | Requires directional representation |
| Example: distance | Example: displacement |
| Example: speed | Example: velocity |
| Example: energy | Example: force |

An important distinction is that speed is scalar, whereas velocity is vector.

Similarly, distance is scalar, whereas displacement is vector.

## 4. Types of Vectors

**Zero vector:**

A vector whose magnitude is zero.

\[
\vec{0}
\]

Its direction is undefined.

**Unit vector:**

A vector with magnitude equal to one.

It indicates direction and is commonly used to represent vector components.

**Equal vectors:**

Vectors having the same magnitude and direction are equal, regardless of their initial positions.

**Negative vectors:**

Two vectors are negative of each other if they have equal magnitudes but opposite directions.

\[
\vec{B}=-\vec{A}
\]

**Parallel vectors:**

Vectors whose directions are parallel. They may point in the same or opposite directions.

**Perpendicular vectors:**

Vectors whose directions differ by 90 degrees.

**Position vector:**

A vector that specifies the position of a point relative to a chosen origin.

## 5. Addition of Vectors

Vector addition combines two or more vectors to produce a resultant vector.

The resultant represents the combined effect of the original vectors.

### Triangle law of vector addition

If two vectors are represented by two sides of a triangle taken in order, their resultant is represented by the third side drawn from the starting point of the first vector to the ending point of the second vector.

Suppose a person walks:

- 3 m east.
- 4 m north.

The resultant displacement is:

\[
R=\sqrt{3^2+4^2}
\]

\[
R=\sqrt{9+16}=5\ \text{m}
\]

Its direction is:

\[
\theta=\tan^{-1}\left(\frac{4}{3}\right)
\]

\[
\theta\approx53.1^\circ
\]

Therefore, the displacement is 5 m at approximately 53.1 degrees north of east.

### Parallelogram law of vector addition

If two vectors acting from the same point are represented by adjacent sides of a parallelogram, their resultant is represented by the diagonal passing through their common starting point.

For two vectors with magnitudes A and B and angle θ between them:

\[
R=\sqrt{A^2+B^2+2AB\cos\theta}
\]

The direction of the resultant relative to vector A is:

\[
\tan\alpha=\frac{B\sin\theta}{A+B\cos\theta}
\]

### Special cases

If vectors act in the same direction:

\[
R=A+B
\]

If vectors act in opposite directions:

\[
R=|A-B|
\]

If vectors are perpendicular:

\[
R=\sqrt{A^2+B^2}
\]

## 6. Subtraction of Vectors

Vector subtraction is performed by adding the negative of a vector.

\[
\vec{A}-\vec{B}=\vec{A}+(-\vec{B})
\]

The negative vector has the same magnitude but opposite direction.

For example, if:

\[
\vec{A}=8\hat{i}
\]

\[
\vec{B}=3\hat{i}
\]

Then:

\[
\vec{A}-\vec{B}=5\hat{i}
\]

Vector subtraction is important when calculating relative position, relative velocity and changes in momentum.

## 7. Resolution of Vectors into Components

A vector can be represented by perpendicular components along coordinate axes.

In two-dimensional Cartesian coordinates:

\[
\vec{A}=A_x\hat{i}+A_y\hat{j}
\]

Where:

- \(A_x\) is the horizontal component.
- \(A_y\) is the vertical component.
- \(\hat{i}\) is the unit vector along the x-axis.
- \(\hat{j}\) is the unit vector along the y-axis.

If a vector has magnitude A and makes an angle θ with the positive x-axis:

\[
A_x=A\cos\theta
\]

\[
A_y=A\sin\theta
\]

Therefore:

\[
\vec{A}=A\cos\theta\hat{i}+A\sin\theta\hat{j}
\]

### Example

A force of 20 N acts at 30 degrees above the horizontal.

Horizontal component:

\[
F_x=20\cos30^\circ
\]

\[
F_x=10\sqrt{3}\ \text{N}
\]

Vertical component:

\[
F_y=20\sin30^\circ
\]

\[
F_y=10\ \text{N}
\]

Resolving vectors simplifies problems involving inclined forces and projectile motion.

## 8. Unit Vectors

A unit vector specifies a direction and has magnitude equal to one.

For a vector:

\[
\vec{A}=A_x\hat{i}+A_y\hat{j}
\]

Its magnitude is:

\[
A=\sqrt{A_x^2+A_y^2}
\]

The unit vector along its direction is:

\[
\hat{A}=\frac{\vec{A}}{|\vec{A}|}
\]

In three dimensions:

\[
\vec{A}=A_x\hat{i}+A_y\hat{j}+A_z\hat{k}
\]

Its magnitude is:

\[
A=\sqrt{A_x^2+A_y^2+A_z^2}
\]

The Cartesian unit vectors \(\hat{i}\), \(\hat{j}\) and \(\hat{k}\) are mutually perpendicular.

## 9. Dot Product of Vectors

The dot product, also called the scalar product, combines two vectors to produce a scalar.

It is defined as:

\[
\vec{A}\cdot\vec{B}=AB\cos\theta
\]

Where θ is the angle between the vectors.

### Component form

For:

\[
\vec{A}=A_x\hat{i}+A_y\hat{j}+A_z\hat{k}
\]

and:

\[
\vec{B}=B_x\hat{i}+B_y\hat{j}+B_z\hat{k}
\]

The dot product is:

\[
\vec{A}\cdot\vec{B}
=A_xB_x+A_yB_y+A_zB_z
\]

### Important properties

- The result is a scalar.
- It is commutative.
- The dot product of perpendicular vectors is zero.
- The dot product of parallel vectors is the product of their magnitudes.
- The dot product of a vector with itself is the square of its magnitude.

\[
\vec{A}\cdot\vec{A}=A^2
\]

### Physical application: Work

Work done by a constant force is:

\[
W=\vec{F}\cdot\vec{s}
\]

\[
W=Fs\cos\theta
\]

Only the component of force along the displacement contributes to work.

## 10. Cross Product of Vectors

The cross product, also called the vector product, produces another vector.

Its magnitude is:

\[
|\vec{A}\times\vec{B}|=AB\sin\theta
\]

Its direction is perpendicular to the plane containing the two vectors.

The direction is determined using the right-hand rule.

### Component form

\[
\vec{A}\times\vec{B}
=
(A_yB_z-A_zB_y)\hat{i}
+
(A_zB_x-A_xB_z)\hat{j}
+
(A_xB_y-A_yB_x)\hat{k}
\]

### Important properties

- The result is a vector.
- It is anti-commutative.

\[
\vec{A}\times\vec{B}
=-(\vec{B}\times\vec{A})
\]

- The cross product of parallel vectors is zero.
- Its magnitude is maximum when vectors are perpendicular.
- The cross product of a vector with itself is zero.

### Physical applications

Torque:

\[
\vec{\tau}=\vec{r}\times\vec{F}
\]

Angular momentum:

\[
\vec{L}=\vec{r}\times\vec{p}
\]

Magnetic force:

\[
\vec{F}=q(\vec{v}\times\vec{B})
\]

## 11. Position, Displacement and Relative Vectors

A position vector specifies the location of an object relative to an origin.

For a point with coordinates (x, y, z):

\[
\vec{r}=x\hat{i}+y\hat{j}+z\hat{k}
\]

Displacement is the change in position.

\[
\Delta\vec{r}=\vec{r}_2-\vec{r}_1
\]

Relative position of object A with respect to object B:

\[
\vec{r}_{AB}=\vec{r}_A-\vec{r}_B
\]

Similarly, relative velocity:

\[
\vec{v}_{AB}=\vec{v}_A-\vec{v}_B
\]

These concepts will become important in the study of relative motion.

## 12. Three-Dimensional Vector Representation

In three-dimensional space, vectors have components along three mutually perpendicular axes.

\[
\vec{A}=A_x\hat{i}+A_y\hat{j}+A_z\hat{k}
\]

Magnitude:

\[
A=\sqrt{A_x^2+A_y^2+A_z^2}
\]

For example:

\[
\vec{A}=2\hat{i}+3\hat{j}+6\hat{k}
\]

Its magnitude is:

\[
A=\sqrt{2^2+3^2+6^2}
\]

\[
A=\sqrt{49}=7
\]

Its unit vector is:

\[
\hat{A}=\frac{2}{7}\hat{i}+\frac{3}{7}\hat{j}+\frac{6}{7}\hat{k}
\]

## Common Exam Traps

- Distance is scalar, while displacement is vector.
- Speed is scalar, while velocity is vector.
- Equal magnitudes do not guarantee equal vectors; directions must also match.
- The resultant of perpendicular vectors must be calculated using the Pythagorean theorem.
- The dot product produces a scalar, whereas the cross product produces a vector.
- The dot product of perpendicular vectors is zero.
- The cross product of parallel vectors is zero.
- The order of vectors matters in a cross product.
- A vector's components can be negative depending on its direction relative to the coordinate axes.
- The magnitude of a vector cannot be negative.

## Quiz

1. Which of the following is a vector quantity?

- [ ] Distance
- [ ] Energy
- [x] Acceleration
- [ ] Temperature

> Acceleration has both magnitude and direction, making it a vector quantity.

2. Two perpendicular vectors have magnitudes 6 units and 8 units. What is the magnitude of their resultant?

- [ ] 10 units
- [x] 10 units
- [ ] 14 units
- [ ] 48 units

> The resultant magnitude is sqrt(6² + 8²) = sqrt(100) = 10 units.

3. What is the dot product of two perpendicular vectors?

- [ ] The product of their magnitudes
- [ ] A vector of maximum magnitude
- [x] Zero
- [ ] Their sum

> The dot product is AB cos(theta). For perpendicular vectors, theta = 90 degrees and cos(90 degrees) = 0.
