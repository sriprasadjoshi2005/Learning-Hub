---
title: Communication Systems and Signal Transmission
level: advanced
---

Communication systems transfer information from one location to another using electrical, electromagnetic or optical signals.

Modern communication includes radio broadcasting, mobile networks, satellite communication, Wi-Fi, Bluetooth, fibre-optic networks and digital data transmission.

Physics explains the propagation, modulation, reception and processing of these signals.

## 1. Basic Communication System

A communication system generally consists of:

1. Information source.
2. Input transducer.
3. Transmitter.
4. Communication channel.
5. Receiver.
6. Output transducer.
7. Destination.

The information source generates the message.

The transmitter processes and prepares the signal for transmission.

The communication channel carries the signal.

The receiver extracts the original information.

## 2. Signals

A signal is a physical quantity that varies with time or space and carries information.

Examples include:
- Electrical voltage.
- Electrical current.
- Electromagnetic waves.
- Optical intensity.
- Acoustic pressure.

Signals can be classified as:

**Analog signals:**

Vary continuously over a range of values.

**Digital signals:**

Represent information using discrete symbols, commonly binary digits.

## 3. Transducers

A transducer converts one form of energy or physical quantity into another.

Examples:

**Microphone:**

Converts sound pressure variations into electrical signals.

**Speaker:**

Converts electrical signals into sound.

**Photodetector:**

Converts incident light into an electrical signal.

**Antenna:**

Converts electrical signals into electromagnetic radiation during transmission and electromagnetic waves into electrical signals during reception.

## 4. Need for Modulation

A low-frequency information signal is often unsuitable for direct radiation over large distances using a practical antenna.

Modulation solves several problems:
- Allows efficient radiation using practical antenna dimensions.
- Enables multiple signals to share a communication medium.
- Helps separate different communication channels.
- Allows communication over suitable frequency bands.

Modulation is the process of varying one or more properties of a high-frequency carrier according to the information signal.

## 5. Carrier Waves

A carrier wave is a high-frequency signal used to carry information.

A sinusoidal carrier may be represented as:

\[
c(t)=A_c\sin(2\pi f_ct+\phi)
\]

Where:
- Ac = carrier amplitude.
- fc = carrier frequency.
- phi = carrier phase.

The information signal modifies the carrier according to the selected modulation method.

## 6. Amplitude Modulation

In amplitude modulation (AM), the amplitude of the carrier changes according to the message signal.

The carrier frequency and phase remain constant in the ideal basic AM model.

For a single-tone message signal:

\[
s(t)=A_c[1+m\cos(2\pi f_mt)]\cos(2\pi f_ct)
\]

Where:
- m = modulation index.
- fm = message frequency.
- fc = carrier frequency.

For conventional AM without overmodulation:

\[
0\leq m\leq1
\]

The modulation index is:

\[
m=\frac{A_m}{A_c}
\]

Here, Am represents the peak amplitude of the modulating signal under the conventional normalised model.

## 7. Frequency Spectrum of AM

A conventional AM signal contains:
- Carrier frequency fc.
- Upper sideband fc + fm.
- Lower sideband fc - fm.

For a single-tone message:

\[
f_{\mathrm{USB}}=f_c+f_m
\]

\[
f_{\mathrm{LSB}}=f_c-f_m
\]

The bandwidth is:

\[
BW=2f_m
\]

For a message containing frequencies up to a maximum fm(max):

\[
BW=2f_{m(\max)}
\]

## 8. Frequency Modulation

In frequency modulation (FM), the instantaneous frequency of the carrier varies according to the message signal.

The carrier amplitude ideally remains constant.

FM is widely used in radio broadcasting because it can provide better resistance to certain forms of amplitude noise than conventional AM.

The modulation index for single-tone FM is:

\[
\beta=\frac{\Delta f}{f_m}
\]

Where:
- Delta f = peak frequency deviation.
- fm = modulating frequency.

Carson's rule gives an approximate transmission bandwidth:

\[
BW\approx2(\Delta f+f_m)
\]

## 9. Phase Modulation

In phase modulation (PM), the instantaneous phase of the carrier varies according to the message signal.

FM and PM are both forms of angle modulation.

They differ in the specific carrier parameter directly controlled by the message.

## 10. Digital Modulation

Digital communication represents information using discrete symbols.

Important methods include:

**Amplitude Shift Keying (ASK):**

Information is represented through changes in carrier amplitude.

**Frequency Shift Keying (FSK):**

