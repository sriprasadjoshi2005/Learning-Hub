---
title: Sinusoidal Alternating Signals and Their Characteristics
level: intermediate
---

# Sinusoidal Alternating Signals and Their Characteristics

## Introduction

Alternating signals are electrical quantities that change magnitude and direction periodically with time. They are fundamental to electrical power systems, communication circuits, signal processing, and electronic equipment.

The most common alternating waveform is the sinusoidal signal. It is widely used because it is naturally produced by rotating electrical machines and can be analysed mathematically using trigonometric functions and phasors.

Understanding sinusoidal signals requires knowledge of amplitude, period, frequency, phase, angular frequency, instantaneous value, peak value, average value, RMS value, and phase relationships.

This lesson develops the mathematical representation of sinusoidal signals, explains their characteristics, introduces basic AC measurements, and prepares the foundation for more advanced AC circuit analysis.

## 1. Introduction to Alternating Signals

An alternating quantity changes direction periodically.

An alternating voltage may become positive, decrease to zero, become negative, and then return to its original value.

Similarly, alternating current changes direction periodically.

A sinusoidal voltage can be represented as:

\[
\boxed{v(t)=V_m\sin(\omega t+\phi)}
\]

Where:
- \(v(t)\) = instantaneous voltage.
- \(V_m\) = maximum or peak voltage.
- \(\omega\) = angular frequency.
- \(t\) = time.
- \(\phi\) = phase angle.

The corresponding current equation is:

\[
\boxed{i(t)=I_m\sin(\omega t+\phi)}
\]

## 2. Sinusoidal Waveform

A sinusoidal waveform consists of a repeating positive and negative variation.

Its important points include:
- Positive peak.
- Negative peak.
- Zero crossings.
- Complete cycle.

The maximum positive value is \(+V_m\).

The maximum negative value is \(-V_m\).

The peak-to-peak voltage is:

\[
\boxed{V_{pp}=2V_m}
\]

For a symmetrical sinusoidal waveform, the positive and negative peak magnitudes are equal.

## 3. Important Characteristics of Sinusoidal Signals

### 3.1 Instantaneous Value

The instantaneous value is the magnitude of a voltage or current at a particular instant.

For example:

\[
v(t)=10\sin(100\pi t)
\]

At a specified time, the voltage can be calculated by substituting that time into the equation.

### 3.2 Peak Value

Peak value is the maximum magnitude reached by a waveform.

It is represented by:
- \(V_m\) for voltage.
- \(I_m\) for current.

### 3.3 Peak-to-Peak Value

Peak-to-peak value is the difference between the maximum positive and maximum negative values.

For a symmetrical sine wave:

\[
V_{pp}=V_m-(-V_m)
\]

\[
\boxed{V_{pp}=2V_m}
\]

### 3.4 Time Period

The time period is the time required for one complete cycle.

It is represented by \(T\).

Its SI unit is the second.

### 3.5 Frequency

Frequency is the number of complete cycles occurring per second.

It is represented by \(f\).

Its SI unit is the hertz (Hz).

\[
\boxed{f=\frac{1}{T}}
\]

And:

\[
\boxed{T=\frac{1}{f}}
\]

A signal with a frequency of 50 Hz completes 50 cycles every second.

## 4. Angular Frequency

Angular frequency represents the rate of change of phase angle with time.

It is represented by \(\omega\).

\[
\boxed{\omega=2\pi f}
\]

Since:

\[
f=\frac{1}{T}
\]

\[
\boxed{\omega=\frac{2\pi}{T}}
\]

The SI unit is radians per second.

One complete cycle corresponds to:

\[
2\pi\text{ radians}=360^\circ
\]

Therefore, angular frequency describes how quickly the waveform progresses through its phase angle.

## 5. Mathematical Representation of a Sinusoidal Signal

A general sinusoidal voltage is:

\[
v(t)=V_m\sin(\omega t+\phi)
\]

Each parameter determines a different characteristic.

