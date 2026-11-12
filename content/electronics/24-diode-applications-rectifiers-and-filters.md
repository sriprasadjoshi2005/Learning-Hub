---
title: Diode Applications Including Rectifiers and Filters
level: intermediate
---

# Diode Applications Including Rectifiers and Filters

A PN junction diode is useful because it conducts strongly in forward bias and blocks current in reverse bias under normal operating conditions.

This directional behaviour allows diodes to perform several important functions, including rectification, waveform shaping, voltage clamping, signal detection, and circuit protection.

One of the most important applications is the conversion of alternating current (AC) into direct current (DC). This process is called rectification.

Rectifiers are widely used in power supplies, battery chargers, electronic instruments, computers, communication equipment, and industrial control systems.

This lesson explains half-wave rectifiers, full-wave rectifiers, bridge rectifiers, filter circuits, ripple, and important performance parameters.

## 1. Introduction to Rectification

Alternating current changes its magnitude and direction periodically.

Direct current flows in one direction, although its magnitude may vary with time.

A rectifier is an electronic circuit that converts an AC input into a unidirectional output.

The output of a basic rectifier is pulsating DC rather than perfectly constant DC.

A typical DC power supply contains:

1. AC source or transformer.
2. Rectifier circuit.
3. Filter circuit.
4. Voltage regulator, when required.
5. Load.

The rectifier performs the AC-to-DC conversion, while the filter reduces unwanted fluctuations in the output.

## 2. Half-Wave Rectifier

A half-wave rectifier uses a single diode to convert only one half-cycle of an AC waveform into a unidirectional output.

### 2.1 Circuit Operation

A basic half-wave rectifier consists of:

- An AC voltage source.
- A diode.
- A load resistor.

The diode is connected in series with the load.

During the positive half-cycle:

- The diode becomes forward-biased.
- Current flows through the diode and load.
- A positive voltage appears across the load.

During the negative half-cycle:

- The diode becomes reverse-biased.
- Current is approximately zero.
- The load voltage is approximately zero.

### 2.2 Circuit Representation

    AC input
       ~
       |
       +─────|>|─────+──── V_out
             D       |
                     R_L
                     |
       ──────────────+──── 0 V

The diode permits current during only one polarity of the input.

### 2.3 Input and Output Waveforms

Input waveform:

    Voltage
       ↑
       |     /‾\       /‾\
       |    /   \     /   \
    0  |___/_____\___/_____\____→ Time
       |           \ /     \ /
       |            V       V

Half-wave output:

    Voltage
       ↑
       |     /‾\       /‾\
       |    /   \     /   \
    0  |___/_____\___/_____\____→ Time

       Negative half-cycles are blocked.

The output contains positive pulses separated by intervals of zero voltage.

### 2.4 Average Output Voltage

For an ideal half-wave rectifier with sinusoidal input:

\[
V_{DC}=\frac{V_m}{\pi}
\]

Where:

- \(V_{DC}\) = average DC output voltage.
- \(V_m\) = peak input voltage.

The average output current for a resistive load is:

\[
I_{DC}=\frac{I_m}{\pi}
\]

Where:

- \(I_m\) = peak load current.

### 2.5 RMS Output Voltage

The RMS output voltage is:

\[
V_{RMS}=\frac{V_m}{2}
\]

For a resistive load:

\[
I_{RMS}=\frac{I_m}{2}
\]

### 2.6 Rectification Efficiency

Rectification efficiency is the ratio of useful DC output power to the AC input power supplied to the rectifier.

\[
\eta=\frac{P_{DC}}{P_{AC}}\times100\%
\]

For an ideal half-wave rectifier with a resistive load and ideal diode:

\[
\eta_{\max}\approx40.6\%
\]

This relatively low efficiency is one limitation of half-wave rectification.

### 2.7 Ripple Frequency

The ripple frequency is the frequency at which the rectified output pulses repeat.

For a half-wave rectifier:

\[
f_r=f
\]

Where:

- \(f_r\) = ripple frequency.
- \(f\) = AC supply frequency.

For a 50 Hz input, the ripple frequency is 50 Hz.

## 3. Full-Wave Rectifier

A full-wave rectifier uses both half-cycles of an AC input to produce a unidirectional output.

It can be implemented using:

1. Two diodes and a centre-tapped transformer.
2. Four diodes in a bridge configuration.

