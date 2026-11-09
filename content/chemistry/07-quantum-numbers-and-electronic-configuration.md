---
title: Quantum Numbers and Electronic Configuration
level: foundation
---

In the quantum mechanical model, an electron's state is described by four **quantum numbers**:

| Symbol | Name | Allowed values | Determines |
|---|---|---|---|
| $n$ | principal | $1, 2, 3, \dots$ | shell, size, energy |
| $l$ | azimuthal | $0$ to $n-1$ | subshell shape ($s,p,d,f$ for $0,1,2,3$) |
| $m_l$ | magnetic | $-l$ to $+l$ | orbital orientation |
| $m_s$ | spin | $\pm\tfrac12$ | spin direction |

A subshell with quantum number $l$ has $2l+1$ orbitals, and each orbital holds at most two electrons. A shell therefore holds $2n^2$ electrons.

## Nodes

A **node** is a region where the probability of finding the electron is zero.

$$\text{radial nodes} = n - l - 1 \qquad \text{angular nodes} = l \qquad \text{total nodes} = n - 1$$

## Filling rules

- **Aufbau principle:** orbitals fill in increasing energy, which follows the $(n+l)$ rule, and for equal $(n+l)$, the lower $n$ first. This gives $1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, \dots$
- **Pauli exclusion principle:** no two electrons in an atom have the same four quantum numbers.
- **Hund's rule:** electrons occupy degenerate orbitals singly, with parallel spins, before pairing.

## Exceptions

Half-filled and fully filled $d$ subshells have extra stability from exchange energy and symmetry. So chromium is $[\mathrm{Ar}]\,3d^5 4s^1$ (not $3d^4 4s^2$) and copper is $[\mathrm{Ar}]\,3d^{10} 4s^1$. When transition metals form cations, they lose the $4s$ electrons **first**, even though $4s$ fills before $3d$.

## Quiz

1. How many electrons in an atom can have $n=3$ and $m_l=+1$?
   - [x] 4
   - [ ] 2
   - [ ] 6
   - [ ] 10
   > For $n=3$, $l$ can be 0, 1 or 2, and $m_l=+1$ exists only for $l=1$ and $l=2$ (since $m_l$ runs from $-l$ to $+l$). That is two orbitals, each holding 2 electrons, so 4 electrons.

2. What are the numbers of unpaired electrons in a ground-state Cr atom and in a $\mathrm{Cu^+}$ ion, respectively?
   - [ ] 4 and 0
   - [ ] 6 and 1
   - [ ] 4 and 1
   - [x] 6 and 0
   > Cr is $3d^5 4s^1$, giving 6 unpaired electrons. Cu is $3d^{10}4s^1$; removing the $4s$ electron gives $\mathrm{Cu^+}$ as $3d^{10}$, with none unpaired.

3. What is the total number of nodes (radial plus angular) in a $4d$ orbital?
   - [ ] 1
   - [ ] 2
   - [x] 3
   - [ ] 4
   > Total nodes $= n-1 = 3$. These are $n-l-1=1$ radial node and $l=2$ angular nodes. The number of total nodes does not depend on $l$.
