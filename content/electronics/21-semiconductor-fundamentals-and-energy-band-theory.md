---
title: Semiconductor Fundamentals and Energy-Band Theory
level: intermediate
---

# Semiconductor Fundamentals and Energy-Band Theory

Semiconductors are the foundation of modern electronics. Diodes, transistors, integrated circuits, processors, memory devices, solar cells, and many other electronic systems depend on the electrical properties of semiconductor materials.

Unlike conductors and insulators, semiconductors have electrical conductivity that can be controlled through temperature, impurities, electric fields, and illumination. Their behaviour is explained using atomic structure, chemical bonding, and energy-band theory.

This lesson introduces semiconductor materials, their atomic structure, covalent bonding, energy bands, band gaps, charge carriers, and the physical principles that make semiconductor devices possible.

## 1. Introduction to Semiconductor Materials

Materials are commonly classified according to their ability to conduct electric current.

The three major classifications are:

1. Conductors.
2. Insulators.
3. Semiconductors.

### 1.1 Conductors

Conductors allow electric current to flow easily because they contain a large number of mobile charge carriers.

Examples include:

- Copper.
- Aluminium.
- Silver.
- Gold.

In conductors, electrons can move relatively freely through the material. When an electric field is applied, these electrons acquire a net drift motion, producing electric current.

### 1.2 Insulators

Insulators strongly resist the movement of electric charge.

Examples include:

- Glass.
- Rubber.
- Mica.
- Plastic.
- Ceramic.

Most electrons in an insulator are tightly bound to their atoms. Very few electrons are available for conduction under ordinary conditions.

### 1.3 Semiconductors

Semiconductors possess electrical conductivity between that of conductors and insulators.

Their conductivity can be modified by:

- Temperature.
- Addition of impurities.
- Applied electric fields.
- Illumination.
- Injection of electrical charge carriers.

Common semiconductor materials include:

| Material | Symbol | Important characteristics |
|---|---|---|
| Silicon | Si | Most widely used semiconductor |
| Germanium | Ge | Historically important semiconductor |
| Gallium arsenide | GaAs | Used in high-frequency and optoelectronic devices |
| Silicon carbide | SiC | Suitable for high-voltage and high-temperature applications |
| Gallium nitride | GaN | Used in efficient power and high-frequency devices |

Silicon is the most widely used semiconductor because it is abundant, relatively inexpensive, thermally stable, and suitable for manufacturing integrated circuits.

## 2. Atomic Structure of Semiconductors

To understand semiconductor behaviour, it is necessary to examine the structure of an atom.

An atom consists of:

- Protons: positively charged particles in the nucleus.
- Neutrons: electrically neutral particles in the nucleus.
- Electrons: negatively charged particles surrounding the nucleus.

Electrons occupy specific allowed energy states around the nucleus.

### 2.1 Electron Shells

Electron shells represent groups of allowed electron energy states.

The maximum number of electrons that can occupy the nth shell is given by:

\[
N=2n^2
\]

Where:

- \(N\) = maximum number of electrons.
- \(n\) = shell number.

For example:

- First shell: \(2(1)^2=2\) electrons.
- Second shell: \(2(2)^2=8\) electrons.
- Third shell: \(2(3)^2=18\) electrons.

The electrons in the outermost occupied shell are called valence electrons.

### 2.2 Valence Electrons

Valence electrons participate in chemical bonding and strongly influence the electrical properties of a material.

Silicon has atomic number 14.

Its electron configuration is:

\[
1s^2\,2s^2\,2p^6\,3s^2\,3p^2
\]

Therefore, silicon has four valence electrons.

Germanium has atomic number 32 and also possesses four valence electrons.

The four valence electrons allow silicon and germanium atoms to form covalent bonds with neighbouring atoms.

## 3. Covalent Bonding in Semiconductors

### 3.1 Formation of Covalent Bonds

In a pure silicon crystal, each silicon atom shares its four valence electrons with four neighbouring silicon atoms.

This sharing produces four covalent bonds.

Each silicon atom effectively achieves a stable outer electron configuration through this sharing.

A simplified two-dimensional representation is:

\[
\begin{array}{c}
Si\\
|\\
Si-Si-Si\\
|\\
Si
\end{array}
\]

