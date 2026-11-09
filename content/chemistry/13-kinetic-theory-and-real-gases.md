---
title: Kinetic Theory and Real Gases
level: intermediate
---

The **kinetic theory** explains gas laws from molecular motion. It assumes molecules are in constant random motion, collisions are perfectly elastic, the molecular volume is negligible, and there are no intermolecular forces. The key results:

- The average kinetic energy per mole is $\tfrac32 RT$. It depends only on temperature, not on the gas.
- At the same temperature, lighter molecules move faster.

## Three kinds of average speed

$$u_{\text{rms}} = \sqrt{\frac{3RT}{M}} \qquad u_{\text{avg}} = \sqrt{\frac{8RT}{\pi M}} \qquad u_{\text{mp}} = \sqrt{\frac{2RT}{M}}$$

with $M$ in **kg mol$^{-1}$** and $R = 8.314$ J mol$^{-1}$ K$^{-1}$. They are in the ratio $u_{\text{mp}} : u_{\text{avg}} : u_{\text{rms}} = 1 : 1.128 : 1.224$. Raising the temperature shifts the Maxwell-Boltzmann distribution to higher speeds and flattens it.

## Why real gases deviate

Two assumptions fail: molecules **do** occupy volume, and they **do** attract one another. The **compressibility factor** $Z = PV/nRT$ equals 1 for an ideal gas.

- At moderate pressure, attractions dominate and $Z < 1$.
- At very high pressure, the finite molecular size dominates (molecules cannot be compressed further) and $Z > 1$.
- For $\mathrm{H_2}$ and $\mathrm{He}$, attractions are so weak that $Z > 1$ at almost all pressures at room temperature.

## The van der Waals equation

$$\left(P + \frac{a\,n^2}{V^2}\right)(V - nb) = nRT$$

The constant $a$ corrects for attractions (larger for easily liquefied gases) and $b$ for the volume excluded by the molecules (roughly four times the actual molecular volume). The critical constants follow from $a$ and $b$:

$$T_c = \frac{8a}{27Rb}, \qquad P_c = \frac{a}{27b^2}, \qquad V_c = 3b.$$

Above $T_c$ a gas cannot be liquefied by pressure alone. The **Boyle temperature**, where a real gas behaves ideally over a range of pressure, is $T_B = a/(Rb)$.

## Quiz

1. What is the root mean square speed of $\mathrm{O_2}$ ($M=0.032$ kg mol$^{-1}$) at $300$ K?
   - [ ] 395 m s$^{-1}$
   - [ ] 446 m s$^{-1}$
   - [x] 484 m s$^{-1}$
   - [ ] 684 m s$^{-1}$
   > $u_{\text{rms}} = \sqrt{3\times8.314\times300/0.032} = 484$ m s$^{-1}$. The values 395 and 446 are the most probable and average speeds, and 684 is $\sqrt2$ times the rms value.

2. At very high pressure, the compressibility factor $Z$ of a real gas is greater than 1 mainly because:
   - [ ] intermolecular attractions become dominant
   - [x] the finite volume of the molecules makes the gas harder to compress than an ideal gas
   - [ ] the average kinetic energy of the molecules decreases
   - [ ] the gas has been cooled below its critical temperature
   > At very high pressure the molecules are packed so tightly that their own volume (the constant $b$) matters most, so $PV$ exceeds $nRT$. Attractions cause $Z<1$ at moderate pressure instead.

3. $\mathrm{O_2}$ has van der Waals constants $a = 1.36$ L$^2$ atm mol$^{-2}$ and $b = 0.0318$ L mol$^{-1}$. What is its critical temperature?
   - [x] 154 K
   - [ ] 521 K
   - [ ] 77 K
   - [ ] 308 K
   > $T_c = 8a/(27Rb) = 8(1.36)/(27\times0.0821\times0.0318) = 154$ K. The value 521 K is $a/(Rb)$, which is the Boyle temperature, not the critical temperature.