| Parameter | Meaning | Effect |
|---|---|---|
| \(V_m\) | Peak amplitude | Determines maximum magnitude |
| \(\omega\) | Angular frequency | Determines how quickly the signal oscillates |
| \(t\) | Time | Determines the observation instant |
| \(\phi\) | Initial phase angle | Determines horizontal waveform position |

### 5.1 Zero Phase

For:

\[
v(t)=V_m\sin(\omega t)
\]

The waveform begins at zero and initially increases in the positive direction.

### 5.2 Positive Phase

For:

\[
v(t)=V_m\sin(\omega t+\phi)
\]

A positive phase angle shifts the waveform to the left relative to the zero-phase sine wave.

### 5.3 Negative Phase

For:

\[
v(t)=V_m\sin(\omega t-\phi)
\]

A negative phase angle shifts the waveform to the right.

## 6. Phase Difference

Phase difference describes the angular displacement between two sinusoidal signals of the same frequency.

Suppose:

\[
v_1(t)=V_{m1}\sin(\omega t)
\]

And:

\[
v_2(t)=V_{m2}\sin(\omega t+\phi)
\]

The phase difference is:

\[
\boxed{\phi}
\]

If \(v_2\) reaches corresponding waveform points earlier, it leads \(v_1\).

If it reaches them later, it lags \(v_1\).

### 6.1 Phase Difference in Degrees and Time

One complete cycle corresponds to 360°.

The time displacement associated with a phase difference is:

\[
\boxed{\Delta t=\frac{\phi}{360^\circ}T}
\]

Where:
- \(\Delta t\) = time displacement.
- \(\phi\) = phase difference in degrees.
- \(T\) = time period.

For radians:

\[
\boxed{\Delta t=\frac{\phi}{2\pi}T}
\]

Here \(\phi\) must be expressed in radians.

## 7. Average Value of a Sinusoidal Signal

The average value is the arithmetic mean of the instantaneous values over a specified interval.

For a symmetrical sine wave over one complete cycle:

\[
\boxed{V_{avg}=0}
\]

This occurs because the positive and negative halves cancel each other.

However, the average value over one half-cycle is non-zero.

For a sine wave:

\[
V_{avg}=\frac{1}{\pi}\int_0^\pi V_m\sin\theta\,d\theta
\]

Integrating:

\[
V_{avg}=\frac{V_m}{\pi}[-\cos\theta]_0^\pi
\]

\[
V_{avg}=\frac{V_m}{\pi}[1-(-1)]
\]

Therefore:

\[
\boxed{V_{avg}=\frac{2V_m}{\pi}}
\]

Approximately:

\[
\boxed{V_{avg}=0.637V_m}
\]

This is the average value over one positive half-cycle.

The average of a full-wave-rectified sine wave is also \(2V_m/\pi\).

## 8. RMS Value

RMS stands for root mean square.

It is the square root of the mean of the squared instantaneous values over one complete cycle.

For voltage:

\[
V_{RMS}=
\sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt}
\]

For a sinusoidal waveform:

\[
v(t)=V_m\sin(\omega t)
\]

Substituting:

\[
V_{RMS}=
\sqrt{\frac{1}{T}\int_0^T V_m^2\sin^2(\omega t)\,dt}
\]

Since the average value of \(\sin^2\) over one complete cycle is \(1/2\):

\[
V_{RMS}=\sqrt{\frac{V_m^2}{2}}
\]

Therefore:

\[
\boxed{V_{RMS}=\frac{V_m}{\sqrt2}}
\]

Similarly:

\[
\boxed{I_{RMS}=\frac{I_m}{\sqrt2}}
\]

Approximately:

\[
V_{RMS}=0.707V_m
\]

\[
I_{RMS}=0.707I_m
\]

### 8.1 Significance of RMS

RMS voltage represents the equivalent DC voltage that produces the same average heating effect in a resistor.

This is why AC supply ratings are generally expressed using RMS values.

For example, a 230 V AC supply refers to approximately 230 V RMS, not 230 V peak.

## 9. Form Factor and Crest Factor

### 9.1 Form Factor

Form factor is the ratio of RMS value to average rectified value.

\[
\boxed{\text{Form factor}=\frac{V_{RMS}}{V_{avg}}}
\]

