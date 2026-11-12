---
title: Transistor Configurations and Characteristics
level: intermediate
---

# Transistor Configurations and Characteristics

A bipolar junction transistor can be connected in different circuit configurations depending on the input signal, output signal, and terminal shared by both circuits.

The three fundamental BJT configurations are:

1. Common-base (CB).
2. Common-emitter (CE).
3. Common-collector (CC).

Each configuration has different current gain, voltage gain, input resistance, output resistance, and phase relationships.

Understanding these configurations is essential for selecting suitable transistor circuits for amplification, impedance matching, and signal processing.

## 1. Introduction to Transistor Configurations

A BJT has three terminals:

- Emitter.
- Base.
- Collector.

A transistor configuration is determined by the terminal that is common to both the input and output circuits.

The remaining two terminals act as the input and output terminals.

For example:

- Common-base: base is common.
- Common-emitter: emitter is common.
- Common-collector: collector is common.

The word common refers to the electrical reference connection shared by the input and output circuits. It does not necessarily mean that the terminal is connected directly to ground.

## 2. Common-Base Configuration

In the common-base configuration, the base terminal is common to both the input and output circuits.

### 2.1 Circuit Arrangement

For an NPN transistor:

- Input is applied between emitter and base.
- Output is measured between collector and base.
- Base is the common terminal.

### 2.2 Current Gain

The current gain is:

\[
\alpha=\frac{I_C}{I_E}
\]

Since:

\[
I_E=I_C+I_B
\]

the collector current is slightly smaller than emitter current.

Therefore, common-base current gain is generally less than one.

### 2.3 Voltage Gain

The common-base configuration can provide substantial voltage gain.

Its voltage gain depends on the load, transistor parameters, and operating conditions.

### 2.4 Input and Output Resistance

Typical characteristics:

- Low input resistance.
- High output resistance.

### 2.5 Phase Relationship

The common-base configuration does not produce the usual 180° voltage phase inversion between input and output.

### 2.6 Applications

- High-frequency amplification.
- Impedance matching between low-resistance and high-resistance circuits.
- Radio-frequency circuits.
- Specialised amplifier stages.

## 3. Common-Emitter Configuration

The common-emitter configuration is one of the most widely used transistor configurations.

The emitter terminal is common to the input and output circuits.

### 3.1 Circuit Arrangement

For an NPN transistor:

- Input is applied between base and emitter.
- Output is taken between collector and emitter.
- Emitter is the common terminal.

### 3.2 Current Gain

The current gain is:

\[
\boxed{\beta=\frac{I_C}{I_B}}
\]

The collector current can be approximated as:

\[
I_C=\beta I_B
\]

in the forward-active region.

The current gain is generally greater than one.

### 3.3 Voltage Gain

The common-emitter configuration can provide substantial voltage gain.

A small input-voltage variation can produce a larger output-voltage variation.

### 3.4 Power Gain

Because the configuration can provide both current gain and voltage gain, it can provide substantial power gain.

### 3.5 Input and Output Resistance

Typical characteristics:

- Moderate input resistance.
- Moderate to high output resistance.

Actual values depend on the circuit and operating conditions.

### 3.6 Phase Relationship

The common-emitter amplifier produces an output voltage approximately 180° out of phase with the input signal when operating as a conventional voltage amplifier.

This is called phase inversion.

When input voltage increases slightly:

- Base current increases.
- Collector current increases.
- Voltage drop across the collector resistor increases.
- Collector output voltage decreases.

### 3.7 Applications

- Audio amplification.
- Voltage amplification.
- General-purpose signal amplification.
- Switching circuits.
- Oscillator stages.

## 4. Common-Collector Configuration

The common-collector configuration is also called an emitter follower.

The collector terminal is common to the input and output circuits.

### 4.1 Circuit Arrangement

For an NPN transistor:

- Input is applied between base and collector.
- Output is taken between emitter and collector.
- Collector is the common terminal.

### 4.2 Current Gain

The current gain is:

\[
\frac{I_E}{I_B}
\]

Since:

\[
I_E=I_C+I_B
\]

and:

\[
I_C=\beta I_B
\]

