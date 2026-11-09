---
title: The Solid State
level: intermediate
---

Solids are either **crystalline** (long-range order, sharp melting point, anisotropic) or **amorphous** (short-range order only, like glass, which softens over a range of temperature). The repeating pattern of a crystal is described by its **unit cell**.

## Cubic unit cells

| Cell | Atoms per cell $Z$ | Coordination number | Packing efficiency | Touching along |
|---|---|---|---|---|
| Simple cubic (SC) | 1 | 6 | 52.4% | edge: $a = 2r$ |
| Body-centred (BCC) | 2 | 8 | 68% | body diagonal: $\sqrt3\,a = 4r$ |
| Face-centred (FCC) | 4 | 12 | 74% | face diagonal: $\sqrt2\,a = 4r$ |

Atoms at corners count $\tfrac18$ each, on faces $\tfrac12$, on edges $\tfrac14$, and inside the cell $1$. Hexagonal close packing (hcp) and cubic close packing (FCC) are the two most efficient arrangements, both with 74% packing and coordination number 12.

## Density of a crystal

$$\rho = \frac{Z\,M}{a^3\,N_A}$$

Keep units consistent: with $a$ in cm and $M$ in g mol$^{-1}$, the density is in g cm$^{-3}$. Remember that $1\ \text{pm} = 10^{-10}$ cm.

## Voids

Close-packed structures contain **tetrahedral** voids ($2$ per atom) and **octahedral** voids ($1$ per atom). In an ionic crystal, the larger ions form the lattice and the smaller ions occupy voids, with the radius ratio $r_+/r_-$ deciding which type.

## Point defects

- **Schottky defect:** equal numbers of cations and anions are missing. The **density decreases**. It is common in ionic compounds where the two ions are similar in size, such as NaCl.
- **Frenkel defect:** an ion leaves its site and sits in an interstitial position. The density is **unchanged**. It occurs when the cation is much smaller than the anion, as in AgBr and ZnS.
- **Non-stoichiometric defects** include metal excess (F-centres, which give colour) and metal deficiency.

## Quiz

1. Copper crystallises in an FCC lattice with an edge length of $361$ pm. What is its density? ($M = 63.55$ g mol$^{-1}$)
   - [ ] 4.49 g cm$^{-3}$
   - [ ] 17.9 g cm$^{-3}$
   - [ ] 2.99 g cm$^{-3}$
   - [x] 8.97 g cm$^{-3}$
   > $\rho = ZM/(a^3N_A) = 4(63.55)/[(3.61\times10^{-8})^3\times6.022\times10^{23}] = 8.97$ g cm$^{-3}$. Using $Z=2$ (as if BCC) would give the value 4.49.

2. An element crystallises in a BCC lattice with an edge length of $400$ pm. What is the atomic radius?
   - [ ] 100 pm
   - [ ] 141 pm
   - [x] 173 pm
   - [ ] 200 pm
   > In BCC, atoms touch along the body diagonal: $\sqrt3\,a = 4r$, so $r = \sqrt3(400)/4 = 173$ pm. The value 141 pm is what you would get for FCC ($\sqrt2\,a/4$).

3. Which statement about point defects is correct?
   - [ ] Schottky defects are common when the cation is much smaller than the anion.
   - [x] Frenkel defects leave the density unchanged, but Schottky defects lower it.
   - [ ] Frenkel defects remove equal numbers of cations and anions from the lattice.
   - [ ] Both defects raise the density of the crystal.
   > In a Frenkel defect, the ion only moves, so mass and volume stay the same. In a Schottky defect, ions leave the crystal altogether, so the density falls. The first two options have the descriptions swapped.