For a sine wave:

\[
\text{Form factor}
=
\frac{V_m/\sqrt2}{2V_m/\pi}
\]

\[
\boxed{\text{Form factor}\approx1.11}
\]

### 9.2 Crest Factor

Crest factor is the ratio of peak value to RMS value.

\[
\boxed{\text{Crest factor}=\frac{V_m}{V_{RMS}}}
\]

For a sine wave:

\[
\boxed{\text{Crest factor}=\sqrt2\approx1.414}
\]

These quantities are useful when interpreting waveform measurements and instrument specifications.

## 10. AC Voltage and Current Through a Resistor

Consider a pure resistor connected to a sinusoidal voltage source.

\[
v(t)=V_m\sin(\omega t)
\]

Using Ohm's law:

\[
i(t)=\frac{v(t)}{R}
\]

Therefore:

\[
i(t)=\frac{V_m}{R}\sin(\omega t)
\]

Since:

\[
I_m=\frac{V_m}{R}
\]

\[
\boxed{i(t)=I_m\sin(\omega t)}
\]

Voltage and current are in phase in a purely resistive circuit.

They reach their positive peaks, negative peaks, and zero crossings simultaneously.

## 11. Frequency and Phase Relationships

### 11.1 Same Frequency

Two signals can have different amplitudes and phase angles while sharing the same frequency.

### 11.2 Different Frequencies

If two signals have different frequencies, their phase difference generally changes continuously with time.

A fixed phase relationship is maintained only when the frequencies are equal.

### 11.3 Leading and Lagging

A signal that reaches corresponding points earlier is said to lead.

A signal that reaches corresponding points later is said to lag.

This terminology is important in AC circuit analysis, particularly when studying inductors and capacitors.

## 12. Worked Numerical Examples

### Example 1: Determining Frequency and Time Period

**Given:**

A sinusoidal signal completes 100 cycles in 2 seconds.

**Find:** Frequency and time period.

**Solution:**

\[
f=\frac{\text{Number of cycles}}{\text{Time}}
\]

\[
f=\frac{100}{2}
\]

\[
\boxed{f=50\text{ Hz}}
\]

Time period:

\[
T=\frac{1}{f}
\]

\[
T=\frac{1}{50}
\]

\[
\boxed{T=0.02\text{ s}=20\text{ ms}}
\]

### Example 2: Calculating Peak Voltage from RMS Voltage

**Given:**

RMS voltage = 230 V.

**Find:** Peak voltage.

**Formula:**

\[
V_m=\sqrt2V_{RMS}
\]

**Solution:**

\[
V_m=1.414\times230
\]

\[
\boxed{V_m\approx325.2\text{ V}}
\]

Peak-to-peak voltage:

\[
V_{pp}=2V_m
\]

\[
\boxed{V_{pp}\approx650.4\text{ V}}
\]

### Example 3: Determining Instantaneous Voltage

**Given:**

\[
v(t)=100\sin(100\pi t)
\]

Find the instantaneous voltage at:

\[
t=0.005\text{ s}
\]

**Solution:**

Substitute the time:

\[
v=100\sin(100\pi\times0.005)
\]

\[
v=100\sin\left(\frac{\pi}{2}\right)
\]

Since:

\[
\sin\left(\frac{\pi}{2}\right)=1
\]

\[
\boxed{v=100\text{ V}}
\]

### Example 4: Determining Phase Difference

**Given:**

Two signals have a frequency of 50 Hz and a time displacement of 5 ms.

**Find:** Phase difference.

**Solution:**

Time period:

\[
T=\frac{1}{50}=20\text{ ms}
\]

Phase difference:

\[
\phi=\frac{\Delta t}{T}\times360^\circ
\]

\[
\phi=\frac{5}{20}\times360^\circ
\]

\[
\boxed{\phi=90^\circ}
\]

### Example 5: Average and RMS Values

**Given:**

Peak voltage = 100 V.

**Find:** Average value over a positive half-cycle and RMS value.

**Solution:**

Average value:

\[
V_{avg}=\frac{2V_m}{\pi}
\]

