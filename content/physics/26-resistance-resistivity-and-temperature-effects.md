---
title: Resistance, Resistivity and Temperature Effects
level: intermediate
---

Electrical resistance determines how strongly a material opposes electric current. Understanding resistance, resistivity and their dependence on temperature is essential for analysing electrical circuits and selecting materials for practical applications.

## 1. Electrical Resistance

Resistance is the opposition offered by a conductor to the flow of electric current.

According to Ohm's law:

R = V/I

Where:
- R = resistance
- V = potential difference
- I = current

The SI unit is the ohm (Ω).

A resistance of 1 Ω allows a current of 1 A to flow when a potential difference of 1 V is applied across it, under ohmic conditions.

## 2. Microscopic Explanation of Resistance

In a metallic conductor, free electrons move through a lattice of positively charged ions.

When an electric field is applied:
- Electrons acquire a drift velocity.
- They undergo scattering due to lattice vibrations, impurities and defects.
- Their motion is interrupted by collisions.
- The average drift motion is limited.

These scattering processes produce electrical resistance.

Resistance converts electrical energy into other forms, particularly thermal energy.

## 3. Resistivity

Resistivity is an intrinsic property of a material that measures its opposition to electric current.

For a uniform conductor:

ρ = RA/L

Rearranging:

R = ρL/A

Where:
- ρ = resistivity
- R = resistance
- L = length
- A = cross-sectional area

The SI unit of resistivity is Ω m.

Unlike resistance, resistivity does not directly depend on the dimensions of the sample.

## 4. Factors Affecting Resistance

Resistance depends on several factors.

### Length

R is directly proportional to length.

R ∝ L

A longer conductor provides a greater path over which charge carriers experience scattering.

### Cross-Sectional Area

R is inversely proportional to area.

R ∝ 1/A

A thicker wire provides more parallel pathways for charge flow.

### Material

Different materials have different resistivities.

Copper and silver have low resistivity, while rubber and glass have very high resistivity.

### Temperature

Resistance changes with temperature.

The nature and magnitude of this change depend on the material.

## 5. Conductivity

Electrical conductivity measures how easily electric current flows through a material.

σ = 1/ρ

Where σ is conductivity.

Its SI unit is siemens per metre (S/m).

A material with high conductivity has low resistivity.

## 6. Temperature Dependence in Metals

For many metals, resistance increases approximately linearly with temperature over a moderate temperature interval.

R = R0[1 + α(T - T0)]

Where:
- R0 = initial resistance
- α = temperature coefficient of resistance
- T0 = initial temperature
- T = final temperature

For metals, α is generally positive.

This occurs because increasing temperature causes greater lattice vibration and more frequent electron scattering.

## 7. Temperature Dependence in Semiconductors

In many semiconductors, resistance decreases as temperature increases over ordinary operating ranges.

This is because higher temperature creates additional mobile charge carriers.

Although carrier scattering also changes with temperature, the increase in carrier concentration often dominates.

Examples include silicon and germanium.

## 8. Temperature Coefficient of Resistance

The temperature coefficient of resistance indicates the fractional change in resistance per degree of temperature change.

α = (R - R0)/(R0ΔT)

Its SI-compatible unit is K^-1.

A positive coefficient means resistance increases with temperature.

A negative coefficient means resistance decreases with temperature.

Some materials have a coefficient close to zero over a particular temperature range.

## 9. Non-Ohmic Conductors

Not every electrical component follows Ohm's law.

For an ohmic conductor, voltage is proportional to current under constant physical conditions.

For a non-ohmic component, the V-I relationship is nonlinear or depends on operating conditions.

Examples:
- Semiconductor diodes.
- Filament lamps.
- Thermistors.
- Transistors.

A filament lamp is non-ohmic because its temperature rises as current increases, changing its resistance.

## 10. V-I Characteristics

A V-I graph shows the relationship between voltage and current.

For an ohmic resistor:
- The graph is a straight line.
- It passes through the origin.
- Its slope on a V-I graph is resistance.

For a non-ohmic component:
- The graph is generally curved.
- Resistance changes with voltage, current or temperature.

Carefully identify which variable is on each axis before interpreting the slope.

## 11. Superconductivity

Superconductivity is a phenomenon in which certain materials exhibit zero electrical resistance below a characteristic critical temperature.

Important properties:
- Electrical resistance becomes zero in the superconducting state.
- Persistent currents can flow without ordinary resistive energy loss.
- Superconductors exhibit the Meissner effect, expelling magnetic flux from their interior under appropriate conditions.

Applications include:
- Magnetic resonance imaging systems.
- Powerful electromagnets.
- Magnetic levitation.
- Certain quantum computing technologies.
- Scientific particle accelerators.

Superconductivity is limited by critical temperature, magnetic field and current density.

## 12. Colour Coding of Resistors

Many fixed resistors use coloured bands to indicate their resistance.

For a common four-band resistor:

- First band: first significant digit.
- Second band: second significant digit.
- Third band: multiplier.
- Fourth band: tolerance.

Digit colours:

| Colour | Digit |
|---|---:|
| Black | 0 |
| Brown | 1 |
| Red | 2 |
| Orange | 3 |
| Yellow | 4 |
| Green | 5 |
| Blue | 6 |
| Violet | 7 |
| Grey | 8 |
| White | 9 |

Gold commonly indicates ±5% tolerance, and silver commonly indicates ±10%.

## 13. Numerical Applications

**Example 1: Resistance**

A conductor has a potential difference of 24 V and current of 3 A.

R = V/I

R = 24/3

R = 8 Ω

**Example 2: Temperature change**

A metal wire has resistance 10 Ω at 20°C. Its temperature coefficient is 0.004 per °C. Find its resistance at 70°C.

R = R0[1 + α(T - T0)]

R = 10[1 + 0.004(70 - 20)]

R = 10(1.2)

R = 12 Ω

**Example 3: Resistivity**

A wire has resistance 5 Ω, length 2 m and area 0.5 × 10^-6 m².

ρ = RA/L

ρ = (5 × 0.5 × 10^-6)/2

ρ = 1.25 × 10^-6 Ω m

## Common Exam Traps

- Resistance and resistivity are different quantities.
- Resistance depends on length and cross-sectional area.
- Resistivity is an intrinsic material property at a specified temperature.
- Conductivity is the reciprocal of resistivity.
- Metallic resistance generally increases with temperature.
- Semiconductor resistance generally decreases with temperature.
- A nonlinear V-I graph indicates non-ohmic behaviour.
- The slope of a V-I graph depends on which quantity is on the vertical axis.
- Superconductivity involves zero DC electrical resistance below critical conditions.
- The Meissner effect is distinct from simply having zero resistance.

## Quiz

1. If the length of a uniform wire is doubled while its cross-sectional area and material remain unchanged, its resistance:

- [ ] Becomes half
- [x] Becomes double
- [ ] Becomes four times
- [ ] Remains unchanged

> Since R = ρL/A, doubling the length doubles the resistance.

2. The temperature coefficient of resistance for most metallic conductors is:

- [x] Positive
- [ ] Negative
- [ ] Always zero
- [ ] Infinite

> Metallic resistance generally increases with temperature, giving a positive temperature coefficient.

3. Which phenomenon is associated with superconductors expelling magnetic flux from their interior?

- [ ] Photoelectric effect
- [ ] Hall effect
- [x] Meissner effect
- [ ] Doppler effect

> The Meissner effect describes the expulsion of magnetic flux from a superconductor in its superconducting state under appropriate conditions.