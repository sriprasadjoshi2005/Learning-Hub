---
title: Oscillators and Waveform Generators
level: intermediate
---

# Oscillators and Waveform Generators

An electronic oscillator is a circuit that generates a periodic electrical signal without requiring a continuously applied periodic input signal.

Oscillators are essential in communication systems, clocks, computers, signal generators, audio equipment, and measurement instruments.

A waveform generator produces electrical signals with particular shapes, frequencies, and amplitudes.

This lesson introduces feedback-based oscillation, Barkhausen's criterion, RC and LC oscillators, crystal oscillators, relaxation oscillators, and common waveform generators.

## 1. Introduction to Oscillators

An oscillator converts energy from a DC power supply into a periodic electrical signal.

The output may be:

- Sinusoidal.
- Square.
- Triangular.
- Sawtooth.
- Pulse-shaped.

An oscillator requires an active device and a suitable feedback network.

The active device compensates for energy losses, while the feedback network determines the conditions and frequency of oscillation.

## 2. Basic Oscillator Structure

A simplified oscillator consists of:

1. Amplifier.
2. Feedback network.
3. DC power supply.

The output of the amplifier is fed back to its input.

Under suitable conditions, the feedback sustains a periodic signal.

Unlike an ordinary amplifier, an oscillator does not require a periodic external input to maintain its output.

## 3. Positive Feedback

Positive feedback occurs when a portion of the output signal is returned to the input in a way that reinforces the original signal.

For sustained sinusoidal oscillation, the total loop gain must satisfy suitable magnitude and phase conditions.

The loop gain is:

\[
A\beta
\]

Where:

- \(A\) = amplifier gain.
- \(\beta\) = feedback-network gain.

## 4. Barkhausen Criterion

The Barkhausen criterion gives the ideal conditions for sustained sinusoidal oscillation in a feedback oscillator.

The conditions are:

### 4.1 Magnitude Condition

\[
\boxed{|A\beta|=1}
\]

The magnitude of the loop gain must be unity.

### 4.2 Phase Condition

\[
\boxed{\angle A\beta=0^\circ}
\]

or an integer multiple of \(360^\circ\).

The feedback signal must return in phase with the original signal.

In practical oscillator start-up, the loop-gain magnitude is initially greater than one. Amplitude stabilization mechanisms then reduce the effective gain towards unity.

The Barkhausen criterion is a useful design condition, but it is not by itself a complete guarantee of stable oscillation.

## 5. RC Phase-Shift Oscillator

An RC phase-shift oscillator uses an amplifier and a network of resistors and capacitors to produce the required feedback phase shift.

A common design uses three RC sections.

The RC network provides approximately \(180^\circ\) phase shift at the oscillation frequency.

An inverting amplifier provides another \(180^\circ\).

The total phase shift becomes:

\[
180^\circ+180^\circ=360^\circ
\]

Therefore, the feedback signal returns in phase.

### 5.1 Frequency of Oscillation

For three identical RC sections under the standard idealized assumptions:

\[
\boxed{
f_o=\frac{1}{2\pi RC\sqrt{6}}
}
\]

Where:

- \(f_o\) = oscillation frequency.
- \(R\) = resistance of each section.
- \(C\) = capacitance of each section.

The amplifier must provide sufficient gain to compensate for attenuation in the RC feedback network.

For the standard idealized circuit, the required amplifier gain magnitude is approximately 29 or greater.

### 5.2 Applications

- Audio-frequency signal generation.
- Laboratory oscillators.
- Low-frequency test signals.

## 6. Wien Bridge Oscillator

A Wien bridge oscillator uses a lead-lag RC network in a positive-feedback arrangement.

It is commonly used to generate low-distortion sinusoidal signals.

### 6.1 Frequency of Oscillation

For equal resistors and equal capacitors:

\[
\boxed{f_o=\frac{1}{2\pi RC}}
\]

At the oscillation frequency, the feedback network provides zero net phase shift and an attenuation of approximately one-third.

Therefore, the amplifier gain must be approximately:

\[
A=3
\]

for ideal sustained oscillation.

### 6.2 Amplitude Stabilization

A practical Wien bridge oscillator requires an amplitude-control mechanism.

This prevents the output from growing indefinitely or decaying to zero.

Possible methods include:

- Lamp-based stabilization.
- Diode networks.
- Automatic gain control.
- Other non-linear control elements.

