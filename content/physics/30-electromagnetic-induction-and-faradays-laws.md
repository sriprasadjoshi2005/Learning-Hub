---
title: Electromagnetic Induction and Faraday's Laws
level: intermediate
---

Electromagnetic induction is the phenomenon in which an electromotive force is produced when the magnetic flux linked with a circuit changes.

It is one of the most important principles in electrical engineering and modern technology. Electric generators, transformers, induction cooktops and many electrical devices operate using electromagnetic induction.

## 1. Discovery of Electromagnetic Induction

Michael Faraday and Joseph Henry independently discovered electromagnetic induction in the nineteenth century.

Their experiments demonstrated that a changing magnetic field can produce an induced electromotive force in a conductor.

A stationary magnetic field does not necessarily produce an induced EMF in a stationary circuit.

The essential requirement is a change in magnetic flux linkage.

## 2. Magnetic Flux

Magnetic flux measures the magnetic field passing through a surface.

For a uniform magnetic field through a flat surface:

ΦB = BA cos θ

Where:
- ΦB = magnetic flux
- B = magnetic field
- A = area
- θ = angle between the magnetic field and the surface normal

The SI unit is the weber (Wb).

1 Wb = 1 T m²

Magnetic flux is a scalar quantity.

## 3. Factors Affecting Magnetic Flux

Magnetic flux depends on:

1. Magnetic field strength.
2. Surface area.
3. Orientation of the surface relative to the field.

Maximum positive flux occurs when θ = 0 degrees.

Zero flux occurs when θ = 90 degrees.

Maximum negative flux occurs when θ = 180 degrees.

## 4. Electromagnetic Induction

Electromagnetic induction occurs when the magnetic flux linked with a circuit changes, producing an induced EMF.

The magnetic flux may change because of:

- A changing magnetic field.
- A changing area of the circuit.
- Rotation of the circuit.
- Relative motion between a magnet and a coil.
- Movement of a conductor through a magnetic field.

An induced current flows only when the circuit provides a closed conducting path.

An induced EMF can exist even when the circuit is open.

## 5. Faraday's First Law

Faraday's first law states that an electromotive force is induced in a circuit whenever the magnetic flux linked with it changes.

If the circuit is closed, the induced EMF drives an induced current.

The magnitude of the induced EMF depends on how quickly the magnetic flux changes.

## 6. Faraday's Second Law

The magnitude of the induced EMF is proportional to the rate of change of magnetic flux linkage.

For a coil of N turns:

ε = -N(dΦB/dt)

For a finite change over a time interval:

εaverage = -N(ΔΦB/Δt)

The negative sign represents Lenz's law.

For a coil with multiple turns, the total flux linkage is NΦB when each turn experiences the same flux.

## 7. Lenz's Law

Lenz's law states that the direction of an induced current is such that its magnetic effect opposes the change in magnetic flux that produced it.

The induced current does not simply oppose the original magnetic field. It opposes the change in magnetic flux.

Examples:

### Increasing Magnetic Flux

If external magnetic flux through a coil increases, the induced magnetic field acts in a direction that opposes the increase.

### Decreasing Magnetic Flux

If external magnetic flux decreases, the induced magnetic field acts in a direction that opposes the decrease.

Lenz's law is consistent with conservation of energy.

Without this opposition, electromagnetic induction could produce energy without an external energy input.

## 8. Induced EMF Due to a Moving Conductor

A straight conductor of length l moving with speed v perpendicular to a uniform magnetic field experiences a motional EMF.

ε = Blv

Where:
- B = magnetic field
- l = conductor length
- v = speed

The formula assumes that the conductor, velocity and magnetic field have the appropriate mutually perpendicular orientation.

For a more general arrangement:

ε = ∫ (v × B) · dl

This expression accounts for the orientation of the conductor and motion.

## 9. Motional EMF and Magnetic Force

When a conductor moves through a magnetic field:
- Free charges inside the conductor experience magnetic forces.
- Positive and negative charges separate.
- An electric field develops inside the conductor.
- A potential difference is established across its ends.

If the circuit is closed, an induced current flows.

The induced current produces a magnetic force opposing the motion that caused the induction.

An external agent must perform work to maintain the motion.

This mechanical work is converted into electrical energy.

## 10. Eddy Currents

Eddy currents are circulating currents induced inside a bulk conductor when the magnetic flux through different regions changes.

They form closed loops within the material.

Effects include:
- Unwanted heating.
- Energy losses in transformers and electrical machines.
- Magnetic damping.

Methods of reducing eddy currents include:
- Laminating transformer cores.
- Using thin insulated sheets.
- Selecting materials with suitable electrical resistivity.

