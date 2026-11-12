---
title: Active Filters and Signal Conditioning
level: intermediate
---

# Active Filters and Signal Conditioning

Electronic systems frequently receive signals containing unwanted frequency components, noise, interference, or unsuitable voltage levels.

Signal conditioning modifies these signals so that they can be measured, processed, transmitted, or used by another circuit.

An important part of signal conditioning is filtering.

Filters selectively allow certain frequency components to pass while attenuating others.

Active filters use active components, commonly operational amplifiers, together with resistors and capacitors.

This lesson introduces filter classifications, frequency response, cutoff frequency, first-order RC filters, active filter configurations, and practical signal-conditioning techniques.

## 1. Introduction to Electronic Filters

An electronic filter is a circuit that modifies a signal according to its frequency.

A filter may:

- Allow low frequencies to pass.
- Allow high frequencies to pass.
- Allow a selected frequency band to pass.
- Reject a selected frequency band.

Filters are used in audio systems, communication circuits, measurement equipment, medical electronics, and control systems.

## 2. Passive and Active Filters

### 2.1 Passive Filters

Passive filters use components such as:

- Resistors.
- Capacitors.
- Inductors.

They do not require an active amplification device.

Advantages:

- Simple construction.
- No amplifier supply required.
- Useful in many high-frequency and power applications.

Limitations:

- Cannot provide power gain.
- May be affected by load impedance.
- Inductors can be bulky at low frequencies.

### 2.2 Active Filters

Active filters use active devices such as op-amps together with resistors and capacitors.

Advantages:

- Can provide voltage gain.
- Often avoid inductors.
- Can provide high input impedance.
- Can provide low output impedance.
- Allow convenient adjustment of filter characteristics.

Limitations:

- Require power supplies.
- Have finite bandwidth.
- Are limited by slew rate and output swing.
- May introduce noise and distortion.

## 3. Frequency Response

Frequency response describes how a circuit's gain changes with input frequency.

For a filter:

\[
A_v(f)=\frac{V_{out}(f)}{V_{in}(f)}
\]

The gain may be expressed as a magnitude or in decibels.

\[
A_{v(dB)}=20\log_{10}|A_v|
\]

A frequency-response graph commonly plots gain against frequency.

The horizontal axis may use a logarithmic frequency scale.

## 4. Cutoff Frequency

The cutoff frequency separates the passband from the region where significant attenuation begins.

For a first-order filter, the cutoff frequency is commonly defined at the point where output voltage magnitude falls to:

\[
\frac{1}{\sqrt{2}}\approx0.707
\]

of its passband value.

The corresponding gain reduction is approximately:

\[
-3\,dB
\]

For a simple RC filter:

\[
\boxed{f_c=\frac{1}{2\pi RC}}
\]

Where:

- \(f_c\) = cutoff frequency in hertz.
- \(R\) = resistance in ohms.
- \(C\) = capacitance in farads.

## 5. Low-Pass Filter

A low-pass filter allows low-frequency signals to pass and attenuates high-frequency signals.

### 5.1 RC Low-Pass Filter

A basic passive RC low-pass filter consists of:

- A resistor in series with the input.
- A capacitor connected from the output node to ground.
- Output measured across the capacitor.

At low frequencies, capacitor reactance is relatively high.

At high frequencies, capacitor reactance becomes lower, causing more of the signal to be diverted to ground.

### 5.2 Transfer Function

The transfer function is:

\[
H(s)=\frac{V_o(s)}{V_i(s)}
\]

For an ideal first-order RC low-pass filter:

\[
\boxed{H(s)=\frac{1}{1+sRC}}
\]

Its cutoff frequency is:

\[
f_c=\frac{1}{2\pi RC}
\]

### 5.3 Applications

- Removing high-frequency noise.
- Smoothing sensor signals.
- Audio tone control.
- Anti-aliasing before analog-to-digital conversion.

## 6. High-Pass Filter

A high-pass filter allows high-frequency signals to pass while attenuating low-frequency signals.

### 6.1 RC High-Pass Filter

A basic RC high-pass filter consists of:

- A capacitor in series with the input.
- A resistor connected from the output node to ground.
- Output measured across the resistor.

At low frequencies, capacitor reactance is high, reducing the output.

At high frequencies, capacitor reactance becomes lower, allowing more signal to reach the output.

### 6.2 Transfer Function

For an ideal first-order RC high-pass filter:

\[
\boxed{H(s)=\frac{sRC}{1+sRC}}
\]

Its cutoff frequency is:

\[
f_c=\frac{1}{2\pi RC}
\]

