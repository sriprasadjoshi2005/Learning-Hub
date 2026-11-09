---
title: Arrhenius Equation, Catalysis and Half-life
level: intermediate
---

## Collision theory and activation energy

For a reaction to occur, molecules must collide with enough energy and the right orientation. The minimum energy needed is the **activation energy** $E_a$. Raising the temperature increases the fraction of molecules above $E_a$, which is why a $10\ \mathrm{K}$ rise often doubles the rate.

## The Arrhenius equation

$$k = A\,e^{-E_a/RT} \qquad\Longleftrightarrow\qquad \ln k = \ln A - \frac{E_a}{RT}$$

$A$ is the frequency factor (collision rate and orientation). A plot of $\ln k$ against $1/T$ is a straight line with slope $-E_a/R$. Comparing two temperatures:

$$\ln\frac{k_2}{k_1} = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right).$$

Use $R = 8.314$ J mol$^{-1}$ K$^{-1}$ and convert $E_a$ to **joules**. A larger $E_a$ makes the rate more sensitive to temperature.

## Catalysis

A **catalyst** provides an alternative pathway with a lower activation energy. It is not consumed, and it speeds up the forward and reverse reactions equally. It therefore changes **neither** $\Delta H$ nor the equilibrium constant, only how fast equilibrium is reached. Because $k$ depends exponentially on $E_a$, even a modest drop gives a huge rate increase.

## Half-life by order

| Order | Integrated form | Half-life |
|---|---|---|
| Zero | $[\mathrm{A}]_0 - [\mathrm{A}] = kt$ | $[\mathrm{A}]_0/2k$ |
| First | $\ln([\mathrm{A}]_0/[\mathrm{A}]) = kt$ | $0.693/k$ |
| Second | $1/[\mathrm{A}] - 1/[\mathrm{A}]_0 = kt$ | $1/(k[\mathrm{A}]_0)$ |

Only the first-order half-life is independent of the starting concentration. For zero-order reactions it is proportional to $[\mathrm{A}]_0$, and for second-order it is **inversely** proportional.

## Quiz

1. The rate of a reaction doubles when the temperature rises from $298$ K to $308$ K. What is the activation energy?
   - [ ] 5.3 kJ mol$^{-1}$
   - [ ] 26.5 kJ mol$^{-1}$
   - [x] 52.9 kJ mol$^{-1}$
   - [ ] 105.8 kJ mol$^{-1}$
   > $E_a = R\ln2\,/(1/298 - 1/308) = 8.314\times0.693/1.089\times10^{-4} = 5.29\times10^4$ J mol$^{-1}$, or $52.9$ kJ mol$^{-1}$.

2. A catalyst lowers the activation energy of a reaction from $75$ kJ mol$^{-1}$ to $50$ kJ mol$^{-1}$ at $300$ K, with the same frequency factor. By roughly what factor does the rate increase?
   - [ ] 1.5
   - [x] $2.3\times10^4$
   - [ ] 25
   - [ ] $1.0\times10^{10}$
   > The rate ratio is $e^{\Delta E_a/RT} = e^{25000/(8.314\times300)} = e^{10.0} \approx 2.3\times10^4$. A drop of only $25$ kJ mol$^{-1}$ makes the reaction tens of thousands of times faster.

3. A second-order reaction has $k = 0.50$ L mol$^{-1}$ s$^{-1}$ and an initial concentration of $0.20$ M. What is its half-life?
   - [x] 10 s
   - [ ] 1.4 s
   - [ ] 5 s
   - [ ] 20 s
   > For second order, $t_{1/2} = 1/(k[\mathrm{A}]_0) = 1/(0.50\times0.20) = 10$ s. The value 1.4 s results from wrongly using the first-order formula, $0.693/k$.
