---
title: Intrinsic and Extrinsic Semiconductors
level: intermediate
---

# Intrinsic and Extrinsic Semiconductors

The electrical conductivity of a semiconductor depends on the concentration of mobile electrons and holes within its crystal structure.

A pure semiconductor produces charge carriers mainly through thermal excitation. However, its conductivity can be increased and controlled by deliberately introducing small quantities of selected impurities.

This process is called doping.

Semiconductors are therefore classified into two major categories:

1. Intrinsic semiconductors: chemically pure semiconductor materials.
2. Extrinsic semiconductors: semiconductor materials whose electrical properties have been modified through doping.

Understanding these two categories is essential for studying PN junction diodes, transistors, integrated circuits, and other semiconductor devices.

## 1. Intrinsic Semiconductors

An intrinsic semiconductor is a semiconductor material in its pure form, without intentionally added impurity atoms.

Examples include:

- Pure silicon.
- Pure germanium.

In an intrinsic semiconductor, electrical conduction occurs because of thermally generated electron-hole pairs.

### 1.1 Charge Carrier Generation

At absolute zero, an ideal intrinsic semiconductor has all its valence electrons involved in covalent bonding.

As temperature increases, some electrons gain sufficient thermal energy to move into the conduction band.

Each electron that enters the conduction band leaves behind a hole in the valence band.

Therefore, electrons and holes are generated in equal numbers.

\[
n=p=n_i
\]

Where:

- \(n\) = electron concentration.
- \(p\) = hole concentration.
- \(n_i\) = intrinsic carrier concentration.

All concentrations are commonly expressed in carriers per cubic metre or per cubic centimetre.

### 1.2 Conductivity of an Intrinsic Semiconductor

The general conductivity equation is:

\[
\sigma=q(n\mu_n+p\mu_p)
\]

For an intrinsic semiconductor:

\[
n=p=n_i
\]

Substituting:

\[
\sigma_i=q(n_i\mu_n+n_i\mu_p)
\]

Taking \(qn_i\) common:

\[
\boxed{\sigma_i=qn_i(\mu_n+\mu_p)}
\]

Where:

- \(\sigma_i\) = intrinsic conductivity.
- \(q\) = magnitude of electron charge.
- \(n_i\) = intrinsic carrier concentration.
- \(\mu_n\) = electron mobility.
- \(\mu_p\) = hole mobility.

### 1.3 Temperature Dependence

The intrinsic carrier concentration increases rapidly with temperature.

An approximate relationship is:

\[
n_i\propto T^{3/2}e^{-E_g/(2kT)}
\]

Where:

- \(T\) = absolute temperature in kelvin.
- \(E_g\) = semiconductor energy gap.
- \(k\) = Boltzmann constant.
- \(e\) = base of the natural exponential function.

The exact carrier concentration depends on the material and temperature.

As temperature increases, more electrons gain enough energy to cross the forbidden energy gap.

Consequently, intrinsic semiconductor conductivity generally increases.

## 2. Extrinsic Semiconductors

An extrinsic semiconductor is produced by intentionally adding a small quantity of impurity atoms to a pure semiconductor.

This process is called doping.

The purpose of doping is to increase the concentration of one type of charge carrier and control the electrical conductivity of the material.

The two major types are:

1. N-type semiconductor.
2. P-type semiconductor.

The impurity atoms used in doping are called dopants.

## 3. N-Type Semiconductors

An N-type semiconductor is formed by doping a pure tetravalent semiconductor, such as silicon or germanium, with a pentavalent impurity.

A pentavalent impurity has five valence electrons.

Common pentavalent dopants include:

- Phosphorus.
- Arsenic.
- Antimony.

### 3.1 Formation of N-Type Material

Consider a silicon crystal.

Each silicon atom has four valence electrons and normally forms four covalent bonds with neighbouring atoms.

When a phosphorus atom replaces a silicon atom in the crystal lattice:

