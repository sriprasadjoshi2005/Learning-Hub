---
title: Semiconductor Physics and Diodes
level: advanced
---

Semiconductor physics forms the foundation of modern electronics. Computers, smartphones, solar cells, sensors, communication devices and countless electronic systems depend on semiconductor materials.

A semiconductor has electrical conductivity between that of a conductor and an insulator. Its conductivity can be controlled through temperature, impurities, electric fields and light.

## 1. Conductors, Insulators and Semiconductors

Materials can be classified according to their ability to conduct electric current.

**Conductors:**

Have many mobile charge carriers.

Examples:
- Copper.
- Aluminium.
- Silver.

**Insulators:**

Have very few freely available charge carriers under ordinary conditions.

Examples:
- Glass.
- Rubber.
- Mica.

**Semiconductors:**

Have controllable electrical conductivity.

Examples:
- Silicon.
- Germanium.
- Gallium arsenide.

## 2. Energy Band Theory

In an isolated atom, electrons occupy discrete energy levels.

When many atoms combine to form a solid, their energy levels form closely spaced energy bands.

Two important bands are:

**Valence band:**

The highest energy band that is normally occupied by electrons in the ground state.

**Conduction band:**

The band in which electrons can move through the material and contribute to electrical conduction.

The energy separation between the valence and conduction bands is called the band gap.

\[
E_g=E_C-E_V
\]

Where:
- EC = conduction-band edge.
- EV = valence-band edge.

## 3. Energy Band Classification

**Conductors:**

The valence and conduction bands overlap or a partially filled band exists.

Electrons can move relatively easily.

**Insulators:**

Have a large forbidden energy gap.

Very few electrons can reach the conduction band under ordinary conditions.

**Semiconductors:**

Have a relatively small energy gap.

Thermal energy, light or other external influences can generate mobile charge carriers.

Typical approximate room-temperature band gaps:

| Material | Band gap |
|---|---:|
| Germanium | 0.66 eV |
| Silicon | 1.12 eV |
| Gallium arsenide | 1.42 eV |

These values depend on temperature and material conditions.

## 4. Intrinsic Semiconductors

An intrinsic semiconductor is a chemically pure semiconductor without intentional impurity doping.

Silicon has four valence electrons.

Each silicon atom forms four covalent bonds with neighbouring atoms in a crystalline structure.

At sufficiently low temperatures, most electrons remain involved in these bonds.

When thermal energy breaks a covalent bond:
- An electron becomes available for conduction.
- A vacancy called a hole remains.

Both electrons and holes contribute to electrical conduction.

For an intrinsic semiconductor:

\[
n=p=n_i
\]

Where:
- n = electron concentration.
- p = hole concentration.
- ni = intrinsic carrier concentration.

## 5. Electron-Hole Pairs

A hole behaves as a positive charge carrier.

When an electron moves into a neighbouring hole, the hole effectively moves in the opposite direction.

Therefore, semiconductor current can result from:
- Electron motion.
- Hole motion.

The total current depends on both carrier concentrations and their mobilities.

## 6. Extrinsic Semiconductors and Doping

An extrinsic semiconductor is produced by intentionally adding small quantities of impurity atoms.

This process is called doping.

Doping significantly changes the concentration of charge carriers.

Two important types are:
- N-type semiconductor.
- P-type semiconductor.

## 7. N-Type Semiconductor

An N-type semiconductor is formed by doping a semiconductor with pentavalent impurities.

Examples include:
- Phosphorus.
- Arsenic.
- Antimony.

A pentavalent impurity has five valence electrons.

Four participate in covalent bonding, while the fifth can become a mobile electron.

Therefore:
- Electrons are majority carriers.
- Holes are minority carriers.

The semiconductor remains electrically neutral overall.

## 8. P-Type Semiconductor

A P-type semiconductor is formed by doping with trivalent impurities.

Examples include:
- Boron.
- Aluminium.
- Gallium.

A trivalent impurity has three valence electrons.

It creates an incomplete covalent bond, producing a hole.

Therefore:
- Holes are majority carriers.
- Electrons are minority carriers.

## 9. Formation of a P-N Junction

A p-n junction is formed by joining p-type and n-type regions within a semiconductor crystal.

When the two regions meet:
1. Electrons diffuse from the n-side towards the p-side.
2. Holes diffuse from the p-side towards the n-side.
3. Electrons and holes recombine near the junction.
4. Immobile charged ions remain.
5. A depletion region forms.

The depletion region contains very few mobile charge carriers.

An internal electric field develops across this region.

The associated potential difference is called the barrier potential.