\[
V_{avg}=\frac{200}{3.1416}
\]

\[
\boxed{V_{avg}\approx63.66\text{ V}}
\]

RMS value:

\[
V_{RMS}=\frac{100}{\sqrt2}
\]

\[
\boxed{V_{RMS}\approx70.71\text{ V}}
\]

### Example 6: Angular Frequency

**Given:**

Frequency = 60 Hz.

**Find:** Angular frequency.

**Formula:**

\[
\omega=2\pi f
\]

**Solution:**

\[
\omega=2\pi(60)
\]

\[
\boxed{\omega\approx376.99\text{ rad/s}}
\]

## 13. Practical Applications

Sinusoidal signals are used in:

- AC power generation.
- Electrical power transmission.
- Signal generators.
- Audio systems.
- Communication systems.
- Electronic testing equipment.
- AC motors and generators.
- Oscillator circuits.
- Signal-processing systems.

### 13.1 Oscilloscopes

An oscilloscope displays voltage variation with time.

It allows engineers to observe:
- Peak amplitude.
- Frequency.
- Time period.
- Phase difference.
- Distortion.
- Noise.

### 13.2 Function Generators

Function generators produce controlled waveforms such as:
- Sine waves.
- Square waves.
- Triangular waves.
- Pulse waveforms.

These signals are used for circuit testing and measurement.

## 14. Important Comparisons and Observations

| Quantity | Formula | Meaning |
|---|---|---|
| Time period | \(T=1/f\) | Time for one cycle |
| Frequency | \(f=1/T\) | Cycles per second |
| Angular frequency | \(\omega=2\pi f\) | Angular rate |
| Peak-to-peak value | \(V_{pp}=2V_m\) | Total waveform excursion |
| RMS value | \(V_m/\sqrt2\) | Equivalent heating value |
| Half-cycle average | \(2V_m/\pi\) | Average over positive half-cycle |
| Form factor | \(V_{RMS}/V_{avg}\) | RMS-to-average ratio |
| Crest factor | \(V_m/V_{RMS}\) | Peak-to-RMS ratio |

## 15. Common Exam Traps

1. **Confusing RMS and peak voltage:** RMS voltage is approximately 0.707 times the peak value for a sine wave.

2. **Using the wrong average interval:** A complete symmetrical sine-wave cycle has zero average, while its positive half-cycle average is non-zero.

3. **Confusing frequency and angular frequency:** Frequency is measured in hertz; angular frequency is measured in radians per second.

4. **Forgetting the factor of \(2\pi\):** Angular frequency is \(2\pi f\), not simply \(f\).

5. **Reversing phase relationships:** A positive phase term shifts a sine wave to the left relative to a zero-phase reference.

6. **Assuming every AC waveform is sinusoidal:** Alternating signals may also be square, triangular, or otherwise periodic.

7. **Treating 230 V AC as a peak value:** Standard AC supply ratings generally refer to RMS voltage.

8. **Using the sine-wave RMS formula for every waveform:** Other waveform shapes have different RMS-to-peak relationships.

## Quiz

1. A sinusoidal signal has a frequency of 100 Hz. What is its time period?

   - [ ] 100 ms
   - [ ] 20 ms
   - [x] 10 ms
   - [ ] 1 ms

   > The time period is \(T=1/f=1/100=0.01\) seconds, which is 10 ms.

2. A sinusoidal voltage has a peak value of 200 V. What is its RMS value?

   - [ ] 200 V
   - [ ] 100 V
   - [x] Approximately 141.4 V
   - [ ] Approximately 282.8 V

   > For a sine wave, \(V_{RMS}=V_m/\sqrt2=200/1.414\approx141.4\) V.

3. Two sinusoidal signals of equal frequency have a phase difference of 180°. What does this indicate?

   - [ ] They are always identical.
   - [ ] They have a phase difference of 90°.
   - [x] Their corresponding instantaneous values are opposite in sign when their amplitudes are equal.
   - [ ] One signal has twice the frequency of the other.

   > A 180° phase difference represents half a cycle of displacement. For equal amplitudes, one signal is the negative of the other at every corresponding instant.