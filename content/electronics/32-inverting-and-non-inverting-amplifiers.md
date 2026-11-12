---
title: Inverting and Non-Inverting Amplifiers
level: intermediate
---

# Inverting and Non-Inverting Amplifiers

Operational amplifiers can be configured with external resistors to produce predictable voltage gains.

Two fundamental configurations are:

1. Inverting amplifier.
2. Non-inverting amplifier.

Both commonly use negative feedback to control gain and maintain linear operation.

The main difference is the input terminal receiving the signal and the phase relationship between input and output.

## 1. Introduction

An operational amplifier has extremely high open-loop gain.

Connecting suitable feedback components allows the circuit to operate with a controlled closed-loop gain.

The closed-loop gain is determined primarily by the external feedback network rather than the op-amp's very large open-loop gain.

The two configurations studied here are among the most important analog amplifier circuits.

## 2. Inverting Amplifier

In an inverting amplifier:

- The input signal is applied through an input resistor \(R_1\) to the inverting terminal.
- The non-inverting terminal is connected to ground.
- A feedback resistor \(R_f\) connects the output to the inverting terminal.

The inverting input operates at approximately zero volts because of the virtual ground concept.

### 2.1 Circuit Arrangement

                 R1                 Rf
Vin ──────────/\/\/\────●────────/\/\/\────┐
                        |                  |
                        |                  |
                       (−)                 |
                     ┌───────┐             |
Ground ──────────────(+)     |             |
                     | Op-Amp|─────────────┘
                     └───────┘
                         |
                        Vout

### 2.2 Derivation of Voltage Gain

For an ideal op-amp:

\[
V_-=V_+=0
\]

The current through the input resistor is:

\[
I_1=\frac{V_{in}}{R_1}
\]

Since no current enters the op-amp input:

\[
I_1=I_f
\]

The feedback current is:

\[
I_f=\frac{0-V_o}{R_f}
\]

Therefore:

\[
\frac{V_{in}}{R_1}=-\frac{V_o}{R_f}
\]

Rearranging:

\[
\boxed{V_o=-\frac{R_f}{R_1}V_{in}}
\]

The voltage gain is:

\[
\boxed{A_v=-\frac{R_f}{R_1}}
\]

The negative sign indicates a 180° phase inversion.

### 2.3 Important Characteristics

- Output is inverted relative to input.
- Gain magnitude is determined by the resistor ratio.
- Input resistance is approximately \(R_1\) for an ideal op-amp.
- The inverting input acts as a virtual ground.
- The circuit provides controlled voltage amplification or attenuation.

## 3. Non-Inverting Amplifier

In a non-inverting amplifier:

- The input signal is applied to the non-inverting terminal.
- The inverting terminal receives a fraction of the output through a feedback network.
- Negative feedback controls the output.

### 3.1 Circuit Arrangement

Vin ────────────────────────(+) 
                         ┌────────┐
                         | Op-Amp |────── Vout
                         └───(−)──┘       |
                              |            |
                              ●──── Rf ────┘
                              |
                              R1
                              |
                            Ground

### 3.2 Derivation of Voltage Gain

For an ideal op-amp under negative feedback:

\[
V_-=V_+=V_{in}
\]

The inverting input voltage is determined by the feedback voltage divider:

\[
V_- = V_o\frac{R_1}{R_1+R_f}
\]

Since:

\[
V_{in}=V_o\frac{R_1}{R_1+R_f}
\]

Rearranging:

\[
V_o=V_{in}\frac{R_1+R_f}{R_1}
\]

Therefore:

\[
\boxed{A_v=1+\frac{R_f}{R_1}}
\]

### 3.3 Important Characteristics

- Output is in phase with input.
- Voltage gain is one or greater in the ideal configuration.
- Input resistance is very high.
- It is useful for amplifying signals without significantly loading the source.

## 4. Voltage Follower

A voltage follower is a special non-inverting amplifier.

The output is directly connected to the inverting input.

The input is applied to the non-inverting terminal.

Therefore:

\[
R_f=0
\]

The feedback arrangement gives:

\[
\boxed{A_v=1}
\]

Thus:

\[
\boxed{V_o=V_{in}}
\]

### 4.1 Purpose

A voltage follower provides:

- Very high input resistance.
- Low output resistance.
- Impedance isolation.
- Buffering between circuit stages.

It does not increase voltage amplitude, but it can allow a weak signal source to drive a lower-resistance load.

## 5. Comparing Inverting and Non-Inverting Amplifiers

| Property | Inverting amplifier | Non-inverting amplifier |
|---|---|---|
| Input terminal | Inverting | Non-inverting |
| Phase relationship | 180° inversion | In phase |
| Ideal voltage gain | \(-R_f/R_1\) | \(1+R_f/R_1\) |
| Input resistance | Approximately \(R_1\) | Very high |
| Virtual ground | Present at inverting input when positive input is grounded | Not normally present |
| Minimum gain magnitude | Can be below, equal to, or above 1 | At least 1 |
| Common application | Signal scaling and summing | High-input-impedance amplification |

