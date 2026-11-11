---
title: Complex Numbers and Advanced Number Theory
level: advanced
---

Complex numbers extend the real number system to include solutions to equations like $x^2 + 1 = 0$. Combining polar representations, Euler's identity, De Moivre's theorem, and modular arithmetic forms the summit of advanced university prep mathematics.

## Complex Number Fundamentals and Argand Plane

A **complex number** $z \in \mathbb{C}$ is written in rectangular form as:

$$z = x + i y \quad (x, y \in \mathbb{R}, i = \sqrt{-1})$$

- **Real Part:** $\text{Re}(z) = x$, **Imaginary Part:** $\text{Im}(z) = y$.
- **Complex Conjugates ($\bar{z}$):** $\bar{z} = x - i y \implies z \cdot \bar{z} = x^2 + y^2 = |z|^2$.
- **Modulus ($|z|$):** Non-negative distance from origin in the Argand plane:
  $$|z| = \sqrt{x^2 + y^2}$$
- **Argument ($\arg(z)$):** Angle $\theta$ made with the positive real axis:
  $$\tan \theta = \frac{y}{x} \implies \text{Principal Arg } \text{Arg}(z) \in (-\pi, \pi]$$

## Polar Form, Euler's Formula, and De Moivre's Theorem

### Polar and Exponential Representation

$$z = r (\cos \theta + i \sin \theta) = r e^{i \theta}$$

where $r = |z|$ and $\theta = \arg(z)$.

### Euler's Identity

$$e^{i \theta} = \cos \theta + i \sin \theta \implies e^{i \pi} + 1 = 0$$

### De Moivre's Theorem

For any real number $n$:

$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta) \implies \Big(e^{i\theta}\Big)^n = e^{i n \theta}$$

### $n$-th Roots of Unity

Solutions to $z^n = 1$ are evenly spaced on the unit circle in the Argand plane:

$$\omega_k = e^{i \frac{2k\pi}{n}} = \cos\left(\frac{2k\pi}{n}\right) + i \sin\left(\frac{2k\pi}{n}\right) \quad (k = 0, 1, \dots, n-1)$$

- For cube roots of unity ($1, \omega, \omega^2$):
  $$1 + \omega + \omega^2 = 0 \qquad \text{and} \qquad \omega^3 = 1$$

## Complex Algebra Master Table

| Concept / Form | Algebraic Expression | Argand Plane Geometric Meaning |
|---|---|---|
| Modulus $|z|$ | $\sqrt{x^2 + y^2}$ | Distance from origin |
| Conjugate $\bar{z}$ | $x - i y$ | Reflection across real axis |
| Exponential Form | $r e^{i\theta}$ | Radius $r$, angle $\theta$ |
| Distance $d(z_1, z_2)$ | $|z_1 - z_2|$ | Distance between points $z_1$ and $z_2$ |
| Circle Locus | $|z - z_0| = R$ | Circle with center $z_0$ and radius $R$ |
| Perpendicular Bisector | $|z - z_1| = |z - z_2|$ | Line equidistant from $z_1$ and $z_2$ |

## Important Formulas and Number Theory Proof Identities

Triangle Inequality for Complex Numbers:

$$||z_1| - |z_2|| \le |z_1 + z_2| \le |z_1| + |z_2|$$

Fermat's Little Theorem:

$$\text{If } p \text{ is prime and } \gcd(a, p) = 1 \implies a^{p-1} \equiv 1 \pmod p$$

Cube Roots of Unity Sum Identity:

$$1 + \omega + \omega^2 = 0 \quad \text{where } \omega = e^{i \frac{2\pi}{3}} = -\frac{1}{2} + i \frac{\sqrt{3}}{2}$$

## Common Exam Traps

- **Principal Argument Range Error:** Writing $\text{Arg}(z) = 240^\circ$ or $\frac{4\pi}{3}$. Principal argument **must lie in** $(-\pi, \pi]$, so $240^\circ$ must be expressed as $-120^\circ$ ($-\frac{2\pi}{3}$).
- **Square Root of Negative Numbers Product Fallacy:** Writing $\sqrt{-2} \cdot \sqrt{-3} = \sqrt{(-2)(-3)} = \sqrt{6}$. Correct formulation is $(i\sqrt{2})(i\sqrt{3}) = i^2 \sqrt{6} = -\sqrt{6}$.
- **Confusing $\text{Im}(z)$ as Imaginary:** Writing $\text{Im}(3 + 4i) = 4i$. The imaginary part is a **real scalar**: $\text{Im}(3 + 4i) = 4$.

## Quiz

1. Evaluate the exact numerical value of $(1 + i)^8$.
  - [ ] $8$
  - [ ] $16 i$
  - [x] $16$
  - [ ] $32$
   > Convert to polar form: $1 + i = \sqrt{2} e^{i \pi/4}$. Apply De Moivre's theorem: $(1 + i)^8 = (\sqrt{2})^8 e^{i 8(\pi/4)} = 16 e^{i 2\pi} = 16(1) = 16$.

2. If $\omega$ is a complex non-real cube root of unity, simplify the expression: $(1 - \omega + \omega^2)(1 + \omega - \omega^2)$.
  - [ ] $1$
  - [ ] $2$
  - [x] $4$
  - [ ] $0$
   > Use identity $1 + \omega + \omega^2 = 0 \implies 1 + \omega^2 = -\omega$ and $1 + \omega = -\omega^2$. Substitute: $(-\omega - \omega)(-\omega^2 - \omega^2) = (-2\omega)(-2\omega^2) = 4 \omega^3 = 4(1) = 4$.

3. Find the locus of point $z$ in the Argand plane satisfying the equation $|z - 3i| = 5$.
  - [ ] Straight line passing through $(0, 3)$
  - [x] Circle centered at $(0, 3)$ with radius $5$
  - [ ] Parabola with focus at $(0, 3)$
  - [ ] Ellipse with foci at $(0, \pm 3)$
   > The equation $|z - z_0| = R$ represents a circle centered at $z_0$ with radius $R$. Here $z_0 = 3i = (0, 3)$ and $R = 5$.