The central silicon atom forms four covalent bonds with its neighbouring atoms.

In an actual silicon crystal, the atoms form a three-dimensional crystal lattice rather than a flat arrangement.

### 3.2 Behaviour at Absolute Zero

At absolute zero temperature, an ideal pure semiconductor has its valence electrons bound in covalent bonds.

There are no thermally generated free electrons available for ordinary electrical conduction.

Therefore, an ideal intrinsic semiconductor behaves approximately like an insulator at absolute zero.

### 3.3 Effect of Temperature

When temperature increases, some covalent bonds acquire enough thermal energy to break.

An electron may gain sufficient energy to leave its covalent bond and become a free electron.

The departure of the electron leaves an empty position in the bond called a hole.

Thus, thermal energy produces two charge carriers:

- A free electron.
- A hole.

These carriers contribute to electrical conduction.

## 4. Energy-Band Theory

Energy-band theory explains the electrical behaviour of solids by describing the allowed energy states available to electrons.

When many atoms come together to form a solid, their individual atomic energy levels interact and split into closely spaced energy states.

These states form energy bands.

Three important energy regions are:

1. Valence band.
2. Conduction band.
3. Forbidden energy gap.

### 4.1 Valence Band

The valence band is the highest energy band that is occupied by electrons under normal equilibrium conditions at low temperatures.

Electrons in this band participate in bonding.

When electrons receive sufficient energy, they may move out of the valence band into the conduction band.

### 4.2 Conduction Band

The conduction band is the energy band in which electrons can move through the material and contribute to electrical conduction.

Electrons in this band are comparatively free to respond to an applied electric field.

### 4.3 Forbidden Energy Gap

The forbidden energy gap is the energy interval between the valence band and the conduction band in which no allowed electron energy states exist in an ideal crystal.

It is represented by:

\[
E_g=E_C-E_V
\]

Where:

- \(E_g\) = forbidden energy gap.
- \(E_C\) = minimum energy of the conduction band.
- \(E_V\) = maximum energy of the valence band.

The energy gap determines how much energy is required to excite an electron from the valence band into the conduction band.

### 4.4 Energy-Band Diagram

A simplified energy-band representation is:

    Energy ↑

    ┌───────────────────────────┐
    │       Conduction Band     │
    └───────────────────────────┘
                  ↑
                  │
           Forbidden Gap
                  │
                  ↓
    ┌───────────────────────────┐
    │         Valence Band      │
    └───────────────────────────┘

The vertical direction represents increasing electron energy.

## 5. Energy Bands in Conductors, Insulators and Semiconductors

The size and arrangement of energy bands determine whether a material behaves as a conductor, semiconductor, or insulator.

### 5.1 Conductors

In conductors, the valence band and conduction band may overlap, or a partially filled band may be available.

Consequently, electrons can move into nearby available energy states with very little additional energy.

This allows relatively easy electrical conduction.

### 5.2 Insulators

Insulators have a large forbidden energy gap.

Under ordinary conditions, electrons cannot easily acquire enough energy to move into the conduction band.

Therefore, electrical conductivity is extremely low.

### 5.3 Semiconductors

Semiconductors possess a relatively small forbidden energy gap.

At ordinary temperatures, some electrons can acquire sufficient thermal energy to enter the conduction band.

This produces free electrons and holes.

Typical room-temperature energy-gap values are:

| Material | Approximate energy gap |
|---|---:|
| Germanium | 0.66 eV |
| Silicon | 1.12 eV |
| Gallium arsenide | 1.42 eV |

The energy gap is generally measured in electronvolts (eV).

One electronvolt is the energy gained by an electron when it moves through a potential difference of one volt.

\[
1\,eV=1.602\times10^{-19}\,J
\]

### 5.4 Comparison of Energy Bands

| Property | Conductor | Semiconductor | Insulator |
|---|---|---|---|
| Energy gap | Zero or overlapping bands | Small | Large |
| Conductivity | High | Moderate and controllable | Very low |
| Free carriers | Abundant | Limited in pure material | Extremely limited |
| Temperature effect | Usually conductivity decreases | Conductivity generally increases | Conductivity may increase slightly |
| Examples | Copper, silver | Silicon, germanium | Glass, rubber |

## 6. Electron-Hole Pair Generation and Recombination