Applications include:
- Induction heating.
- Electromagnetic braking.
- Damping in measuring instruments.
- Metal detection systems.

## 11. Self-Induction

Self-induction occurs when a changing current in a circuit changes its own magnetic flux linkage, producing an induced EMF in the same circuit.

The induced EMF is:

ε = -L(dI/dt)

Where:
- L = self-inductance
- dI/dt = rate of change of current

The SI unit of inductance is the henry (H).

One henry is the inductance of a circuit in which a current changing at 1 A/s produces an induced EMF of 1 V in magnitude.

The negative sign follows Lenz's law.

## 12. Self-Inductance of a Solenoid

For a long ideal solenoid:

L = μN²A/l

Where:
- μ = permeability of the core material
- N = number of turns
- A = cross-sectional area
- l = length of the solenoid

Increasing the number of turns increases inductance significantly because L is proportional to N².

## 13. Mutual Induction

Mutual induction occurs when a changing current in one coil produces a changing magnetic flux through a nearby coil, inducing an EMF in it.

The induced EMF in the secondary coil is:

ε2 = -M(dI1/dt)

Where:
- M = mutual inductance
- I1 = current in the primary coil

The SI unit of mutual inductance is the henry.

Mutual induction is the operating principle of transformers.

## 14. Energy Stored in an Inductor

An inductor stores energy in its magnetic field.

The stored energy is:

U = 1/2 LI²

Where:
- L = inductance
- I = current

The energy is supplied by the source while establishing the current against the induced EMF.

## 15. Alternating Magnetic Flux in a Rotating Coil

Consider a coil of N turns and area A rotating at angular speed ω in a uniform magnetic field B.

The magnetic flux through the coil is:

ΦB = BA cos(ωt)

Flux linkage is:

NΦB = NBA cos(ωt)

Using Faraday's law:

ε = NBAω sin(ωt)

Therefore:

ε = ε0 sin(ωt)

Where:

ε0 = NBAω

This is the basic principle behind an AC generator.

## 16. Applications of Electromagnetic Induction

Electromagnetic induction is used in:

- Electric generators.
- Transformers.
- Induction cooktops.
- Wireless charging systems.
- Dynamic microphones.
- Electric guitar pickups.
- Metal detectors.
- Electromagnetic braking.
- Inductive sensors.

## 17. Numerical Applications

**Example 1: Induced EMF**

A coil has 100 turns. Its magnetic flux per turn changes from 0.02 Wb to 0.005 Wb in 0.05 seconds.

Magnitude of induced EMF:

|ε| = N|ΔΦB/Δt|

|ε| = 100 × |0.005 - 0.02| / 0.05

|ε| = 30 V

**Example 2: Motional EMF**

A conductor of length 0.5 m moves at 4 m/s perpendicular to a magnetic field of 0.2 T.

ε = Blv

ε = 0.2 × 0.5 × 4

ε = 0.4 V

**Example 3: Energy stored in an inductor**

An inductor of 2 H carries a current of 3 A.

U = 1/2 LI²

U = 1/2 × 2 × 3²

U = 9 J

## Common Exam Traps

- Magnetic flux is a scalar quantity.
- Flux depends on the angle measured from the surface normal.
- A changing magnetic flux induces EMF.
- A closed circuit is required for induced current, but not for induced EMF.
- Faraday's law includes a negative sign because of Lenz's law.
- Lenz's law opposes the change in flux, not necessarily the original field.
- Motional EMF depends on conductor length, speed and magnetic field orientation.
- Self-induction occurs in the same circuit.
- Mutual induction occurs between different circuits.
- Eddy currents are circulating currents inside bulk conductors.
- An inductor stores energy in its magnetic field.
- A changing current is required to produce self-induced EMF.

## Quiz

1. According to Faraday's law, induced EMF is proportional to:

- [ ] Total resistance of the circuit
- [x] Rate of change of magnetic flux linkage
- [ ] Magnetic field alone
- [ ] Total charge stored in the circuit

> Faraday's law states that induced EMF equals the negative rate of change of magnetic flux linkage.

2. Lenz's law states that induced current opposes:

- [ ] The existence of every magnetic field
- [ ] The motion of every charge
- [x] The change in magnetic flux that produces it
- [ ] The resistance of the circuit

> The induced magnetic effect opposes the change in flux responsible for induction, consistent with conservation of energy.

3. An inductor of 4 H carries a current of 2 A. The energy stored is:

- [ ] 4 J
- [x] 8 J
- [ ] 16 J
- [ ] 32 J

> U = 1/2 LI² = 1/2 × 4 × 2² = 8 J.