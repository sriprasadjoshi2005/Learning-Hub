---
title: Operational Amplifiers and Ideal Op-Amp Characteristics
level: intermediate
---

# Operational Amplifiers and Ideal Op-Amp Characteristics

An operational amplifier, commonly called an op-amp, is a high-gain electronic voltage amplifier designed to amplify the difference between two input voltages.

Operational amplifiers are fundamental building blocks in analog electronics. They are used in signal amplification, mathematical operations, filtering, waveform generation, measurement systems, and control circuits.

This lesson introduces op-amp terminals, internal operation, ideal and practical characteristics, open-loop operation, feedback, virtual short concepts, and common applications.

## 1. Introduction to Operational Amplifiers

An operational amplifier is a differential amplifier with very high voltage gain.

It has two input terminals:

- Inverting input, marked with a minus sign \((-)\).
- Non-inverting input, marked with a plus sign \((+)\).

It also has one output terminal.

The output voltage depends on the difference between the two input voltages.

\[
V_o=A_{OL}(V_+-V_-)
\]

Where:

- \(V_o\) = output voltage.
- \(A_{OL}\) = open-loop voltage gain.
- \(V_+\) = non-inverting input voltage.
- \(V_-\) = inverting input voltage.

The output polarity depends on which input voltage is greater.

## 2. Op-Amp Symbol and Terminals

A simplified op-amp symbol is:

                    +VCC
                      |
             ┌─────────────┐
V+ ──────────| +           |
             |             |────── Vo
V- ──────────| -           |
             └─────────────┘
                      |
                    -VEE

The supply terminals provide energy for amplification.

The input terminals receive the signal, while the output terminal provides the amplified result.

Many practical op-amps also have offset-null, enable, or other device-specific terminals.

## 3. Differential Input Voltage

The differential input voltage is:

\[
V_d=V_+-V_-
\]

The ideal open-loop output relationship is:

\[
V_o=A_{OL}V_d
\]

A very small differential input can produce a large output because open-loop gain is extremely high.

For example, if:

\[
A_{OL}=100000
\]

and:

\[
V_d=100\,\mu V
\]

then:

\[
V_o=100000(100\times10^{-6})
\]

\[
V_o=10\,V
\]

In a real circuit, the output cannot exceed the available supply-voltage limits.

## 4. Ideal Operational Amplifier Characteristics

An ideal op-amp is a theoretical model used to simplify circuit analysis.

Its important characteristics are:

### 4.1 Infinite Open-Loop Voltage Gain

\[
A_{OL}\rightarrow\infty
\]

An infinitely small differential input would theoretically produce a finite output.

### 4.2 Infinite Input Resistance

\[
R_{in}\rightarrow\infty
\]

No current flows into either input terminal in the ideal model.

\[
I_+=I_-=0
\]

### 4.3 Zero Output Resistance

\[
R_{out}=0
\]

The output voltage is unaffected by the load in the ideal model.

### 4.4 Infinite Bandwidth

An ideal op-amp amplifies signals at every frequency without reducing gain.

### 4.5 Infinite Slew Rate

The output can change instantaneously.

### 4.6 Infinite Common-Mode Rejection Ratio

The op-amp amplifies only the difference between its inputs and completely rejects signals common to both.

### 4.7 Zero Input Offset Voltage

When both inputs have equal voltage, the ideal output is zero under open-loop conditions.

## 5. Practical Op-Amp Characteristics

Real operational amplifiers approximate ideal behaviour but have limitations.

Important practical parameters include:

| Parameter | Meaning |
|---|---|
| Open-loop gain | Gain without external feedback |
| Input resistance | Resistance seen at the input |
| Output resistance | Internal resistance at the output |
| Input offset voltage | Small differential voltage needed to make output zero |
| Input bias current | Small current entering the input terminals |
| Slew rate | Maximum output-voltage change per unit time |
| Bandwidth | Frequency range over which gain is maintained |
| CMRR | Ability to reject common-mode signals |
| PSRR | Ability to reject supply-voltage variations |

## 6. Open-Loop Operation

An op-amp is operating open-loop when no feedback path connects its output to its input.

Its output is:

\[
V_o=A_{OL}(V_+-V_-)
\]

Because open-loop gain is very high, even a small differential voltage can drive the output towards a supply limit.

The output is therefore usually driven into positive or negative saturation.

### 6.1 Positive Output Saturation

If:

\[
V_+>V_-
\]

the output tends towards positive saturation.

### 6.2 Negative Output Saturation

If:

\[
V_+<V_-
\]

the output tends towards negative saturation.

The actual output limits depend on the op-amp supply voltage and output-stage design.

## 7. Feedback in Operational Amplifiers

Feedback means returning a portion of the output signal to the input.

There are two main types.

### 7.1 Negative Feedback

Negative feedback opposes changes in the input difference.

It is commonly used in linear amplifiers.

Advantages include:

- More stable gain.
- Reduced distortion.
- Increased bandwidth in many designs.
- Improved control of circuit behaviour.

### 7.2 Positive Feedback

Positive feedback reinforces changes in the input difference.

It is commonly used in:

- Comparators with hysteresis.
- Schmitt triggers.
- Oscillator circuits.

Positive feedback can cause an op-amp to switch rapidly between output states.

## 8. Virtual Short Concept

When an op-amp operates with negative feedback and remains in its linear region, its differential input voltage is approximately zero.

Therefore:

\[
\boxed{V_+\approx V_-}
\]

This is called the virtual short concept.

It does not mean that the input terminals are physically connected.

Their voltages are approximately equal, but the ideal input current remains zero.

### 8.1 Virtual Ground