### 6.1 Electron-Hole Pair Generation

When an electron receives sufficient energy to move from the valence band into the conduction band, it leaves behind a hole.

The electron and hole are generated together.

This process is called electron-hole pair generation.

The required energy must be sufficient to overcome the energy gap.

\[
E\geq E_g
\]

Where:

- \(E\) = energy supplied to the electron.
- \(E_g\) = semiconductor energy gap.

The energy may come from thermal excitation, light, or another suitable energy source.

### 6.2 Electron-Hole Pair Recombination

When a free electron loses energy and occupies an available hole state, the electron and hole disappear as separate mobile charge carriers.

This process is called recombination.

The released energy may appear as heat or electromagnetic radiation, depending on the semiconductor and recombination mechanism.

### 6.3 Equilibrium Carrier Concentration

In an intrinsic semiconductor, electrons and holes are generated in pairs.

Therefore, the electron concentration and hole concentration are equal:

\[
n=p=n_i
\]

Where:

- \(n\) = electron concentration.
- \(p\) = hole concentration.
- \(n_i\) = intrinsic carrier concentration.

The intrinsic carrier concentration depends strongly on temperature and semiconductor material.

At thermal equilibrium, the generation and recombination rates balance one another.

This means that the average carrier concentrations remain constant, even though individual generation and recombination events continue.

## 7. Electrons and Holes as Charge Carriers

Both electrons and holes contribute to semiconductor current.

### 7.1 Electron Conduction

Electrons are negatively charged.

When an electric field is applied, free electrons experience a force opposite to the direction of the electric field.

Their average drift motion is therefore opposite to the conventional current direction.

### 7.2 Hole Conduction

A hole represents an unoccupied electron state in the valence band.

When a neighbouring valence electron moves into the hole, it leaves another hole behind.

This repeated movement makes the hole appear to move through the crystal.

A hole behaves as a positive charge carrier.

Its effective charge is:

\[
q=+1.602\times10^{-19}\,C
\]

### 7.3 Conventional Current

Conventional current is defined as the direction in which positive charge would move.

Therefore:

- Electron movement is opposite to conventional current.
- Hole movement is in the same direction as conventional current.

Both electrons and holes can contribute to the total current in a semiconductor.

## 8. Semiconductor Conductivity

The conductivity of a semiconductor depends on the number of available charge carriers and how easily they move through the material.

The conductivity equation is:

\[
\sigma=q(n\mu_n+p\mu_p)
\]

Where:

- \(\sigma\) = electrical conductivity in S/m.
- \(q\) = magnitude of electron charge in C.
- \(n\) = electron concentration in m\(^{-3}\).
- \(p\) = hole concentration in m\(^{-3}\).
- \(\mu_n\) = electron mobility in m\(^2\)/(V·s).
- \(\mu_p\) = hole mobility in m\(^2\)/(V·s).

The equation contains two contributions:

1. Electron conductivity: \(qn\mu_n\).
2. Hole conductivity: \(qp\mu_p\).

The total conductivity is the sum of these contributions.

Resistivity is the reciprocal of conductivity:

\[
\rho=\frac{1}{\sigma}
\]

Where:

- \(\rho\) = resistivity in \(\Omega\cdot m\).
- \(\sigma\) = conductivity in S/m.

### 8.1 Carrier Mobility

Mobility measures how easily a charge carrier moves through a semiconductor under an applied electric field.

It is defined as:

\[
\mu=\frac{v_d}{E}
\]

Where:

- \(\mu\) = mobility in m\(^2\)/(V·s).
- \(v_d\) = drift velocity in m/s.
- \(E\) = electric field strength in V/m.

Higher mobility generally means that a carrier can achieve a greater drift velocity for the same electric field.

Electron mobility in silicon is generally greater than hole mobility.

## 9. Worked Numerical Examples

### Example 1: Energy Required to Excite an Electron in Silicon

**Given:**

- Energy gap of silicon: \(E_g=1.12\,eV\).
- Electron charge: \(q=1.602\times10^{-19}\,C\).

Calculate the minimum energy in joules required to excite an electron across the energy gap.

**Formula:**

\[
E(J)=E(eV)\times1.602\times10^{-19}
\]

**Solution:**

\[
E=1.12\times1.602\times10^{-19}
\]

