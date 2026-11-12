---
title: PN Junction Diodes and Their Characteristics
level: intermediate
---

# PN Junction Diodes and Their Characteristics

A PN junction diode is a two-terminal semiconductor device formed by joining P-type and N-type semiconductor regions.

It allows current to flow easily in one direction under forward bias and strongly opposes current under reverse bias, within its normal operating limits.

PN junction diodes are fundamental components in rectifiers, voltage regulators, switching circuits, signal-processing systems, protection circuits, and power supplies.

This lesson explains how a PN junction is formed, how the depletion region and potential barrier develop, how forward and reverse bias affect the junction, and how to interpret the diode's current-voltage characteristics.

## 1. Introduction to PN Junction Diodes

A PN junction is formed when P-type and N-type regions exist next to each other in a semiconductor crystal.

The two regions have different majority charge carriers:

- P-type region: holes are the majority carriers.
- N-type region: electrons are the majority carriers.

A diode has two terminals:

1. Anode: connected to the P-type region.
2. Cathode: connected to the N-type region.

The conventional diode symbol is:

    Anode                 Cathode
      A                      K
      |                      |
      ──────────|>|───────────

The vertical bar represents the cathode.

A diode is a non-linear device because its current does not vary linearly with applied voltage.

## 2. Formation of a PN Junction

When P-type and N-type regions are brought together to form a junction, a concentration difference exists across the boundary.

The N-type region contains a high concentration of electrons, while the P-type region contains a high concentration of holes.

This concentration difference causes diffusion.

### 2.1 Diffusion of Charge Carriers

Diffusion is the movement of charge carriers from a region of higher concentration to a region of lower concentration.

At the junction:

- Electrons diffuse from the N-region into the P-region.
- Holes diffuse from the P-region into the N-region.

When electrons enter the P-region, they may recombine with holes.

Similarly, holes entering the N-region may recombine with electrons.

This process leaves behind immobile ionized impurity atoms near the junction.

### 2.2 Formation of the Depletion Region

The region near the junction becomes depleted of mobile majority carriers.

It contains:

- Positively charged donor ions on the N-side.
- Negatively charged acceptor ions on the P-side.

This region is called the depletion region or depletion layer.

The fixed ions create an internal electric field.

### 2.3 Potential Barrier

The electric field produces a potential difference across the depletion region.

This potential difference opposes further diffusion of majority carriers.

It is called the barrier potential or built-in potential.

Typical approximate room-temperature values are:

- Silicon: approximately 0.7 V.
- Germanium: approximately 0.3 V.

These are useful approximate values, not universal fixed turn-on voltages.

The actual built-in potential depends on doping concentrations and temperature.

### 2.4 Equilibrium Condition

At thermal equilibrium, two carrier transport mechanisms oppose one another:

1. Diffusion current caused by carrier concentration gradients.
2. Drift current caused by the electric field in the depletion region.

At equilibrium:

\[
I_{\text{diffusion}}+I_{\text{drift}}=0
\]

Therefore, the net current through the junction is zero when no external voltage is applied.

## 3. Depletion Region and Junction Structure

A simplified representation of a PN junction is:

    P-type region      Depletion region       N-type region

    Holes             Negative ions           Electrons
    + + + +           - - - | + + +           - - - -

                       Junction

The depletion region contains very few mobile majority carriers compared with the neutral regions.

Its width depends on:

- Applied voltage.
- Doping concentration.
- Semiconductor material.
- Temperature.

A lightly doped side generally contains a larger portion of the depletion width.

## 4. Biasing of a PN Junction Diode

Biasing means applying an external voltage to a semiconductor device to control its operation.

A PN junction diode can be operated in two main biasing conditions:

1. Forward bias.
2. Reverse bias.

## 5. Forward Bias

A diode is forward-biased when:

- The positive terminal of the supply is connected to the P-type region.
- The negative terminal of the supply is connected to the N-type region.

### 5.1 Effect of Forward Bias

The external voltage opposes the built-in potential barrier.

As the applied forward voltage increases:

1. The potential barrier decreases.
2. The depletion region becomes narrower.
3. Majority carriers can cross the junction more easily.
4. The forward current increases rapidly.

When the forward voltage is sufficiently large, the diode conducts significant current.

### 5.2 Forward Current

The ideal diode current equation is:

