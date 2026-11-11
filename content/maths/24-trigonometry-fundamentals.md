---
title: Trigonometry Fundamentals
level: intermediate
---

Trigonometry relates the angles and side lengths of triangles. Extending right-triangle definitions to arbitrary real numbers via the unit circle provides the core foundation for periodic functions, analytical geometry, and calculus.

## Right-Triangle Ratios and Radian Measure

### Right-Triangle Definitions

For a right-angled triangle with acute angle $\theta$:

$$\sin \theta = \frac{\text{Opposite}}{\text{Hypotenuse}}, \qquad \cos \theta = \frac{\text{Adjacent}}{\text{Hypotenuse}}, \qquad \tan \theta = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{\sin \theta}{\cos \theta}$$

Reciprocal Ratios:

$$\csc \theta = \frac{1}{\sin \theta}, \qquad \sec \theta = \frac{1}{\cos \theta}, \qquad \cot \theta = \frac{1}{\tan \theta}$$

### Radian Measure and Conversions

A **radian** is the angle subtended at the center of a circle by an arc equal in length to the radius.

$$\pi \text{ radians} = 180^\circ \implies 1 \text{ rad} = \left(\frac{180}{\pi}\right)^\circ \approx 57.2958^\circ$$

- **Degree to Radian:** Multiply by $\frac{\pi}{180^\circ}$.
- **Arc Length ($s$):** $s = r \cdot \theta \quad (\theta \text{ in radians})$.
- **Sector Area ($A$):** $A = \frac{1}{2} r^2 \theta \quad (\theta \text{ in radians})$.

## The Unit Circle and Quadrant Signs (ASTC Rule)

On the unit circle $x^2 + y^2 = 1$, any point $P(\theta)$ has coordinates $(x, y) = (\cos \theta, \sin \theta)$.

```text
                     Unit Circle Quadrant Signs (ASTC)
                                   y-axis
                                     │
                    Quadrant II      │      Quadrant I
                   (Sin positive)    │    (All positive)
                   S                 │    A
                                     │
                   ──────────────────┼────────────────── x-axis
                                     │
                    Quadrant III     │      Quadrant IV
                   (Tan positive)    │    (Cos positive)
                   T                 │    C
                                     │
```

## Trigonometric Values of Special Angles Table

| Angle $\theta$ (Deg) | Angle $\theta$ (Rad) | $\sin \theta$ | $\cos \theta$ | $\tan \theta$ |
|---|---|---|---|---|
| $0^\circ$ | $0$ | $0$ | $1$ | $0$ |
| $30^\circ$ | $\frac{\pi}{6}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}}$ |
| $45^\circ$ | $\frac{\pi}{4}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{\sqrt{2}}$ | $1$ |
| $60^\circ$ | $\frac{\pi}{3}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| $90^\circ$ | $\frac{\pi}{2}$ | $1$ | $0$ | Undefined |
| $180^\circ$ | $\pi$ | $0$ | $-1$ | $0$ |
| $270^\circ$ | $\frac{3\pi}{2}$ | $-1$ | $0$ | Undefined |

## Important Formulas and Periodicity Identities

Pythagorean Identity:

$$\sin^2 \theta + \cos^2 \theta = 1$$

Coterminal & Periodic Properties ($k \in \mathbb{Z}$):

$$\sin(\theta + 2k\pi) = \sin \theta, \qquad \cos(\theta + 2k\pi) = \cos \theta, \qquad \tan(\theta + k\pi) = \tan \theta$$

Negative Angle Identities (Even / Odd Properties):

$$\sin(-\theta) = -\sin \theta \quad (\text{Odd}), \qquad \cos(-\theta) = \cos \theta \quad (\text{Even}), \qquad \tan(-\theta) = -\tan \theta \quad (\text{Odd})$$

## Common Exam Traps

- **Mixing Degree and Radian Modes:** Evaluating $\sin(2)$ on a calculator set to degree mode instead of radian mode (or forgetting to convert $\theta$ to radians before applying $s = r\theta$).
- **Sign Error in Quadrants II, III, IV:** Forgetting that cosine is negative in Quadrant II ($90^\circ < \theta < 180^\circ$) and tangent is negative in Quadrant IV.
- **Dividing by Zero at Quadrantal Angles:** Assuming $\tan(90^\circ)$ or $\sec(90^\circ)$ equals $0$ or $1$. $\tan(90^\circ) = \frac{1}{0}$ is **undefined**.

## Quiz

1. Convert an angle of $225^\circ$ into exact radian measure.
  - [ ] $\frac{7\pi}{6}$
  - [x] $\frac{5\pi}{4}$
  - [ ] $\frac{4\pi}{3}$
  - [ ] $\frac{3\pi}{2}$
   > Multiply by $\frac{\pi}{180^\circ}$: $225^\circ \times \frac{\pi}{180^\circ} = \frac{225}{180} \pi = \frac{5\pi}{4}$.

2. Evaluate the exact numerical value of $\cos\left(\frac{2\pi}{3}\right)$.
  - [ ] $\frac{1}{2}$
  - [x] $-\frac{1}{2}$
  - [ ] $\frac{\sqrt{3}}{2}$
  - [ ] $-\frac{\sqrt{3}}{2}$
   > Angle $\frac{2\pi}{3} = 120^\circ$ lies in Quadrant II, where cosine is negative. Reference angle is $180^\circ - 120^\circ = 60^\circ$. Thus $\cos(120^\circ) = -\cos(60^\circ) = -\frac{1}{2}$.

3. A circular arc of length $s = 15\text{ cm}$ subtends a central angle $\theta = 3\text{ radians}$. Find the area of the corresponding sector.
  - [ ] $22.5\text{ cm}^2$
  - [x] $37.5\text{ cm}^2$
  - [ ] $45\text{ cm}^2$
  - [ ] $75\text{ cm}^2$
   > Arc length $s = r \theta \implies 15 = r(3) \implies r = 5\text{ cm}$. Sector area $A = \frac{1}{2} r^2 \theta = \frac{1}{2} (5)^2 (3) = \frac{1}{2} (25)(3) = \frac{75}{2} = 37.5\text{ cm}^2$.