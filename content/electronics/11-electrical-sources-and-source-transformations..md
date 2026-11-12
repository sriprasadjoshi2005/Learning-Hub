---
title: Electrical Sources and Source Transformations
level: intermediate
---

# Electrical Sources and Source Transformations

## Introduction

Electrical sources are active circuit elements that supply energy to electrical networks. They establish the voltage or current required for circuit operation and are fundamental to the analysis of electrical and electronic systems.

Practical sources are not perfectly ideal. Batteries, power supplies, and signal generators possess internal resistance and other non-ideal characteristics. Understanding these characteristics allows engineers to predict terminal voltage, current delivery, power losses, and circuit behaviour.

This lesson examines independent and dependent sources, ideal and practical voltage and current sources, internal resistance, source models, and source transformation techniques.

## 1. Introduction to Electrical Sources

An electrical source is an active circuit element capable of supplying electrical energy to a network.

The two fundamental independent source types are:

1. Voltage sources.
2. Current sources.

### 1.1 Voltage Source

A voltage source maintains a specified potential difference across its terminals.

Its voltage is represented by \(V_s\).

An ideal voltage source maintains constant terminal voltage regardless of the current drawn by the load.

Examples include:
- Batteries.
- DC power supplies.
- Function generators.
- Solar-cell models.

### 1.2 Current Source

A current source maintains a specified current through the connected circuit.

Its current is represented by \(I_s\).

An ideal current source maintains constant current regardless of the voltage developed across its terminals.

Examples include:
- Constant-current LED drivers.
- Current-regulated circuits.
- Transistor-based current sources.

## 2. Ideal and Practical Voltage Sources

### 2.1 Ideal Voltage Source

An ideal voltage source has zero internal resistance.

Its terminal voltage remains constant regardless of the load current.

\[
V_L=V_s
\]

Where:
- \(V_L\) = load voltage in volts.
- \(V_s\) = source voltage in volts.

An ideal voltage source can theoretically supply unlimited current under a short circuit. This is physically impossible in a real source.

### 2.2 Practical Voltage Source

A practical voltage source is modelled as an ideal voltage source connected in series with an internal resistance.

The internal resistance is represented by \(R_s\).

When a load is connected, current flows through both the internal resistance and the load.

Applying Kirchhoff's voltage law:

\[
V_s=IR_s+V_L
\]

Therefore:

\[
\boxed{V_L=V_s-IR_s}
\]

The terminal voltage decreases as the load current increases.

### 2.3 Open-Circuit Voltage

When no load is connected, the output current is zero.

\[
I=0
\]

Therefore, there is no voltage drop across the internal resistance.

\[
\boxed{V_{OC}=V_s}
\]

### 2.4 Short-Circuit Current

Under short-circuit conditions, the load resistance becomes approximately zero.

\[
V_L=0
\]

Therefore:

\[
V_s=I_{SC}R_s
\]

\[
\boxed{I_{SC}=\frac{V_s}{R_s}}
\]

The internal resistance limits the short-circuit current.

### 2.5 Voltage Regulation

Voltage regulation describes how well a practical source maintains its output voltage when the load changes.

One commonly used expression is:

\[
\%VR=\frac{V_{NL}-V_{FL}}{V_{FL}}\times100
\]

Where:
- \(V_{NL}\) = no-load voltage.
- \(V_{FL}\) = full-load voltage.

A smaller percentage indicates better voltage regulation.

## 3. Ideal and Practical Current Sources

### 3.1 Ideal Current Source

An ideal current source maintains constant current independently of the voltage across its terminals.

Its internal resistance is theoretically infinite.

### 3.2 Practical Current Source

A practical current source is represented by an ideal current source connected in parallel with an internal resistance.

Where:
- \(I_s\) = ideal source current.
- \(R_p\) = parallel internal resistance.

The source current divides between the load and internal resistance.

Applying Kirchhoff's current law:

\[
I_s=I_L+I_p
\]

Since:

\[
I_p=\frac{V_L}{R_p}
\]

We obtain:

\[
\boxed{I_L=I_s-\frac{V_L}{R_p}}
\]

### 3.3 Open-Circuit Voltage

Under open-circuit conditions, all source current flows through the internal resistance.

\[
\boxed{V_{OC}=I_sR_p}
\]

### 3.4 Short-Circuit Current

Under short-circuit conditions, terminal voltage becomes zero.

No current flows through the parallel internal resistance.

\[
\boxed{I_{SC}=I_s}
\]

## 4. Comparison of Voltage and Current Sources

| Property | Voltage source | Current source |
|---|---|---|
| Maintained quantity | Voltage | Current |
| Ideal internal resistance | Zero | Infinite |
| Practical model | Series resistance | Parallel resistance |
| Open-circuit behaviour | Voltage maintained | Voltage determined by internal resistance |
| Short-circuit behaviour | Current limited by internal resistance | Current equals source current |
| Common application | Power supplies | Current regulators |

## 5. Independent and Dependent Sources

Electrical sources are also classified according to whether their values depend on other circuit variables.

### 5.1 Independent Sources

An independent source provides a specified voltage or current that does not depend on any other circuit variable.

