---
title: Summing Amplifiers and Comparator Circuits
level: intermediate
---

# Summing Amplifiers and Comparator Circuits

Operational amplifiers can perform mathematical operations on analog signals.

Two important applications are:

1. Summing amplifiers, which combine multiple input signals.
2. Comparators, which determine which of two input voltages is greater.

Summing amplifiers are used in audio mixers, signal processing, and analog computing. Comparators are used in threshold detectors, switching circuits, sensor interfaces, and waveform generation.

## 1. Introduction to Summing Amplifiers

A summing amplifier produces an output proportional to the algebraic sum of two or more input voltages.

It is commonly constructed using an inverting op-amp configuration.

Multiple input signals are connected to the inverting input through separate resistors.

The non-inverting input is connected to ground.

## 2. Inverting Summing Amplifier

### 2.1 Circuit Arrangement

Each input voltage is connected to the inverting input through an input resistor.

A feedback resistor connects the output to the inverting input.

Because the inverting input is at virtual ground, each input produces a current through its corresponding resistor.

These currents add at the summing node.

### 2.2 Derivation

For an ideal op-amp:

\[
V_-\approx0
\]

The current contributed by the first input is:

\[
I_1=\frac{V_1}{R_1}
\]

Similarly:

\[
I_2=\frac{V_2}{R_2}
\]

For \(n\) inputs:

\[
I_f=I_1+I_2+\cdots+I_n
\]

The feedback current is:

\[
I_f=\frac{-V_o}{R_f}
\]

Therefore:

\[
\frac{-V_o}{R_f}
=
\frac{V_1}{R_1}
+\frac{V_2}{R_2}
+\cdots+
\frac{V_n}{R_n}
\]

Rearranging:

\[
\boxed{
V_o=-R_f
\left(
\frac{V_1}{R_1}
+\frac{V_2}{R_2}
+\cdots+
\frac{V_n}{R_n}
\right)
}
\]

### 2.3 Equal-Resistor Summing Amplifier

If all input resistors are equal to \(R\):

\[
R_1=R_2=\cdots=R_n=R
\]

then:

\[
\boxed{
V_o=-\frac{R_f}{R}(V_1+V_2+\cdots+V_n)
}
\]

If:

\[
R_f=R
\]

then:

\[
\boxed{V_o=-(V_1+V_2+\cdots+V_n)}
\]

The output is the negative sum of the input voltages.

## 3. Weighted Summing Amplifier

A weighted summing amplifier allows different input signals to contribute different amounts to the output.

Its output is:

\[
V_o=-R_f
\left(
\frac{V_1}{R_1}
+\frac{V_2}{R_2}
+\cdots
\right)
\]

Each input's contribution depends on its resistor.

A smaller input resistance produces a larger current contribution for the same input voltage.

This is useful when signals must be combined with different weights.

## 4. Averaging Amplifier

An averaging amplifier produces an output proportional to the average of several input voltages.

For \(n\) equal input resistors \(R\):

\[
V_o=-\frac{R_f}{R}(V_1+V_2+\cdots+V_n)
\]

To obtain the negative average:

\[
\frac{R_f}{R}=\frac{1}{n}
\]

Therefore:

\[
\boxed{
V_o=-\frac{V_1+V_2+\cdots+V_n}{n}
}
\]

An additional inverting stage can reverse the polarity if a positive average is required.

## 5. Differential Amplifier

A differential amplifier produces an output proportional to the difference between two input voltages.

For a properly matched four-resistor differential amplifier:

\[
\boxed{
V_o=\frac{R_2}{R_1}(V_2-V_1)
}
\]

This expression assumes the resistor ratios on both sides are matched:

\[
\frac{R_2}{R_1}=\frac{R_4}{R_3}
\]

The differential amplifier is useful when the difference between two signals is important and common-mode interference should be rejected.

## 6. Introduction to Comparators

A comparator is a circuit that compares two input voltages and produces an output indicating which voltage is greater.

An op-amp can be used as a comparator by operating it without the usual linear negative-feedback network.

The output generally moves towards one of its saturation limits.

### 6.1 Basic Operation

If:

\[
V_+>V_-
\]

the output moves towards positive saturation.

If:

\[
V_+<V_-
\]

the output moves towards negative saturation.

The output is therefore approximately a two-state signal.

A dedicated comparator IC is often preferred in practical switching applications because it is designed specifically for rapid and reliable comparison.

## 7. Zero-Crossing Detector

A zero-crossing detector compares an input signal with a zero-volt reference.

The input is applied to one op-amp terminal, while the other is connected to ground.

For an input applied to the non-inverting terminal:

- Positive input voltage produces a high output.
- Negative input voltage produces a low output.

The output changes state whenever the input crosses zero.

### 7.1 Applications

- AC waveform detection.
- Frequency measurement.
- Phase-related circuits.
- Signal conditioning.
- Switching at zero crossings.

## 8. Non-Inverting Comparator

In a non-inverting comparator:

- Signal voltage is applied to the non-inverting input.
- Reference voltage is applied to the inverting input.

Therefore:

\[
V_o\approx V_{OH}
\quad\text{when}\quad
V_{in}>V_{ref}
\]

\[
V_o\approx V_{OL}
\quad\text{when}\quad
V_{in}<V_{ref}
\]

Where:

- \(V_{OH}\) = high output level.
- \(V_{OL}\) = low output level.

## 9. Inverting Comparator

In an inverting comparator:

- Signal voltage is applied to the inverting input.
- Reference voltage is applied to the non-inverting input.

Therefore:

\[
V_o\approx V_{OH}
\quad\text{when}\quad
V_{in}<V_{ref}
\]