Information is represented through different carrier frequencies.

**Phase Shift Keying (PSK):**

Information is represented through different carrier phases.

**Quadrature Amplitude Modulation (QAM):**

Information is represented using combinations of amplitude and phase.

Higher-order modulation schemes can carry more bits per symbol but generally require better signal quality for reliable detection.

## 11. Sampling and the Nyquist Criterion

Sampling converts a continuous-time signal into a sequence of discrete-time values.

For a band-limited signal with maximum frequency fm, the ideal Nyquist sampling condition is:

\[
f_s>2f_m
\]

Where fs is the sampling frequency.

The minimum theoretical sampling rate is twice the highest signal frequency.

Sampling below this limit can produce aliasing.

An anti-aliasing low-pass filter is commonly used before sampling to limit unwanted high-frequency components.

## 12. Quantisation

Quantisation maps sampled signal amplitudes to a finite set of discrete levels.

An analogue-to-digital converter (ADC) performs sampling and quantisation, along with binary encoding.

For an ideal uniform n-bit ADC:

\[
L=2^n
\]

Where L is the number of quantisation levels.

Increasing the number of bits generally improves amplitude resolution.

The ideal quantisation step size for a full-scale range Vrange is approximately:

\[
\Delta=\frac{V_{\mathrm{range}}}{2^n}
\]

## 13. Noise and Signal-to-Noise Ratio

Noise is unwanted disturbance that affects a communication signal.

Sources include:
- Thermal noise.
- Electronic device noise.
- Atmospheric interference.
- Electromagnetic interference.
- Quantisation noise.

Signal-to-noise ratio is:

\[
SNR=\frac{P_s}{P_n}
\]

Where:
- Ps = signal power.
- Pn = noise power.

In decibels:

\[
SNR_{\mathrm{dB}}=10\log_{10}\left(\frac{P_s}{P_n}\right)
\]

A larger SNR generally indicates a cleaner signal.

## 14. Electromagnetic Communication Channels

Different communication systems use different frequency ranges and propagation methods.

Examples include:
- Radio communication.
- Microwave communication.
- Satellite communication.
- Infrared communication.
- Visible-light communication.

Radio waves can propagate through space without a material medium.

Optical fibre guides light through a suitable transparent core.

## 15. Antennas

An antenna is a device that transmits or receives electromagnetic waves.

Important antenna properties include:
- Resonant frequency.
- Radiation pattern.
- Gain.
- Directivity.
- Polarisation.
- Bandwidth.
- Impedance matching.

A half-wave dipole has a total length approximately equal to half the wavelength in an ideal simplified model.

\[
L\approx\frac{\lambda}{2}
\]

Practical antenna dimensions depend on geometry, surroundings and design.

## 16. Worked Numerical Example

An AM transmitter uses a carrier frequency of 1 MHz and a maximum message frequency of 5 kHz.

Calculate its approximate bandwidth.

For conventional AM:

\[
BW=2f_{m(\max)}
\]

\[
BW=2(5\text{ kHz})
\]

\[
\boxed{BW=10\text{ kHz}}
\]

The sidebands extend approximately 5 kHz above and below the carrier frequency.

## Common Exam Traps

- Modulation transfers information onto a carrier.
- AM changes carrier amplitude.
- FM changes instantaneous frequency.
- PM changes instantaneous phase.
- Conventional single-tone AM has two sidebands.
- AM bandwidth is twice the highest modulating frequency.
- The Nyquist criterion prevents ideal band-limited signals from being undersampled.
- Higher SNR generally indicates better signal quality.
- An antenna transmits and receives electromagnetic waves.

## Quiz

1. In amplitude modulation, the property of the carrier that is varied is:

- [ ] Frequency
- [ ] Phase
- [x] Amplitude
- [ ] Speed of light

> AM changes the carrier amplitude according to the information signal.

2. A signal contains frequencies up to 4 kHz. What is the minimum theoretical Nyquist sampling rate?

- [ ] 2 kHz
- [ ] 4 kHz
- [x] 8 kHz
- [ ] 16 kHz

> The Nyquist sampling condition requires a sampling rate greater than twice the highest signal frequency. The theoretical boundary is 8 kHz.

3. If signal power is 100 mW and noise power is 1 mW, the SNR in decibels is:

- [ ] 10 dB
- [x] 20 dB
- [ ] 40 dB
- [ ] 100 dB

> SNR = 100/1 = 100. In decibels, 10 log10(100) = 20 dB.