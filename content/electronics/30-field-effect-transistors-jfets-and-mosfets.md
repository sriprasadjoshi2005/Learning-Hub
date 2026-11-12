---
title: Field-Effect Transistors Including JFETs and MOSFETs
level: advanced
---

# Field-Effect Transistors Including JFETs and MOSFETs

A field-effect transistor (FET) is a semiconductor device in which an electric field controls the current flowing through a conducting channel.

Unlike a bipolar junction transistor, which uses both electrons and holes and is commonly controlled by base current, a FET is primarily a voltage-controlled device.

FETs are widely used in digital integrated circuits, switching power supplies, amplifiers, microprocessors, memory devices, motor controllers, and electronic power systems.

The two major categories studied in this lesson are:

1. Junction field-effect transistors (JFETs).
2. Metal-oxide-semiconductor field-effect transistors (MOSFETs).

This lesson explains their construction, operation, characteristics, important equations, configurations, and practical applications.

## 1. Introduction to Field-Effect Transistors

A field-effect transistor controls current by using an electric field to influence the conductivity of a semiconductor channel.

Its three main terminals are:

1. Gate.
2. Source.
3. Drain.

The source supplies charge carriers to the channel.

The drain collects charge carriers from the channel.

The gate controls the channel conductivity.

The main advantage of many FETs is their high input resistance, which results from the very small gate current under normal operating conditions.

## 2. Classification of FETs

Field-effect transistors are classified into two major families:

### 2.1 Junction Field-Effect Transistor

A JFET uses a reverse-biased PN junction to control the width of its conducting channel.

Types:

- N-channel JFET.
- P-channel JFET.

### 2.2 Metal-Oxide-Semiconductor Field-Effect Transistor

A MOSFET uses an insulated gate separated from the semiconductor channel by a thin dielectric layer, usually silicon dioxide or another gate dielectric.

Types include:

- N-channel enhancement MOSFET.
- P-channel enhancement MOSFET.
- N-channel depletion MOSFET.
- P-channel depletion MOSFET.

## 3. Junction Field-Effect Transistor

A JFET contains a semiconductor channel between the source and drain terminals.

The gate forms a PN junction with the channel.

For an N-channel JFET, the channel is N-type and the gate regions are P-type.

### 3.1 Construction of an N-Channel JFET

A simplified structure is:

    P-type Gate       P-type Gate
         |                 |
         |                 |
    ┌────┴─────────────────┴────┐
    │                           │
    │       N-type Channel      │
    │                           │
    └───────────────────────────┘
        Source          Drain

The gate junction is normally reverse-biased during operation.

### 3.2 Working Principle

When a drain-to-source voltage is applied:

- Electrons flow through the N-type channel.
- Drain current is established.
- The reverse-biased gate junction produces depletion regions.
- The depletion regions extend into the channel.

Changing gate-to-source voltage changes the depletion-region width.

This changes the effective channel width and controls drain current.

### 3.3 N-Channel JFET Operation

For an N-channel JFET, the gate-to-source voltage is normally zero or negative.

Making the gate voltage more negative:

1. Increases reverse bias.
2. Widens the depletion region.
3. Narrows the conducting channel.
4. Reduces drain current.

At a sufficiently negative gate voltage, the channel is effectively cut off.

### 3.4 P-Channel JFET

A P-channel JFET has a P-type channel and N-type gate regions.

Its voltage and current polarities are opposite to those of an N-channel JFET.

The main operating principle remains the same: a reverse-biased gate junction controls the channel width.

## 4. JFET Characteristics

The drain characteristics describe the relationship between drain current and drain-to-source voltage for different gate-to-source voltages.

### 4.1 Ohmic Region

At small drain-to-source voltage:

- The channel behaves approximately like a voltage-controlled resistor.
- Drain current increases with drain voltage.

This region is also called the linear region.

### 4.2 Pinch-Off and Saturation Region

As drain voltage increases, the channel becomes progressively narrower near the drain.

Eventually, the current becomes approximately constant for a given gate voltage.

This is the pinch-off or saturation region.

The term pinch-off describes the formation of a strongly depleted region near the drain; it does not mean that the drain current immediately becomes zero.

### 4.3 Cut-Off Region

When the gate-to-source voltage reaches the cut-off condition:

\[
V_{GS}=V_{GS(off)}
\]

The channel current becomes approximately zero.

For an N-channel JFET, \(V_{GS(off)}\) is normally negative.

### 4.4 Simplified Characteristic

    Drain current I_D
          ↑
          |       V_GS = 0 V
          |     ─────────────
          |   /
          |  /    V_GS = -1 V
          | /   ────────────
          |/  /
          | /       V_GS = -2 V
          |/      ─────────
          |________________________→ V_DS