- Four of its five valence electrons participate in covalent bonding.
- The fifth electron is weakly bound compared with the bonding electrons.
- A relatively small amount of energy can release this electron into the conduction band.

The phosphorus atom becomes a positively charged donor ion after releasing the electron.

The released electron contributes to electrical conduction.

### 3.2 Donor Impurities

Pentavalent impurities are called donor impurities because they donate electrons to the semiconductor.

Their energy level lies close to the conduction band.

Only a small amount of thermal energy is generally required to move a donor electron into the conduction band.

### 3.3 Majority and Minority Carriers

In an N-type semiconductor:

- Electrons are the majority carriers.
- Holes are the minority carriers.

The word majority does not mean that holes are absent.

A small number of holes still exist because of thermal generation.

For a semiconductor at thermal equilibrium, the mass-action law is:

\[
\boxed{np=n_i^2}
\]

Where:

- \(n\) = electron concentration.
- \(p\) = hole concentration.
- \(n_i\) = intrinsic carrier concentration.

For an N-type semiconductor in which donor atoms are fully ionized and donor concentration is much greater than intrinsic carrier concentration:

\[
n\approx N_D
\]

Therefore:

\[
p\approx\frac{n_i^2}{N_D}
\]

Where \(N_D\) is the donor concentration.

## 4. P-Type Semiconductors

A P-type semiconductor is formed by doping a pure tetravalent semiconductor with a trivalent impurity.

A trivalent impurity has three valence electrons.

Common trivalent dopants include:

- Boron.
- Aluminium.
- Gallium.
- Indium.

### 4.1 Formation of P-Type Material

When a boron atom replaces a silicon atom in the crystal lattice:

- Three valence electrons form three covalent bonds.
- The fourth bond lacks an electron.
- This incomplete bond creates a hole.

A nearby valence electron can move into the incomplete bond, leaving a new hole behind.

The hole therefore appears to move through the crystal.

The boron atom can accept an electron and is called an acceptor impurity.

### 4.2 Acceptor Impurities

Trivalent impurities are called acceptor impurities because they can accept electrons from neighbouring covalent bonds.

Their energy level lies close to the valence band.

A relatively small amount of energy allows electrons to move from the valence band into acceptor states, leaving holes behind.

### 4.3 Majority and Minority Carriers

In a P-type semiconductor:

- Holes are the majority carriers.
- Electrons are the minority carriers.

For a P-type semiconductor with fully ionized acceptors and negligible compensation:

\[
p\approx N_A
\]

Using the mass-action law:

\[
n\approx\frac{n_i^2}{N_A}
\]

Where \(N_A\) is the acceptor concentration.

## 5. Comparison of N-Type and P-Type Semiconductors

| Property | N-Type | P-Type |
|---|---|---|
| Dopant | Pentavalent | Trivalent |
| Examples | Phosphorus, arsenic | Boron, gallium |
| Impurity role | Donor | Acceptor |
| Majority carriers | Electrons | Holes |
| Minority carriers | Holes | Electrons |
| Main carrier contribution | Electron conduction | Hole conduction |
| Fermi level | Closer to conduction band | Closer to valence band |

Both types remain electrically neutral overall.

Doping changes the concentration of mobile charge carriers; it does not make the entire semiconductor positively or negatively charged.

## 6. Energy-Band Representation of Doped Semiconductors

Doping introduces impurity energy levels within the forbidden energy gap.

### 6.1 N-Type Energy Bands

Donor energy levels lie slightly below the conduction band.

An electron can move from the donor level into the conduction band with relatively little energy.

Simplified representation:

    Energy ↑

    ┌─────────────────────────┐
    │     Conduction Band     │
    └─────────────────────────┘
             ↑
    ─────────────────────────
         Donor Level

    ─────────────────────────
         Valence Band

### 6.2 P-Type Energy Bands

Acceptor energy levels lie slightly above the valence band.

Electrons can move from the valence band into acceptor levels, creating holes in the valence band.