Its value may be constant or time-varying.

Examples:
- A 12 V battery.
- A 2 A constant-current source.
- A sinusoidal signal generator.

### 5.2 Dependent Sources

A dependent source has a voltage or current controlled by another voltage or current elsewhere in the circuit.

These sources are commonly used to model transistor circuits, operational amplifiers, and other active electronic devices.

There are four fundamental dependent-source types.

#### A. Voltage-Controlled Voltage Source (VCVS)

The output voltage depends on another voltage.

\[
V_o=\mu V_x
\]

Where:
- \(V_o\) = output voltage.
- \(V_x\) = controlling voltage.
- \(\mu\) = dimensionless voltage gain.

#### B. Current-Controlled Voltage Source (CCVS)

The output voltage depends on another current.

\[
V_o=r_m I_x
\]

Where \(r_m\) is transresistance measured in ohms.

#### C. Voltage-Controlled Current Source (VCCS)

The output current depends on another voltage.

\[
I_o=g_mV_x
\]

Where \(g_m\) is transconductance measured in siemens.

#### D. Current-Controlled Current Source (CCCS)

The output current depends on another current.

\[
I_o=\beta I_x
\]

Where \(\beta\) is a dimensionless current gain.

### 5.3 Dependent Source Summary

| Source type | Controlling quantity | Output quantity |
|---|---|---|
| VCVS | Voltage | Voltage |
| CCVS | Current | Voltage |
| VCCS | Voltage | Current |
| CCCS | Current | Current |

Dependent sources are generally represented using diamond-shaped symbols in circuit diagrams, whereas independent sources use circular symbols.

## 6. Source Transformation

Source transformation is a technique that converts a practical voltage-source representation into an equivalent practical current-source representation, or vice versa.

It simplifies circuit analysis without changing the electrical behaviour observed at the external terminals.

### 6.1 Voltage Source to Current Source

A practical voltage source consists of:
- An ideal voltage source \(V_s\).
- A series resistance \(R_s\).

It can be transformed into:
- An ideal current source \(I_s\).
- A parallel resistance \(R_p\).

The equivalent current is:

\[
\boxed{I_s=\frac{V_s}{R_s}}
\]

The resistance remains numerically equal:

\[
\boxed{R_p=R_s}
\]

The transformed circuit is called a Norton-form representation.

### 6.2 Current Source to Voltage Source

A practical current source consists of:
- An ideal current source \(I_s\).
- A parallel resistance \(R_p\).

It can be transformed into:
- An ideal voltage source \(V_s\).
- A series resistance \(R_s\).

The equivalent voltage is:

\[
\boxed{V_s=I_sR_p}
\]

The resistance remains numerically equal:

\[
\boxed{R_s=R_p}
\]

The transformed circuit is called a Thevenin-form representation.

### 6.3 Source Transformation Relationship

The fundamental relationship is:

\[
\boxed{V_s=I_sR}
\]

And:

\[
\boxed{I_s=\frac{V_s}{R}}
\]

The resistance \(R\) has the same numerical value in both representations.

### 6.4 Polarity and Current Direction

The polarity of the voltage source and direction of the current source must be consistent.

For a voltage source with its positive terminal at the top, the equivalent current source must drive current out of the corresponding positive terminal.

Incorrectly choosing the current direction changes the equivalent terminal behaviour.

## 7. Conditions for Valid Source Transformation

Source transformation is valid under the following conditions:

1. The voltage source must have a resistance in series with it.
2. The current source must have a resistance in parallel with it.
3. The resistance value must remain unchanged during transformation.
4. The voltage and current must satisfy \(V_s=I_sR\).
5. The external terminal behaviour must remain equivalent.
6. Dependent sources must retain their controlling relationships.

An ideal voltage source with zero internal resistance cannot be transformed into a finite current source using the ordinary formula.

Similarly, an ideal current source with infinite parallel resistance cannot be transformed into a finite voltage source using ordinary finite-value calculations.

## 8. Mathematical Derivation of Source Transformation

Consider a practical voltage source \(V_s\) with series resistance \(R_s\), connected to a load resistance \(R_L\).

Using Ohm's law:

\[
I_L=\frac{V_s}{R_s+R_L}
\]

Now consider its equivalent current-source model.

The source current is:

\[
I_s=\frac{V_s}{R_s}
\]

The current divides between \(R_s\) and \(R_L\).

Using the current-divider relationship:

\[
I_L=I_s\frac{R_s}{R_s+R_L}
\]

Substituting:

\[
I_L=\frac{V_s}{R_s}\times\frac{R_s}{R_s+R_L}
\]

Cancelling \(R_s\):

\[
\boxed{I_L=\frac{V_s}{R_s+R_L}}
\]

Both representations produce the same load current.

The terminal voltage is also identical because:

\[
V_L=I_LR_L
\]

Therefore, the two source models are externally equivalent for any finite load resistance.

## 9. Worked Numerical Examples

### Example 1: Transforming a Voltage Source into a Current Source

**Given:**

- Voltage source = 24 V
- Series resistance = 6 Ω

**Find:** Equivalent current source.

**Formula:**