Full-wave rectification produces a higher average output voltage and a higher ripple frequency than half-wave rectification for the same input frequency and peak voltage.

## 4. Centre-Tapped Full-Wave Rectifier

A centre-tapped full-wave rectifier uses:

- A centre-tapped transformer secondary.
- Two diodes.
- A load resistor.

The transformer secondary provides two equal voltages with opposite phase relative to the centre tap.

### 4.1 Positive Half-Cycle

During one half-cycle:

- The upper end of the secondary is positive relative to the centre tap.
- The first diode becomes forward-biased.
- The second diode is reverse-biased.
- Current flows through the load in a particular direction.

### 4.2 Negative Half-Cycle

During the next half-cycle:

- The lower end of the secondary becomes positive relative to the centre tap.
- The second diode becomes forward-biased.
- The first diode is reverse-biased.
- Current flows through the load in the same direction.

Thus, both half-cycles contribute to the output.

### 4.3 Average Output Voltage

For an ideal full-wave rectifier:

\[
V_{DC}=\frac{2V_m}{\pi}
\]

Where \(V_m\) is the peak voltage across each half of the transformer secondary.

The average output current is:

\[
I_{DC}=\frac{2I_m}{\pi}
\]

### 4.4 RMS Output Voltage

\[
V_{RMS}=\frac{V_m}{\sqrt{2}}
\]

### 4.5 Ripple Frequency

For a full-wave rectifier:

\[
f_r=2f
\]

For a 50 Hz input:

\[
f_r=2(50)=100\,Hz
\]

## 5. Bridge Rectifier

A bridge rectifier uses four diodes arranged in a bridge configuration.

It converts both half-cycles of an AC input into unidirectional current through the load.

### 5.1 Circuit Structure

A simplified bridge arrangement is:

             D1             D2
    AC A ───|>|─────+─────|<|─── AC B
                      |
                    + Vout
                      |
                     R_L
                      |
                    - Vout
                      |
    AC A ───|<|─────+─────|>|─── AC B
             D3             D4

The exact current path depends on the polarity of the AC input.

### 5.2 Positive Half-Cycle

When AC terminal A is positive relative to B:

- One pair of diagonally opposite diodes conducts.
- The other pair remains reverse-biased.
- Current passes through the load in the defined positive direction.

### 5.3 Negative Half-Cycle

When AC terminal B is positive relative to A:

- The other diagonal pair conducts.
- The first pair blocks current.
- Load current continues in the same direction.

### 5.4 Advantages of a Bridge Rectifier

- Uses both AC half-cycles.
- Does not require a centre-tapped transformer.
- Provides a higher average output than a half-wave rectifier for comparable input conditions.
- Uses the transformer secondary more effectively than a centre-tapped arrangement in many applications.

### 5.5 Limitation

Two diodes conduct in series during each half-cycle.

Therefore, the total forward voltage drop is approximately twice the forward drop of one diode.

For silicon diodes:

\[
V_{\text{drop,total}}\approx2(0.7)=1.4\,V
\]

This approximation is useful for basic circuit calculations.

## 6. Comparison of Rectifier Types

| Parameter | Half-wave | Centre-tapped full-wave | Bridge full-wave |
|---|---:|---:|---:|
| Number of diodes | 1 | 2 | 4 |
| Input half-cycles used | 1 | 2 | 2 |
| Ripple frequency | \(f\) | \(2f\) | \(2f\) |
| Ideal average output | \(V_m/\pi\) | \(2V_m/\pi\) | \(2V_m/\pi\) |
| Maximum ideal efficiency | 40.6% | 81.2% | 81.2% |
| Centre tap required | No | Yes | No |
| Diodes conducting at a time | 1 | 1 | 2 |

The table assumes ideal diodes and comparable peak voltage definitions. For a bridge rectifier, \(V_m\) is the peak voltage across the full secondary winding.

## 7. Capacitor Filters

The output of a rectifier is pulsating DC.

Many electronic circuits require a smoother voltage.

A capacitor filter is commonly connected in parallel with the load to reduce output ripple.

### 7.1 Working Principle

Consider a full-wave rectifier with a capacitor connected across its load.

During a rising rectified waveform:

- The diode conducts when the input voltage exceeds the capacitor voltage sufficiently.
- The capacitor charges towards the peak output voltage.