### 6.3 Applications

- Removing DC components.
- Reducing low-frequency drift.
- Audio coupling.
- Detecting rapidly changing signals.

## 7. Band-Pass Filter

A band-pass filter allows a selected range of frequencies to pass.

Frequencies below the lower cutoff and above the upper cutoff are attenuated.

It can be constructed by combining high-pass and low-pass filtering sections.

### 7.1 Important Frequencies

A band-pass filter has:

- Lower cutoff frequency \(f_L\).
- Upper cutoff frequency \(f_H\).

Its bandwidth is:

\[
\boxed{BW=f_H-f_L}
\]

The centre frequency for a common second-order band-pass response is:

\[
\boxed{f_0=\sqrt{f_Lf_H}}
\]

The quality factor is:

\[
\boxed{Q=\frac{f_0}{BW}}
\]

A higher Q generally indicates a narrower passband.

## 8. Band-Stop Filter

A band-stop filter attenuates a selected range of frequencies while allowing frequencies below and above that range to pass.

It is also called a band-reject filter.

A narrow band-stop filter is commonly called a notch filter.

### 8.1 Applications

- Rejecting 50 Hz or 60 Hz power-line interference.
- Removing unwanted tones.
- Reducing narrowband interference in measurement systems.

## 9. Active First-Order Filters

An op-amp can be combined with an RC network to form an active filter.

A common arrangement uses an RC frequency-selective network with a non-inverting amplifier.

The amplifier can provide gain while buffering the filter from load effects.

For a first-order active low-pass or high-pass filter, the cutoff frequency is still determined by the relevant RC time constant in the basic configuration.

The exact transfer function and gain depend on the circuit topology.

## 10. Filter Order

Filter order is related to the number of independent energy-storage elements or poles in the transfer function.

A first-order filter has one pole.

A second-order filter has two poles.

Higher-order filters generally provide steeper attenuation beyond the cutoff region.

For idealized Butterworth responses, the asymptotic attenuation slope is approximately:

- First order: \(20\,dB/decade\).
- Second order: \(40\,dB/decade\).
- Third order: \(60\,dB/decade\).
- Fourth order: \(80\,dB/decade\).

A decade represents a tenfold change in frequency.

## 11. Butterworth, Chebyshev and Bessel Responses

Different filter designs trade off passband flatness, transition sharpness, and phase behaviour.

### 11.1 Butterworth Filter

Characteristics:

- Maximally flat magnitude response in the passband.
- Smooth frequency response.
- No passband ripple.

### 11.2 Chebyshev Filter

Characteristics:

- Sharper transition than a Butterworth filter of the same order in common designs.
- Allows ripple in the passband or stopband, depending on type.

### 11.3 Bessel Filter

Characteristics:

- Good phase and group-delay behaviour.
- Preserves waveform shape better in many time-domain applications.
- Has a less sharp magnitude transition than comparable Butterworth or Chebyshev designs.

## 12. Signal Conditioning

Signal conditioning prepares a signal for a particular electronic system.

Common operations include:

### 12.1 Amplification

A weak sensor signal may need amplification before measurement.

### 12.2 Attenuation

A high-voltage signal may need to be reduced to a safe input range.

### 12.3 Filtering

Unwanted frequency components and noise may be removed.

### 12.4 Level Shifting

A signal may be shifted to a suitable DC reference level.

### 12.5 Isolation

Electrical isolation may be required to protect equipment and prevent unwanted ground-current paths.

### 12.6 Impedance Matching and Buffering

A buffer can prevent one circuit stage from loading another.

### 12.7 Linearization

Some sensors have non-linear output characteristics. Signal-conditioning circuits can compensate for these characteristics.

## 13. Anti-Aliasing Filters

An analog signal is often filtered before it is sampled by an analog-to-digital converter.

This prevents high-frequency components from folding into the sampled frequency range.

Such a filter is called an anti-aliasing filter.

The sampling theorem requires:

\[
f_s>2f_{max}
\]

Where:

- \(f_s\) = sampling frequency.
- \(f_{max}\) = highest frequency component to be preserved.

A practical anti-aliasing filter requires a transition band and suitable attenuation beyond the desired signal bandwidth.

## 14. Worked Numerical Examples

### Example 1: RC Low-Pass Cutoff Frequency

**Given:**

- \(R=10\,k\Omega\).
- \(C=0.01\,\mu F\).

Calculate the cutoff frequency.

**Formula:**

\[
f_c=\frac{1}{2\pi RC}
\]

**Solution:**

