---
title: Buffers, Hydrolysis and Solubility Product
level: intermediate
---

## Buffer solutions

A **buffer** resists changes in pH when small amounts of acid or base are added. It contains a weak acid with its conjugate base (or a weak base with its conjugate acid) in comparable amounts. Added $\mathrm{OH^-}$ is consumed by the acid, and added $\mathrm{H^+}$ by the base. The pH is given by the **Henderson-Hasselbalch equation**:

$$\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}.$$

A buffer works best when the ratio is near 1, so $\mathrm{pH} \approx \mathrm{p}K_a$, within about one unit. Dilution does not change the ratio, so it barely changes the pH, but it reduces the buffer capacity. When a strong acid or base is added, use stoichiometry first to update the moles of $\mathrm{HA}$ and $\mathrm{A^-}$, then apply the equation.

## Salt hydrolysis

A salt dissolves into ions, which may react with water:

| Salt of | Example | Solution |
|---|---|---|
| strong acid + strong base | $\mathrm{NaCl}$ | neutral |
| weak acid + strong base | $\mathrm{CH_3COONa}$ | basic |
| strong acid + weak base | $\mathrm{NH_4Cl}$ | acidic |
| weak acid + weak base | $\mathrm{CH_3COONH_4}$ | depends on $K_a$ and $K_b$ |

For a salt of a weak acid, the hydrolysis constant is $K_h = K_w/K_a$, and
$$\mathrm{pH} = 7 + \tfrac12\left(\mathrm{p}K_a + \log C\right).$$

## Solubility product

For a sparingly soluble salt $\mathrm{A_xB_y}$, the solid is in equilibrium with its ions, and

$$K_{sp} = [\mathrm{A}^{y+}]^x[\mathrm{B}^{x-}]^y.$$

If the molar solubility is $s$: for $\mathrm{AgCl}$, $K_{sp} = s^2$; for $\mathrm{CaF_2}$, $K_{sp} = 4s^3$.

- **Precipitation occurs** when the ion product $Q > K_{sp}$.
- **Common ion effect:** adding an ion already in the equilibrium lowers solubility, because the equilibrium shifts to the solid.

## Quiz

1. What is the pH of a buffer containing $0.20$ M $\mathrm{CH_3COOH}$ and $0.10$ M $\mathrm{CH_3COONa}$? ($\mathrm{p}K_a = 4.74$)
   - [ ] 4.74
   - [x] 4.44
   - [ ] 5.04
   - [ ] 4.14
   > $\mathrm{pH} = 4.74 + \log(0.10/0.20) = 4.74 - 0.30 = 4.44$. The ratio is base over acid, so having more acid pushes the pH below the $\mathrm{p}K_a$. The value 5.04 inverts the ratio.

2. $0.010$ mol of solid NaOH is added to $1.00$ L of a buffer containing $0.10$ mol of $\mathrm{CH_3COOH}$ and $0.10$ mol of $\mathrm{CH_3COO^-}$ ($\mathrm{p}K_a = 4.74$). What is the new pH, ignoring any volume change?
   - [x] 4.83
   - [ ] 4.74
   - [ ] 5.04
   - [ ] 12.00
   > The $\mathrm{OH^-}$ converts $0.010$ mol of acid to base: $\mathrm{HA}=0.09$, $\mathrm{A^-}=0.11$. $\mathrm{pH} = 4.74 + \log(0.11/0.09) = 4.83$, a change of only $0.09$ units. The same amount of NaOH added to pure water would raise the pH to 12.

3. What is the molar solubility of $\mathrm{AgCl}$ ($K_{sp} = 1.8\times10^{-10}$) in $0.10$ M NaCl?
   - [ ] $1.3\times10^{-5}$ M
   - [ ] $1.8\times10^{-10}$ M
   - [ ] $1.8\times10^{-11}$ M
   - [x] $1.8\times10^{-9}$ M
   > In $0.10$ M NaCl, $[\mathrm{Cl^-}] \approx 0.10$ M, so $s = K_{sp}/[\mathrm{Cl^-}] = 1.8\times10^{-9}$ M. In pure water $s = \sqrt{K_{sp}} = 1.3\times10^{-5}$ M, and the common ion lowers it by a factor of about $7000$.