The actual curves depend on the device and its parameters.

## 5. Shockley Equation for a JFET

The Shockley equation describes the drain current in the saturation region of an idealized JFET.

\[
\boxed{
I_D=I_{DSS}
\left(1-\frac{V_{GS}}{V_P}\right)^2
}
\]

Where:

- \(I_D\) = drain current.
- \(I_{DSS}\) = drain current when \(V_{GS}=0\) in the saturation region.
- \(V_{GS}\) = gate-to-source voltage.
- \(V_P\) = pinch-off voltage parameter, using the sign convention of the device.

For an N-channel JFET, \(V_P\) is commonly negative.

The equation is applicable over the normal transfer-characteristic range and should not be used outside the model's operating conditions.

### 5.1 Special Conditions

When:

\[
V_{GS}=0
\]

Then:

\[
I_D=I_{DSS}
\]

When:

\[
V_{GS}=V_P
\]

Then:

\[
I_D=0
\]

This is the idealized cut-off condition.

## 6. MOSFET Construction

A MOSFET consists of:

- Gate.
- Source.
- Drain.
- Semiconductor body or substrate.
- Thin insulating gate dielectric.

The gate is electrically insulated from the semiconductor by the dielectric.

Therefore, almost no steady-state DC current normally flows into the gate, apart from leakage.

### 6.1 N-Channel MOSFET

An N-channel MOSFET commonly uses:

- P-type substrate.
- N-type source region.
- N-type drain region.
- Insulated gate above the channel region.

When the appropriate gate voltage is applied, an N-type conducting channel can form or become stronger.

### 6.2 P-Channel MOSFET

A P-channel MOSFET uses opposite semiconductor polarities.

Its operating voltage and current polarities are generally opposite to those of an N-channel MOSFET.

## 7. Enhancement-Mode MOSFET

An enhancement MOSFET is normally OFF when its gate-to-source voltage is zero.

Applying a suitable gate voltage creates a conducting channel.

### 7.1 N-Channel Enhancement MOSFET

For an N-channel enhancement MOSFET:

- The body is normally P-type.
- Source and drain are N-type.
- A positive gate-to-source voltage attracts electrons towards the gate dielectric interface.
- A conducting inversion channel forms when the threshold condition is reached.

The voltage at which significant channel formation begins is called the threshold voltage.

It is represented by:

\[
V_{TH}
\]

When:

\[
V_{GS}<V_{TH}
\]

the MOSFET is ideally in the cut-off condition in the simple long-channel model.

When:

\[
V_{GS}>V_{TH}
\]

a conducting channel can form.

### 7.2 P-Channel Enhancement MOSFET

A P-channel enhancement MOSFET operates with opposite polarity.

Its gate-to-source voltage must become sufficiently negative relative to the source to form a conducting channel.

### 7.3 Characteristics

Enhancement MOSFETs are normally OFF without sufficient gate drive.

They are widely used in:

- Switching regulators.
- Digital logic.
- Motor drivers.
- Power switching.
- CMOS integrated circuits.

## 8. Depletion-Mode MOSFET

A depletion MOSFET has a conducting channel even when:

\[
V_{GS}=0
\]

Its gate voltage can either reduce or increase channel conductivity.

For an N-channel depletion MOSFET:

- Negative gate voltage depletes the channel.
- Positive gate voltage enhances channel conductivity.

This behaviour differs from an enhancement MOSFET, which is normally OFF at zero gate-to-source voltage.

## 9. MOSFET Operating Regions

An enhancement MOSFET commonly operates in three regions.

### 9.1 Cut-Off Region

For an N-channel enhancement MOSFET:

\[
V_{GS}<V_{TH}
\]

The channel is not strongly formed and drain current is approximately zero in the idealized model.

### 9.2 Linear or Triode Region

When:

\[
V_{GS}>V_{TH}
\]

and:

\[
V_{DS}<V_{GS}-V_{TH}
\]

the MOSFET operates in the linear region.

The channel exists along its length and the device behaves approximately like a voltage-controlled resistance.

### 9.3 Saturation Region

When:

\[
V_{DS}\geq V_{GS}-V_{TH}
\]

the MOSFET enters saturation in the long-channel model.

Drain current becomes approximately independent of drain-to-source voltage, provided the device remains within the model's operating assumptions.

### 9.4 Important Distinction

MOSFET saturation is not the same as BJT saturation.

- BJT saturation is normally associated with switching operation.
- MOSFET saturation is commonly used for amplification.

A MOSFET used as a fully enhanced power switch normally operates in its linear or ohmic region when ON.

