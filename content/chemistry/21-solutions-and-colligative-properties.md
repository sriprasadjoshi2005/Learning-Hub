---
title: Solutions and Colligative Properties
level: intermediate
---

**Colligative properties** depend only on the **number** of dissolved solute particles, not on what they are. There are four: lowering of vapour pressure, elevation of boiling point, depression of freezing point, and osmotic pressure. They apply to dilute solutions of **non-volatile** solutes.

## Raoult's law

For a solution with a non-volatile solute, the vapour pressure of the solvent is $P = x_{\text{solvent}}P^\circ$, so the relative lowering is

$$\frac{P^\circ - P}{P^\circ} = x_{\text{solute}}.$$

For two volatile liquids, each follows $P_i = x_iP_i^\circ$ in an ideal solution. Positive deviation (weaker A-B attractions, e.g. ethanol-water) raises the vapour pressure and lowers the boiling point; negative deviation (stronger A-B attractions, e.g. acetone-chloroform) does the opposite.

## Boiling point elevation and freezing point depression

$$\Delta T_b = i\,K_b\,m \qquad \Delta T_f = i\,K_f\,m$$

where $m$ is **molality** and $K_b$, $K_f$ depend only on the solvent. For water, $K_b = 0.512$ and $K_f = 1.86$ K kg mol$^{-1}$.

## Osmotic pressure

Osmosis is the flow of solvent across a semipermeable membrane toward the more concentrated solution. The pressure needed to stop it is

$$\pi = i\,C\,R\,T$$

with $C$ in mol L$^{-1}$. Because the relationship has the form of the ideal gas law, it works well even for macromolecules, where freezing-point changes are too small to measure.

## The van't Hoff factor

$i$ is the ratio of particles actually present to the number of formula units dissolved:

- A salt that dissociates completely: $i \approx$ number of ions ($\mathrm{NaCl}$ about 2, $\mathrm{CaCl_2}$ about 3).
- **Association** (e.g. ethanoic acid dimerising in benzene): $i < 1$.
- For a solute that dissociates with degree $\alpha$ into $n$ particles, $i = 1 + (n-1)\alpha$; for association into dimers, $i = 1 - \alpha/2$.

## Quiz

1. What is the freezing point of a solution of $6.0$ g urea ($M=60.06$) in $200$ g of water? ($K_f = 1.86$ K kg mol$^{-1}$)
   - [ ] $-0.19\,^\circ$C
   - [ ] $-1.86\,^\circ$C
   - [x] $-0.93\,^\circ$C
   - [ ] $-0.46\,^\circ$C
   > $m = (6.0/60.06)/0.200 = 0.50$ mol kg$^{-1}$, and urea does not dissociate ($i=1$). $\Delta T_f = 1.86\times0.50 = 0.93$ K, so the solution freezes at $-0.93\,^\circ$C. Using $0.100$ kg of solvent by mistake would give $-1.86$.

2. What is the osmotic pressure of $0.010$ M NaCl (assume complete dissociation) at $300$ K?
   - [ ] 0.25 atm
   - [x] 0.49 atm
   - [ ] 0.74 atm
   - [ ] 0.98 atm
   > $\pi = iCRT = 2\times0.010\times0.0821\times300 = 0.49$ atm. The value 0.25 atm ignores the dissociation ($i=1$).

3. A solute dimerises in benzene with a degree of association of $0.80$. What is the van't Hoff factor?
   - [x] 0.60
   - [ ] 0.20
   - [ ] 0.40
   - [ ] 1.80
   > Starting with 1 mol, $0.80$ mol of molecules form $0.40$ mol of dimers, leaving $0.20$ mol of monomers: $0.20 + 0.40 = 0.60$ mol of particles. This is $i = 1 - \alpha/2 = 0.60$. A value below 1 is the signature of association.