## 6. Practical Gain Limitations

The ideal gain equations assume:

- Very high open-loop gain.
- Suitable negative feedback.
- Operation within output-voltage limits.
- Sufficient bandwidth.
- Adequate slew rate.
- No significant loading effects.

In practical circuits, the output cannot exceed the op-amp's output swing.

The actual output may be limited by the supply rails.

For example, an amplifier requiring a 15 V output cannot provide it if its supply and output-stage limits permit only 10 V.

## 7. Gain in Decibels

Voltage gain can be expressed in decibels:

\[
A_{v(dB)}=20\log_{10}|A_v|
\]

The absolute value is used because decibel magnitude does not represent phase inversion.

A negative voltage gain indicates phase inversion, not negative amplification power.

## 8. Worked Numerical Examples

### Example 1: Inverting Amplifier

**Given:**

- Input resistor: \(R_1=10\,k\Omega\).
- Feedback resistor: \(R_f=100\,k\Omega\).
- Input voltage: \(V_{in}=0.2\,V\).

Calculate voltage gain and output voltage.

**Formula:**

\[
A_v=-\frac{R_f}{R_1}
\]

\[
V_o=A_vV_{in}
\]

**Solution:**

\[
A_v=-\frac{100}{10}
\]

\[
A_v=-10
\]

Output voltage:

\[
V_o=-10(0.2)
\]

\[
V_o=-2\,V
\]

**Final Answer:**

\[
\boxed{A_v=-10}
\]

\[
\boxed{V_o=-2\,V}
\]

The output is ten times the input magnitude and is inverted.

### Example 2: Non-Inverting Amplifier

**Given:**

- \(R_f=90\,k\Omega\).
- \(R_1=10\,k\Omega\).
- Input voltage: \(V_{in}=0.5\,V\).

Calculate the voltage gain and output voltage.

**Formula:**

\[
A_v=1+\frac{R_f}{R_1}
\]

\[
V_o=A_vV_{in}
\]

**Solution:**

\[
A_v=1+\frac{90}{10}
\]

\[
A_v=10
\]

Output:

\[
V_o=10(0.5)
\]

\[
V_o=5\,V
\]

**Final Answer:**

\[
\boxed{A_v=10}
\]

\[
\boxed{V_o=5\,V}
\]

The output is in phase with the input.

### Example 3: Voltage Follower

**Given:**

- Input voltage: \(V_{in}=3.2\,V\).
- Ideal op-amp voltage follower.

Calculate the output voltage.

**Formula:**

\[
V_o=V_{in}
\]

**Solution:**

\[
V_o=3.2\,V
\]

**Final Answer:**

\[
\boxed{V_o=3.2\,V}
\]

## 9. Applications

Inverting amplifiers are used in:

- Signal inversion.
- Signal scaling.
- Analog computing.
- Summing circuits.
- Active filters.

Non-inverting amplifiers are used in:

- Sensor signal amplification.
- High-input-impedance interfaces.
- Instrumentation stages.
- Buffering.
- Voltage amplification without phase inversion.

Voltage followers are particularly useful when connecting a high-impedance sensor to a circuit that requires more drive capability.

## 10. Common Examination Traps

1. The inverting amplifier has a negative voltage gain.
2. The non-inverting amplifier has a positive voltage gain.
3. The negative sign represents phase inversion.
4. The inverting gain is \(-R_f/R_1\).
5. The non-inverting gain is \(1+R_f/R_1\).
6. A voltage follower has unity voltage gain.
7. A virtual ground is not a physical ground connection.
8. The ideal op-amp input currents are zero.
9. The voltage follower is a non-inverting configuration.
10. A non-inverting amplifier cannot have a gain below one under the ideal standard configuration.
11. Practical output voltage is limited by the supply and output-stage characteristics.
12. A high voltage gain does not guarantee unlimited bandwidth.

## 11. Quiz

### Question 1

An inverting amplifier has \(R_f=60\,k\Omega\) and \(R_1=10\,k\Omega\). What is its voltage gain?

- [ ] +6.
- [x] -6.
- [ ] +10.
- [ ] -10.

> **Explanation:** The inverting gain is \(A_v=-R_f/R_1=-60/10=-6\). The negative sign represents 180° phase inversion.

### Question 2

What is the ideal voltage gain of a voltage follower?

- [ ] Zero.
- [ ] -1.
- [x] +1.
- [ ] Infinite.

> **Explanation:** A voltage follower directly connects the output to the inverting input. Negative feedback makes the output voltage equal to the input voltage.

### Question 3

Which configuration normally offers the higher input resistance?

- [ ] Inverting amplifier.
- [x] Non-inverting amplifier.
- [ ] Both always have zero input resistance.
- [ ] Neither has an input terminal.

> **Explanation:** The non-inverting input of an ideal op-amp draws no current, giving the non-inverting configuration extremely high input resistance.