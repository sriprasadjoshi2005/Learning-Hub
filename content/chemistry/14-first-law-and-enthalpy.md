---
title: First Law of Thermodynamics and Enthalpy
level: intermediate
---

Thermodynamics tracks energy changes. We separate the **system** (what we study) from its **surroundings**. The sign convention used in most Indian boards and JEE is:

- $q > 0$ when heat flows **into** the system; $w > 0$ when work is done **on** the system.

## The first law

Energy is conserved:

$$\Delta U = q + w$$

For gas expansion against a constant external pressure, $w = -P_{\text{ext}}\Delta V$ (the system loses energy as it pushes back the surroundings). The internal energy $U$ and enthalpy $H$ are **state functions**, so their change depends only on the initial and final states; $q$ and $w$ are not.

## Reversible isothermal work

For an ideal gas expanding slowly (reversibly) at constant temperature, $\Delta U = 0$ because $U$ depends only on $T$, so $q = -w$ and

$$w_{\text{rev}} = -nRT\ln\frac{V_2}{V_1}.$$

Natural logarithm, not base 10, and the work done by the gas is the **maximum** possible for that expansion.

## Enthalpy

At constant pressure, the heat exchanged equals the change in enthalpy $H = U + PV$:

$$q_P = \Delta H, \qquad \Delta H = \Delta U + \Delta n_g RT$$

where $\Delta n_g$ is the change in the number of moles of **gas** in the balanced equation. If $\Delta n_g = 0$, then $\Delta H \approx \Delta U$.

## Heat capacity

$C_P$ and $C_V$ are the heat needed to raise the temperature of one mole by 1 K at constant pressure and constant volume. For an ideal gas $C_P - C_V = R$, and $C_P > C_V$ because at constant pressure some of the heat is also used for expansion work.

## Special cases

- **Isothermal:** $\Delta T = 0$, so $\Delta U = 0$.
- **Adiabatic:** $q = 0$, so $\Delta U = w$.
- **Free expansion** (into a vacuum): $w = 0$, and if also insulated, $q=0$ so $\Delta U = 0$.

## Quiz

1. Two moles of an ideal gas expand reversibly and isothermally from $10$ L to $20$ L at $300$ K. What is the work done on the gas?
   - [ ] $+3.46$ kJ
   - [ ] $-1.50$ kJ
   - [ ] $-4.99$ kJ
   - [x] $-3.46$ kJ
   > $w = -nRT\ln(V_2/V_1) = -2(8.314)(300)\ln2 = -3.46$ kJ. The sign is negative because the gas does the work. The value $-1.50$ kJ comes from using $\log_{10}$ instead of $\ln$, and $-4.99$ kJ omits the logarithm.

2. For $\mathrm{N_2(g) + 3H_2(g) \rightarrow 2NH_3(g)}$, $\Delta H = -92.2$ kJ at $298$ K. What is $\Delta U$?
   - [ ] $-97.2$ kJ
   - [ ] $-92.2$ kJ
   - [x] $-87.2$ kJ
   - [ ] $-89.7$ kJ
   > $\Delta n_g = 2-4 = -2$. $\Delta U = \Delta H - \Delta n_g RT = -92.2 + 2(8.314)(298)/1000 = -87.2$ kJ. The value $-89.7$ kJ would result from using $\Delta n_g=-1$.

3. An ideal gas expands into an evacuated container (free expansion) and the whole system is thermally insulated. Which statement is correct?
   - [ ] The temperature falls because the gas does work.
   - [x] $q = 0$, $w = 0$, $\Delta U = 0$, and the temperature is unchanged.
   - [ ] $q > 0$ because the gas spreads out.
   - [ ] $\Delta U < 0$ because the volume increases.
   > There is nothing to push against, so $w=0$; insulation gives $q=0$. Then $\Delta U = 0$, and since $U$ of an ideal gas depends only on temperature, $T$ stays the same.