## 10. Forward Bias

A p-n junction is forward biased when:
- The positive terminal of the source is connected to the p-side.
- The negative terminal is connected to the n-side.

This reduces the potential barrier and narrows the depletion region.

A sufficiently large forward voltage allows substantial current to flow.

Typical approximate forward voltage drops for ordinary silicon and germanium diodes are:
- Silicon: 0.7 V.
- Germanium: 0.3 V.

These are practical approximations, not exact fixed thresholds.

## 11. Reverse Bias

A p-n junction is reverse biased when:
- The positive terminal is connected to the n-side.
- The negative terminal is connected to the p-side.

This increases the potential barrier and widens the depletion region.

Only a small reverse leakage current generally flows.

At sufficiently high reverse voltage, breakdown may occur.

## 12. Semiconductor Diode

A semiconductor diode is a two-terminal device that allows current to flow much more easily in one direction than the other under ordinary operating conditions.

Its terminals are:
- Anode: p-side.
- Cathode: n-side.

Conventional forward current flows from anode to cathode.

The diode is widely used in rectification, protection and signal processing.

## 13. Rectification

Rectification converts alternating current into unidirectional current.

**Half-wave rectifier:**

Uses one diode to pass one half-cycle of an AC input.

The other half-cycle is blocked.

**Full-wave rectifier:**

Uses both half-cycles to produce a unidirectional output.

A bridge rectifier typically uses four diodes.

A capacitor filter can reduce the fluctuations in the rectified output.

## 14. Zener Diode

A Zener diode is designed to operate in the reverse-breakdown region.

When reverse voltage reaches its specified breakdown value, the voltage across the diode remains approximately constant over a suitable operating-current range.

It is commonly used for:
- Voltage regulation.
- Reference voltage generation.
- Overvoltage protection.

A series resistor is normally needed to limit current.

## 15. Light-Emitting Diode

An LED emits light when forward biased.

Electrons and holes recombine, releasing energy in the form of photons.

The photon energy is related to the semiconductor band gap:

\[
E=hf
\]

Where:
- h = Planck's constant.
- f = photon frequency.

The approximate wavelength is:

\[
\lambda=\frac{hc}{E}
\]

Different semiconductor materials produce different emission wavelengths.

## 16. Photodiode

A photodiode converts incident light into electrical current.

It is commonly operated under reverse bias.

When photons are absorbed, electron-hole pairs are generated.

The resulting photocurrent can be used to measure light intensity.

Applications include:
- Optical communication.
- Light sensors.
- Barcode scanners.
- Automatic lighting systems.

## 17. Solar Cell

A solar cell converts light energy directly into electrical energy through the photovoltaic effect.

When sunlight is absorbed, electron-hole pairs are generated.

The p-n junction's internal electric field helps separate these charge carriers, producing a potential difference and current through an external circuit.

Solar cells are commonly connected into modules and arrays.

## 18. Worked Numerical Example

A silicon diode is connected in series with a 1 kOhm resistor and a 5 V DC supply.

Assume a forward voltage drop of 0.7 V.

Calculate the current.

Voltage across the resistor:

\[
V_R=5-0.7=4.3\text{ V}
\]

Using Ohm's law:

\[
I=\frac{V_R}{R}
\]

\[
I=\frac{4.3}{1000}
\]

\[
\boxed{I=4.3\text{ mA}}
\]

## Common Exam Traps

- N-type semiconductors have electrons as majority carriers.
- P-type semiconductors have holes as majority carriers.
- Doping does not make the semiconductor electrically charged overall.
- Forward bias narrows the depletion region.
- Reverse bias widens the depletion region.
- A Zener diode is commonly used in reverse breakdown.
- An LED converts electrical energy into light.
- A solar cell converts light energy into electrical energy.

## Quiz

1. In an N-type semiconductor, the majority charge carriers are:

- [ ] Holes
- [x] Electrons
- [ ] Protons
- [ ] Neutrons

> Pentavalent doping introduces donor electrons, making electrons the majority charge carriers.

2. When a p-n junction is forward biased, its depletion region generally:

- [x] Becomes narrower
- [ ] Becomes wider
- [ ] Disappears under every voltage condition
- [ ] Becomes electrically neutral throughout

> Forward bias reduces the potential barrier and allows charge carriers to approach and cross the junction more easily.

3. A Zener diode is commonly used for:

- [ ] Producing mechanical motion
- [ ] Generating sound waves
- [x] Voltage regulation
- [ ] Increasing the mass of charge carriers

> A Zener diode operates in a controlled reverse-breakdown region to maintain an approximately constant voltage.