After the input peak:

- The rectified voltage begins to decrease.
- The diode becomes reverse-biased when the capacitor voltage exceeds the instantaneous rectifier voltage.
- The capacitor discharges through the load.
- The load voltage decreases gradually rather than falling immediately to zero.

When the next rectified peak arrives, the capacitor is recharged.

This process produces a smoother output.

### 7.2 Capacitor Filter Circuit

    Rectifier output
          |
          +───────────+──── V_out
          |           |
          C          R_L
          |           |
          +───────────+──── 0 V

The capacitor is connected in parallel with the load.

### 7.3 Ripple Voltage

Ripple voltage is the remaining periodic variation in the output after filtering.

For a sufficiently large capacitor and approximately constant load current:

\[
V_{r(pp)}\approx\frac{I_L}{f_rC}
\]

Where:

- \(V_{r(pp)}\) = peak-to-peak ripple voltage.
- \(I_L\) = load current.
- \(f_r\) = ripple frequency.
- \(C\) = filter capacitance.

For a half-wave rectifier:

\[
V_{r(pp)}\approx\frac{I_L}{fC}
\]

For a full-wave rectifier:

\[
V_{r(pp)}\approx\frac{I_L}{2fC}
\]

These approximations assume relatively small ripple and a capacitor that discharges mainly through the load between charging peaks.

### 7.4 Effect of Capacitance

Increasing the filter capacitance generally:

- Reduces ripple voltage.
- Improves output smoothing.
- Increases the charge stored between peaks.
- Can increase diode charging-current peaks.

A larger capacitor is not automatically better in every design because diode surge current, transformer ratings, startup current, and cost must also be considered.

## 8. Other Filter Types

### 8.1 Inductor Filter

An inductor connected in series with the load opposes changes in current.

It reduces variations in load current and can smooth the rectifier output.

Inductor filters are used in some higher-power applications.

### 8.2 LC Filter

An LC filter uses an inductor and capacitor.

The inductor opposes changes in current, while the capacitor opposes changes in voltage.

Together they provide improved filtering.

### 8.3 Pi Filter

A capacitor-input pi filter commonly consists of:

- A capacitor.
- A series inductor.
- A second capacitor.

Its simplified arrangement resembles the Greek letter \(\pi\).

It can provide substantial ripple reduction.

## 9. Ripple Factor

Ripple factor measures the amount of AC variation remaining in a rectifier output relative to its DC component.

It is defined as:

\[
r=\frac{V_{AC,rms}}{V_{DC}}
\]

Where:

- \(V_{AC,rms}\) = RMS value of the AC component of output voltage.
- \(V_{DC}\) = average DC output voltage.

An equivalent expression is:

\[
r=\sqrt{\left(\frac{V_{RMS}}{V_{DC}}\right)^2-1}
\]

Where \(V_{RMS}\) is the total RMS output voltage.

For ideal unfiltered rectifiers:

- Half-wave ripple factor: approximately 1.21.
- Full-wave ripple factor: approximately 0.482.

A lower ripple factor indicates a smoother DC output.

## 10. Worked Numerical Examples

### Example 1: Half-Wave Rectifier Output

**Given:**

- Peak AC input voltage: \(V_m=20\,V\).
- Ideal diode.

Calculate the average output voltage and RMS output voltage.

**Formula:**

\[
V_{DC}=\frac{V_m}{\pi}
\]

\[
V_{RMS}=\frac{V_m}{2}
\]

**Solution:**

Average output:

\[
V_{DC}=\frac{20}{3.1416}
\]

\[
V_{DC}\approx6.37\,V
\]

RMS output:

\[
V_{RMS}=\frac{20}{2}
\]

\[
V_{RMS}=10\,V
\]

**Final Answer:**

\[
\boxed{V_{DC}\approx6.37\,V}
\]

\[
\boxed{V_{RMS}=10\,V}
\]

### Example 2: Full-Wave Bridge Rectifier

**Given:**

- Peak input voltage: \(V_m=24\,V\).
- Silicon diode forward drop: \(0.7\,V\).
- Two diodes conduct in each half-cycle.

Estimate the peak load voltage.

**Formula:**

\[
V_{L,peak}=V_m-2V_D
\]

**Solution:**

\[
V_{L,peak}=24-2(0.7)
\]

\[
V_{L,peak}=24-1.4
\]