\[
I_s=\frac{V_s}{R_s}
\]

**Solution:**

\[
I_s=\frac{24}{6}
\]

\[
I_s=4\text{ A}
\]

The parallel resistance remains:

\[
R_p=6\ \Omega
\]

**Final Answer:**

- Equivalent current source = 4 A.
- Parallel resistance = 6 Ω.

### Example 2: Transforming a Current Source into a Voltage Source

**Given:**

- Current source = 3 A
- Parallel resistance = 8 Ω

**Find:** Equivalent voltage source.

**Formula:**

\[
V_s=I_sR_p
\]

**Solution:**

\[
V_s=3\times8
\]

\[
V_s=24\text{ V}
\]

The series resistance remains:

\[
R_s=8\ \Omega
\]

**Final Answer:**

- Equivalent voltage source = 24 V.
- Series resistance = 8 Ω.

### Example 3: Determining Load Current Using Both Source Models

**Given:**

- Voltage source = 20 V
- Series resistance = 5 Ω
- Load resistance = 15 Ω

**Method 1: Voltage-source model**

\[
I_L=\frac{V_s}{R_s+R_L}
\]

\[
I_L=\frac{20}{5+15}
\]

\[
\boxed{I_L=1\text{ A}}
\]

**Method 2: Current-source model**

Transform the source:

\[
I_s=\frac{20}{5}=4\text{ A}
\]

The 5 Ω resistance is now parallel with the 15 Ω load.

Using the current-divider rule:

\[
I_L=4\times\frac{5}{5+15}
\]

\[
\boxed{I_L=1\text{ A}}
\]

Both methods give the same answer.

### Example 4: Finding Terminal Voltage of a Practical Voltage Source

**Given:**

- Source voltage = 12 V
- Internal resistance = 0.5 Ω
- Load current = 2 A

**Find:** Terminal voltage.

**Formula:**

\[
V_L=V_s-IR_s
\]

**Solution:**

\[
V_L=12-(2\times0.5)
\]

\[
V_L=12-1
\]

\[
\boxed{V_L=11\text{ V}}
\]

The source loses 1 V internally because of its internal resistance.

## 10. Practical Applications

Source models and transformations are useful in:

- Battery modelling and power-delivery analysis.
- Simplification of complicated resistor networks.
- Analysis of transistor equivalent circuits.
- Design of current-regulated power supplies.
- Modelling of sensors and signal generators.
- Electrical network simulation.
- Analysing circuits containing multiple independent sources.

In electronic circuit design, a source is often represented using whichever equivalent model makes the required calculation easier.

## 11. Important Comparisons and Observations

| Concept | Important observation |
|---|---|
| Ideal voltage source | Zero internal resistance |
| Practical voltage source | Non-zero series internal resistance |
| Ideal current source | Infinite internal resistance |
| Practical current source | Large parallel internal resistance |
| Source transformation | Changes representation, not external behaviour |
| Voltage-to-current conversion | Divide voltage by series resistance |
| Current-to-voltage conversion | Multiply current by parallel resistance |
| Dependent source | Controlled by another circuit variable |

## 12. Common Exam Traps

1. **Changing the resistance during transformation:** The numerical resistance value remains the same. Only its connection changes from series to parallel or vice versa.

2. **Using multiplication instead of division:** Voltage-to-current conversion requires \(I_s=V_s/R_s\).

3. **Ignoring source polarity:** The transformed current-source direction must preserve the original terminal polarity.

4. **Confusing ideal and practical sources:** An ideal voltage source has zero internal resistance, whereas an ideal current source has infinite internal resistance.

5. **Assuming source transformation changes load behaviour:** Correctly transformed sources produce the same terminal voltage and load current.

6. **Treating a dependent source as independent:** Its controlling relationship must be preserved.

7. **Ignoring internal resistance:** Practical sources experience internal voltage drops and power losses.

## Quiz

1. A practical voltage source of 30 V has a series internal resistance of 10 Ω. What is its equivalent current-source representation?

   - [ ] 10 A in parallel with 30 Ω
   - [x] 3 A in parallel with 10 Ω
   - [ ] 3 A in series with 10 Ω
   - [ ] 300 A in parallel with 10 Ω

   > The equivalent current is \(I_s=V_s/R_s=30/10=3\) A. The resistance remains 10 Ω and becomes parallel to the current source.

2. Which statement correctly describes an ideal current source?

   - [ ] It maintains constant voltage regardless of load.
   - [ ] It has zero internal resistance.
   - [x] It maintains constant current regardless of terminal voltage.
   - [ ] Its output current becomes zero when the load resistance increases.

   > An ideal current source maintains its specified current independently of terminal voltage. Its ideal internal resistance is infinite.

3. A practical voltage source has an open-circuit voltage of 18 V and an internal resistance of 3 Ω. It is connected to a 6 Ω load. What is the load voltage?

   - [ ] 6 V
   - [x] 12 V
   - [ ] 15 V
   - [ ] 18 V

   > The circuit current is \(I=18/(3+6)=2\) A. Therefore, the load voltage is \(V_L=IR_L=2\times6=12\) V. The remaining 6 V is dropped across the internal resistance.