### 6.3 Applications

- Audio signal generators.
- Laboratory waveform generators.
- Low-distortion sine-wave sources.

## 7. LC Oscillators

LC oscillators use an inductor and capacitor to determine the oscillation frequency.

Energy alternates between:

- The electric field of the capacitor.
- The magnetic field of the inductor.

An amplifier compensates for circuit losses.

### 7.1 Resonant Frequency

For an ideal LC resonant circuit:

\[
\boxed{
f_o=\frac{1}{2\pi\sqrt{LC}}
}
\]

Where:

- \(L\) = inductance in henries.
- \(C\) = capacitance in farads.

### 7.2 Hartley Oscillator

A Hartley oscillator uses an inductive feedback arrangement.

Its frequency is determined by the equivalent inductance and capacitance.

For two uncoupled series inductors:

\[
L_T=L_1+L_2
\]

A simplified frequency expression is:

\[
f_o=\frac{1}{2\pi\sqrt{L_TC}}
\]

Mutual coupling may alter the effective inductance.

### 7.3 Colpitts Oscillator

A Colpitts oscillator uses a capacitive voltage divider for feedback.

The effective capacitance of two series capacitors is:

\[
C_T=\frac{C_1C_2}{C_1+C_2}
\]

The approximate oscillation frequency is:

\[
f_o=\frac{1}{2\pi\sqrt{LC_T}}
\]

### 7.4 Applications

LC oscillators are widely used in radio-frequency circuits and communication systems.

## 8. Crystal Oscillator

A crystal oscillator uses the mechanical resonance of a piezoelectric crystal to establish a highly stable frequency.

Quartz is commonly used.

When an alternating voltage is applied, the crystal mechanically vibrates.

Its resonance produces a highly selective frequency response.

### 8.1 Advantages

- High frequency stability.
- High quality factor.
- Low frequency drift.
- Good accuracy.

### 8.2 Applications

- Microcontroller clock circuits.
- Digital watches.
- Communication equipment.
- Frequency references.
- Computers and embedded systems.

## 9. Relaxation Oscillators

A relaxation oscillator produces periodic waveforms through repeated charging and discharging of a capacitor or another energy-storage element.

It commonly uses switching devices rather than a sinusoidal resonant network.

Examples include:

- Astable multivibrators.
- Timer-based oscillators.
- Schmitt-trigger oscillators.

Relaxation oscillators often generate square, triangular, or pulse waveforms.

## 10. Astable Multivibrator

An astable multivibrator has no stable output state.

It continuously switches between two states.

An RC timing network determines how long the circuit remains in each state.

Its output is typically a square wave.

### 10.1 Applications

- Clock generation.
- LED flashing circuits.
- Pulse generation.
- Timing circuits.

## 11. Monostable and Bistable Multivibrators

### 11.1 Monostable Multivibrator

A monostable multivibrator has:

- One stable state.
- One temporary quasi-stable state.

An external trigger causes the circuit to enter the temporary state.

After a predetermined interval, it returns to its stable state.

Applications include:

- Pulse generation.
- Timing delays.
- Switch debouncing.
- Triggered control circuits.

### 11.2 Bistable Multivibrator

A bistable multivibrator has two stable states.

An external trigger changes the circuit from one state to the other.

It is used in:

- Flip-flops.
- Memory elements.
- Switching circuits.

## 12. Waveform Generators

A waveform generator produces signals with selected shapes and frequencies.

### 12.1 Sine-Wave Generator

Produces a sinusoidal signal.

Applications include:

- Audio testing.
- Communication systems.
- Frequency response measurements.

### 12.2 Square-Wave Generator

Produces alternating high and low voltage levels.

Applications include:

- Digital clocks.
- Timing signals.
- Logic testing.

### 12.3 Triangle-Wave Generator

Produces a waveform with approximately linear rising and falling slopes.

Applications include:

- Function generators.
- Sweep circuits.
- Modulation systems.

### 12.4 Sawtooth-Wave Generator

Produces a waveform with a gradual rise followed by a rapid fall, or the reverse.

Applications include:

- Sweep circuits.
- Time-base circuits.
- Signal generation.

## 13. Worked Numerical Examples

### Example 1: Wien Bridge Oscillator

**Given:**

- \(R=10\,k\Omega\).
- \(C=10\,nF\).

