---
title: Acids, Bases and pH
level: intermediate
---

Three definitions are used, each wider than the last:

- **Arrhenius:** acids give $\mathrm{H^+}$ in water; bases give $\mathrm{OH^-}$.
- **Brønsted-Lowry:** an acid is a proton donor and a base is a proton acceptor. Every acid has a **conjugate base**, and a stronger acid has a weaker conjugate base.
- **Lewis:** an acid accepts an electron pair; a base donates one. This covers $\mathrm{BF_3}$ and $\mathrm{Al^{3+}}$ as acids.

## Water and pH

Water ionises slightly, and at $25\,^\circ$C

$$K_w = [\mathrm{H^+}][\mathrm{OH^-}] = 1.0\times10^{-14}, \qquad \mathrm{pH} + \mathrm{pOH} = 14.$$

$$\mathrm{pH} = -\log[\mathrm{H^+}].$$

Because pH is logarithmic, a change of one pH unit means a tenfold change in $[\mathrm{H^+}]$. Neutral water has pH 7 at $25\,^\circ$C only; $K_w$ increases with temperature, so hot water has a pH below 7 but is still neutral.

## Weak acids and bases

A weak acid $\mathrm{HA}$ ionises only partially:

$$K_a = \frac{[\mathrm{H^+}][\mathrm{A^-}]}{[\mathrm{HA}]}.$$

For an initial concentration $C$ with small ionisation, $[\mathrm{H^+}] \approx \sqrt{K_aC}$ and the degree of ionisation is $\alpha = \sqrt{K_a/C}$ (Ostwald's dilution law). Weak acids ionise **more** as they are diluted. For a conjugate pair,

$$K_a \times K_b = K_w.$$

## Pitfalls

- For a very dilute strong acid (near $10^{-7}$ M), water's own $\mathrm{H^+}$ matters. Solve $[\mathrm{H^+}]^2 - C[\mathrm{H^+}] - K_w = 0$ rather than taking $\mathrm{pH} = -\log C$, which would wrongly give a basic pH for an acid.
- When mixing an acid and a base, calculate **moles** first. The excess reagent, divided by the **total volume**, gives the concentration.

## Quiz

1. What is the pH of $1.0\times10^{-8}$ M HCl at $25\,^\circ$C?
   - [x] 6.98
   - [ ] 8.00
   - [ ] 7.00
   - [ ] 6.00
   > An acid cannot give a pH above 7. Water contributes $\mathrm{H^+}$ too, so $[\mathrm{H^+}]^2 - 10^{-8}[\mathrm{H^+}] - 10^{-14} = 0$ gives $[\mathrm{H^+}] = 1.05\times10^{-7}$ M, so pH $=6.98$.

2. What is the pH of $0.10$ M acetic acid ($K_a = 1.8\times10^{-5}$)?
   - [ ] 1.00
   - [ ] 4.74
   - [ ] 3.37
   - [x] 2.87
   > $[\mathrm{H^+}] \approx \sqrt{K_aC} = \sqrt{1.8\times10^{-6}} = 1.34\times10^{-3}$ M, so pH $=2.87$. The value 1.00 treats the acid as strong, and 4.74 is its $\mathrm{p}K_a$.

3. A $0.10$ M solution of a weak base $\mathrm{B}$ has a pH of $11.00$. What is $K_b$?
   - [ ] $1.0\times10^{-3}$
   - [ ] $1.0\times10^{-6}$
   - [x] $1.0\times10^{-5}$
   - [ ] $1.0\times10^{-8}$
   > pOH $=3$, so $[\mathrm{OH^-}] = 10^{-3}$ M. $K_b = [\mathrm{BH^+}][\mathrm{OH^-}]/[\mathrm{B}] = (10^{-3})^2/(0.10-10^{-3}) \approx 1.0\times10^{-5}$.
