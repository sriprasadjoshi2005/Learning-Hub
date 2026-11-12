---
title: Inductors and Inductance
level: intermediate
---

# Inductors and Inductance

## Introduction

An inductor is a passive electrical component that stores energy in a magnetic field when electric current flows through it.

It commonly consists of a conducting wire wound into a coil. When current flows through the coil, a magnetic field is established around it. Changes in this current produce a changing magnetic field, which induces an electromotive force that opposes the change.

Inductors are widely used in filters, oscillators, switching power supplies, transformers, radio-frequency circuits, and energy-storage systems.

This lesson examines magnetic flux, inductance, self-induction, mutual induction, series and parallel combinations, energy storage, inductive reactance, and practical inductor applications.

## 1. Construction of an Inductor

An inductor generally consists of a conducting wire wound into a coil.

A magnetic core may be inserted to increase its inductance.

Common core materials include:
- Air.
- Ferrite.
- Laminated iron.
- Powdered iron.

```text
      Coil
    ((((((((
   (((((((((
    (((((((((
```

When current flows through the coil, magnetic flux is produced.

The inductor opposes changes in current through electromagnetic induction.

## 2. Magnetic Flux

Magnetic flux represents the total magnetic field passing through a specified surface.

It is represented by:

\[
\Phi
\]

The SI unit of magnetic flux is the weber (Wb).

For a uniform magnetic field:

\[
\boxed{\Phi=BA\cos\theta}
\]

Where:
- \(B\) = magnetic flux density in tesla.
- \(A\) = area in square metres.
- \(\theta\) = angle between the magnetic field and the surface normal.

Magnetic flux is important because changes in flux are responsible for induced electromotive force.

## 3. Inductance

Inductance is the property of a circuit that opposes changes in current by producing an induced electromotive force.

For a coil with \(N\) turns and magnetic flux \(\Phi\):

\[
\boxed{L=\frac{N\Phi}{I}}
\]

Where:
- \(L\) = inductance in henries.
- \(N\) = number of turns.
- \(\Phi\) = magnetic flux through each turn, assuming the same flux links every turn.
- \(I\) = current.

The SI unit of inductance is the henry (H).

One henry is the inductance that produces an induced voltage of one volt when current changes at one ampere per second.

\[
1\text{ H}=1\frac{\text{V}\cdot\text{s}}{\text{A}}
\]

Common smaller units include:
- Millihenry (mH).
- Microhenry (μH).
- Nanohenry (nH).

## 4. Factors Affecting Inductance

For a long solenoid with a uniform core:

\[
\boxed{L=\frac{\mu N^2A}{l}}
\]

Where:
- \(\mu\) = permeability of the core.
- \(N\) = number of turns.
- \(A\) = cross-sectional area.
- \(l\) = magnetic path length.

### 4.1 Number of Turns

Inductance is proportional to the square of the number of turns.

\[
L\propto N^2
\]

Doubling the number of turns ideally increases inductance by a factor of four, assuming all other parameters remain unchanged.

### 4.2 Core Permeability

A core material with higher magnetic permeability generally increases inductance.

### 4.3 Cross-Sectional Area

Increasing the core cross-sectional area increases inductance for the ideal solenoid model.

### 4.4 Magnetic Path Length

Increasing the magnetic path length reduces inductance when the other parameters remain constant.

## 5. Faraday's Law of Electromagnetic Induction

Faraday's law states that the induced electromotive force is proportional to the rate of change of magnetic flux linkage.

\[
\boxed{e=-N\frac{d\Phi}{dt}}
\]

The negative sign represents Lenz's law.

### 5.1 Lenz's Law

Lenz's law states that the direction of induced electromotive force is such that it opposes the change in magnetic flux responsible for producing it.

This opposition is a consequence of energy conservation.

In an inductor, the induced voltage opposes changes in current.

## 6. Self-Induction

Self-induction occurs when a changing current in a coil produces a changing magnetic field, which induces an electromotive force in the same coil.

The induced voltage is:

\[
\boxed{v_L=-L\frac{di}{dt}}
\]

The negative sign indicates opposition to the change in current under the passive sign convention.

The magnitude is:

\[
|v_L|=L\left|\frac{di}{dt}\right|
\]

An inductor opposes rapid changes in current more strongly than slow changes.

### 6.1 Important Consequences

- Constant current produces zero ideal induced voltage.
- Increasing current produces an induced voltage opposing the increase.
- Decreasing current produces an induced voltage opposing the decrease.
- An ideal inductor cannot experience an instantaneous current change under finite voltage.

## 7. Ideal and Practical Inductors

### 7.1 Ideal Inductor

An ideal inductor has:
- Zero winding resistance.
- No core losses.
- No parasitic capacitance.
- Perfect magnetic coupling within its own winding.

