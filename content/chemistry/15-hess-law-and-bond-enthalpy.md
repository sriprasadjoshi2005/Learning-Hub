---
title: Hess's Law and Bond Enthalpy
level: intermediate
---

Because enthalpy is a state function, the total $\Delta H$ for a reaction is the same whether it occurs in one step or in several. This is **Hess's law**, and it lets us calculate enthalpies that cannot be measured directly.

## Using enthalpies of formation

The **standard enthalpy of formation** $\Delta_f H^\circ$ is the enthalpy change when one mole of a compound forms from its elements in their standard states. By definition, $\Delta_f H^\circ = 0$ for an element in its standard state. Then

$$\Delta_r H^\circ = \sum n\,\Delta_f H^\circ(\text{products}) - \sum n\,\Delta_f H^\circ(\text{reactants}).$$

Multiply each value by its stoichiometric coefficient, and take care with physical states: $\mathrm{H_2O(l)}$ is $-285.8$ kJ mol$^{-1}$ but $\mathrm{H_2O(g)}$ is $-241.8$.

## Combining equations

To apply Hess's law to a set of reactions:

1. Reverse an equation and its $\Delta H$ changes sign.
2. Multiply an equation by a factor and $\Delta H$ is multiplied by the same factor.
3. Add the equations so that the intermediates cancel, and add the $\Delta H$ values.

## Bond enthalpy

The **bond enthalpy** is the energy needed to break one mole of a particular bond in the gas phase. Breaking bonds requires energy (positive) and forming bonds releases it:

$$\Delta_r H \approx \sum \text{BE(bonds broken)} - \sum \text{BE(bonds formed)}.$$

Values are averages, so results are estimates. Only gas-phase species work with this method; liquids and solids need extra terms for vaporisation or sublimation.

## Other named enthalpies

| Enthalpy | Process |
|---|---|
| Combustion | one mole of substance burns completely in oxygen |
| Atomisation | one mole of gaseous atoms forms from the element |
| Neutralisation | one mole of water forms from an acid and a base (about $-57$ kJ for strong ones) |
| Lattice | one mole of solid ionic compound forms from its gaseous ions |

## Quiz

1. Given $\Delta_f H^\circ$ ($\mathrm{kJ\,mol^{-1}}$): $\mathrm{CO_2(g)}$ $-393.5$, $\mathrm{H_2O(l)}$ $-285.8$, $\mathrm{C_2H_4(g)}$ $+52.3$. What is $\Delta H^\circ$ for $\mathrm{C_2H_4 + 3O_2 \rightarrow 2CO_2 + 2H_2O(l)}$?
   - [x] $-1410.9$ kJ
   - [ ] $-1125.1$ kJ
   - [ ] $-1306.3$ kJ
   - [ ] $-1323.0$ kJ
   > $2(-393.5)+2(-285.8)-(+52.3) = -1410.9$ kJ. The value $-1125.1$ forgets the coefficient 2 on water, $-1306.3$ adds the $\mathrm{C_2H_4}$ term instead of subtracting it, and $-1323.0$ uses gaseous water.

2. Estimate $\Delta H$ for $\mathrm{C_2H_4 + H_2 \rightarrow C_2H_6}$ using bond enthalpies (kJ mol$^{-1}$): C=C 614, C-C 348, C-H 413, H-H 436.
   - [ ] $+124$ kJ
   - [ ] $-266$ kJ
   - [ ] $-390$ kJ
   - [x] $-124$ kJ
   > Broken: C=C and H-H, $614+436=1050$. Formed: one C-C and two new C-H, $348+826=1174$. $\Delta H = 1050-1174 = -124$ kJ. The value $-390$ forgets that the C=C bond is converted, not fully broken, to a single bond.

3. $\mathrm{C(graphite)+O_2 \rightarrow CO_2}$ has $\Delta H=-393.5$ kJ and $\mathrm{CO + \tfrac12 O_2 \rightarrow CO_2}$ has $\Delta H=-283.0$ kJ. What is $\Delta H$ for $\mathrm{C(graphite)+\tfrac12 O_2 \rightarrow CO}$?
   - [ ] $-676.5$ kJ
   - [ ] $+110.5$ kJ
   - [x] $-110.5$ kJ
   - [ ] $-283.0$ kJ
   > Reverse the second equation (giving $+283.0$ kJ) and add it to the first: $-393.5+283.0=-110.5$ kJ. Adding without reversing gives the incorrect value $-676.5$ kJ.
