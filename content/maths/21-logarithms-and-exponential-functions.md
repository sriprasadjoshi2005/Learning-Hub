---
title: Logarithms and Exponential Functions
level: intermediate
---

Exponential functions model continuous growth and decay, while logarithmic functions serve as their algebraic inverses. Mastery of logarithms is essential for calculus, financial models, and solving exponential equations.

## Logarithmic Definitions and Base Properties

The logarithm of a positive number $x$ to a positive base $b$ ($b \neq 1$) is the exponent $y$ to which $b$ must be raised to yield $x$:

$$y = \log_b(x) \iff b^y = x \quad (x > 0, b > 0, b \neq 1)$$

- **Common Logarithm:** Base $10$, written as $\log(x)$ or $\log_{10}(x)$.
- **Natural Logarithm:** Base $e \approx 2.71828$, written as $\ln(x)$ or $\log_e(x)$.

### Laws of Logarithms

For any valid bases and positive numbers $M, N > 0$:

1. **Product Rule:** $\log_b(M \cdot N) = \log_b(M) + \log_b(N)$
2. **Quotient Rule:** $\log_b\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)$
3. **Power Rule:** $\log_b(M^k) = k \cdot \log_b(M)$
4. **Identity & Zero Rules:** $\log_b(b) = 1$ and $\log_b(1) = 0$
5. **Change of Base Formula:** For any new valid base $a > 0$:
$$\log_b(x) = \frac{\log_a(x)}{\log_a(b)} = \frac{\ln(x)}{\ln(b)}$$

## Exponential Growth and Decay Models

Exponential relationships follow the general differential model $\frac{dy}{dt} = k y$, giving the standard growth/decay function:

$$A(t) = A_0 e^{k t} \quad \text{or} \quad A(t) = A_0 (1 \pm r)^t$$

- **Exponential Growth ($k > 0$ or $r > 0$):** Populations, compound interest ($A = P(1 + \frac{r}{n})^{nt}$).
- **Exponential Decay ($k < 0$):** Radioactive decay, depreciation, half-life problems ($T_{1/2} = \frac{\ln 2}{|k|}$).

## Logarithm Properties Summary Table

| Property / Rule | Mathematical Formula | Key Application |
|---|---|---|
| Definition | $\log_b(x) = y \iff b^y = x$ | Converting between logarithmic & exponential form |
| Product Rule | $\log_b(MN) = \log_b M + \log_b N$ | Combining split logarithmic terms |
| Quotient Rule | $\log_b(M/N) = \log_b M - \log_b N$ | Simplifying ratios inside logarithms |
| Power Rule | $\log_b(M^p) = p \log_b M$ | Bringing exponents down to solve for variables |
| Change of Base | $\log_b x = \frac{\ln x}{\ln b}$ | Evaluating non-standard bases on calculators |
| Reciprocal Base | $\log_b a = \frac{1}{\log_a b}$ | Solving reciprocal logarithmic equations |

## Important Formulas and Exponential Identities

Inverse Function Relationship:

$$b^{\log_b(x)} = x \quad (x > 0) \qquad \text{and} \qquad \log_b(b^x) = x \quad (x \in \mathbb{R})$$

Half-Life Decay Formula:

$$N(t) = N_0 \cdot \left(\frac{1}{2}\right)^{\frac{t}{T_{1/2}}} = N_0 e^{-\lambda t} \quad \text{where } \lambda = \frac{\ln 2}{T_{1/2}}$$

Continuously Compounded Interest:

$$A = P e^{r t}$$

## Common Exam Traps

- **Distributing Logarithms over Addition:** Incorrectly writing $\log(A + B) = \log(A) + \log(B)$. The correct rule is $\log(A \cdot B) = \log(A) + \log(B)$.
- **Ignoring Extraneous Logarithmic Solutions:** Forgetting to check candidate solutions in the original logarithmic equation. $\log_b(x)$ requires $x > 0$.
- **Canceling Terms inside Logarithms:** Writing $\frac{\log(A)}{\log(B)} = \log(A - B)$ or $\log(A/B)$. Note that $\frac{\log A}{\log B} = \log_B A$.

## Quiz

1. Evaluate the exact value of the logarithmic expression: $\log_2(32) - \log_3\left(\frac{1}{27}\right)$.
  - [ ] $2$
  - [x] $8$
  - [ ] $5$
  - [ ] $-1$
   > $\log_2(32) = \log_2(2^5) = 5$. $\log_3(1/27) = \log_3(3^{-3}) = -3$. Thus $5 - (-3) = 5 + 3 = 8$.

2. Solve for $x$ in the equation: $\log_4(x) + \log_4(x - 6) = 2$.
  - [ ] $x = 2$ and $x = 8$
  - [x] $x = 8$ only
  - [ ] $x = 4$ only
  - [ ] $x = -2$ and $x = 8$
   > Combine using product rule: $\log_4[x(x - 6)] = 2 \implies x(x - 6) = 4^2 = 16 \implies x^2 - 6x - 16 = 0 \implies (x - 8)(x + 2) = 0$. So $x = 8$ or $x = -2$. Since $\log_4(-2)$ is undefined, $x = 8$ is the only valid solution.

3. A radioactive isotope has a half-life of $10$ years. If an initial sample has a mass of $80\text{ grams}$, how much remains after $30\text{ years}$?
  - [ ] $20\text{ grams}$
  - [x] $10\text{ grams}$
  - [ ] $5\text{ grams}$
  - [ ] $2.5\text{ grams}$
   > Number of half-lives elapsed $n = \frac{30}{10} = 3$. Remaining mass $N(30) = 80 \times \left(\frac{1}{2}\right)^3 = 80 \times \frac{1}{8} = 10\text{ grams}$.