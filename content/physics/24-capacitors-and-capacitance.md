---
title: Capacitors and Capacitance
level: intermediate
---

Capacitors are electrical components designed to store electric charge and electrical energy. They are used in electronic circuits, power supplies, communication systems, timing circuits and energy-storage applications.

Understanding capacitance is essential for studying electrostatics and electrical circuits.

## 1. Introduction to Capacitors

A capacitor is a device consisting of two conductors separated by an insulating material called a dielectric.

When connected to a voltage source:
- One plate accumulates positive charge.
- The other plate accumulates an equal amount of negative charge.
- An electric field develops between the plates.
- Electrical energy is stored in the electric field.

A capacitor does not normally store a net excess charge for the complete two-plate system. It stores equal and opposite charges on its plates.

## 2. Capacitance

Capacitance is the ability of a capacitor to store charge per unit potential difference.

C = Q / V

Where:
- C = capacitance
- Q = magnitude of charge on either plate
- V = potential difference between the plates

The SI unit is the farad (F).

1 F = 1 C/V

A capacitor has a capacitance of one farad if it stores one coulomb of charge when the potential difference across it is one volt.

Common practical units:

- 1 microfarad = 10^-6 F
- 1 nanofarad = 10^-9 F
- 1 picofarad = 10^-12 F

Capacitance depends on the geometry of the conductors and the dielectric material, not directly on the charge stored.

## 3. Parallel-Plate Capacitor

A parallel-plate capacitor consists of two large conducting plates separated by a small distance d.

For plates of area A, separated by a vacuum:

C = ε0A/d

Where:
- ε0 = permittivity of free space
- A = area of each plate
- d = separation between plates

The equation assumes that edge effects are negligible.

### Factors Affecting Capacitance

Capacitance increases when:

- Plate area increases.
- Separation between plates decreases.
- A dielectric material with higher permittivity is introduced.

## 4. Capacitor with a Dielectric

A dielectric is an insulating material placed between capacitor plates.

Examples include:
- Air.
- Paper.
- Glass.
- Mica.
- Ceramic.
- Certain polymers.

The dielectric reduces the effective electric field produced by the separated charges for a fixed free charge.

For a dielectric completely filling the space:

C = κε0A/d

Therefore:

C = κC0

Where:
- κ = dielectric constant or relative permittivity
- C0 = capacitance without the dielectric

The dielectric increases the capacitance by a factor of κ.

## 5. Polarisation of a Dielectric

When a dielectric is placed in an electric field, its molecules or atoms become polarised.

Polarisation involves:
- Slight separation of positive and negative charge centres.
- Alignment of permanent molecular dipoles.
- Development of bound surface charges.

The induced field opposes the original electric field produced by the capacitor plates.

Consequently, the effective field inside the dielectric is reduced for a fixed free charge.

## 6. Combination of Capacitors

Capacitors can be connected in series or parallel.

### Capacitors in Parallel

In a parallel combination:
- All capacitors have the same potential difference.
- Their charges may be different.
- Total charge is the sum of individual charges.

Qtotal = Q1 + Q2 + Q3

Equivalent capacitance:

Ceq = C1 + C2 + C3 + ...

Parallel connection increases the total capacitance.

### Capacitors in Series

In a series combination:
- Every capacitor carries the same magnitude of charge.
- The total voltage is the sum of individual voltages.

Vtotal = V1 + V2 + V3

Equivalent capacitance:

1/Ceq = 1/C1 + 1/C2 + 1/C3 + ...

For two capacitors:

Ceq = C1C2 / (C1 + C2)

Series connection decreases the equivalent capacitance below the smallest individual capacitance.

## 7. Energy Stored in a Capacitor

Energy is stored in the electric field between capacitor plates.

The energy stored is:

U = 1/2 CV²

Other equivalent expressions are:

U = 1/2 QV

U = Q² / 2C

These equations describe the same stored energy under the relation Q = CV.

## 8. Energy Density of an Electric Field

Energy density is the energy stored per unit volume.

For an electric field in a vacuum:

u = 1/2 ε0E²

For a linear dielectric:

u = 1/2 εE²

Where:
- u = energy density
- E = electric field magnitude
- ε = permittivity of the medium

The SI unit is J/m³.

## 9. Charging a Capacitor