we obtain:

\[
I_E=(\beta+1)I_B
\]

Therefore:

\[
\boxed{A_i=\beta+1}
\]

The current gain is high.

### 4.3 Voltage Gain

The voltage gain is approximately one:

\[
A_v\approx1
\]

The output voltage follows the input voltage, with a small difference caused by the base-emitter junction.

For an NPN silicon transistor:

\[
V_E\approx V_B-0.7\,V
\]

This is an approximate relationship under normal conduction conditions.

### 4.4 Input and Output Resistance

Typical characteristics:

- High input resistance.
- Low output resistance.

These characteristics make the emitter follower useful for impedance matching.

### 4.5 Phase Relationship

The output voltage is approximately in phase with the input voltage.

### 4.6 Applications

- Buffer amplifiers.
- Impedance matching.
- Driving low-resistance loads.
- Interstage coupling.
- Signal isolation.

## 5. Comparison of the Three Configurations

| Property | Common-base | Common-emitter | Common-collector |
|---|---|---|---|
| Common terminal | Base | Emitter | Collector |
| Input terminal | Emitter | Base | Base |
| Output terminal | Collector | Collector | Emitter |
| Current gain | Less than 1 | High | High |
| Voltage gain | High | High | Approximately 1 |
| Power gain | Moderate to high | High | Moderate to high |
| Input resistance | Low | Moderate | High |
| Output resistance | High | Moderate to high | Low |
| Phase relationship | No inversion | 180° inversion | No inversion |
| Main application | High-frequency circuits | Voltage amplification | Buffering |

These are typical qualitative characteristics. Actual circuit values depend on biasing, load resistance, transistor parameters, and frequency.

## 6. Transistor Characteristic Curves

Transistor characteristics describe the relationships between terminal currents and voltages.

The most commonly studied characteristics are:

1. Input characteristics.
2. Output characteristics.
3. Transfer characteristics.

### 6.1 Input Characteristics

Input characteristics show how input current changes with input voltage while another voltage is held constant.

For a common-emitter transistor:

\[
I_B=f(V_{BE})
\]

with \(V_{CE}\) held constant.

The curve resembles the forward characteristic of a PN junction because the base-emitter junction is forward-biased.

### 6.2 Output Characteristics

Output characteristics show the relationship between collector current and collector-emitter voltage for different fixed base currents.

\[
I_C=f(V_{CE})
\]

with \(I_B\) held constant.

The output characteristic helps identify:

- Cut-off region.
- Active region.
- Saturation region.

### 6.3 Transfer Characteristics

Transfer characteristics describe the relationship between output current and input current or voltage.

For a common-emitter transistor:

\[
I_C=f(I_B)
\]

The approximate slope in the active region represents current gain:

\[
\beta=\frac{\Delta I_C}{\Delta I_B}
\]

This is the incremental current gain.

## 7. Input and Output Resistance

### 7.1 Input Resistance

Input resistance describes how much the input circuit opposes current flow.

It is approximated by:

\[
R_{in}=\frac{\Delta V_{in}}{\Delta I_{in}}
\]

For a common-emitter transistor:

\[
R_{in}\approx\frac{\Delta V_{BE}}{\Delta I_B}
\]

under the specified output-voltage condition.

### 7.2 Output Resistance

Output resistance describes how much the output voltage changes when output current changes.

A simplified incremental expression is:

\[
R_{out}=\frac{\Delta V_{out}}{\Delta I_{out}}
\]

For transistor characteristic curves, output resistance is associated with the slope of the output characteristics.

A flatter output characteristic generally corresponds to higher output resistance.

## 8. Transistor Gain

### 8.1 Current Gain

\[
A_i=\frac{\Delta I_{out}}{\Delta I_{in}}
\]

### 8.2 Voltage Gain

\[
A_v=\frac{\Delta V_{out}}{\Delta V_{in}}
\]

### 8.3 Power Gain

\[
A_p=\frac{P_{out}}{P_{in}}
\]

For an amplifier, power gain can be expressed approximately as:

\[
A_p=A_vA_i
\]

when voltage and current gain are defined consistently using the same input and output conventions.