Simplified representation:

    Energy ↑

    ┌─────────────────────────┐
    │     Conduction Band     │
    └─────────────────────────┘

    ─────────────────────────
         Acceptor Level
             ↑

    ┌─────────────────────────┐
    │       Valence Band      │
    └─────────────────────────┘

These diagrams are simplified and not drawn to scale.

## 7. The Fermi Level

The Fermi level is an important energy reference used to describe the probability that an available electron energy state is occupied.

At thermal equilibrium, the Fermi-Dirac occupation probability is:

\[
f(E)=\frac{1}{1+e^{(E-E_F)/(kT)}}
\]

Where:

- \(f(E)\) = probability that an energy state at energy \(E\) is occupied.
- \(E_F\) = Fermi energy.
- \(k\) = Boltzmann constant.
- \(T\) = absolute temperature.

For an intrinsic semiconductor, the Fermi level is approximately near the middle of the forbidden energy gap.

For an N-type semiconductor, the Fermi level shifts closer to the conduction band.

For a P-type semiconductor, it shifts closer to the valence band.

The Fermi level helps explain carrier concentrations and the behaviour of semiconductor junctions.

## 8. The Mass-Action Law

At thermal equilibrium, the product of electron and hole concentrations is:

\[
\boxed{np=n_i^2}
\]

This relationship is known as the mass-action law.

It applies to non-degenerate semiconductors under thermal equilibrium.

### 8.1 Example: N-Type Semiconductor

Suppose an N-type silicon sample has:

\[
n_i=1.0\times10^{10}\,cm^{-3}
\]

and:

\[
N_D=1.0\times10^{16}\,cm^{-3}
\]

Assuming complete donor ionization:

\[
n\approx N_D
\]

Therefore:

\[
p=\frac{n_i^2}{n}
\]

\[
p=\frac{(1.0\times10^{10})^2}{1.0\times10^{16}}
\]

\[
p=\frac{1.0\times10^{20}}{1.0\times10^{16}}
\]

\[
\boxed{p=1.0\times10^4\,cm^{-3}}
\]

The electron concentration is much greater than the hole concentration.

## 9. Worked Numerical Examples

### Example 1: Conductivity of an N-Type Semiconductor

**Given:**

- Electron concentration: \(n=5\times10^{20}\,m^{-3}\).
- Hole concentration: \(p=2\times10^{15}\,m^{-3}\).
- Electron mobility: \(\mu_n=0.13\,m^2/(V\cdot s)\).
- Hole mobility: \(\mu_p=0.05\,m^2/(V\cdot s)\).
- Electron charge: \(q=1.6\times10^{-19}\,C\).

Calculate the conductivity.

**Formula:**

\[
\sigma=q(n\mu_n+p\mu_p)
\]

**Solution:**

\[
\sigma=1.6\times10^{-19}
[(5\times10^{20})(0.13)+(2\times10^{15})(0.05)]
\]

\[
\sigma=1.6\times10^{-19}
[6.5\times10^{19}+1.0\times10^{14}]
\]

The hole contribution is very small compared with the electron contribution.

\[
\sigma\approx1.6\times10^{-19}\times6.5\times10^{19}
\]

\[
\boxed{\sigma\approx10.4\,S/m}
\]

**Final Answer:**

\[
\boxed{\sigma\approx10.4\,S/m}
\]

### Example 2: Minority Carrier Concentration

**Given:**

- Intrinsic carrier concentration: \(n_i=1.5\times10^{10}\,cm^{-3}\).
- Donor concentration: \(N_D=1.0\times10^{16}\,cm^{-3}\).

Assume complete donor ionization and negligible compensation.

Calculate the minority carrier concentration.

**Formula:**

\[
np=n_i^2
\]

For an N-type semiconductor:

\[
n\approx N_D
\]

Therefore:

\[
p=\frac{n_i^2}{N_D}
\]

**Solution:**

\[
p=\frac{(1.5\times10^{10})^2}{1.0\times10^{16}}
\]

