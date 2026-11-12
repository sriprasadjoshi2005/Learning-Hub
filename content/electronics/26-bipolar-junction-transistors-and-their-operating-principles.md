---
title: Bipolar Junction Transistors and Their Operating Principles
level: intermediate
---

# Bipolar Junction Transistors and Their Operating Principles

A bipolar junction transistor (BJT) is a three-terminal semiconductor device used for signal amplification and electronic switching.

It controls a relatively large collector current using a much smaller base current in its common-emitter operating mode.

BJTs are widely used in amplifiers, switching circuits, oscillators, signal-processing systems, power-control circuits, and electronic instrumentation.

This lesson introduces transistor structure, NPN and PNP types, transistor terminals, operating principles, current relationships, operating regions, and basic transistor calculations.

## 1. Introduction to Bipolar Junction Transistors

A bipolar junction transistor consists of three semiconductor regions arranged to form two PN junctions.

The three terminals are:

1. Emitter.
2. Base.
3. Collector.

The word bipolar indicates that both electrons and holes participate in the device's operation.

There are two main types:

- NPN transistor.
- PNP transistor.

### 1.1 NPN Transistor

An NPN transistor consists of:

- N-type emitter.
- P-type base.
- N-type collector.

Its simplified structure is:

    Emitter       Base       Collector
      N             P            N
    ┌─────┐       ┌───┐       ┌─────┐
    │  N  │───────│ P │───────│  N  │
    └─────┘       └───┘       └─────┘

The emitter arrow in the circuit symbol points outward.

### 1.2 PNP Transistor

A PNP transistor consists of:

- P-type emitter.
- N-type base.
- P-type collector.

Its simplified structure is:

    Emitter       Base       Collector
      P             N            P
    ┌─────┐       ┌───┐       ┌─────┐
    │  P  │───────│ N │───────│  P  │
    └─────┘       └───┘       └─────┘

The emitter arrow in the circuit symbol points inward.

### 1.3 Main Difference

| Property | NPN | PNP |
|---|---|---|
| Region arrangement | N-P-N | P-N-P |
| Main carrier movement | Electrons | Holes |
| Conventional emitter current direction | Out of emitter | Into emitter |
| Symbol arrow | Points outward | Points inward |
| Typical base bias for active operation | Positive relative to emitter | Negative relative to emitter |

## 2. Transistor Construction

The three transistor regions have different physical characteristics.

### 2.1 Emitter

The emitter is heavily doped.

Its purpose is to inject a large number of majority carriers into the base.

### 2.2 Base

The base is:

- Very thin.
- Lightly doped.
- Located between the emitter and collector.

Its thin structure allows most carriers injected from the emitter to cross the base without recombining.

### 2.3 Collector

The collector is generally:

- Moderately doped.
- Physically larger than the emitter in many discrete devices.
- Designed to collect carriers and dissipate heat.

The collector-base junction must withstand the reverse voltage encountered during normal operation.

## 3. The Two PN Junctions

A BJT contains two PN junctions:

1. Emitter-base junction.
2. Collector-base junction.

Their bias conditions determine the operating region.

For normal forward-active operation of an NPN transistor:

- The emitter-base junction is forward-biased.
- The collector-base junction is reverse-biased.

This combination allows carriers injected from the emitter to pass through the thin base and be collected by the collector.

## 4. Operating Principle of an NPN Transistor

Consider an NPN transistor operating in the forward-active region.

### 4.1 Carrier Injection

The emitter-base junction is forward-biased.

Electrons are injected from the heavily doped N-type emitter into the P-type base.

Because the base is thin and lightly doped, only a small proportion of these electrons recombine with holes in the base.

### 4.2 Base Current

The recombination process requires a small current through the base terminal.

This is one reason why base current is much smaller than collector current in normal active operation.

### 4.3 Collector Current

The collector-base junction is reverse-biased.

Its electric field attracts and collects most of the electrons that have crossed the base.

This produces collector current.

The result is a relatively large collector current controlled by a smaller base current.

## 5. Transistor Current Relationships

The three terminal currents are:

- \(I_E\) = emitter current.
- \(I_B\) = base current.
- \(I_C\) = collector current.

By Kirchhoff's current law:

\[
\boxed{I_E=I_C+I_B}
\]

This relationship applies to the transistor terminal currents using their conventional directions.

### 5.1 Common-Base Current Gain

The common-base current gain is represented by alpha:

\[
\alpha=\frac{I_C}{I_E}
\]

For a transistor operating in the active region, alpha is generally slightly less than 1.

Typical values may be around 0.95 to 0.998, depending on the transistor.

### 5.2 Common-Emitter Current Gain

The common-emitter current gain is represented by beta:

\[
\boxed{\beta=\frac{I_C}{I_B}}
\]

A transistor's beta may range widely depending on its design, operating current, temperature, and collector-emitter voltage.

It is not a perfectly constant value.

### 5.3 Relationship Between Alpha and Beta

Starting with:

\[
\alpha=\frac{I_C}{I_E}
\]

Using:

\[
I_E=I_C+I_B
\]