## 10. MOSFET Current Equations

For a simplified long-channel N-channel enhancement MOSFET, the idealized drain-current equations are as follows.

### 10.1 Cut-Off Region

\[
I_D\approx0
\]

when:

\[
V_{GS}<V_{TH}
\]

### 10.2 Linear Region

\[
\boxed{
I_D=k\left[
(V_{GS}-V_{TH})V_{DS}
-\frac{V_{DS}^2}{2}
\right]
}
\]

Where:

- \(I_D\) = drain current.
- \(k\) = process-dependent device parameter.
- \(V_{GS}\) = gate-to-source voltage.
- \(V_{DS}\) = drain-to-source voltage.
- \(V_{TH}\) = threshold voltage.

### 10.3 Saturation Region

\[
\boxed{
I_D=\frac{k}{2}(V_{GS}-V_{TH})^2
}
\]

This simplified equation neglects channel-length modulation and other non-ideal effects.

The value of \(k\) depends on device geometry, carrier mobility, and gate-oxide capacitance.

## 11. Comparison of JFET and MOSFET

| Property | JFET | MOSFET |
|---|---|---|
| Gate structure | Reverse-biased PN junction | Insulated gate |
| Gate current | Small reverse leakage | Very small DC leakage |
| Input resistance | High | Extremely high |
| Operating types | Normally depletion-type | Enhancement and depletion |
| Channel control | Depletion-region width | Electric field through gate dielectric |
| Gate protection | Less sensitive to static charge than many MOSFETs | Often sensitive to electrostatic discharge |
| Applications | Low-noise amplification, analogue circuits | Digital logic, power switching, amplification |

## 12. MOSFET as a Switch

MOSFETs are widely used as electronic switches.

### 12.1 OFF State

For an N-channel enhancement MOSFET:

\[
V_{GS}<V_{TH}
\]

The device is in cut-off in the simplified model.

The drain current is approximately zero, apart from leakage.

### 12.2 ON State

When the gate voltage is sufficiently high, the MOSFET forms a conducting channel.

For power-switching operation, the device is normally driven strongly enough to achieve a low on-state resistance.

This resistance is called:

\[
R_{DS(on)}
\]

The conduction loss can be approximated by:

\[
P_{cond}=I_D^2R_{DS(on)}
\]

Where:

- \(P_{cond}\) = conduction power loss.
- \(I_D\) = drain current.
- \(R_{DS(on)}\) = drain-to-source on-resistance.

The on-resistance depends on gate voltage, junction temperature, and device characteristics.

### 12.3 Gate Drive

The gate is insulated, but it has capacitance.

A gate driver must supply or remove charge to change the MOSFET's state.

Therefore, gate current is required during switching transitions even though steady-state DC gate current is very small.

## 13. Body Diode and MOSFET Protection

Many power MOSFETs contain an intrinsic body diode due to the semiconductor structure.

This diode provides a current path under certain reverse-current conditions.

It is important in:

- Motor drivers.
- Half-bridge circuits.
- Synchronous converters.
- Inductive switching applications.

MOSFET gates can be damaged by excessive voltage or electrostatic discharge.

Practical precautions include:

- Appropriate gate-source voltage limits.
- Gate resistors.
- Gate-source protection components.
- Proper handling and ESD precautions.

## 14. Worked Numerical Examples

### Example 1: JFET Drain Current

**Given:**

- \(I_{DSS}=12\,mA\).
- \(V_{GS}= -2\,V\).
- \(V_P=-6\,V\).

Calculate the drain current using the Shockley equation.

**Formula:**

\[
I_D=I_{DSS}
\left(1-\frac{V_{GS}}{V_P}\right)^2
\]

**Solution:**

Substitute:

\[
I_D=12
\left(1-\frac{-2}{-6}\right)^2
\]

\[
I_D=12
\left(1-\frac{1}{3}\right)^2
\]

\[
I_D=12\left(\frac{2}{3}\right)^2
\]

\[
I_D=12\times\frac{4}{9}
\]

\[
I_D=5.33\,mA
\]

**Final Answer:**

\[
\boxed{I_D\approx5.33\,mA}
\]

### Example 2: MOSFET Saturation Current

**Given:**

- \(k=0.5\,mA/V^2\).
- \(V_{GS}=5\,V\).
- \(V_{TH}=2\,V\).
- The MOSFET is operating in saturation.

Calculate the drain current.

**Formula:**

\[
I_D=\frac{k}{2}(V_{GS}-V_{TH})^2
\]

**Solution:**

\[
I_D=\frac{0.5}{2}(5-2)^2
\]

\[
I_D=0.25(3)^2
\]

\[
I_D=0.25\times9
\]