\[
p=\frac{2.25\times10^{20}}{1.0\times10^{16}}
\]

\[
\boxed{p=2.25\times10^4\,cm^{-3}}
\]

**Final Answer:**

The minority hole concentration is:

\[
\boxed{2.25\times10^4\,cm^{-3}}
\]

## 10. Doping Concentration and Compensation

The amount of impurity added determines the conductivity of an extrinsic semiconductor.

A higher concentration of electrically active dopants generally increases the majority carrier concentration.

However, conductivity does not increase indefinitely in direct proportion to doping because carrier mobility can decrease at high impurity concentrations due to increased scattering.

### 10.1 Compensation Doping

A semiconductor may contain both donor and acceptor impurities.

If donor concentration exceeds acceptor concentration, the material generally behaves as N-type.

If acceptor concentration exceeds donor concentration, it generally behaves as P-type.

For a compensated semiconductor with complete ionization, a simplified net dopant concentration is:

\[
N_D-N_A
\]

for N-type material, or:

\[
N_A-N_D
\]

for P-type material.

A complete carrier calculation must also account for charge neutrality and the mass-action law.

## 11. Practical Applications

### 11.1 PN Junction Devices

Combining P-type and N-type regions produces a PN junction, which forms the basis of ordinary semiconductor diodes.

### 11.2 Transistors

Bipolar junction transistors use differently doped semiconductor regions to control current.

### 11.3 Integrated Circuits

Integrated circuit fabrication uses carefully controlled doping to create transistor channels, source and drain regions, wells, and other device structures.

### 11.4 Photodetectors

Semiconductor doping and junction design influence how efficiently light-generated charge carriers can be collected.

### 11.5 Power Devices

High-voltage semiconductor devices use carefully engineered doping profiles to balance voltage blocking capability, resistance, and switching performance.

## 12. Common Examination Traps

1. Intrinsic semiconductors are ideally pure; extrinsic semiconductors are intentionally doped.
2. Pentavalent impurities produce N-type material.
3. Trivalent impurities produce P-type material.
4. N-type material has electrons as majority carriers, not positive charge as its overall electrical state.
5. P-type material has holes as majority carriers, not a net positive charge.
6. Donor impurities provide electrons; acceptor impurities accept electrons.
7. Minority carriers are still present in doped semiconductors.
8. At thermal equilibrium, \(np=n_i^2\).
9. The Fermi level moves towards the conduction band in N-type material and towards the valence band in P-type material.
10. Doping changes carrier concentration and generally changes mobility as well.

## 13. Quiz

### Question 1

Which impurity is commonly used to produce N-type silicon?

- [ ] Boron.
- [x] Phosphorus.
- [ ] Aluminium.
- [ ] Gallium.

> **Explanation:** Phosphorus is pentavalent and has five valence electrons. Four participate in covalent bonds, while the fifth can be released as a conduction electron. It therefore acts as a donor impurity.

### Question 2

In a P-type semiconductor, which carriers are the majority carriers?

- [ ] Free electrons.
- [ ] Protons.
- [x] Holes.
- [ ] Neutrons.

> **Explanation:** Trivalent acceptor impurities create holes in the valence band. These holes become the majority carriers, while electrons remain minority carriers.

### Question 3

An N-type semiconductor has an electron concentration of \(4\times10^{16}\,cm^{-3}\). Its intrinsic carrier concentration is \(2\times10^{10}\,cm^{-3}\). Assuming thermal equilibrium, calculate its hole concentration.

- [ ] \(8\times10^{26}\,cm^{-3}\).
- [x] \(1\times10^4\,cm^{-3}\).
- [ ] \(2\times10^{10}\,cm^{-3}\).
- [ ] \(4\times10^{16}\,cm^{-3}\).

> **Explanation:** Apply the mass-action law: \(np=n_i^2\). Therefore, \(p=(2\times10^{10})^2/(4\times10^{16})=1\times10^4\,cm^{-3}\).