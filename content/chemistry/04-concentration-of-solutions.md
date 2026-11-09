---
title: Concentration of Solutions
level: foundation
---

A solution is a homogeneous mixture of a **solute** dissolved in a **solvent**. Chemists express how much solute is present in several ways, and exam problems mix them freely, so you must be able to convert between them.

| Quantity | Definition | Depends on temperature? |
|---|---|---|
| Molarity $M$ | moles of solute per litre of **solution** | Yes (volume changes) |
| Molality $m$ | moles of solute per kg of **solvent** | No (mass does not change) |
| Mole fraction $x_A$ | $n_A / (n_A + n_B + \dots)$ | No |
| Mass percent | grams of solute per 100 g of solution | No |

## Converting between units

The bridge between mass-based and volume-based units is **density**. For a solution of mass percent $w$ and density $d$ (g mL$^{-1}$):

$$M = \frac{10\, w\, d}{M_{\text{solute}}}$$

The factor of 10 comes from converting 1000 mL to litres and the percentage to a fraction. For dilute aqueous solutions, molarity and molality are nearly equal because 1 L of solution is close to 1 kg of water; for concentrated solutions they differ a lot.

## Dilution and mixing

Adding solvent does not change the moles of solute, so
$$M_1V_1 = M_2V_2.$$
When mixing solutions, add the **moles** first and divide by the **total volume**. Do not average the molarities unless the volumes are equal, and never forget that a salt may release more than one ion per formula unit: $\mathrm{CaCl_2}$ gives two moles of $\mathrm{Cl^-}$ per mole.

## Mole fraction from molality

A solution that is $m$ molal contains $m$ mol of solute per 1000 g of water, and $1000/18.02 = 55.49$ mol of water. So
$$x_{\text{solute}} = \frac{m}{m + 55.49}.$$

## Quiz

1. Concentrated sulfuric acid is 98% $\mathrm{H_2SO_4}$ by mass with density 1.84 g mL$^{-1}$ ($M=98.08$ g mol$^{-1}$). What is its molarity?
   - [ ] 9.2 M
   - [x] 18.4 M
   - [ ] 36.8 M
   - [ ] 10.0 M
   > $M = 10\times98\times1.84/98.08 = 18.4$ M. Per litre there are $1840$ g of solution, of which $98\%=1803$ g is acid, and $1803/98.08=18.4$ mol.

2. $200$ mL of $0.50$ M $\mathrm{NaCl}$ is mixed with $300$ mL of $0.20$ M $\mathrm{CaCl_2}$. Assuming volumes are additive, what is the concentration of $\mathrm{Cl^-}$?
   - [x] 0.44 M
   - [ ] 0.35 M
   - [ ] 0.22 M
   - [ ] 0.60 M
   > Moles of $\mathrm{Cl^-}$: from NaCl $0.200\times0.50=0.100$; from $\mathrm{CaCl_2}$ $0.300\times0.20\times2=0.120$. Total $0.220$ mol in $0.500$ L gives $0.44$ M. The value 0.35 M simply averages 0.5 and 0.2.

3. What is the mole fraction of solute in a 2.00 molal aqueous solution?
   - [ ] 0.0174
   - [ ] 0.0360
   - [ ] 0.0720
   - [x] 0.0348
   > Water: $1000/18.02=55.49$ mol. $x = 2.00/(2.00+55.49)=0.0348$. The value 0.0360 divides by the moles of water alone, forgetting that the solute is also part of the total.