It stores and releases energy without dissipating it.

### 7.2 Practical Inductor

A practical inductor has:
- Winding resistance.
- Core losses.
- Leakage flux.
- Parasitic capacitance.
- Possible magnetic saturation.

Winding resistance produces heat when current flows.

Core losses may include hysteresis and eddy-current losses.

### 7.3 Magnetic Saturation

Magnetic saturation occurs when increasing magnetising current produces progressively smaller increases in magnetic flux density.

Beyond the saturation region, the effective inductance may decrease significantly.

This is important in power-converter design.

## 8. Inductors in Series

For uncoupled inductors connected in series, the same current flows through every inductor.

The total voltage is the sum of individual voltages.

\[
V_T=V_1+V_2+\cdots+V_n
\]

Since:

\[
V=L\frac{di}{dt}
\]

For uncoupled inductors:

\[
\boxed{L_T=L_1+L_2+\cdots+L_n}
\]

For two inductors:

\[
L_T=L_1+L_2
\]

This relationship assumes negligible mutual magnetic coupling.

## 9. Inductors in Parallel

For uncoupled inductors connected in parallel, the voltage across every inductor is equal.

The equivalent inductance is:

\[
\boxed{
\frac{1}{L_T}=
\frac{1}{L_1}+
\frac{1}{L_2}+\cdots+
\frac{1}{L_n}
}
\]

For two inductors:

\[
\boxed{L_T=\frac{L_1L_2}{L_1+L_2}}
\]

This relationship also assumes negligible mutual coupling.

## 10. Mutual Induction

Mutual induction occurs when a changing current in one coil produces a changing magnetic flux that links another coil and induces a voltage in it.

The mutual inductance is represented by \(M\).

The induced voltage in the second coil is:

\[
\boxed{v_2=-M\frac{di_1}{dt}}
\]

Where:
- \(M\) = mutual inductance in henries.
- \(di_1/dt\) = rate of change of current in the first coil.

Mutual induction is the operating principle behind transformers.

### 10.1 Coupling Coefficient

The coupling coefficient measures the degree of magnetic coupling between two coils.

\[
\boxed{k=\frac{M}{\sqrt{L_1L_2}}}
\]

For ordinary passive magnetic coupling:

\[
0\leq k\leq1
\]

A value close to 1 indicates strong coupling.

A lower value indicates greater leakage flux.

## 11. Energy Stored in an Inductor

An inductor stores energy in its magnetic field.

The instantaneous power absorbed by an ideal inductor is:

\[
p=vi
\]

Using:

\[
v=L\frac{di}{dt}
\]

Therefore:

\[
p=Li\frac{di}{dt}
\]

Since:

\[
p=\frac{dW}{dt}
\]

\[
dW=Li\,di
\]

Integrating from zero current to final current \(I\):

\[
W=\int_0^I Li\,di
\]

\[
W=L\left[\frac{i^2}{2}\right]_0^I
\]

Therefore:

\[
\boxed{W=\frac12LI^2}
\]

Where:
- \(W\) = stored energy in joules.
- \(L\) = inductance in henries.
- \(I\) = current in amperes.

## 12. Inductive Reactance

In an AC circuit, an inductor opposes alternating current through inductive reactance.

\[
\boxed{X_L=2\pi fL}
\]

Where:
- \(X_L\) = inductive reactance in ohms.
- \(f\) = frequency in hertz.
- \(L\) = inductance in henries.

As frequency increases, inductive reactance increases.

As inductance increases, inductive reactance increases.

For an ideal inductor in sinusoidal steady state, voltage leads current by \(90^\circ\).

## 13. Inductor Behaviour in DC and AC Circuits

### 13.1 DC Steady State

For a constant DC current:

\[
\frac{di}{dt}=0
\]

Therefore:

\[
v_L=0
\]

An ideal inductor behaves as a short circuit under DC steady-state conditions.

A practical inductor still has winding resistance.

### 13.2 During Switching

An inductor opposes sudden current changes.

If a circuit attempts to interrupt the current suddenly, the inductor may generate a large voltage.

This is why switching inductive loads can produce voltage spikes.

Flyback diodes, snubber circuits, and other protection methods are used to control these effects.

## 14. Worked Numerical Examples

### Example 1: Calculating Inductance

**Given:**

- Number of turns = 200.
- Flux per turn = 0.5 mWb.
- Current = 2 A.

**Find:** Inductance.

**Formula:**

\[
L=\frac{N\Phi}{I}
\]

**Solution:**

\[
L=\frac{200(0.5\times10^{-3})}{2}
\]

\[
L=\frac{0.1}{2}
\]

\[
\boxed{L=0.05\text{ H}=50\text{ mH}}
\]

### Example 2: Induced Voltage

**Given:**