If the non-inverting input is connected to ground:

\[
V_+=0
\]

Under negative feedback:

\[
V_-\approx0
\]

The inverting input is therefore at approximately zero volts without being physically connected to ground.

This is called virtual ground.

## 9. Important Op-Amp Parameters

### 9.1 Common-Mode Rejection Ratio

Common-mode rejection ratio measures how effectively an op-amp rejects signals that appear equally at both inputs.

\[
CMRR=\frac{A_d}{A_c}
\]

Where:

- \(A_d\) = differential gain.
- \(A_c\) = common-mode gain.

In decibels:

\[
CMRR_{dB}=20\log_{10}(CMRR)
\]

A higher CMRR is generally desirable.

### 9.2 Slew Rate

Slew rate is the maximum rate of change of output voltage.

\[
SR=\max\left|\frac{dV_o}{dt}\right|
\]

Its unit is volts per microsecond:

\[
V/\mu s
\]

If an op-amp has insufficient slew rate, the output cannot follow a rapidly changing input waveform accurately.

### 9.3 Gain-Bandwidth Product

For many internally compensated op-amps, the gain-bandwidth product is approximately constant over a useful frequency range.

\[
GBW\approx A_vf
\]

Where:

- \(A_v\) = closed-loop voltage gain magnitude.
- \(f\) = corresponding bandwidth.

A higher closed-loop gain generally results in a lower available bandwidth.

## 10. Worked Numerical Examples

### Example 1: Open-Loop Output Voltage

**Given:**

- Open-loop gain: \(A_{OL}=200000\).
- Non-inverting input: \(V_+=2.001\,V\).
- Inverting input: \(V_-=2.000\,V\).

Calculate the ideal open-loop output.

**Formula:**

\[
V_o=A_{OL}(V_+-V_-)
\]

**Solution:**

\[
V_d=2.001-2.000
\]

\[
V_d=0.001\,V
\]

\[
V_o=200000(0.001)
\]

\[
V_o=200\,V
\]

**Final Answer:**

\[
\boxed{V_o=200\,V}
\]

This is the theoretical result. A practical op-amp cannot produce this output unless its supply rails permit it, so its actual output would saturate near a supply limit.

### Example 2: CMRR in Decibels

**Given:**

- Differential gain: \(A_d=100000\).
- Common-mode gain: \(A_c=0.01\).

Calculate CMRR in decibels.

**Formula:**

\[
CMRR=\frac{A_d}{A_c}
\]

\[
CMRR_{dB}=20\log_{10}(CMRR)
\]

**Solution:**

\[
CMRR=\frac{100000}{0.01}
\]

\[
CMRR=10^7
\]

\[
CMRR_{dB}=20\log_{10}(10^7)
\]

\[
CMRR_{dB}=140\,dB
\]

**Final Answer:**

\[
\boxed{CMRR=140\,dB}
\]

### Example 3: Slew-Rate Requirement

**Given:**

- Output voltage changes from \(-4\,V\) to \(+4\,V\).
- Required transition time: \(2\,\mu s\).

Calculate the required average slew rate.

**Formula:**

\[
SR=\frac{\Delta V_o}{\Delta t}
\]

**Solution:**

\[
\Delta V_o=4-(-4)=8\,V
\]

\[
SR=\frac{8}{2}
\]

\[
SR=4\,V/\mu s
\]

**Final Answer:**

\[
\boxed{SR=4\,V/\mu s}
\]

The selected op-amp should have a slew rate greater than this value, with suitable design margin.

## 11. Applications of Operational Amplifiers

Operational amplifiers are used in:

- Voltage amplifiers.
- Comparators.
- Active filters.
- Oscillators.
- Signal conditioning.
- Sensor interfaces.
- Instrumentation systems.
- Analog mathematical circuits.
- Audio electronics.

## 12. Common Examination Traps

1. An op-amp amplifies the difference between its two input voltages.
2. The non-inverting input is marked with a plus sign.
3. The inverting input is marked with a minus sign.
4. Ideal input resistance is infinite.
5. Ideal output resistance is zero.
6. Ideal input currents are zero.
7. Open-loop gain is extremely high.
8. Open-loop operation commonly drives the output into saturation.
9. The virtual short concept requires suitable negative feedback and linear operation.
10. Virtual ground is not a physical ground connection.
11. Negative feedback generally stabilizes gain.
12. Positive feedback is useful in switching and oscillator circuits.
13. CMRR measures rejection of common-mode signals.
14. Slew rate limits how rapidly the output can change.
15. Gain-bandwidth product limits the combination of closed-loop gain and bandwidth.

## 13. Quiz

### Question 1

What is the ideal input resistance of an operational amplifier?

- [ ] Zero.
- [ ] 50 ohms.
- [x] Infinite.
- [ ] Equal to its output resistance.

> **Explanation:** An ideal op-amp draws no current at either input terminal. This corresponds to infinite input resistance.

### Question 2

Under negative feedback and linear operation, what is the approximate relationship between the two input voltages?

- [ ] \(V_+=2V_-\).
- [x] \(V_+\approx V_-\).
- [ ] \(V_+=0\) under all conditions.
- [ ] \(V_+-V_-=V_{CC}\).

> **Explanation:** Negative feedback drives the differential input voltage towards zero. The two input voltages become approximately equal, although they are not physically shorted together.

### Question 3

What does slew rate specify?

- [ ] Maximum input resistance.
- [ ] Maximum common-mode voltage.
- [x] Maximum rate of change of output voltage.
- [ ] Maximum DC current entering the input.

> **Explanation:** Slew rate is the maximum value of the output-voltage derivative, usually expressed in volts per microsecond.