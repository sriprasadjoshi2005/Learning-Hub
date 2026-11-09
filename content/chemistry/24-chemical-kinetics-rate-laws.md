---
title: Chemical Kinetics: Rate Laws
level: intermediate
---

Thermodynamics says whether a reaction can happen; **kinetics** says how fast. The **rate** is the change in concentration per unit time. For $a\mathrm{A} + b\mathrm{B} \rightarrow$ products, the experimentally found **rate law** is

$$\text{rate} = k[\mathrm{A}]^m[\mathrm{B}]^n$$

where $m$ and $n$ are the **orders** with respect to each reactant and $m+n$ is the overall order. Orders come from experiment and need not equal the stoichiometric coefficients. The rate constant $k$ has units that depend on the overall order $x$: $(\text{mol L}^{-1})^{1-x}\,\text{s}^{-1}$. So zero order is mol L$^{-1}$ s$^{-1}$, first order is s$^{-1}$, and second order is L mol$^{-1}$ s$^{-1}$.

## Method of initial rates

Compare experiments in which only one concentration changes. If doubling $[\mathrm{A}]$ makes the rate go up 4 times, the order in A is 2; if it doubles the rate, the order is 1; if it has no effect, the order is 0. Then use any one experiment to calculate $k$.

## Molecularity and mechanism

**Molecularity** is the number of species colliding in an **elementary** step (1, 2 or rarely 3), always a whole number. Orders can be fractional or zero. For a multi-step mechanism, the rate law is set by the **slowest (rate-determining) step**.

## First-order reactions

For $\mathrm{A} \rightarrow$ products with rate $= k[\mathrm{A}]$:

$$\ln\frac{[\mathrm{A}]_0}{[\mathrm{A}]} = kt, \qquad t_{1/2} = \frac{0.693}{k}.$$

The half-life is **independent of the initial concentration**, which is the signature of first-order kinetics (radioactive decay is the standard example). After $n$ half-lives, the fraction remaining is $(1/2)^n$.

## Quiz

1. For $\mathrm{A + B \rightarrow}$ products, initial rates were $2.0\times10^{-3}$ for $[\mathrm{A}]=[\mathrm{B}]=0.10$ M; $8.0\times10^{-3}$ for $[\mathrm{A}]=0.20$, $[\mathrm{B}]=0.10$; and $1.6\times10^{-2}$ for $[\mathrm{A}]=0.20$, $[\mathrm{B}]=0.20$ (mol L$^{-1}$ s$^{-1}$). What are the overall order and $k$?
   - [ ] 2; $0.20$ L mol$^{-1}$ s$^{-1}$
   - [x] 3; $2.0$ L$^2$ mol$^{-2}$ s$^{-1}$
   - [ ] 3; $20$ L$^2$ mol$^{-2}$ s$^{-1}$
   - [ ] 2; $2.0$ L mol$^{-1}$ s$^{-1}$
   > Doubling A raises the rate fourfold, so order 2 in A. Doubling B doubles the rate, so order 1 in B. Rate $= k[\mathrm{A}]^2[\mathrm{B}]$, and $k = 2.0\times10^{-3}/(0.10^2\times0.10) = 2.0$ L$^2$ mol$^{-2}$ s$^{-1}$.

2. A first-order reaction is 75% complete after $40$ minutes. What is the rate constant?
   - [x] 0.0347 min$^{-1}$
   - [ ] 0.0173 min$^{-1}$
   - [ ] 0.0693 min$^{-1}$
   - [ ] 0.0116 min$^{-1}$
   > 75% complete means two half-lives have passed, so $t_{1/2} = 20$ min and $k = 0.693/20 = 0.0347$ min$^{-1}$. Check: $k = (1/40)\ln4 = 0.0347$.

3. For a first-order reaction, approximately how many half-lives are needed for 99.9% completion?
   - [ ] 3.3
   - [ ] 5
   - [ ] 100
   - [x] 10
   > $t = (1/k)\ln(1000)$ and $t_{1/2} = \ln2/k$, so $t/t_{1/2} = \ln1000/\ln2 = 9.97 \approx 10$. After 10 half-lives only $(1/2)^{10} \approx 0.1\%$ remains.