\[
I_D=I_S\left(e^{V_D/(\eta V_T)}-1\right)
\]

Where:

- \(I_D\) = diode current.
- \(I_S\) = reverse saturation current.
- \(V_D\) = voltage across the diode.
- \(\eta\) = ideality factor.
- \(V_T\) = thermal voltage.

Thermal voltage is:

\[
V_T=\frac{kT}{q}
\]

At approximately 300 K:

\[
V_T\approx25.85\,mV
\]

The ideality factor is commonly between 1 and 2, depending on the diode and operating conditions.

The exponential relationship explains why a small increase in forward voltage can cause a large increase in diode current.

## 6. Reverse Bias

A diode is reverse-biased when:

- The positive terminal of the supply is connected to the N-type region.
- The negative terminal of the supply is connected to the P-type region.

### 6.1 Effect of Reverse Bias

The external voltage supports the built-in potential barrier.

As the reverse voltage increases:

1. The potential barrier increases.
2. The depletion region becomes wider.
3. Majority carrier movement across the junction becomes more difficult.
4. Only a very small reverse current normally flows.

This small current is mainly due to minority carriers and is called reverse saturation current.

### 6.2 Reverse Saturation Current

Reverse saturation current is usually small in ordinary diodes.

It depends on:

- Semiconductor material.
- Junction temperature.
- Junction area.
- Device construction.

It generally increases significantly with temperature.

## 7. Breakdown in a PN Junction

If reverse voltage becomes sufficiently high, the diode may enter breakdown.

The reverse current can increase sharply.

Two important breakdown mechanisms are:

### 7.1 Zener Breakdown

Zener breakdown occurs when a sufficiently strong electric field allows electrons to tunnel through the junction barrier.

It is generally associated with heavily doped junctions and relatively thin depletion regions.

It commonly occurs at lower breakdown voltages.

### 7.2 Avalanche Breakdown

Avalanche breakdown occurs when charge carriers accelerated by the electric field gain enough energy to create additional electron-hole pairs through impact ionization.

This produces carrier multiplication and a large reverse current.

It is generally associated with more lightly doped junctions and wider depletion regions.

Both mechanisms are important in voltage-reference and protection devices.

A normal diode must not be operated in breakdown unless it is specifically designed and rated for that condition.

## 8. Current-Voltage Characteristics

The current-voltage characteristic describes how diode current changes with the voltage applied across it.

A diode characteristic has three important regions.

### 8.1 Forward Region

In forward bias, current is initially small and then rises rapidly as voltage increases.

For a silicon diode, a forward voltage around 0.7 V is often used as a practical approximation in simple circuit analysis.

The actual forward voltage depends on current and temperature.

### 8.2 Reverse Region

In reverse bias, a small reverse saturation current flows.

Before breakdown, this current changes relatively little with reverse voltage.

### 8.3 Breakdown Region

At the breakdown voltage, reverse current increases sharply.

A suitable external current-limiting resistance is necessary to prevent excessive current.

### 8.4 Simplified I-V Characteristic

    Diode current I_D
          ↑
          |
          |                   /
          |                 /
          |              __/
          |_____________/________________→ V_D
          |            Forward region
          |
          |  Reverse saturation current
          |-------------------------
          |
          |                 |
          |                 |
          |                 ↓
          |            Breakdown

This is a conceptual diagram and is not drawn to scale.

## 9. Diode Models

Different diode models are used depending on the required accuracy.

### 9.1 Ideal Diode Model

An ideal diode behaves as:

- A short circuit in forward bias.
- An open circuit in reverse bias.

Thus:

\[
V_D=0
\]

for an ideal conducting diode.

The ideal model ignores forward voltage drop and reverse leakage.

### 9.2 Practical Constant-Voltage Model

A practical model assumes a nearly constant forward voltage.

Typical approximations are:

- Silicon: \(V_D\approx0.7\,V\).
- Germanium: \(V_D\approx0.3\,V\).

These values simplify ordinary circuit calculations.

### 9.3 Piecewise-Linear Model

A more detailed model includes:

- A threshold or cut-in voltage.
- A small forward resistance.

The forward voltage can be approximated as:

\[
V_D=V_\gamma+I_Dr_d
\]

Where:

- \(V_\gamma\) = approximate threshold voltage.
- \(r_d\) = incremental or model resistance.
- \(I_D\) = diode current.

