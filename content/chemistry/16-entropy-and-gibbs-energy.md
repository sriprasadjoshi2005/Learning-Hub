---
title: Entropy and Gibbs Energy
level: intermediate
---

The first law says energy is conserved, but not which processes actually happen. Ice melts above $0\,^\circ$C and never refreezes by itself in a warm room. The second law gives the direction.

## Entropy

**Entropy** $S$ measures the number of ways energy and matter can be arranged (disorder). For a reversible process at constant temperature,

$$\Delta S = \frac{q_{\text{rev}}}{T}.$$

Entropy rises when a solid melts or a liquid boils, when a gas expands, when a solute dissolves, and when a reaction produces more moles of gas. It falls when gas is converted to liquid or solid, or when $\Delta n_g < 0$. The **second law**: the total entropy of the system plus surroundings increases in a spontaneous process. The **third law**: the entropy of a perfect crystal at $0$ K is zero.

## Gibbs energy: one criterion for the system alone

Tracking the surroundings is awkward, so at constant $T$ and $P$ we use

$$\Delta G = \Delta H - T\Delta S.$$

- $\Delta G < 0$: spontaneous.
- $\Delta G = 0$: at equilibrium.
- $\Delta G > 0$: non-spontaneous (the reverse reaction is spontaneous).

| $\Delta H$ | $\Delta S$ | Spontaneous? |
|---|---|---|
| $-$ | $+$ | at all temperatures |
| $+$ | $-$ | never |
| $-$ | $-$ | only at low $T$ |
| $+$ | $+$ | only at high $T$ |

For the last two, the **crossover temperature** is $T = \Delta H/\Delta S$, where $\Delta G = 0$. Keep units consistent: $\Delta H$ is usually in kJ, but $\Delta S$ is in J K$^{-1}$.

## Link to the equilibrium constant

$$\Delta G^\circ = -RT\ln K = -2.303\,RT\log K$$

A negative $\Delta G^\circ$ means $K > 1$ (products favoured); a positive one means $K < 1$. Note that $\Delta G^\circ$ refers to standard conditions, whereas $\Delta G$ at any moment depends on the reaction quotient: $\Delta G = \Delta G^\circ + RT\ln Q$.

## Quiz

1. For $\mathrm{CaCO_3(s) \rightarrow CaO(s) + CO_2(g)}$, $\Delta H = +178$ kJ and $\Delta S = +161$ J K$^{-1}$. Above roughly what temperature does the decomposition become spontaneous?
   - [ ] 1.11 K
   - [x] 1106 K
   - [ ] 2212 K
   - [ ] 553 K
   > $T = \Delta H/\Delta S = 178000/161 = 1106$ K. The value 1.11 K results from forgetting to convert kJ to J.

2. A reaction has $\Delta G^\circ = -11.4$ kJ mol$^{-1}$ at $298$ K. What is the approximate equilibrium constant?
   - [x] 100
   - [ ] 10
   - [ ] 4.6
   - [ ] 1000
   > $\ln K = 11400/(8.314\times298) = 4.60$, so $K = e^{4.60}\approx100$. The value 4.6 is $\ln K$ itself, not $K$.

3. Which of the following reactions has a positive $\Delta S$?
   - [ ] $\mathrm{2H_2(g) + O_2(g) \rightarrow 2H_2O(l)}$
   - [ ] $\mathrm{CaO(s) + CO_2(g) \rightarrow CaCO_3(s)}$
   - [ ] $\mathrm{N_2(g) + 3H_2(g) \rightarrow 2NH_3(g)}$
   - [x] $\mathrm{N_2O_4(g) \rightarrow 2NO_2(g)}$
   > Only the last increases the number of gas moles ($1 \to 2$). The others convert gas to liquid or solid, or reduce the gas moles from 4 to 2, so $\Delta S$ is negative.
