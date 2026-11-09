---
title: Chemical Equilibrium: Kc and Kp
level: intermediate
---

Many reactions do not go to completion. They reach **dynamic equilibrium**, where the forward and reverse rates are equal and the concentrations stay constant, though both reactions continue. For
$$a\mathrm{A} + b\mathrm{B} \rightleftharpoons c\mathrm{C} + d\mathrm{D}$$
the equilibrium constant is

$$K_c = \frac{[\mathrm{C}]^c[\mathrm{D}]^d}{[\mathrm{A}]^a[\mathrm{B}]^b}, \qquad K_p = \frac{P_{\mathrm{C}}^{\,c}P_{\mathrm{D}}^{\,d}}{P_{\mathrm{A}}^{\,a}P_{\mathrm{B}}^{\,b}}.$$

Pure solids and pure liquids do not appear in the expression. The two constants are related by

$$K_p = K_c\,(RT)^{\Delta n_g}$$

with $R = 0.0821$ L atm mol$^{-1}$ K$^{-1}$ when pressures are in atm.

## Rules for manipulating K

- Reverse the reaction: $K' = 1/K$.
- Multiply the equation by $n$: $K' = K^n$.
- Add two reactions: multiply their $K$ values.
- Temperature is the **only** thing that changes the value of $K$.

A large $K$ means products are favoured, and a small $K$ means reactants are favoured, but $K$ says nothing about how fast equilibrium is reached.

## Solving problems: the ICE table

1. Write **I**nitial amounts, the **C**hange in terms of $x$ using the stoichiometry, and **E**quilibrium amounts.
2. Substitute into the expression for $K$.
3. Solve for $x$. If $K$ is very small, assume $x$ is negligible next to the initial value and check afterwards that it is under about 5%.

## Degree of dissociation

For $\mathrm{N_2O_4 \rightleftharpoons 2NO_2}$ starting with 1 mol and dissociating a fraction $\alpha$, the equilibrium mixture contains $(1-\alpha)$ of $\mathrm{N_2O_4}$ and $2\alpha$ of $\mathrm{NO_2}$, for a total of $(1+\alpha)$ moles. At total pressure $P$:

$$K_p = \frac{4\alpha^2 P}{1-\alpha^2}.$$

## Quiz

1. For $\mathrm{H_2 + I_2 \rightleftharpoons 2HI}$, $K_c = 49$. If $1.0$ mol each of $\mathrm{H_2}$ and $\mathrm{I_2}$ are placed in a $1.0$ L container, what is $[\mathrm{HI}]$ at equilibrium?
   - [ ] 0.78 M
   - [ ] 1.00 M
   - [x] 1.56 M
   - [ ] 0.44 M
   > $K_c = (2x)^2/(1-x)^2 = 49$, so $2x/(1-x) = 7$ and $x = 7/9 = 0.778$. Then $[\mathrm{HI}] = 2x = 1.56$ M. The value 0.78 M is $x$, not $2x$.

2. For $\mathrm{PCl_5(g) \rightleftharpoons PCl_3(g) + Cl_2(g)}$, $K_c = 0.040$ at $500$ K. What is $K_p$ (pressures in atm)?
   - [ ] 0.040
   - [x] 1.64
   - [ ] $9.7\times10^{-4}$
   - [ ] 16.4
   > $\Delta n_g = 2 - 1 = +1$, so $K_p = K_c(RT) = 0.040\times0.0821\times500 = 1.64$. The value $9.7\times10^{-4}$ divides by $RT$ instead of multiplying.

3. For $\mathrm{N_2O_4 \rightleftharpoons 2NO_2}$, $K_p = 0.14$ atm. What is the degree of dissociation at a total pressure of $1.0$ atm?
   - [x] 0.18
   - [ ] 0.034
   - [ ] 0.50
   - [ ] 0.37
   > $K_p = 4\alpha^2P/(1-\alpha^2)$ rearranges to $\alpha^2 = K_p/(4P+K_p) = 0.14/4.14 = 0.0338$, so $\alpha = 0.18$. The value 0.034 is $\alpha^2$, not $\alpha$.