Gain may also be expressed in decibels.

Voltage gain:

\[
A_{v(dB)}=20\log_{10}|A_v|
\]

Power gain:

\[
A_{p(dB)}=10\log_{10}A_p
\]

## 9. Worked Numerical Examples

### Example 1: Common-Base Current Gain

**Given:**

- Emitter current: \(I_E=6\,mA\).
- Collector current: \(I_C=5.88\,mA\).

Calculate alpha and base current.

**Formula:**

\[
\alpha=\frac{I_C}{I_E}
\]

\[
I_B=I_E-I_C
\]

**Solution:**

\[
\alpha=\frac{5.88}{6}
\]

\[
\alpha=0.98
\]

Base current:

\[
I_B=6-5.88
\]

\[
I_B=0.12\,mA
\]

**Final Answer:**

\[
\boxed{\alpha=0.98}
\]

\[
\boxed{I_B=120\,\mu A}
\]

### Example 2: Common-Collector Current Gain

**Given:**

- Common-emitter current gain: \(\beta=99\).
- Base current: \(I_B=20\,\mu A\).

Calculate emitter current.

**Formula:**

\[
I_E=(\beta+1)I_B
\]

**Solution:**

\[
I_E=(99+1)(20\,\mu A)
\]

\[
I_E=100\times20\,\mu A
\]

\[
I_E=2000\,\mu A
\]

\[
I_E=2\,mA
\]

**Final Answer:**

\[
\boxed{I_E=2\,mA}
\]

### Example 3: Voltage Gain in Decibels

**Given:**

- Voltage gain magnitude: \(A_v=20\).

Calculate voltage gain in decibels.

**Formula:**

\[
A_{v(dB)}=20\log_{10}|A_v|
\]

**Solution:**

\[
A_{v(dB)}=20\log_{10}(20)
\]

\[
A_{v(dB)}=20(1.3010)
\]

\[
A_{v(dB)}\approx26.02\,dB
\]

**Final Answer:**

\[
\boxed{A_{v(dB)}\approx26.02\,dB}
\]

## 10. Selecting a Transistor Configuration

The appropriate configuration depends on the circuit requirement.

Choose common-base when:

- Low input resistance is useful.
- High-frequency operation is important.
- Current gain below one is acceptable.

Choose common-emitter when:

- Substantial voltage and current gain are needed.
- General-purpose amplification is required.
- Phase inversion is acceptable.

Choose common-collector when:

- High input resistance is needed.
- Low output resistance is useful.
- Voltage buffering is required.
- Impedance matching is important.

## 11. Common Examination Traps

1. The common terminal is shared by both input and output circuits.
2. Common-base current gain is alpha.
3. Common-emitter current gain is beta.
4. Common-collector current gain is approximately beta plus one.
5. Common-emitter produces approximately 180° phase inversion.
6. Common-collector voltage gain is approximately one, not zero.
7. Common-base has low input resistance.
8. Common-collector has high input resistance and low output resistance.
9. The input characteristic describes input current against input voltage.
10. The output characteristic describes output current against output voltage.
11. Incremental gain is based on changes in current or voltage, not necessarily the ratio of total values.
12. A transistor configuration's actual gain depends on its external circuit.

## Quiz

1. Which BJT configuration is commonly called an emitter follower?

- [ ] Common-base.
- [ ] Common-emitter.
- [x] Common-collector.
- [ ] Reverse-active.

> In the common-collector configuration, the output is taken from the emitter. Its voltage approximately follows the base input voltage, which gives it the name emitter follower.

2. Which configuration normally produces approximately 180° phase inversion between input and output voltage?

- [ ] Common-base.
- [x] Common-emitter.
- [ ] Common-collector.
- [ ] All three configurations.

> In a common-emitter amplifier, increasing base current increases collector current. The larger voltage drop across the collector resistor reduces collector output voltage, producing phase inversion.

3. A transistor has a common-emitter current gain of 49. What is its approximate common-collector current gain?

- [ ] 49.
- [ ] 48.
- [x] 50.
- [ ] 98.

> Common-collector current gain is approximately \(\beta+1\). Therefore, \(49+1=50\).