Convert capacitance:

\[
C=0.01\times10^{-6}\,F
\]

\[
C=10^{-8}\,F
\]

Substitute:

\[
f_c=\frac{1}{2\pi(10000)(10^{-8})}
\]

\[
f_c=\frac{1}{2\pi(10^{-4})}
\]

\[
f_c\approx1591.5\,Hz
\]

**Final Answer:**

\[
\boxed{f_c\approx1.59\,kHz}
\]

### Example 2: Band-Pass Filter Bandwidth

**Given:**

- Lower cutoff frequency: \(f_L=500\,Hz\).
- Upper cutoff frequency: \(f_H=2500\,Hz\).

Calculate bandwidth and centre frequency.

**Formula:**

\[
BW=f_H-f_L
\]

\[
f_0=\sqrt{f_Lf_H}
\]

**Solution:**

Bandwidth:

\[
BW=2500-500
\]

\[
BW=2000\,Hz
\]

Centre frequency:

\[
f_0=\sqrt{500\times2500}
\]

\[
f_0=\sqrt{1250000}
\]

\[
f_0\approx1118.0\,Hz
\]

**Final Answer:**

\[
\boxed{BW=2\,kHz}
\]

\[
\boxed{f_0\approx1.118\,kHz}
\]

### Example 3: Sampling Frequency

**Given:**

- Highest signal frequency: \(f_{max}=4\,kHz\).

Calculate the minimum theoretical sampling frequency.

**Formula:**

\[
f_s>2f_{max}
\]

**Solution:**

\[
f_s>2(4\,kHz)
\]

\[
f_s>8\,kHz
\]

**Final Answer:**

\[
\boxed{f_s>8\,kHz}
\]

In practice, a higher sampling frequency and an appropriate anti-aliasing filter are used.

## 15. Practical Applications

### 15.1 Audio Systems

Low-pass, high-pass, and band-pass filters control the frequency content of audio signals.

### 15.2 Sensor Interfaces

Filtering reduces noise in signals from temperature, pressure, light, and other sensors.

### 15.3 Communication Systems

Filters select desired frequency bands and suppress unwanted interference.

### 15.4 Data Acquisition

Signal conditioning prepares analog signals for accurate conversion into digital data.

### 15.5 Biomedical Electronics

Filters remove unwanted interference from physiological measurement signals.

## 16. Common Examination Traps

1. A low-pass filter passes low frequencies and attenuates high frequencies.
2. A high-pass filter passes high frequencies and attenuates low frequencies.
3. A band-pass filter passes a selected frequency range.
4. A band-stop filter rejects a selected frequency range.
5. The first-order RC cutoff frequency is \(1/(2\pi RC)\).
6. At the -3 dB point, voltage magnitude is approximately 0.707 of its passband value.
7. Bandwidth is \(f_H-f_L\).
8. The centre frequency of a common band-pass response is \(\sqrt{f_Lf_H}\).
9. Higher-order filters generally provide steeper attenuation.
10. Butterworth filters have a maximally flat magnitude response.
11. Bessel filters are valued for their phase and group-delay behaviour.
12. Anti-aliasing filters are placed before analog-to-digital conversion.
13. Sampling above the Nyquist limit alone does not eliminate aliasing if unwanted high-frequency components are present.
14. Active filters require suitable power supplies and have practical bandwidth limits.

## 17. Quiz

### Question 1

Which filter allows low frequencies to pass while attenuating high frequencies?

- [x] Low-pass filter.
- [ ] High-pass filter.
- [ ] Band-stop filter.
- [ ] Notch filter.

> **Explanation:** A low-pass filter passes frequencies below its cutoff region and attenuates frequencies above it.

### Question 2

An RC filter has \(R=10\,k\Omega\) and \(C=10\,nF\). What is its approximate cutoff frequency?

- [ ] 159 Hz.
- [x] 1.59 kHz.
- [ ] 15.9 kHz.
- [ ] 159 kHz.

> **Explanation:** \(f_c=1/(2\pi RC)\). Substituting \(R=10000\,\Omega\) and \(C=10\times10^{-9}\,F\) gives approximately \(1591.5\,Hz\).

### Question 3

What is the primary purpose of an anti-aliasing filter?

- [ ] Increase the ADC's resolution.
- [ ] Convert an analog signal into a digital signal.
- [x] Attenuate unwanted high-frequency components before sampling.
- [ ] Increase the DC supply voltage.

> **Explanation:** An anti-aliasing filter reduces frequency components that could otherwise fold into the sampled frequency range and distort the digital representation.