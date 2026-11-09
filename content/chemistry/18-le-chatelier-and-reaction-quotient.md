---
title: Le Chatelier's Principle and the Reaction Quotient
level: intermediate
---

The **reaction quotient** $Q$ has the same form as $K$ but uses the concentrations (or pressures) present **at any moment**. Comparing the two shows which way a reaction will go:

- $Q < K$: not enough product, so the reaction proceeds **forward**.
- $Q = K$: at equilibrium.
- $Q > K$: too much product, so the reaction goes **backward**.

## Le Chatelier's principle

When a system at equilibrium is disturbed, it shifts to partly counteract the disturbance.

| Change | Shift | Effect on $K$ |
|---|---|---|
| Add reactant (or remove product) | forward | none |
| Increase pressure (decrease volume) | toward fewer moles of gas | none |
| Increase temperature | in the **endothermic** direction | changes |
| Add a catalyst | none (speeds both directions equally) | none |
| Add inert gas, constant volume | none (partial pressures unchanged) | none |
| Add inert gas, constant total pressure | toward more moles of gas (volume increases, so dilution) | none |

Only a temperature change alters $K$. A catalyst only helps the system reach equilibrium faster.

## The effect of temperature, quantitatively

The van't Hoff equation links the constants at two temperatures:

$$\ln\frac{K_2}{K_1} = \frac{\Delta H^\circ}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right).$$

For an endothermic reaction ($\Delta H > 0$), $K$ rises with temperature; for an exothermic one, it falls. Use $R = 8.314$ J mol$^{-1}$ K$^{-1}$ and $\Delta H$ in joules.

## Industrial compromise: the Haber process

$\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$ ($\Delta H = -92$ kJ) is favoured by high pressure and low temperature. But low temperature makes the reaction too slow, so a compromise of about $450\,^\circ$C, high pressure and an iron catalyst is used.

## Quiz

1. For $\mathrm{2SO_2 + O_2 \rightleftharpoons 2SO_3}$ at a certain temperature, $K_c = 280$. A mixture has $[\mathrm{SO_2}]=0.10$, $[\mathrm{O_2}]=0.10$ and $[\mathrm{SO_3}]=0.30$ M. Which statement is true?
   - [ ] $Q = 90$, so the reaction proceeds in the reverse direction.
   - [ ] $Q = 280$, so the mixture is at equilibrium.
   - [ ] $Q = 0.011$, so the reaction proceeds in the forward direction.
   - [x] $Q = 90$, so the reaction proceeds in the forward direction.
   > $Q = (0.30)^2/[(0.10)^2(0.10)] = 90$. Since $Q < K = 280$, there is too little product, so the reaction moves forward.

2. A reaction has $\Delta H^\circ = +50$ kJ mol$^{-1}$. By what factor does $K$ change when the temperature rises from $300$ K to $310$ K?
   - [ ] 0.52
   - [ ] 1.1
   - [x] 1.9
   - [ ] 3.8
   > $\ln(K_2/K_1) = (50000/8.314)(1/300 - 1/310) = 0.647$, so $K_2/K_1 = e^{0.647} = 1.9$. For an endothermic reaction $K$ increases with temperature, so the factor must exceed 1.

3. Argon is added to an equilibrium mixture of $\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$. How does the yield of $\mathrm{NH_3}$ change if the argon is added (i) at constant volume, and (ii) at constant total pressure?
   - [ ] Decreases; no change
   - [x] No change; decreases
   - [ ] Increases; decreases
   - [ ] No change; increases
   > At constant volume the partial pressures of the reacting gases do not change, so nothing shifts. At constant total pressure the volume expands, lowering the partial pressures, and the equilibrium shifts toward the side with more gas moles (reactants), reducing the ammonia yield.