## 10. Worked Numerical Examples

### Example 1: Forward-Biased Silicon Diode

**Given:**

- Supply voltage: \(V_S=10\,V\).
- Series resistance: \(R=1\,k\Omega\).
- Silicon diode forward voltage: \(V_D=0.7\,V\).

Calculate the diode current using the constant-voltage model.

**Formula:**

\[
I_D=\frac{V_S-V_D}{R}
\]

**Solution:**

\[
I_D=\frac{10-0.7}{1000}
\]

\[
I_D=\frac{9.3}{1000}
\]

\[
I_D=0.0093\,A
\]

**Final Answer:**

\[
\boxed{I_D=9.3\,mA}
\]

### Example 2: Diode Power Dissipation

**Given:**

- Forward voltage: \(V_D=0.7\,V\).
- Forward current: \(I_D=20\,mA\).

Calculate the power dissipated by the diode.

**Formula:**

\[
P_D=V_DI_D
\]

**Solution:**

Convert current:

\[
I_D=20\times10^{-3}\,A
\]

Substitute:

\[
P_D=0.7\times20\times10^{-3}
\]

\[
P_D=0.014\,W
\]

**Final Answer:**

\[
\boxed{P_D=14\,mW}
\]

## 11. Temperature Effects on Diode Characteristics

Temperature affects both forward and reverse diode behaviour.

For a silicon diode operating at a specified current, the forward voltage generally decreases as junction temperature increases.

A commonly used approximate temperature coefficient is around:

\[
-2\,mV/^\circ C
\]

This is only an approximation and varies with current and device construction.

Reverse saturation current generally increases strongly with temperature.

These effects are important in:

- Temperature-sensitive circuits.
- Power supplies.
- Thermal protection.
- Precision measurement systems.
- Semiconductor device design.

## 12. Practical Applications of PN Junction Diodes

### 12.1 Rectification

Diodes convert alternating current into unidirectional current.

Rectifiers are used in power supplies and electronic equipment.

### 12.2 Signal Clipping

Diodes can limit a signal's voltage to a specified range.

### 12.3 Signal Clamping

Diode circuits can shift the DC level of a waveform.

### 12.4 Reverse Polarity Protection

A diode can protect a circuit against incorrect supply polarity.

### 12.5 Switching

Diodes can control current paths in switching and logic circuits.

### 12.6 Protection Against Inductive Voltage Spikes

A diode connected across an inductive load can provide a path for current when the driving switch turns off.

This application is particularly important for relay coils and small motors.

## 13. Common Examination Traps

1. The anode is connected to the P-type region; the cathode is connected to the N-type region.
2. Forward bias reduces the depletion-region width.
3. Reverse bias increases the depletion-region width.
4. Forward current is mainly associated with majority carrier injection.
5. Reverse leakage current is mainly associated with minority carriers.
6. The approximate 0.7 V silicon value is not an exact universal turn-on voltage.
7. A diode is non-linear and does not obey Ohm's law as a complete device model.
8. Breakdown produces a sharp increase in reverse current.
9. Zener and avalanche breakdown are different physical mechanisms.
10. A normal diode requires current limiting if it is operated in a region of substantial conduction.

## Quiz

1. What happens to the depletion region when a PN junction diode is forward-biased?

- [ ] It becomes infinitely wide.
- [x] It becomes narrower.
- [ ] It disappears under every possible forward voltage.
- [ ] It changes into an insulating crystal.

> Forward bias opposes the built-in potential barrier. This reduces the depletion-region width and allows majority carriers to cross the junction more easily.

2. Which carriers are mainly responsible for the small reverse saturation current in an ordinary PN junction diode?

- [ ] Majority carriers only.
- [ ] Fixed donor ions.
- [x] Minority carriers.
- [ ] Neutrons.

> Minority carriers generated thermally near the junction can be swept across the depletion region by the electric field, producing the small reverse saturation current.

3. A silicon diode has a forward voltage of 0.7 V and carries 15 mA. What is its power dissipation?

- [ ] 1.05 W.
- [ ] 0.105 W.
- [x] 10.5 mW.
- [ ] 105 mW.

> Power is \(P=VI\). Therefore, \(P=0.7\times0.015=0.0105\,W=10.5\,mW\).