Calculate the oscillation frequency.

**Formula:**

\[
f_o=\frac{1}{2\pi RC}
\]

**Solution:**

\[
f_o=\frac{1}{2\pi(10000)(10\times10^{-9})}
\]

\[
f_o=\frac{1}{2\pi(10^{-4})}
\]

\[
f_o\approx1591.5\,Hz
\]

**Final Answer:**

\[
\boxed{f_o\approx1.59\,kHz}
\]

### Example 2: LC Oscillator

**Given:**

- \(L=100\,\mu H\).
- \(C=100\,pF\).

Calculate the ideal resonant frequency.

**Formula:**

\[
f_o=\frac{1}{2\pi\sqrt{LC}}
\]

**Solution:**

Convert units:

\[
L=100\times10^{-6}\,H
\]

\[
C=100\times10^{-12}\,F
\]

Substitute:

\[
f_o=
\frac{1}{2\pi\sqrt{(100\times10^{-6})(100\times10^{-12})}}
\]

\[
f_o=
\frac{1}{2\pi\sqrt{10^{-14}}}
\]

\[
f_o=\frac{1}{2\pi(10^{-7})}
\]

\[
f_o\approx1.5915\times10^6\,Hz
\]

**Final Answer:**

\[
\boxed{f_o\approx1.59\,MHz}
\]

### Example 3: RC Phase-Shift Oscillator

**Given:**

- \(R=10\,k\Omega\).
- \(C=0.01\,\mu F\).

Calculate the approximate oscillation frequency.

**Formula:**

\[
f_o=\frac{1}{2\pi RC\sqrt{6}}
\]

**Solution:**

\[
C=10^{-8}\,F
\]

\[
f_o=
\frac{1}{2\pi(10000)(10^{-8})\sqrt{6}}
\]

\[
f_o\approx\frac{1591.55}{2.449}
\]

\[
f_o\approx649.9\,Hz
\]

**Final Answer:**

\[
\boxed{f_o\approx650\,Hz}
\]

## 14. Practical Applications

Oscillators and waveform generators are used in:

- Microcontroller clock circuits.
- Radio transmitters and receivers.
- Audio signal generators.
- Digital timing systems.
- Frequency synthesizers.
- Test and measurement instruments.
- Communication systems.
- Pulse-generation circuits.

## 15. Common Examination Traps

1. An oscillator generates a periodic output without a continuously applied periodic input.
2. The amplifier supplies energy from the DC source.
3. The feedback network determines the oscillation conditions and frequency.
4. Barkhausen's ideal magnitude condition is \(|A\beta|=1\).
5. The total loop phase shift must be an integer multiple of \(360^\circ\).
6. An RC phase-shift oscillator uses an RC network and an inverting amplifier.
7. A Wien bridge oscillator is commonly used for low-distortion sine-wave generation.
8. An LC oscillator uses inductance and capacitance to determine frequency.
9. A crystal oscillator provides high frequency stability.
10. A relaxation oscillator commonly generates non-sinusoidal waveforms.
11. An astable multivibrator has no stable state.
12. A monostable multivibrator has one stable state.
13. A bistable multivibrator has two stable states.
14. The Barkhausen criterion alone does not guarantee stable practical oscillation.
15. Oscillation amplitude must be controlled in a practical oscillator.

## 16. Quiz

### Question 1

Which oscillator is commonly used to generate low-distortion sinusoidal signals?

- [ ] Astable multivibrator.
- [x] Wien bridge oscillator.
- [ ] Bistable multivibrator.
- [ ] Digital counter.

> **Explanation:** A Wien bridge oscillator uses an RC feedback network and amplitude stabilization to generate low-distortion sinusoidal signals.

### Question 2

What is the ideal resonant frequency of an LC oscillator?

- [ ] \(1/(2\pi RC)\).
- [ ] \(RC/(2\pi)\).
- [x] \(1/(2\pi\sqrt{LC})\).
- [ ] \(2\pi LC\).

> **Explanation:** The ideal resonant frequency of an LC circuit is \(f_o=1/(2\pi\sqrt{LC})\).

### Question 3

Which multivibrator has no stable state and continuously switches between two states?

- [x] Astable.
- [ ] Monostable.
- [ ] Bistable.
- [ ] Differential.

> **Explanation:** An astable multivibrator has no stable state. Its timing network causes continuous switching between two output states.