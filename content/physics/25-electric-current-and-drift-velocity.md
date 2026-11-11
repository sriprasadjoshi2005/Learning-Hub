---
title: Electric Current and Drift Velocity
level: intermediate
---

Electric current is the movement of electric charge through a conductor. It is fundamental to electrical circuits and electronic devices.

Understanding current requires examining how charges move through materials, how resistance develops and how electrical energy is transferred.

## 1. Electric Current

Electric current is the rate of flow of electric charge through a cross-sectional area.

I = dQ/dt

For constant current:

I = Q/t

Where:
- I = electric current
- Q = charge transferred
- t = time

The SI unit is the ampere (A).

One ampere corresponds to one coulomb of charge passing through a cross-section every second.

1 A = 1 C/s

## 2. Direction of Electric Current

Conventional current is defined as the direction in which positive charges would move.

In a metallic conductor:
- Electrons carry the moving charge.
- Electrons move from the negative terminal towards the positive terminal.
- Conventional current is opposite to electron drift.

In electrolytes and other conducting media, both positive and negative ions may contribute to current.

## 3. Direct Current and Alternating Current

### Direct Current (DC)

Direct current flows in one direction.

Its magnitude may remain constant or vary with time without reversing direction.

Examples:
- Batteries.
- Solar cells under steady conditions.
- DC power supplies.

### Alternating Current (AC)

Alternating current periodically changes direction.

Its magnitude generally varies with time.

Examples:
- Domestic electrical supply.
- Alternators.
- AC generators.

## 4. Drift Velocity

Drift velocity is the average velocity acquired by charge carriers in a conductor due to an applied electric field.

In the absence of an electric field, free electrons move randomly due to thermal motion.

When an electric field is applied:
- Electrons experience an electric force.
- Their random motion continues.
- A small average velocity develops opposite to the electric field.

This average velocity is called drift velocity.

For electrons:

vd = -eEτ/m

Where:
- e = magnitude of electron charge
- E = electric field
- τ = average relaxation time
- m = electron mass

The negative sign indicates that electron drift is opposite to the electric field.

## 5. Relation Between Current and Drift Velocity

Consider a conductor of:
- Cross-sectional area A.
- Charge carrier number density n.
- Carrier charge magnitude e.
- Drift speed vd.

The charge passing through the conductor per second gives:

I = neAvd

This is a fundamental equation of electric current.

For a carrier with charge magnitude q:

I = nqAvd

Where n is the number of charge carriers per unit volume.

### Current Density

Current density is current per unit cross-sectional area.

J = I/A

For uniform drift:

J = nevd

In vector form for electrons, conventional current density is opposite to electron drift velocity.

The SI unit is A/m².

## 6. Mobility of Charge Carriers

Mobility measures how easily charge carriers move through a material under an applied electric field.

μ = vd/E

For electrons, this equation refers to the magnitude of drift velocity.

The SI unit is m²/(V s).

Higher mobility means carriers acquire a greater drift speed for the same electric field.

Mobility depends on:
- Material properties.
- Temperature.
- Scattering processes.
- Carrier type.

## 7. Ohm's Law

Ohm's law states that, for a conductor maintained under constant physical conditions, current is directly proportional to the potential difference across it.

V = IR

Where:
- V = potential difference
- I = current
- R = resistance

Resistance is measured in ohms (Ω).

A conductor obeying Ohm's law is called an ohmic conductor.

The relationship may be represented by a straight-line V-I graph passing through the origin.

## 8. Electrical Resistance

Resistance is the opposition offered by a material to the flow of electric current.

For a uniform conductor:

R = ρL/A

Where:
- R = resistance
- ρ = resistivity
- L = conductor length
- A = cross-sectional area

Resistance:
- Increases with length.
- Decreases with cross-sectional area.
- Depends on the material.
- Depends on temperature.

## 9. Resistivity and Conductivity

Resistivity is an intrinsic material property describing how strongly a material opposes current flow.

The SI unit is Ω m.

