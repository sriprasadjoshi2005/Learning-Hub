---
title: Ratios, Proportions and Rates
level: foundation
---

Ratios compare quantities of similar units, proportions establish the equality of two ratios, and rates compare quantities with different units. These concepts form the backbone of scale modeling, mixture problems, and work-rate-time applications.

## Ratios and Proportions

A **ratio** $a : b$ (read as "$a$ to $b$") compares two quantities $a$ and $b$ of the same dimension, written as the fraction $\frac{a}{b}$ where $b \neq 0$.

- **Scaling Ratios:** Multiplying or dividing both terms of a ratio by a non-zero scalar $k$ preserves the ratio: $a : b = (a \cdot k) : (b \cdot k)$.
- **Dividing a Total into Ratios:** If a total quantity $T$ is divided in the ratio $a : b : c$, the share corresponding to $a$ is:
$$\text{Share of } a = T \cdot \frac{a}{a + b + c}$$

### Proportions and Fundamental Theorem of Proportion

A **proportion** is an equation stating that two ratios are equal: $\frac{a}{b} = \frac{c}{d}$ or $a : b = c : d$.

- **Extremes and Means:** In $a : b = c : d$, $a$ and $d$ are called the *extremes*, while $b$ and $c$ are called the *means*.
- **Cross-Multiplication Rule:**
$$\frac{a}{b} = \frac{c}{d} \iff a \cdot d = b \cdot c$$
- **Types of Proportion:**
  - *Direct Proportion ($y \propto x$):* $y = k \cdot x \implies \frac{y_1}{x_1} = \frac{y_2}{x_2}$. As $x$ increases, $y$ increases proportionally.
  - *Inverse Proportion ($y \propto \frac{1}{x}$):* $y = \frac{k}{x} \implies x_1 \cdot y_1 = x_2 \cdot y_2$. As $x$ increases, $y$ decreases proportionally.

## Rates, Speed, and Work Applications

A **rate** is a comparison of two quantities measured in different units (e.g., speed in $\text{km/h}$, rate of work in $\text{tasks/hour}$).

### Distance, Speed, and Time
$$\text{Distance } (D) = \text{Speed } (S) \times \text{Time } (T)$$

$$\text{Average Speed} = \frac{\text{Total Distance Traveled}}{\text{Total Time Taken}}$$

### Work and Time Rate Formula
If a person or machine completes a whole task in $W$ hours, their work rate $R$ is $R = \frac{1}{W}$ task per hour. When multiple independent entities work together, their rates add up linearly:

$$R_{\text{combined}} = R_1 + R_2 = \frac{1}{W_1} + \frac{1}{W_2} \implies T_{\text{together}} = \frac{W_1 \cdot W_2}{W_1 + W_2}$$

## Summary Table of Proportionality Rules

| Relationship Type | Mathematical Form | Constant Statement | Key Operational Formula |
|---|---|---|---|
| Direct Variation | $y \propto x$ | $\frac{y}{x} = k$ | $\frac{y_1}{x_1} = \frac{y_2}{x_2}$ |
| Inverse Variation | $y \propto \frac{1}{x}$ | $x \cdot y = k$ | $x_1 \cdot y_1 = x_2 \cdot y_2$ |
| Joint Variation | $z \propto x \cdot y$ | $\frac{z}{x \cdot y} = k$ | $\frac{z_1}{x_1 \cdot y_1} = \frac{z_2}{x_2 \cdot y_2}$ |
| Work Rate | $\text{Work} = \text{Rate} \times \text{Time}$ | $\text{Task} = 1$ | $R_{\text{total}} = R_1 + R_2 + \dots$ |

## Important Formulas and Structural Theorems

Properties of Proportions (given $\frac{a}{b} = \frac{c}{d}$):

$$\text{Componendo}: \frac{a + b}{b} = \frac{c + d}{d}$$

$$\text{Dividendo}: \frac{a - b}{b} = \frac{c - d}{d}$$

$$\text{Componendo and Dividendo}: \frac{a + b}{a - b} = \frac{c + d}{c - d}$$

Average Speed for Two Equal Distances (with speeds $v_1$ and $v_2$):

$$v_{\text{avg}} = \frac{2 \cdot v_1 \cdot v_2}{v_1 + v_2}$$

## Common Exam Traps

- **Arithmetic Mean of Speeds Error:** Calculating average speed as $\frac{v_1 + v_2}{2}$ when distances traveled at each speed are equal. The correct formula requires using harmonic mean: $\frac{2 v_1 v_2}{v_1 + v_2}$.
- **Adding Work Times Directly:** Assuming if Worker A takes $6$ hours and Worker B takes $3$ hours, working together takes $6 + 3 = 9$ hours. Rates must be added ($\frac{1}{6} + \frac{1}{3} = \frac{1}{2} \implies 2$ hours).
- **Unit Inconsistency:** Mixing incompatible units such as multiplying speed in $\text{km/h}$ by time in minutes without converting time to hours ($\div 60$).

## Quiz

1. Three partners share profits of $\$60,000$ in the ratio $2 : 3 : 5$. What is the share of the partner receiving the largest portion?
  - [ ] $\$18,000$
  - [ ] $\$24,000$
  - [x] $\$30,000$
  - [ ] $\$36,000$
   > Sum of ratio parts $= 2 + 3 + 5 = 10$. The largest share corresponds to $5$ parts. Share $= 60,000 \times \frac{5}{10} = \$30,000$.

2. If $12$ workers can construct a wall in $8$ days, how many days will it take $6$ workers to build the exact same wall, assuming equal individual work rates?
  - [ ] $4$ days
  - [ ] $12$ days
  - [x] $16$ days
  - [ ] $24$ days
   > Number of workers and time taken are inversely proportional ($W_1 \cdot T_1 = W_2 \cdot T_2$). So, $12 \times 8 = 6 \times T_2 \implies 96 = 6 T_2 \implies T_2 = 16$ days.

3. Pump A fills a reservoir in $4$ hours, while Pump B drains the full reservoir in $6$ hours. If both pumps operate simultaneously on an empty reservoir, how long will it take to fill it completely?
  - [ ] $2.4$ hours
  - [ ] $10$ hours
  - [x] $12$ hours
  - [ ] $5$ hours
   > Fill rate of A $= +\frac{1}{4}$ reservoir/hr. Drain rate of B $= -\frac{1}{6}$ reservoir/hr. Combined net rate $= \frac{1}{4} - \frac{1}{6} = \frac{3-2}{12} = \frac{1}{12}$ reservoir/hr. Total time $= 12$ hours.