Therefore:

\[
\alpha=\frac{I_C}{I_C+I_B}
\]

Divide numerator and denominator by \(I_B\):

\[
\alpha=\frac{\beta}{\beta+1}
\]

Hence:

\[
\boxed{\beta=\frac{\alpha}{1-\alpha}}
\]

These relationships are important in transistor calculations.

## 6. Transistor Operating Regions

A BJT can operate in different regions depending on the biasing of its two junctions.

### 6.1 Cut-Off Region

In cut-off:

- The emitter-base junction is not sufficiently forward-biased.
- The collector-base junction is reverse-biased in the usual switching condition.
- Collector current is approximately zero, apart from leakage.

The transistor behaves approximately like an open switch.

### 6.2 Forward-Active Region

In forward-active operation:

- Emitter-base junction is forward-biased.
- Collector-base junction is reverse-biased.

The collector current is controlled by the base current.

This region is commonly used for amplification.

### 6.3 Saturation Region

In saturation:

- Both transistor junctions are forward-biased.
- The transistor is strongly conducting.
- Collector current is mainly limited by the external circuit.

The transistor behaves approximately like a closed switch.

The collector-emitter saturation voltage is usually small but not exactly zero.

### 6.4 Reverse-Active Region

In reverse-active operation:

- Emitter-base junction is reverse-biased.
- Collector-base junction is forward-biased.

The transistor operates with the emitter and collector functions effectively interchanged.

This region is rarely used in ordinary circuits because its current gain is generally much lower.

### 6.5 Comparison of Operating Regions

| Region | Emitter-base junction | Collector-base junction | Main application |
|---|---|---|---|
| Cut-off | Not forward-biased | Reverse-biased in normal switching | OFF state |
| Forward-active | Forward-biased | Reverse-biased | Amplification |
| Saturation | Forward-biased | Forward-biased | ON state |
| Reverse-active | Reverse-biased | Forward-biased | Special operation |

## 7. Transistor as an Amplifier

A transistor can amplify a small input signal when appropriately biased in its forward-active region.

A small variation in base current produces a larger variation in collector current.

For a common-emitter transistor:

\[
\Delta I_C\approx\beta\Delta I_B
\]

Where:

- \(\Delta I_C\) = change in collector current.
- \(\Delta I_B\) = change in base current.
- \(\beta\) = common-emitter current gain.

A collector resistor converts the collector-current variation into an output-voltage variation.

The output voltage is:

\[
V_C=V_{CC}-I_CR_C
\]

Where:

- \(V_C\) = collector voltage.
- \(V_{CC}\) = supply voltage.
- \(R_C\) = collector resistor.

As collector current increases, the voltage drop across the collector resistor increases, causing collector voltage to decrease.

This produces an inverted output signal in a common-emitter amplifier.

Detailed amplifier operation is studied in a later lesson.

## 8. Transistor as an Electronic Switch

A BJT can operate as an electronic switch by moving between cut-off and saturation.

### 8.1 OFF State

When the base-emitter voltage is insufficient to establish significant conduction:

\[
I_B\approx0
\]

The collector current is approximately zero, apart from leakage.

The transistor behaves like an open switch.

### 8.2 ON State

When sufficient base current is supplied, the transistor can enter saturation.

The collector-emitter voltage becomes relatively small:

\[
V_{CE}\approx V_{CE(sat)}
\]

The transistor behaves approximately like a closed switch.

### 8.3 Applications

- LED control.
- Relay driving.
- Motor switching.
- Digital logic.
- Microcontroller output interfaces.
- Electronic power control.

A base resistor is normally required to limit base current.

## 9. Base-Emitter Voltage

For a silicon BJT operating under ordinary forward-active conditions, the base-emitter voltage is often approximately:

\[
V_{BE}\approx0.7\,V
\]

This is a useful approximation rather than an exact fixed value.

The actual voltage depends on:

- Collector current.
- Temperature.
- Transistor construction.
- Operating conditions.

For a PNP transistor, the polarity is reversed relative to an NPN transistor.

## 10. Worked Numerical Examples

### Example 1: Calculating Collector and Emitter Currents

**Given:**

- Base current: \(I_B=40\,\mu A\).
- Current gain: \(\beta=100\).

Calculate the collector current and emitter current.

**Formula:**

\[
I_C=\beta I_B
\]

\[
I_E=I_C+I_B
\]

**Solution:**

Collector current:

\[
I_C=100\times40\,\mu A
\]

\[
I_C=4000\,\mu A
\]

\[
I_C=4\,mA
\]

Emitter current:

\[
I_E=4\,mA+0.04\,mA
\]

\[
I_E=4.04\,mA
\]

**Final Answer:**

\[
\boxed{I_C=4\,mA}
\]

\[
\boxed{I_E=4.04\,mA}
\]

### Example 2: Finding Current Gain

**Given:**

- Emitter current: \(I_E=5\,mA\).
- Collector current: \(I_C=4.9\,mA\).

Calculate alpha and beta.

**Formula:**

\[
\alpha=\frac{I_C}{I_E}
\]