\[
E=1.79424\times10^{-19}\,J
\]

**Final Answer:**

\[
\boxed{E\approx1.79\times10^{-19}\,J}
\]

### Example 2: Semiconductor Conductivity

**Given:**

- Electron concentration: \(n=2\times10^{16}\,m^{-3}\).
- Hole concentration: \(p=2\times10^{16}\,m^{-3}\).
- Electron mobility: \(\mu_n=0.14\,m^2/(V\cdot s)\).
- Hole mobility: \(\mu_p=0.05\,m^2/(V\cdot s)\).
- Electron charge: \(q=1.6\times10^{-19}\,C\).

Calculate the conductivity.

**Formula:**

\[
\sigma=q(n\mu_n+p\mu_p)
\]

**Solution:**

Substitute the values:

\[
\sigma=1.6\times10^{-19}
[(2\times10^{16})(0.14)+(2\times10^{16})(0.05)]
\]

\[
\sigma=1.6\times10^{-19}
[2.8\times10^{15}+1.0\times10^{15}]
\]

\[
\sigma=1.6\times10^{-19}\times3.8\times10^{15}
\]

\[
\sigma=6.08\times10^{-4}\,S/m
\]

**Final Answer:**

\[
\boxed{\sigma=6.08\times10^{-4}\,S/m}
\]

## 10. Practical Applications of Semiconductor Fundamentals

The physical properties introduced in this lesson are used in many electronic technologies.

### 10.1 Diodes

Diodes use semiconductor junctions to control the direction of current flow.

### 10.2 Transistors

Transistors use controlled semiconductor conduction to amplify signals or operate as electronic switches.

### 10.3 Integrated Circuits

Integrated circuits contain large numbers of semiconductor devices fabricated on a small semiconductor substrate.

### 10.4 Solar Cells

Solar cells use light-generated electron-hole pairs to produce electrical energy.

### 10.5 Light-Emitting Diodes

LEDs convert electrical energy into light through electron-hole recombination.

### 10.6 Power Electronics

Materials such as silicon carbide and gallium nitride are used in high-efficiency power conversion systems.

## 11. Common Examination Traps

1. A semiconductor is not simply a material with conductivity exactly halfway between a conductor and an insulator.
2. The valence band and conduction band are different energy regions.
3. The forbidden energy gap contains no allowed energy states in the ideal band model.
4. A hole is not a positively charged proton; it is an effective positive charge carrier representing an unoccupied electron state.
5. Electron movement and conventional current have opposite directions.
6. In an intrinsic semiconductor, electron and hole concentrations are equal.
7. Electron-hole pairs are generated together.
8. Silicon has an approximate room-temperature band gap of 1.12 eV, not 1.12 J.
9. Conductivity depends on both carrier concentration and mobility.
10. Thermal excitation generally increases the conductivity of an intrinsic semiconductor.

## Quiz

1. Which statement best describes the forbidden energy gap?

- [ ] It is the region containing all free electrons.
- [x] It is the energy interval between the valence band and conduction band where no allowed electron energy states exist in the ideal band model.
- [ ] It is the region occupied by protons.
- [ ] It is the energy required to remove an atom from a crystal.

> The forbidden energy gap separates the valence band from the conduction band. An electron must acquire sufficient energy to cross this gap and enter the conduction band.

2. What happens when a covalent bond in a pure semiconductor breaks due to thermal energy?

- [ ] Two holes are produced.
- [ ] Two free electrons are produced.
- [x] One free electron and one hole are produced.
- [ ] The semiconductor becomes a conductor permanently.

> When a valence electron gains sufficient thermal energy to leave its covalent bond, it becomes a free electron. The empty state left behind behaves as a hole. They form an electron-hole pair.

3. An intrinsic semiconductor has an electron concentration of \(5\times10^{15}\,m^{-3}\). What is its hole concentration at thermal equilibrium?

- [ ] \(2.5\times10^{15}\,m^{-3}\).
- [ ] \(1\times10^{16}\,m^{-3}\).
- [ ] Zero.
- [x] \(5\times10^{15}\,m^{-3}\).

> In an intrinsic semiconductor, electrons and holes are generated in pairs. Therefore, their equilibrium concentrations are equal: \(n=p=n_i\).