Conductivity is the reciprocal of resistivity.

σ = 1/ρ

The SI unit is S/m.

Good conductors generally have low resistivity and high conductivity.

Insulators generally have very high resistivity.

## 10. Temperature Dependence of Resistance

For many metallic conductors over a moderate temperature range:

R = R0[1 + α(T - T0)]

Where:
- R0 = resistance at reference temperature T0
- α = temperature coefficient of resistance
- T = final temperature

For most metals, resistance increases with temperature because increased lattice vibrations cause more frequent scattering of electrons.

Semiconductors often show a decrease in resistance as temperature increases over ordinary operating ranges.

## 11. Electromotive Force

Electromotive force (EMF) is the energy supplied by a source per unit charge.

ε = W/Q

The SI unit is the volt.

Despite its name, EMF is not a mechanical force.

It represents the energy provided by a battery or another source to move charge around a complete circuit.

## 12. Internal Resistance of a Cell

A real cell has internal resistance r.

When current I flows through a cell, some voltage is lost inside the cell.

For a cell supplying current:

Vterminal = ε - Ir

Where:
- ε = EMF
- r = internal resistance
- Vterminal = terminal potential difference

When no current flows, terminal voltage equals EMF in the ideal measurement condition.

When a cell is being charged:

Vterminal = ε + Ir

## 13. Cells in Series and Parallel

### Cells in Series

For cells connected in series with the same orientation:

εtotal = ε1 + ε2 + ...

For identical cells:

εtotal = nε

If internal resistances are also in series:

rtotal = nr

### Cells in Parallel

For n identical cells connected in parallel:

εtotal = ε

rtotal = r/n

Parallel connection reduces effective internal resistance without increasing the total EMF for identical cells.

## 14. Numerical Applications

**Example 1: Electric current**

A charge of 30 C passes through a conductor in 10 seconds.

I = Q/t

I = 30/10

I = 3 A

**Example 2: Drift velocity**

A conductor has:
- Current = 2 A.
- Cross-sectional area = 1 × 10^-6 m².
- Carrier density = 8 × 10^28 electrons/m³.

Using:

vd = I/(neA)

vd = 2 / (8 × 10^28 × 1.6 × 10^-19 × 10^-6)

vd ≈ 1.56 × 10^-4 m/s

**Example 3: Resistance**

A wire has resistivity 1.7 × 10^-8 Ω m, length 2 m and cross-sectional area 1 × 10^-6 m².

R = ρL/A

R = (1.7 × 10^-8 × 2)/(1 × 10^-6)

R = 0.034 Ω

## Common Exam Traps

- Conventional current is opposite to electron drift in metallic conductors.
- Current is the rate of charge flow.
- Drift velocity is generally much smaller than the random thermal speed of electrons.
- Current density is a vector quantity.
- Resistance depends on the dimensions and material of a conductor.
- Resistivity is a material property.
- Conductivity is the reciprocal of resistivity.
- Ohm's law applies when physical conditions remain constant.
- EMF is energy supplied per unit charge, not a mechanical force.
- Terminal voltage is generally lower than EMF when a cell supplies current.

## Quiz

1. Conventional current in a metallic conductor flows:

- [ ] In the same direction as electron drift
- [x] Opposite to electron drift
- [ ] Perpendicular to electron drift
- [ ] Randomly without any defined direction

> Conventional current is defined as the direction of positive charge flow. Electrons are negatively charged, so their drift is opposite.

2. The current through a conductor is 4 A. How much charge passes through it in 5 seconds?

- [ ] 0.8 C
- [ ] 9 C
- [x] 20 C
- [ ] 40 C

> Q = It = 4 × 5 = 20 C.

3. The resistance of a uniform wire is doubled in length while its cross-sectional area and material remain unchanged. Its resistance becomes:

- [ ] Half
- [x] Twice
- [ ] Four times
- [ ] Unchanged

> R = ρL/A. Resistance is directly proportional to the length of the wire.