\[
\beta=\frac{\alpha}{1-\alpha}
\]

**Solution:**

\[
\alpha=\frac{4.9}{5}
\]

\[
\alpha=0.98
\]

Now:

\[
\beta=\frac{0.98}{1-0.98}
\]

\[
\beta=\frac{0.98}{0.02}
\]

\[
\beta=49
\]

**Final Answer:**

\[
\boxed{\alpha=0.98}
\]

\[
\boxed{\beta=49}
\]

### Example 3: Base Resistor for a Switching Circuit

**Given:**

- Supply voltage: \(V_{CC}=12\,V\).
- Relay coil resistance: \(R_C=120\,\Omega\).
- Transistor saturation voltage: \(V_{CE(sat)}=0.2\,V\).
- Base supply: \(V_{IN}=5\,V\).
- Base-emitter voltage: \(V_{BE}=0.7\,V\).
- Selected forced current gain: 10.

Calculate the relay current and approximate base resistor.

**Formula:**

\[
I_C=\frac{V_{CC}-V_{CE(sat)}}{R_C}
\]

For a conservative switching design:

\[
I_B=\frac{I_C}{10}
\]

\[
R_B=\frac{V_{IN}-V_{BE}}{I_B}
\]

**Solution:**

Collector current:

\[
I_C=\frac{12-0.2}{120}
\]

\[
I_C=\frac{11.8}{120}
\]

\[
I_C\approx98.3\,mA
\]

Required base current:

\[
I_B=\frac{98.3}{10}
\]

\[
I_B=9.83\,mA
\]

Base resistor:

\[
R_B=\frac{5-0.7}{9.83\times10^{-3}}
\]

\[
R_B\approx437\,\Omega
\]

A standard resistor value of \(430\,\Omega\) or \(390\,\Omega\) may be considered after checking the transistor's ratings and the actual drive-source capability.

**Final Answer:**

\[
\boxed{I_C\approx98.3\,mA}
\]

\[
\boxed{R_B\approx437\,\Omega}
\]

## 11. BJT Power Dissipation and Safe Operation

A transistor dissipates electrical power while operating.

A simplified estimate of collector-emitter power is:

\[
P_D\approx V_{CE}I_C
\]

Where:

- \(P_D\) = transistor power dissipation.
- \(V_{CE}\) = collector-emitter voltage.
- \(I_C\) = collector current.

The actual device power calculation may also need to include base-terminal power.

The transistor must remain within its safe operating area (SOA).

Important limits include:

- Maximum collector current.
- Maximum collector-emitter voltage.
- Maximum power dissipation.
- Maximum junction temperature.
- Secondary breakdown limitations.

Power transistors may require heat sinks to keep junction temperature within safe limits.

## 12. Practical Applications of BJTs

### 12.1 Audio Amplifiers

BJTs can amplify low-level audio signals.

### 12.2 Switching Circuits

They can control relays, LEDs, motors, and other loads.

### 12.3 Oscillators

Transistors are used in circuits that generate periodic electrical signals.

### 12.4 Signal Processing

BJT circuits are used in signal amplification, conditioning, and other analog functions.

### 12.5 Differential Amplifiers

Matched transistor pairs are used in differential amplifier circuits, including the input stages of many operational amplifiers.

## 13. Common Examination Traps

1. A BJT has three terminals: emitter, base, and collector.
2. The emitter is generally heavily doped.
3. The base is thin and lightly doped.
4. The collector is designed to collect carriers and dissipate heat.
5. In forward-active operation, the emitter-base junction is forward-biased and collector-base junction is reverse-biased.
6. In saturation, both junctions are forward-biased.
7. In cut-off, collector current is approximately zero.
8. The emitter current is the sum of collector and base currents.
9. Alpha is slightly less than one, while beta is usually greater than one.
10. A transistor's beta is not perfectly constant.
11. A PNP transistor has the opposite symbol-arrow direction to an NPN transistor.
12. A base resistor is normally necessary when driving a BJT from a voltage source.

## Quiz

1. Which transistor region is normally used for linear signal amplification?

- [ ] Cut-off.
- [x] Forward-active.
- [ ] Saturation.
- [ ] Reverse breakdown.

> In forward-active operation, the emitter-base junction is forward-biased and the collector-base junction is reverse-biased. Collector current is controlled by base current, allowing signal amplification.

2. A BJT has a base current of 50 μA and a common-emitter current gain of 80. Calculate its collector current.

- [ ] 0.625 mA.
- [ ] 50 mA.
- [x] 4 mA.
- [ ] 6.4 mA.

> The collector current is \(I_C=\beta I_B=80\times50\,\mu A=4000\,\mu A=4\,mA\).

3. Which statement correctly describes an NPN transistor operating in saturation?

- [ ] Both junctions are reverse-biased.
- [ ] Only the collector-base junction is forward-biased.
- [x] Both the emitter-base and collector-base junctions are forward-biased.
- [ ] The transistor has no collector current.

> In saturation, both PN junctions are forward-biased. The transistor is strongly conducting and behaves approximately like a closed switch.