\[
I_D=2.25\,mA
\]

**Final Answer:**

\[
\boxed{I_D=2.25\,mA}
\]

### Example 3: MOSFET Conduction Loss

**Given:**

- Drain current: \(I_D=8\,A\).
- On-resistance: \(R_{DS(on)}=0.025\,\Omega\).

Calculate the conduction power loss.

**Formula:**

\[
P_{cond}=I_D^2R_{DS(on)}
\]

**Solution:**

\[
P_{cond}=8^2\times0.025
\]

\[
P_{cond}=64\times0.025
\]

\[
P_{cond}=1.6\,W
\]

**Final Answer:**

\[
\boxed{P_{cond}=1.6\,W}
\]

This calculation assumes a constant on-resistance. Actual resistance changes with temperature and gate drive.

## 15. Practical Applications of FETs

### 15.1 Digital Integrated Circuits

MOSFETs form the basic switching elements in modern digital integrated circuits.

### 15.2 Microprocessors

Millions or billions of MOSFETs can be integrated into a microprocessor.

### 15.3 Switching Power Supplies

Power MOSFETs switch rapidly to control energy transfer in DC-DC converters and other power-conversion circuits.

### 15.4 Motor Control

MOSFETs are used in motor drivers and electronic speed-control systems.

### 15.5 Low-Noise Amplifiers

JFETs and selected MOSFETs are useful in high-input-impedance and low-noise amplifier circuits.

### 15.6 Sensor Interfaces

FET input stages can measure signals from high-impedance sensors without heavily loading them.

## 16. BJT and FET Comparison

| Property | BJT | FET |
|---|---|---|
| Control type | Commonly current-controlled in basic analysis | Voltage-controlled |
| Main carriers | Electrons and holes | Majority carriers in the channel |
| Input resistance | Generally lower | Generally higher |
| Input current | Requires base current | Very small steady-state gate current |
| Gain parameters | Alpha and beta | Transconductance and other FET parameters |
| Main applications | Amplification and switching | Switching, amplification, digital logic |
| Thermal behaviour | Can suffer thermal runaway | Device-dependent; power MOSFETs can have useful thermal sharing properties |

The comparison is general. Actual device behaviour depends on construction, circuit configuration, and operating conditions.

## 17. Common Examination Traps

1. FETs are voltage-controlled devices.
2. A JFET uses a reverse-biased PN junction at its gate.
3. A MOSFET has an insulated gate.
4. N-channel and P-channel devices have opposite voltage and current polarities.
5. A JFET normally conducts at zero gate-to-source voltage.
6. An enhancement MOSFET is normally OFF at zero gate-to-source voltage.
7. A depletion MOSFET has a conducting channel at zero gate-to-source voltage.
8. JFET pinch-off does not mean that drain current immediately becomes zero.
9. MOSFET saturation and BJT saturation are different operating conditions.
10. A power MOSFET used as a fully ON switch normally operates in its low-resistance linear region.
11. MOSFET gates have capacitance and require charge during switching.
12. A MOSFET's very high input resistance does not mean that its gate is immune to electrostatic damage.
13. \(R_{DS(on)}\) determines an important part of MOSFET conduction loss.
14. The Shockley JFET equation and idealized MOSFET equations apply only under their stated assumptions.

## Quiz

1. What is the main mechanism used by a JFET to control its channel current?

- [ ] Forward current through the gate junction.
- [x] Changing the depletion-region width using a reverse-biased gate junction.
- [ ] Injecting base current into the channel.
- [ ] Changing the resistance of an external collector resistor.

> A JFET uses a reverse-biased gate-channel PN junction. Changing the gate-to-source voltage changes the depletion-region width and therefore the effective conducting channel.

2. Which statement correctly describes an N-channel enhancement MOSFET?

- [ ] It normally conducts strongly when its gate-to-source voltage is zero.
- [x] It requires a sufficiently positive gate-to-source voltage to form a conducting channel.
- [ ] It uses a forward-biased gate PN junction as its normal control mechanism.
- [ ] It requires continuous DC gate current to maintain conduction.

> An N-channel enhancement MOSFET is normally OFF at zero gate-to-source voltage. A sufficiently positive gate voltage creates an inversion channel. The insulated gate requires very little steady-state DC current.

3. A power MOSFET carries 10 A and has an on-resistance of 0.02 Ω. Calculate its approximate conduction loss.

- [ ] 0.2 W.
- [ ] 1 W.
- [x] 2 W.
- [ ] 20 W.

> Conduction loss is \(P=I_D^2R_{DS(on)}\). Therefore, \(P=10^2\times0.02=100\times0.02=2\,W\).
