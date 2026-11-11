---
title: Fractions, Decimals and Percentages
level: foundation
---

Fractions, decimals, and percentages are three different mathematical representations of proportional parts of a whole. Fluency in converting between these forms and performing arithmetic operations with them is fundamental to quantitative reasoning.

## Fraction Operations and Simplification

A fraction represents a division of a numerator $a$ by a non-zero denominator $b$, written as $\frac{a}{b}$.

- **Proper Fractions:** $a < b$ (e.g., $\frac{3}{5}$).
- **Improper Fractions:** $a \ge b$ (e.g., $\frac{7}{4}$). Can be written as a mixed number: $1\frac{3}{4}$.
- **Equivalent Fractions:** Created by multiplying or dividing numerator and denominator by the same non-zero integer $k$: $\frac{a}{b} = \frac{a \cdot k}{b \cdot k}$.

### Arithmetic Operations on Fractions

1. **Addition and Subtraction:** Find a Least Common Denominator (LCD), convert to equivalent fractions, and combine numerators:
$$\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}$$

2. **Multiplication:** Multiply numerators together and denominators together:
$$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$

3. **Division:** Multiply by the reciprocal of the divisor:
$$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c} = \frac{ad}{bc}$$

## Decimals and Percentages

### Decimal Conversions

- **Terminating Decimals to Fractions:** Write the decimal digits over the corresponding power of $10$ and simplify (e.g., $0.375 = \frac{375}{1000} = \frac{3}{8}$).
- **Repeating Decimals to Fractions:** Let $x = 0.\overline{ab}$. Multiply by $10^n$ (where $n$ is the period length) and subtract the original equation:
$$x = 0.\overline{45} \implies 100x = 45.\overline{45} \implies 99x = 45 \implies x = \frac{45}{99} = \frac{5}{11}$$

### Percentages and Percentage Change

A percentage represents a fraction with a denominator of $100$: $P\% = \frac{P}{100}$.

- **Percentage Change:**
$$\text{Percentage Change} = \left( \frac{\text{New Value} - \text{Original Value}}{\text{Original Value}} \right) \times 100\%$$
- **Percentage Increase / Decrease Multiplier:**
$$\text{Final Value} = \text{Original Value} \times \left(1 \pm \frac{P}{100}\right)$$

## Equivalent Form Conversion Table

| Fraction | Decimal | Percentage |
|---|---|---|
| $\frac{1}{2}$ | $0.5$ | $50\%$ |
| $\frac{1}{3}$ | $0.\overline{3}$ | $33.\overline{3}\%$ |
| $\frac{1}{4}$ | $0.25$ | $25\%$ |
| $\frac{1}{5}$ | $0.2$ | $20\%$ |
| $\frac{1}{8}$ | $0.125$ | $12.5\%$ |
| $\frac{3}{8}$ | $0.375$ | $37.5\%$ |
| $\frac{2}{3}$ | $0.\overline{6}$ | $66.\overline{6}\%$ |
| $\frac{4}{5}$ | $0.8$ | $80\%$ |

## Important Formulas and Conversion Rules

Converting Repeating Decimal $0.\overline{a_1 a_2 \dots a_n}$ to Fraction:

$$x = 0.\overline{a_1 a_2 \dots a_n} = \frac{a_1 a_2 \dots a_n}{\underbrace{99\dots9}_{n \text{ nines}}}$$

Successive Percentage Changes Formula:

$$\text{Total Multiplier} = \left(1 + \frac{p_1}{100}\right) \cdot \left(1 + \frac{p_2}{100}\right)$$

$$\text{Net Percentage Change} = \left[\left(1 + \frac{p_1}{100}\right)\left(1 + \frac{p_2}{100}\right) - 1\right] \times 100\%$$

## Common Exam Traps

- **Adding Denominators directly:** Writing $\frac{a}{b} + \frac{c}{d} = \frac{a+c}{b+d}$. Denominators must be equalized using an LCD before adding numerators.
- **Base Confusion in Percentage Changes:** Calculating percentage decrease using the new value in the denominator instead of the original base value.
- **Successive Percentages Addition Error:** Assuming a $20\%$ increase followed by a $20\%$ decrease results in no change. Net multiplier is $1.20 \times 0.80 = 0.96$, resulting in a net $4\%$ decrease.

## Quiz

1. Evaluate the complex fraction expression: $\frac{\frac{2}{3} + \frac{1}{4}}{\frac{5}{6} - \frac{1}{2}}$.
  - [ ] $\frac{11}{12}$
  - [x] $\frac{11}{4}$
  - [ ] $\frac{7}{4}$
  - [ ] $\frac{11}{6}$
   > Numerator: $\frac{2}{3} + \frac{1}{4} = \frac{8+3}{12} = \frac{11}{12}$. Denominator: $\frac{5}{6} - \frac{3}{6} = \frac{2}{6} = \frac{1}{3}$. Dividing gives $\frac{11/12}{1/3} = \frac{11}{12} \times \frac{3}{1} = \frac{11}{4}$.

2. Convert the repeating decimal $0.2\overline{6}$ into its simplest fractional form.
  - [ ] $\frac{26}{99}$
  - [ ] $\frac{13}{50}$
  - [x] $\frac{4}{15}$
  - [ ] $\frac{24}{90}$
   > Let $x = 0.2\overline{6} \implies 10x = 2.\overline{6}$ and $100x = 26.\overline{6}$. Subtracting: $90x = 24 \implies x = \frac{24}{90} = \frac{4}{15}$.

3. A store increases the price of an item by $25\%$, and later decreases the new price by $20\%$. What is the net overall percentage change in the price of the item?
  - [ ] $+5\%$ increase
  - [ ] $-5\%$ decrease
  - [x] $0\%$ (Price remains unchanged)
  - [ ] $+4\%$ increase
   > Multiplier for $+25\%$ is $1.25 = \frac{5}{4}$. Multiplier for $-20\%$ is $0.80 = \frac{4}{5}$. Total multiplier: $\frac{5}{4} \times \frac{4}{5} = 1.00$. Thus, there is $0\%$ net change.