- Inductance = 0.2 H.
- Current increases from 1 A to 5 A.
- Time interval = 0.02 s.

**Find:** Magnitude of induced voltage.

**Solution:**

\[
\frac{di}{dt}=\frac{5-1}{0.02}
\]

\[
\frac{di}{dt}=200\text{ A/s}
\]

Using:

\[
|v_L|=L\frac{di}{dt}
\]

\[
|v_L|=0.2\times200
\]

\[
\boxed{|v_L|=40\text{ V}}
\]

The induced voltage acts in opposition to the current increase.

### Example 3: Energy Stored in an Inductor

**Given:**

- Inductance = 0.5 H.
- Current = 4 A.

**Find:** Stored energy.

**Formula:**

\[
W=\frac12LI^2
\]

**Solution:**

\[
W=\frac12(0.5)(4)^2
\]

\[
W=0.25\times16
\]

\[
\boxed{W=4\text{ J}}
\]

### Example 4: Inductive Reactance

**Given:**

- Frequency = 50 Hz.
- Inductance = 0.1 H.

**Find:** Inductive reactance.

**Formula:**

\[
X_L=2\pi fL
\]

**Solution:**

\[
X_L=2\pi(50)(0.1)
\]

\[
\boxed{X_L\approx31.42\ \Omega}
\]

### Example 5: Inductors in Parallel

**Given:**

- \(L_1=6\text{ mH}\)
- \(L_2=3\text{ mH}\)

**Find:** Equivalent inductance.

**Solution:**

\[
L_T=\frac{L_1L_2}{L_1+L_2}
\]

\[
L_T=\frac{6\times3}{6+3}
\]

\[
\boxed{L_T=2\text{ mH}}
\]

## 15. Practical Applications

Inductors are used in:

- DC-DC converters.
- Switching power supplies.
- Radio-frequency filters.
- Signal-processing circuits.
- Oscillators.
- Electromagnetic interference filters.
- Energy-storage systems.
- Transformers and coupled circuits.
- Motor drives.
- Relay and solenoid circuits.

### 15.1 Switching Power Supplies

Inductors store energy during one part of a switching cycle and release it during another.

This enables efficient voltage conversion.

### 15.2 Filters

Inductive reactance increases with frequency, making inductors useful in frequency-selective circuits.

### 15.3 Electromagnetic Interference Suppression

Inductors and chokes oppose unwanted high-frequency current components and help reduce conducted interference.

## 16. Capacitors and Inductors Compared

| Property | Capacitor | Inductor |
|---|---|---|
| Stored energy | Electric field | Magnetic field |
| Main property | Capacitance | Inductance |
| SI unit | Farad | Henry |
| Opposes | Sudden voltage change | Sudden current change |
| DC steady-state ideal behaviour | Open circuit | Short circuit |
| AC reactance | Decreases with frequency | Increases with frequency |
| Energy formula | \(\frac12CV^2\) | \(\frac12LI^2\) |

## 17. Common Exam Traps

1. **Confusing reactance formulas:** Capacitive reactance is inversely proportional to frequency, while inductive reactance is directly proportional to frequency.

2. **Ignoring the negative sign in Faraday's law:** The sign represents Lenz's law.

3. **Using the wrong energy formula:** Inductor energy is \(\frac12LI^2\).

4. **Assuming an inductor blocks DC:** An ideal inductor behaves as a short circuit under steady DC conditions.

5. **Ignoring winding resistance:** Practical inductors dissipate power.

6. **Applying series and parallel rules without checking coupling:** Mutual inductance can change the equivalent inductance.

7. **Confusing inductance with reactance:** Inductance is a component property, whereas reactance depends on both inductance and frequency.

## Quiz

1. An inductor of 0.25 H carries a current of 4 A. What energy is stored in its magnetic field?

   - [ ] 1 J
   - [ ] 4 J
   - [x] 2 J
   - [ ] 8 J

   > Stored energy is \(W=\frac12LI^2=\frac12(0.25)(4^2)=2\) J.

2. What happens to the inductive reactance when the frequency of an AC supply doubles while inductance remains constant?

   - [ ] It becomes half.
   - [ ] It remains unchanged.
   - [x] It doubles.
   - [ ] It becomes zero.

   > Inductive reactance is \(X_L=2\pi fL\). It is directly proportional to frequency, so doubling frequency doubles reactance.

3. An ideal inductor is connected to a constant DC voltage source through a suitable circuit. Immediately after switching, current begins to increase. What principle explains this behaviour?

   - [ ] The inductor immediately becomes an open circuit.
   - [ ] The inductor stores energy in an electric field.
   - [x] The induced voltage opposes the change in current.
   - [ ] The inductance becomes zero.

   > Self-induction produces an electromotive force that opposes the change in current. The current therefore cannot change instantaneously and increases according to the applied circuit voltage.