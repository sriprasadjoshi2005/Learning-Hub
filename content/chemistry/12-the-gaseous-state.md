---
title: The Gaseous State
level: intermediate
---

An **ideal gas** has point-like molecules with no attractions between them. Real gases behave almost ideally at **low pressure and high temperature**. Four laws describe ideal behaviour:

- **Boyle:** $PV = \text{constant}$ at fixed $n$ and $T$.
- **Charles:** $V/T = \text{constant}$ at fixed $n$ and $P$ (temperature in kelvin).
- **Avogadro:** equal volumes of gases at the same $T$ and $P$ contain equal numbers of molecules.
- **Combined:** $PV = nRT$.

The gas constant depends on the units: $R = 0.0821$ L atm mol$^{-1}$ K$^{-1}$ $= 8.314$ J mol$^{-1}$ K$^{-1}$. Mixing units is the most common error; check which one your pressure and volume demand.

## Density and molar mass

Writing $n = m/M$ in the ideal gas equation gives

$$d = \frac{PM}{RT} \qquad\text{so}\qquad M = \frac{dRT}{P}.$$

Gas density rises with pressure and falls with temperature, and heavier gases are denser at the same conditions.

## Dalton's law of partial pressures

In a mixture of non-reacting gases the total pressure is the sum of the partial pressures, and each partial pressure is the mole fraction times the total:

$$P_i = x_i\,P_{\text{total}}, \qquad P_{\text{total}} = \frac{n_{\text{total}}RT}{V}.$$

When a gas is collected over water, subtract the water's vapour pressure to get the pressure of the dry gas.

## Graham's law of diffusion and effusion

At constant $T$ and $P$, the rate of diffusion or effusion is inversely proportional to the square root of molar mass:

$$\frac{r_1}{r_2} = \sqrt{\frac{M_2}{M_1}}.$$

Since rate is inversely proportional to time for a fixed volume, the **time** taken varies as $\sqrt{M}$. A heavier gas takes longer, and four times the molar mass means twice the time.

## Quiz

1. What is the density of $\mathrm{CO_2}$ ($M=44.01$ g mol$^{-1}$) at $27\,^\circ\mathrm{C}$ and $2.00$ atm?
   - [ ] 1.79 g L$^{-1}$
   - [x] 3.57 g L$^{-1}$
   - [ ] 7.14 g L$^{-1}$
   - [ ] 0.28 g L$^{-1}$
   > $d = PM/RT = (2.00\times44.01)/(0.0821\times300) = 3.57$ g L$^{-1}$. Remember to convert $27\,^\circ\mathrm{C}$ to $300$ K.

2. A gas X takes twice as long as the same volume of methane ($M=16$) to effuse through a small hole under identical conditions. What is its molar mass?
   - [x] 64
   - [ ] 32
   - [ ] 128
   - [ ] 8
   > Time is proportional to $\sqrt{M}$, so $\sqrt{M_X/16}=2$, giving $M_X = 4\times16 = 64$. A common slip is to say 32 by doubling the mass instead of squaring the ratio.

3. A $10.0$ L vessel at $300$ K contains $4.0$ g of $\mathrm{H_2}$ and $28$ g of $\mathrm{N_2}$. What is the partial pressure of $\mathrm{H_2}$?
   - [ ] 2.46 atm
   - [ ] 7.35 atm
   - [ ] 3.67 atm
   - [x] 4.89 atm
   > Moles: $\mathrm{H_2}$ $=1.98$, $\mathrm{N_2}$ $=1.00$, total $2.98$. $P_{\text{total}} = nRT/V = 7.35$ atm, and $P_{\mathrm{H_2}} = (1.98/2.98)\times7.35 = 4.89$ atm. The value 7.35 atm is the total pressure, and 2.46 atm is the partial pressure of $\mathrm{N_2}$.
