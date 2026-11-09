---
title: Electrochemical Cells and the Nernst Equation
level: intermediate
---

A **galvanic (voltaic) cell** turns the energy of a spontaneous redox reaction into electrical energy. Oxidation occurs at the **anode** (negative terminal) and reduction at the **cathode** (positive terminal). Electrons flow through the external wire from anode to cathode, while ions move through a salt bridge to complete the circuit and keep each half-cell neutral.

## Cell notation and standard potentials

The Daniell cell is written $\mathrm{Zn(s)\,|\,Zn^{2+}(aq)\,\|\,Cu^{2+}(aq)\,|\,Cu(s)}$. Each half-reaction has a **standard reduction potential** $E^\circ$ measured against the standard hydrogen electrode (SHE, defined as $0$ V). Some values (V): $\mathrm{Zn^{2+}/Zn}$ $-0.76$, $\mathrm{Fe^{2+}/Fe}$ $-0.44$, $\mathrm{Cu^{2+}/Cu}$ $+0.34$, $\mathrm{Ag^+/Ag}$ $+0.80$.

$$E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$$

Never multiply $E^\circ$ by stoichiometric coefficients. It is an intensive property. A positive $E^\circ_{\text{cell}}$ means a spontaneous reaction. A metal with a more negative $E^\circ$ is a stronger reducing agent and will displace metals below it.

## Link to thermodynamics

$$\Delta G^\circ = -nFE^\circ_{\text{cell}} \qquad \log K = \frac{nE^\circ_{\text{cell}}}{0.0592}\ \text{(at 298 K)}$$

where $F = 96485$ C mol$^{-1}$ and $n$ is the number of electrons transferred. At equilibrium, $E_{\text{cell}} = 0$ and the cell is "dead".

## The Nernst equation

Under non-standard concentrations,

$$E = E^\circ - \frac{0.0592}{n}\log Q \quad (298\ \text{K}).$$

For $\mathrm{Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu}$, $Q = [\mathrm{Zn^{2+}}]/[\mathrm{Cu^{2+}}]$. Pure solids do not appear in $Q$.

A **concentration cell** has identical electrodes in solutions of different concentration. Here $E^\circ = 0$, and the emf comes entirely from the concentration difference: current flows until the two concentrations equalise.

## Quiz

1. A Daniell cell ($E^\circ = 1.10$ V) has $[\mathrm{Zn^{2+}}] = 0.01$ M and $[\mathrm{Cu^{2+}}] = 1.0$ M at $298$ K. What is its emf?
   - [ ] 1.04 V
   - [ ] 1.10 V
   - [ ] 1.22 V
   - [x] 1.16 V
   > $E = 1.10 - (0.0592/2)\log(0.01/1.0) = 1.10 + 0.0592 = 1.16$ V. Low $[\mathrm{Zn^{2+}}]$ makes $Q$ small, which favours the forward reaction and raises the emf.

2. What is the emf of the concentration cell $\mathrm{Ag\,|\,Ag^+(0.001\ M)\,\|\,Ag^+(0.1\ M)\,|\,Ag}$ at $298$ K?
   - [ ] 0.059 V
   - [ ] 0.177 V
   - [x] 0.118 V
   - [ ] 0.236 V
   > $E = (0.0592/1)\log(0.1/0.001) = 0.0592\times2 = 0.118$ V. Here $n=1$ for $\mathrm{Ag^+}$, and the more concentrated side is the cathode.

3. What is the equilibrium constant for $\mathrm{Zn + Cu^{2+} \rightleftharpoons Zn^{2+} + Cu}$ at $298$ K ($E^\circ_{\text{cell}} = 1.10$ V, $n=2$)?
   - [ ] $3.8\times10^{18}$
   - [x] $1.5\times10^{37}$
   - [ ] $2.2\times10^{74}$
   - [ ] $12.6$
   > $\log K = nE^\circ/0.0592 = 2(1.10)/0.0592 = 37.2$, so $K \approx 1.5\times10^{37}$. The value $3.8\times10^{18}$ forgets the factor $n=2$.