\[
V_{L,peak}=22.6\,V
\]

**Final Answer:**

\[
\boxed{V_{L,peak}=22.6\,V}
\]

### Example 3: Capacitor Filter Design

**Given:**

- Load current: \(I_L=0.1\,A\).
- AC input frequency: \(f=50\,Hz\).
- Full-wave rectifier.
- Desired peak-to-peak ripple: \(V_{r(pp)}=1\,V\).

Calculate the approximate filter capacitance.

**Formula:**

For a full-wave rectifier:

\[
V_{r(pp)}\approx\frac{I_L}{2fC}
\]

Rearranging:

\[
C\approx\frac{I_L}{2fV_{r(pp)}}
\]

**Solution:**

\[
C=\frac{0.1}{2(50)(1)}
\]

\[
C=\frac{0.1}{100}
\]

\[
C=0.001\,F
\]

Convert to microfarads:

\[
C=1000\,\mu F
\]

**Final Answer:**

\[
\boxed{C\approx1000\,\mu F}
\]

A practical design would also consider capacitor tolerance, voltage rating, ripple-current rating, and the actual load conditions.

## 11. Other Important Diode Applications

### 11.1 Clippers

A clipper circuit removes portions of a waveform above or below a selected voltage level.

Applications include:

- Input protection.
- Waveform shaping.
- Signal amplitude limiting.

### 11.2 Clampers

A clamper shifts a waveform's DC level without ideally changing its peak-to-peak amplitude.

Applications include:

- Signal restoration.
- Voltage-level shifting.
- Pulse-processing circuits.

### 11.3 Diode Detectors

Diodes can extract the envelope of an amplitude-modulated signal.

This is used in simple radio signal detection.

### 11.4 Voltage Multipliers

Diodes and capacitors can be arranged to produce DC voltages greater than the peak AC input voltage.

Voltage multipliers are used in selected high-voltage, low-current applications.

## 12. Practical Design Considerations

When selecting diodes for a rectifier, consider:

1. Maximum forward current.
2. Maximum reverse voltage.
3. Peak inverse voltage (PIV).
4. Forward voltage drop.
5. Reverse recovery time.
6. Power dissipation.
7. Thermal limits.
8. Surge current capability.

Peak inverse voltage is the maximum reverse voltage a diode must withstand during normal circuit operation.

The selected diode must have a suitable voltage rating with an appropriate safety margin.

## 13. Common Examination Traps

1. A rectifier produces pulsating DC, not automatically perfectly smooth DC.
2. A half-wave rectifier uses only one half-cycle.
3. A full-wave rectifier uses both half-cycles.
4. The ripple frequency of a full-wave rectifier is twice the supply frequency.
5. A bridge rectifier has two conducting diodes in its current path during each half-cycle.
6. A centre-tapped full-wave rectifier uses one conducting diode in each half-cycle.
7. A capacitor filter is connected in parallel with the load.
8. Increasing capacitance generally reduces ripple but may increase diode surge current.
9. Ripple factor and rectification efficiency describe different properties.
10. The peak inverse voltage rating must be sufficient to withstand reverse voltage.

## 14. Quiz

### Question 1

A full-wave rectifier is supplied with a 50 Hz sinusoidal input. What is its output ripple frequency before filtering?

- [ ] 25 Hz.
- [ ] 50 Hz.
- [x] 100 Hz.
- [ ] 200 Hz.

> **Explanation:** A full-wave rectifier uses both half-cycles. Therefore, it produces two output pulses for every input cycle. The ripple frequency is \(2f=2(50)=100\,Hz\).

### Question 2

Where is a capacitor connected in a basic capacitor-filter rectifier circuit?

- [ ] In series with the AC source only.
- [x] In parallel with the load.
- [ ] In series with the diode.
- [ ] Across the transformer primary only.

> **Explanation:** The capacitor charges near the rectified voltage peaks and discharges through the load between peaks. Connecting it in parallel with the load smooths the output voltage.

### Question 3

A full-wave rectifier operates at 60 Hz. What is its ripple frequency?

- [ ] 30 Hz.
- [ ] 60 Hz.
- [x] 120 Hz.
- [ ] 240 Hz.

> **Explanation:** The ripple frequency of a full-wave rectifier is twice the AC input frequency. Thus, \(f_r=2(60)=120\,Hz\).