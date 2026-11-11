---
title: Statistics and Data Analysis
level: advanced
---

Statistics measures central tendencies, dispersion, and statistical dependencies in numerical data. Understanding variance, standard deviation, linear regression, and normal distributions is essential for quantitative data analysis.

## Central Tendencies and Measures of Dispersion

### Measures of Central Tendency

1. **Mean ($\bar{x}$):** Arithmetic average of data points:
   $$\bar{x} = \frac{\sum x_i}{n} \quad \text{or} \quad \bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$
2. **Median:** Middle value of an ordered dataset (or average of two middle values).
3. **Mode:** Most frequently occurring value in the dataset.

### Measures of Dispersion

1. **Range:** Difference between maximum and minimum values ($\text{Max} - \text{Min}$).
2. **Variance ($\sigma^2$):** Average squared deviation from the mean:
   $$\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n} = \frac{\sum x_i^2}{n} - (\bar{x})^2$$
3. **Standard Deviation ($\sigma$):** Square root of variance: $\sigma = \sqrt{\text{Variance}}$.
4. **Coefficient of Variation ($\text{CV}$):** Relative dispersion measure:
   $$\text{CV} = \frac{\sigma}{\bar{x}} \times 100\%$$

## Correlation, Linear Regression, and Normal Distribution

### Karl Pearson's Correlation Coefficient ($r$)

Measures strength and direction of linear relationship between two variables $X$ and $Y$ ($-1 \le r \le 1$):

$$r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

### Linear Regression Lines

- **Regression Line of $Y$ on $X$:** $y - \bar{y} = b_{yx} (x - \bar{x})$ where $b_{yx} = r \frac{\sigma_y}{\sigma_x}$.
- **Regression Line of $X$ on $Y$:** $x - \bar{x} = b_{xy} (y - \bar{y})$ where $b_{xy} = r \frac{\sigma_x}{\sigma_y}$.
- **Relationship:** $r^2 = b_{yx} \cdot b_{xy}$.

### The Normal (Gaussian) Distribution

A continuous bell-shaped distribution defined by mean $\mu$ and standard deviation $\sigma$. The **Standard Normal Variable ($Z$)** is:

$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

## Statistical Formulas Master Table

| Metric / Term | Mathematical Formula | Key Property |
|---|---|---|
| Variance ($\sigma^2$) | $\frac{\sum x_i^2}{n} - (\bar{x})^2$ | Non-negative dispersion measure |
| Standard Deviation ($\sigma$) | $\sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$ | Measured in same units as data |
| Covariance $\text{Cov}(X, Y)$ | $\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n}$ | Unstandardized joint variation |
| Correlation ($r$) | $\frac{\text{Cov}(X, Y)}{\sigma_x \sigma_y}$ | $-1 \le r \le 1$ |
| Regression Product | $r^2 = b_{yx} \cdot b_{xy}$ | Coefficient of determination |
| Standard $Z$-Score | $Z = \frac{X - \mu}{\sigma}$ | Mean $= 0$, Variance $= 1$ |

## Important Formulas and Transformation Theorems

Effect of Linear Transformation $y_i = a x_i + b$ on Statistics:

$$\text{New Mean}: \bar{y} = a \bar{x} + b$$

$$\text{New Variance}: \sigma_y^2 = a^2 \sigma_x^2$$

$$\text{New Standard Deviation}: \sigma_y = |a| \sigma_x$$

$$\text{(Note: Adding constant } b \text{ changes the mean, but does NOT change variance or standard deviation!)}$$

## Common Exam Traps

- **Assuming Adding a Constant Changes Standard Deviation:** Believing that adding $+5$ to every number in a dataset increases standard deviation by $+5$. Standard deviation remains **completely unchanged** under translation.
- **Sign Mismatch in Correlation and Regression:** Assigning a positive correlation $r$ when regression coefficients $b_{yx}$ and $b_{xy}$ are negative. $r$ must take the **same sign** as $b_{yx}$ and $b_{xy}$.
- **Dividing by $n$ vs. $n-1$:** Using sample variance formula ($n-1$) when population variance ($n$) is explicitly required in entrance exam items.

## Quiz

1. If every value in a dataset with mean $\bar{x} = 20$ and standard deviation $\sigma = 4$ is multiplied by $3$ and then increased by $5$, what are the new mean and new standard deviation?
  - [ ] Mean $= 65$, New $\sigma = 17$
  - [x] Mean $= 65$, New $\sigma = 12$
  - [ ] Mean $= 60$, New $\sigma = 12$
  - [ ] Mean $= 65$, New $\sigma = 4$
   > New Mean $= 3(20) + 5 = 60 + 5 = 65$. New standard deviation $= |3| \times 4 = 12$ (the additive constant $+5$ does not affect standard deviation).

2. Calculate the variance of the first $5$ positive integers ($1, 2, 3, 4, 5$).
  - [ ] $1.5$
  - [x] $2.0$
  - [ ] $2.5$
  - [ ] $3.0$
   > Mean $\bar{x} = \frac{1+2+3+4+5}{5} = 3$. Squared sum $\sum x_i^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55$. Variance $\sigma^2 = \frac{55}{5} - (3)^2 = 11 - 9 = 2.0$.

3. Given regression coefficients $b_{yx} = 0.8$ and $b_{xy} = 0.45$, compute the correlation coefficient $r$.
  - [ ] $r = 0.36$
  - [x] $r = 0.6$
  - [ ] $r = 0.65$
  - [ ] $r = 0.85$
   > Use $r^2 = b_{yx} \cdot b_{xy} = (0.8)(0.45) = 0.36 \implies r = \sqrt{0.36} = 0.6$. (Since both regression coefficients are positive, $r = +0.6$).