When an initially uncharged capacitor is connected to a DC source through a resistor, charge gradually accumulates on its plates.

The charging process is not instantaneous.

For a series RC circuit:

q(t) = CV(1 - e^(-t/RC))

Current during charging:

i(t) = (V/R)e^(-t/RC)

Where:
- V = source voltage
- R = resistance
- C = capacitance
- t = time
- e = mathematical exponential constant

At the beginning:
- Charge is zero.
- Current is maximum.

After a long time:
- Capacitor charge approaches CV.
- Current approaches zero.

## 10. Discharging a Capacitor

When a charged capacitor is connected across a resistor without an external source, it discharges.

Charge during discharging:

q(t) = Q0e^(-t/RC)

Current magnitude:

i(t) = (Q0/RC)e^(-t/RC)

The charge and current decrease exponentially.

The direction of discharge current is opposite to the direction of charging current.

## 11. Time Constant of an RC Circuit

The time constant is:

τ = RC

It determines how quickly a capacitor charges or discharges.

During charging:
- At t = τ, charge reaches approximately 63.2% of its final value.
- At t = 2τ, it reaches approximately 86.5%.
- At t = 3τ, it reaches approximately 95%.
- At t = 5τ, it reaches approximately 99.3%.

During discharging:
- At t = τ, approximately 36.8% of the initial charge remains.
- At t = 2τ, approximately 13.5% remains.
- At t = 5τ, approximately 0.67% remains.

The time constant has the unit of seconds.

## 12. Capacitor with a Battery Connected and Disconnected

The behaviour of a capacitor when a dielectric is inserted depends on whether the battery remains connected.

### Battery Connected

The potential difference remains constant.

When a dielectric is inserted:
- Capacitance increases.
- Charge increases.
- Stored energy increases.

### Battery Disconnected

The charge remains constant because there is no conducting path for charge to enter or leave.

When a dielectric is inserted:
- Capacitance increases.
- Potential difference decreases.
- Stored energy decreases.

These distinctions are important in conceptual and numerical questions.

## 13. Applications of Capacitors

Capacitors are used in:

- Power supply filtering.
- Signal coupling and decoupling.
- Timing circuits.
- Camera flashes.
- Radio tuning circuits.
- Energy storage.
- Motor starting circuits.
- Electronic noise suppression.
- Oscillator circuits.

## 14. Numerical Applications

**Example 1: Capacitance**

A capacitor stores 20 μC of charge at a potential difference of 10 V.

C = Q/V

C = 20 × 10^-6 / 10

C = 2 μF

**Example 2: Energy stored**

A 100 μF capacitor is charged to 12 V.

U = 1/2 CV²

U = 1/2 × 100 × 10^-6 × 12²

U = 0.0072 J

**Example 3: Series combination**

Two capacitors of 6 μF and 3 μF are connected in series.

Ceq = C1C2/(C1 + C2)

Ceq = (6 × 3)/(6 + 3)

Ceq = 2 μF

## Common Exam Traps

- Capacitance is the ratio of charge to potential difference.
- Capacitance is determined by geometry and dielectric properties.
- In parallel, capacitors have the same voltage.
- In series, capacitors have the same magnitude of charge.
- Parallel capacitances add directly.
- Reciprocals of capacitances add in series.
- Energy stored in a capacitor is proportional to the square of voltage for fixed capacitance.
- A dielectric increases capacitance.
- With a battery connected, voltage remains constant.
- With a battery disconnected, charge remains constant.
- An RC time constant is the product of resistance and capacitance.

## Quiz

1. Two capacitors are connected in parallel. Which quantity is the same across both capacitors?

- [ ] Charge
- [x] Potential difference
- [ ] Energy stored
- [ ] Capacitance

> Parallel components share the same two connection points, so their potential differences are equal.

2. A dielectric completely fills a capacitor and has dielectric constant κ. Its capacitance becomes:

- [ ] C0/κ
- [x] κC0
- [ ] C0 + κ
- [ ] Unchanged

> The capacitance of a completely filled parallel-plate capacitor is multiplied by the dielectric constant.

3. An RC circuit has resistance 2 kΩ and capacitance 5 μF. Its time constant is:

- [ ] 0.001 s
- [x] 0.01 s
- [ ] 0.1 s
- [ ] 10 s

> τ = RC = 2000 × 5 × 10^-6 = 0.01 seconds.