\[
V_o\approx V_{OL}
\quad\text{when}\quad
V_{in}>V_{ref}
\]

The output polarity is opposite to that of the non-inverting comparator for the same signal and reference relationship.

## 10. Reference Voltage and Threshold Detection

A comparator can be used to detect when a measured voltage crosses a selected threshold.

For example, a temperature sensor may produce an output voltage that increases with temperature.

A comparator can compare that voltage with a reference representing a desired temperature threshold.

When the sensor voltage crosses the reference, the output changes state.

Reference voltages may be generated using:

- Resistor dividers.
- Reference-voltage ICs.
- Zener diode circuits.
- Precision reference sources.

## 11. Comparator Limitations and Practical Considerations

A practical comparator circuit must consider:

- Input common-mode voltage range.
- Input offset voltage.
- Propagation delay.
- Output voltage levels.
- Input noise.
- Hysteresis requirements.
- Output compatibility with the next circuit.

When the input voltage is close to the reference, noise can cause repeated output transitions.

Hysteresis can help prevent this behaviour.

Hysteresis is examined further in the context of positive feedback and waveform generation.

## 12. Worked Numerical Examples

### Example 1: Inverting Summing Amplifier

**Given:**

- \(V_1=1\,V\).
- \(V_2=2\,V\).
- \(V_3=0.5\,V\).
- All input resistors: \(R=10\,k\Omega\).
- Feedback resistor: \(R_f=20\,k\Omega\).

Calculate the output voltage.

**Formula:**

\[
V_o=-\frac{R_f}{R}(V_1+V_2+V_3)
\]

**Solution:**

\[
V_o=-\frac{20}{10}(1+2+0.5)
\]

\[
V_o=-2(3.5)
\]

\[
V_o=-7\,V
\]

**Final Answer:**

\[
\boxed{V_o=-7\,V}
\]

### Example 2: Weighted Summing Amplifier

**Given:**

- \(V_1=2\,V\), \(R_1=10\,k\Omega\).
- \(V_2=1\,V\), \(R_2=20\,k\Omega\).
- \(R_f=40\,k\Omega\).

Calculate the output voltage.

**Formula:**

\[
V_o=-R_f
\left(
\frac{V_1}{R_1}
+\frac{V_2}{R_2}
\right)
\]

**Solution:**

\[
V_o=-40\,k\Omega
\left(
\frac{2}{10\,k\Omega}
+\frac{1}{20\,k\Omega}
\right)
\]

\[
V_o=-40(0.2+0.05)
\]

\[
V_o=-10\,V
\]

**Final Answer:**

\[
\boxed{V_o=-10\,V}
\]

### Example 3: Comparator Decision

**Given:**

- Non-inverting input: \(V_+=3.2\,V\).
- Inverting input: \(V_-=2.5\,V\).

Determine the output direction.

**Formula:**

\[
V_d=V_+-V_-
\]

**Solution:**

\[
V_d=3.2-2.5
\]

\[
V_d=0.7\,V
\]

Since:

\[
V_+>V_-
\]

the output moves towards positive saturation.

**Final Answer:**

The output is HIGH, assuming the comparator's output convention defines the positive output state as HIGH.

## 13. Practical Applications

### 13.1 Audio Mixing

Summing amplifiers combine signals from multiple microphones or audio sources.

### 13.2 Analog Computing

Summing amplifiers perform addition and weighted addition of analog signals.

### 13.3 Threshold Detection

Comparators detect whether sensor voltages exceed a reference.

### 13.4 Battery Monitoring

A comparator can indicate when a battery voltage falls below a selected threshold.

### 13.5 Zero-Crossing Detection

Zero-crossing detectors identify transitions of AC signals through zero volts.

## 14. Common Examination Traps

1. A summing amplifier combines multiple input voltages.
2. The standard inverting summing amplifier produces a negative weighted sum.
3. Smaller input resistance gives a larger contribution for the same input voltage.
4. Equal input resistors produce equal weighting.
5. An averaging amplifier requires suitable feedback-resistor selection.
6. A differential amplifier responds to the difference between two inputs.
7. A comparator generally operates open-loop rather than as a linear amplifier.
8. A non-inverting comparator produces a high output when its signal input exceeds its reference.
9. An inverting comparator reverses that comparison relationship.
10. A zero-crossing detector uses zero volts as its reference.
11. Noise near the threshold can cause repeated switching.
12. Comparator output levels depend on the device and its supply arrangement.

## 15. Quiz

### Question 1

An inverting summing amplifier has equal input resistors and a feedback resistor twice their value. What is its output?

- [ ] The positive average of the inputs.
- [x] Negative twice the sum of the inputs.
- [ ] Positive twice the sum of the inputs.
- [ ] Zero for every input combination.

> **Explanation:** With equal input resistors \(R\) and \(R_f=2R\), the output is \(-2(V_1+V_2+\cdots+V_n)\).

### Question 2

A non-inverting comparator has \(V_{in}=4\,V\) and \(V_{ref}=3\,V\). What output state is expected?

- [x] HIGH.
- [ ] LOW.
- [ ] Always zero.
- [ ] It behaves as a unity-gain amplifier.

> **Explanation:** The signal is connected to the non-inverting input. Since \(V_{in}>V_{ref}\), the output moves towards its high state.

### Question 3

What does a zero-crossing detector identify?

- [ ] The maximum amplitude of a signal.
- [ ] The signal's RMS value.
- [x] The points at which a signal crosses zero volts.
- [ ] The frequency at which amplifier gain becomes zero.

> **Explanation:** A zero-crossing detector compares the input against a zero-volt reference and changes output state when the signal crosses that reference.