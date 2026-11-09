---
title: Physical Chemistry Numerical Strategies
level: exam
---

Numerical questions in JEE and board exams are won or lost on method, not on difficult maths. A reliable routine saves marks.

## A five-step routine

1. **Write the formula first**, with symbols, before substituting numbers.
2. **Convert units** before anything else: $^\circ$C to K, mL to L, kJ to J, pm to cm, minutes to seconds.
3. **Choose the right constant**: $R = 0.0821$ L atm mol$^{-1}$ K$^{-1}$ or $8.314$ J mol$^{-1}$ K$^{-1}$, matching your other units.
4. **Estimate** the answer's size and sign before calculating. A negative pH or a yield above 100% signals an error.
5. **Check units and significant figures** at the end.

## Common traps

- $\ln x = 2.303\log_{10}x$, and confusing them changes answers by a factor of about 2.3.
- Weak acid and base approximations: $[\mathrm{H^+}] = \sqrt{K_aC}$ is valid only if ionisation is under about 5%.
- For salt hydrolysis, use $K_h = K_w/K_a$ (or $K_w/K_b$), never $K_a$ itself.
- Count every ion a salt releases: $\mathrm{CaCl_2}$ gives $2\ \mathrm{Cl^-}$ per formula unit.
- Titrations: compare **moles** (or milliequivalents), not volumes. For $\mathrm{H_2SO_4}$ with NaOH the ratio is $1:2$.

## Linking quantities

| Chain | Route |
|---|---|
| Electrolysis | $I,t \rightarrow Q \rightarrow$ mol of electrons $\rightarrow$ mol of substance $\rightarrow$ mass |
| Gas problems | $PV = nRT \rightarrow n \rightarrow m = nM$ |
| Equilibrium | ICE table $\rightarrow K_c$ or $K_p$ ($K_p = K_c(RT)^{\Delta n}$) |
| Thermochemistry | moles $\times\ \Delta H$ per mole |

## Quiz

1. What is the pH of $0.010$ M $\mathrm{NH_4Cl}$? ($K_b$ of $\mathrm{NH_3} = 1.8\times10^{-5}$)
   - [ ] 3.37
   - [x] 5.63
   - [ ] 7.00
   - [ ] 8.37
   > $\mathrm{NH_4^+}$ is a weak acid with $K_a = K_w/K_b = 5.6\times10^{-10}$. $[\mathrm{H^+}] = \sqrt{5.6\times10^{-10}\times0.010} = 2.4\times10^{-6}$, so pH $=5.63$. The value 8.37 comes from mistakenly treating that quantity as $[\mathrm{OH^-}]$.

2. $14.3$ g of a gas occupies $4.0$ L at $2.0$ atm and $27\,^\circ$C. What is its molar mass?
   - [x] 44.0 g mol$^{-1}$
   - [ ] 11.0 g mol$^{-1}$
   - [ ] 22.0 g mol$^{-1}$
   - [ ] 88.1 g mol$^{-1}$
   > $M = mRT/(PV) = 14.3\times0.0821\times300/(2.0\times4.0) = 44.0$ g mol$^{-1}$. Forgetting to convert $27\,^\circ$C to $300$ K would give a very different, wrong value.

3. For how long must a current of $2.00$ A flow to deposit $10.8$ g of silver from $\mathrm{AgNO_3}$? ($M_{\mathrm{Ag}} = 107.87$ g mol$^{-1}$)
   - [ ] 8.05 min
   - [ ] 40.3 min
   - [ ] 161 min
   - [x] 80.5 min
   > $10.8$ g is $0.100$ mol of Ag, needing $0.100$ mol of electrons ($z=1$), which is $0.100\times96485 = 9660$ C. Then $t = Q/I = 9660/2.00 = 4830$ s $= 80.5$ min.
