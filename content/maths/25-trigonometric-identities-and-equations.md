---
title: Trigonometric Identities and Equations
level: intermediate
---

Trigonometric identities enable structural transformation of complex trigonometric expressions. Solving trigonometric equations requires combining identities, algebraic factoring, and general solution rules across periodic cycles.

## Fundamental Identities and Compound Angle Formulas

### Pythagorean Identities

$$\sin^2 x + \cos^2 x = 1$$

$$1 + \tan^2 x = \sec^2 x$$

$$1 + \cot^2 x = \csc^2 x$$

### Compound Angle Formulas

$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$$

$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$$

$$\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$$

### Double-Angle and Half-Angle Formulas

- **Double Angle:**
$$\sin(2A) = 2 \sin A \cos A$$

$$\cos(2A) = \cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A$$

$$\tan(2A) = \frac{2\tan A}{1 - \tan^2 A}$$

- **Half-Angle Power Reduction:**
$$\sin^2 A = \frac{1 - \cos(2A)}{2}, \qquad \cos^2 A = \frac{1 + \cos(2A)}{2}$$

## Laws of Sines, Cosines, and General Equation Solutions

### Oblique Triangle Laws

For any triangle $\triangle ABC$ with sides $a, b, c$:

1. **Law of Sines:**
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

2. **Law of Cosines:**
$$c^2 = a^2 + b^2 - 2ab \cos C \implies \cos C = \frac{a^2 + b^2 - c^2}{2ab}$$

### General Solutions of Trigonometric Equations ($n \in \mathbb{Z}$)

- **$\sin x = \sin \alpha \implies x = n\pi + (-1)^n \alpha$**
- **$\cos x = \cos \alpha \implies x = 2n\pi \pm \alpha$**
- **$\tan x = \tan \alpha \implies x = n\pi + \alpha$**

## Trigonometric Identity Master Table

| Category | Primary Identity Formula | Structural Use |
|---|---|---|
| Pythagorean | $1 + \tan^2 x = \sec^2 x$ | Converting between $\tan$ and $\sec$ |
| Sum-to-Product | $\sin A + \sin B = 2 \sin\left(\frac{A+B}{2}\right) \cos\left(\frac{A-B}{2}\right)$ | Simplifying sums of wave terms |
| Product-to-Sum | $2 \sin A \cos B = \sin(A+B) + \sin(A-B)$ | Integrating products of sine & cosine |
| Linear Combination | $a \sin x + b \cos x = R \sin(x + \phi)$ | Amplitude $R = \sqrt{a^2+b^2}, \tan \phi = b/a$ |

## Important Formulas and Wave Combination Identities

Linear Combination Form ($a \sin x + b \cos x$):

$$a \sin x + b \cos x = R \sin(x + \phi) \quad \text{where } R = \sqrt{a^2 + b^2}, \quad \tan \phi = \frac{b}{a}$$

$$\text{Range}: \left[-\sqrt{a^2 + b^2}, \sqrt{a^2 + b^2}\right]$$

## Common Exam Traps

- **Canceling Trigonometric Functions Across Equations:** Dividing both sides of $\sin x \cos x = \sin x$ by $\sin x$, losing the solution set where $\sin x = 0$. Always factor instead: $\sin x (\cos x - 1) = 0$.
- **Forgetting $(-1)^n$ in General Sine Solution:** Writing $x = n\pi + \alpha$ for sine instead of $x = n\pi + (-1)^n \alpha$.
- **Ambiguous Case in Law of Sines (SSA):** Ignoring the possibility of two valid triangles when given two sides and a non-included acute angle (where $\sin B = \frac{b \sin A}{a} < 1$).

## Quiz

1. Simplify the trigonometric expression: $\frac{\sin(2x)}{1 + \cos(2x)}$.
  - [ ] $\sin x$
  - [ ] $\cos x$
  - [x] $\tan x$
  - [ ] $\cot x$
   > Use double-angle formulas: $\sin(2x) = 2\sin x \cos x$ and $1 + \cos(2x) = 2\cos^2 x$. The ratio becomes $\frac{2\sin x \cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x$.

2. Find all solutions for $x \in [0, 2\pi)$ satisfying $2\cos^2 x - 1 = 0$.
  - [ ] $x = \frac{\pi}{4}, \frac{3\pi}{4}$
  - [x] $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$
  - [ ] $x = \frac{\pi}{6}, \frac{5\pi}{6}, \frac{7\pi}{6}, \frac{11\pi}{6}$
  - [ ] $x = \frac{\pi}{3}, \frac{2\pi}{3}, \frac{4\pi}{3}, \frac{5\pi}{3}$
   > $2\cos^2 x = 1 \implies \cos^2 x = \frac{1}{2} \implies \cos x = \pm \frac{1}{\sqrt{2}}$. In $[0, 2\pi)$, $\cos x = \frac{1}{\sqrt{2}} \implies x = \frac{\pi}{4}, \frac{7\pi}{4}$, and $\cos x = -\frac{1}{\sqrt{2}} \implies x = \frac{3\pi}{4}, \frac{5\pi}{4}$.

3. What is the maximum value of the function $f(x) = 3\sin x - 4\cos x$?
  - [ ] $1$
  - [ ] $3$
  - [x] $5$
  - [ ] $7$
   > Express in linear combination form $R \sin(x + \phi)$ where $R = \sqrt{a^2 + b^2} = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$. Maximum value is $+R = 5$.