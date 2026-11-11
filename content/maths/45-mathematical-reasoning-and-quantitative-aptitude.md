---
title: Mathematical Reasoning and Quantitative Aptitude
level: exam
---

Quantitative aptitude and logical reasoning sections evaluate speed arithmetic, algebraic shortcuts, data sufficiency, and pattern identification under time constraints.

## Speed Arithmetic and Quantitative Techniques

### Rapid Calculation Rules

1. **Digital Root (Mod 9) Verification:** The sum of digits of a calculation modulo $9$ must equal the digital root of the result.
2. **Unit Digit Analysis:** Determine the last digit of $a^b$ by finding the 4-cycle of powers:
   $$\text{Cyclicity of } 2, 3, 7, 8 \text{ is } 4; \quad 4, 9 \text{ is } 2; \quad 0, 1, 5, 6 \text{ is } 1$$

## Data Sufficiency Framework

Data Sufficiency questions present a question followed by two statements (1) and (2).

```text
                     Data Sufficiency Decision Pipeline
                                     │
  1. Evaluate Statement (1) ALONE:
     - Sufficient? ──> Answer is (A) or (D)
     - Insufficient? ──> Answer is (B), (C), or (E)
                                     │
  2. Evaluate Statement (2) ALONE:
     - Sufficient (and St. 1 was Sufficient)? ──> Answer is (D)
     - Sufficient (and St. 1 was Insufficient)? ──> Answer is (B)
                                     │
  3. If BOTH are Insufficient alone, combine Statements (1) + (2):
     - Sufficient together? ──> Answer is (C)
     - Still Insufficient?  ──> Answer is (E)
```

## Quantitative Aptitude Master Table

| Technique / Category | Operational Principle | Typical Exam Application |
|---|---|---|
| Cyclicity of Powers | Powers repeat every $4$ exponent steps | Unit digit of $7^{2026}$ |
| Digital Root | Calculation check $\bmod 9$ | Rapid option elimination |
| Data Sufficiency | Determine adequacy, do NOT calculate! | Efficiency testing |
| Mixture Alligation | $\frac{V_1}{V_2} = \frac{C_m - C_2}{C_1 - C_m}$ | Average price/concentration mixtures |

## Important Formulas and Alligation Rule

Rule of Alligation (Weighted Averages):

$$\frac{\text{Quantity of Cheaper } (Q_c)}{\text{Quantity of Dearer } (Q_d)} = \frac{\text{Dearer Price } (d) - \text{Mean Price } (m)}{\text{Mean Price } (m) - \text{Cheaper Price } (c)}$$

Unit Digit Power Cyclicity Formula ($n = 4k + r$):

$$\text{Unit Digit}(a^n) = \text{Unit Digit}(a^r) \quad (\text{If } r = 0, \text{ use } r = 4)$$

## Common Exam Traps

- **Solving Completely in Data Sufficiency:** Spending 2 minutes computing the exact numerical answer when determining *that* it can be solved is sufficient.
- **Ignoring Negative Values in Statements:** Assuming variables like $x$ or $y$ are positive integers when statement logic allows negative or non-integer numbers.
- **Forgetting Cyclicity $r = 0$ Reset:** Evaluating $7^{40}$ as $7^0 = 1$ instead of taking exponent $r = 4 \implies 7^4 \to \text{unit digit } 1$.

## Quiz

1. What is the unit digit of the large exponential number $7^{103}$?
  - [ ] $1$
  - [ ] $3$
  - [x] $3$
  - [ ] $9$
   > Cyclicity of $7$ is $4$. Divide exponent $103$ by $4$: $103 = 4 \times 25 + 3 \implies$ remainder $r = 3$. Unit digit is $7^3 = 343 \implies 3$.

2. In what ratio must a merchant mix tea worth $\$60/\text{kg}$ with tea worth $\$75/\text{kg}$ to produce a mixture worth $\$65/\text{kg}$?
  - [ ] $1 : 2$
  - [x] $2 : 1$
  - [ ] $3 : 1$
  - [ ] $5 : 2$
   > Apply Alligation rule: $\frac{Q_{\text{cheap}}}{Q_{\text{dear}}} = \frac{75 - 65}{65 - 60} = \frac{10}{5} = \frac{2}{1}$. Ratio is $2 : 1$.

3. Is integer $x$ divisible by $6$?
   Statement (1): $x$ is divisible by $3$.
   Statement (2): $x$ is divisible by $2$.
  - [ ] Statement (1) ALONE is sufficient
  - [ ] Statement (2) ALONE is sufficient
  - [x] BOTH statements TOGETHER are sufficient, but NEITHER alone is sufficient
  - [ ] Statements (1) and (2) TOGETHER are NOT sufficient
   > An integer is divisible by $6$ if and only if it is divisible by both $2$ and $3$. Statement 1 alone is insufficient ($9$ is div by 3, not 6). Statement 2 alone is insufficient ($4$ is div by 2, not 6). Combined, $x$ is divisible by $\text{LCM}(2, 3) = 6$. Answer is (C).