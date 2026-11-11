---
title: Advanced Algebra and Equation Techniques
level: exam
---

Entrance examination algebra items test non-standard equation manipulation, symmetric polynomials, functional equations, and advanced bounding techniques under strict time constraints.

## Advanced Polynomial Symmetry and Vieta's Extensions

For a general polynomial equation of degree $n$:

$$a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 = 0$$

### Vieta's Formulas for Cubic Equations ($a x^3 + b x^2 + c x + d = 0$)

If roots are $\alpha, \beta, \gamma$:

1. **Sum of Roots:** $\alpha + \beta + \gamma = -\frac{b}{a}$
2. **Sum of Pairwise Products:** $\alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a}$
3. **Product of Roots:** $\alpha \beta \gamma = -\frac{d}{a}$

### Symmetric Polynomial Transformations

Newton's Sums method allows recursive computation of sums of powers of roots $S_k = \alpha^k + \beta^k + \gamma^k$:

$$a S_k + b S_{k-1} + c S_{k-2} + d S_{k-3} = 0$$

## Advanced System Solving and Bounding Strategies

```text
                      Advanced Algebraic Problem Attacks
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
  Symmetry Exploitation         AM-GM / Cauchy Bounding        Functional Substitutions
  - Set u = x + y, v = xy       - Force equality conditions    - Let x = tan θ or cos θ
  - Reduce system degree        - Bound ranges tightly         - Use periodic properties
```

## Advanced Algebraic Strategy Master Table

| Technique | Mathematical Mechanism | Ideal Problem Type |
|---|---|---|
| Newton's Sums | $a S_k + b S_{k-1} + c S_{k-2} = 0$ | High-power sum of roots $\alpha^n + \beta^n$ |
| Cauchy-Schwarz | $(\sum a_i^2)(\sum b_i^2) \ge (\sum a_i b_i)^2$ | Multi-variable inequality bounds |
| Reciprocal Equations | Divide by middle power $x^k$, set $u = x + \frac{1}{x}$ | Symmetric high-degree polynomials |
| Trigonometric Substitution | Set $x = \tan \theta$ or $\cos \theta$ | Algebraic expressions resembling trig identities |

## Important Formulas and Bounding Theorems

Cauchy-Schwarz Inequality:

$$(a_1^2 + a_2^2 + \dots + a_n^2)(b_1^2 + b_2^2 + \dots + b_n^2) \ge (a_1 b_1 + a_2 b_2 + \dots + a_n b_n)^2$$

Reciprocal Substitution Identity:

$$\text{If } u = x + \frac{1}{x} \implies x^2 + \frac{1}{x^2} = u^2 - 2, \quad x^3 + \frac{1}{x^3} = u^3 - 3u$$

## Common Exam Traps

- **Sign Alternation Errors in Vieta's:** Forgetting that Vieta's signs alternate: $-, +, -, +, \dots$. The product of roots for a cubic is $-\frac{d}{a}$, but for a quartic it is $+\frac{e}{a}$.
- **Assuming Real Roots Without Discriminant Check:** Finding candidate algebraic solutions that turn out to be non-real complex numbers when real solutions are explicitly demanded.
- **Ignoring AM-GM Positivity Constraint:** Applying AM-GM to negative quantities. AM-GM requires non-negative terms ($a_i \ge 0$).

## Quiz

1. If $\alpha, \beta, \gamma$ are roots of $x^3 - 6x^2 + 11x - 6 = 0$, evaluate $\alpha^2 + \beta^2 + \gamma^2$.
  - [ ] $36$
  - [x] $14$
  - [ ] $22$
  - [ ] $12$
   > By Vieta's: $\alpha + \beta + \gamma = 6$ and $\alpha\beta + \beta\gamma + \gamma\alpha = 11$. Use identity $\alpha^2 + \beta^2 + \gamma^2 = (\alpha + \beta + \gamma)^2 - 2(\alpha\beta + \beta\gamma + \gamma\alpha) = 6^2 - 2(11) = 36 - 22 = 14$.

2. Solve for $x \in \mathbb{R}$ in the reciprocal equation $x^4 - 5x^3 + 6x^2 - 5x + 1 = 0$.
  - [ ] $x = 1, 2$
  - [x] $x = \frac{3 \pm \sqrt{5}}{2}$
  - [ ] $x = 3 \pm \sqrt{5}$
  - [ ] $x = \frac{5 \pm \sqrt{21}}{2}$
   > Divide by $x^2$: $(x^2 + \frac{1}{x^2}) - 5(x + \frac{1}{x}) + 6 = 0$. Let $u = x + \frac{1}{x} \implies (u^2 - 2) - 5u + 6 = 0 \implies u^2 - 5u + 4 = 0 \implies (u - 4)(u - 1) = 0$. If $u = 4 \implies x + \frac{1}{x} = 4 \implies x^2 - 4x + 1 = 0 \implies x = \frac{4 \pm \sqrt{12}}{2} = 2 \pm \sqrt{3}$. If $u = 1 \implies x^2 - x + 1 = 0$ (no real roots). For $x^2 - 3x + 1 = 0 \implies x = \frac{3 \pm \sqrt{5}}{2}$.

3. Find the minimum real value of $f(x, y) = x^2 + 4y^2$ subject to the linear constraint $x + 2y = 10$.
  - [ ] $20$
  - [ ] $25$
  - [x] $50$
  - [ ] $100$
   > Apply Cauchy-Schwarz: $(x^2 + (2y)^2)(1^2 + 1^2) \ge (x(1) + 2y(1))^2 \implies (x^2 + 4y^2)(2) \ge (10)^2 = 100 \implies x^2 + 4y^2 \ge 50$. Minimum value is $50$.