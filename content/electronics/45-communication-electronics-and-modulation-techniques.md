---
title: Communication Electronics and Modulation Techniques
level: advanced
---

# Communication Electronics and Modulation Techniques

Communication electronics deals with the transmission and reception of information using electrical and electromagnetic signals.

Communication systems allow information to travel between distant locations through wired or wireless channels.

Examples include radio broadcasting, television, mobile networks, satellite communication, Wi-Fi, Bluetooth, and optical-fibre communication.

A communication system must convert information into a suitable signal, transmit it through a channel, and recover the original information at the receiver.

This lesson introduces communication-system components, signal types, modulation, amplitude modulation, frequency modulation, phase modulation, digital modulation, multiplexing, noise, and communication performance.

## 1. Introduction to Communication Systems

A communication system transfers information from a source to a destination.

A basic communication system contains:

1. Information source.
2. Input transducer.
3. Transmitter.
4. Communication channel.
5. Receiver.
6. Output transducer.
7. Destination.

### 1.1 Information Source

The source produces the information to be transmitted.

Examples include:

- Human speech.
- Music.
- Video.
- Sensor measurements.
- Computer data.

### 1.2 Transmitter

The transmitter prepares the information for transmission.

Its functions may include:

- Signal conditioning.
- Modulation.
- Frequency conversion.
- Amplification.
- Filtering.

### 1.3 Communication Channel

The channel provides the path through which the signal travels.

Examples:

- Copper cables.
- Coaxial cables.
- Optical fibres.
- Free space.

### 1.4 Receiver

The receiver processes the incoming signal to recover the transmitted information.

Its functions may include:

- Amplification.
- Filtering.
- Demodulation.
- Decoding.
- Signal reconstruction.

## 2. Types of Communication Systems

### 2.1 Wired Communication

Wired communication uses a physical transmission medium.

Examples include:

- Twisted-pair cables.
- Coaxial cables.
- Optical fibres.

Advantages may include controlled transmission paths and reduced exposure to some forms of wireless interference.

### 2.2 Wireless Communication

Wireless communication uses electromagnetic waves to transmit information without a physical signal cable between communicating devices.

Examples include:

- Radio broadcasting.
- Mobile communication.
- Wi-Fi.
- Bluetooth.
- Satellite links.

## 3. Communication Signals

A communication system may transmit analog or digital information.

### 3.1 Analog Signals

An analog signal varies continuously with time.

Examples include:

- Microphone output.
- Traditional analog radio signals.
- Continuous sensor signals.

### 3.2 Digital Signals

Digital signals represent information using discrete symbols.

Binary digital systems commonly use two symbols:

\[
0,\quad1
\]

Digital communication systems may provide advantages such as reliable regeneration, error detection, and efficient data processing.

## 4. Carrier Signals

A carrier is a signal used to transport information through a communication channel.

A sinusoidal carrier can be represented as:

\[
c(t)=A_c\cos(2\pi f_ct+\phi_c)
\]

Where:

- \(A_c\) = carrier amplitude.
- \(f_c\) = carrier frequency.
- \(\phi_c\) = carrier phase.

The information signal modifies one or more properties of the carrier during modulation.

## 5. Modulation

Modulation is the process of varying a carrier signal according to the information signal.

It is used to make signals suitable for transmission through a communication channel.

Modulation can:

- Allow practical antenna sizes.
- Enable frequency allocation.
- Support multiple simultaneous transmissions.
- Improve transmission suitability.
- Move information into a suitable frequency band.

The three fundamental analog modulation techniques are:

1. Amplitude modulation.
2. Frequency modulation.
3. Phase modulation.

## 6. Amplitude Modulation

Amplitude Modulation (AM) varies the amplitude of the carrier according to the message signal.

The carrier frequency and phase remain constant in ideal conventional AM.

For a single-tone message, the AM signal can be expressed as:

\[
\boxed{
s(t)=A_c[1+m\cos(2\pi f_mt)]\cos(2\pi f_ct)
}
\]

Where:

- \(A_c\) = carrier amplitude.
- \(f_c\) = carrier frequency.
- \(f_m\) = message frequency.
- \(m\) = modulation index.

### 6.1 Modulation Index

The modulation index measures the extent of amplitude variation.

\[
\boxed{m=\frac{A_m}{A_c}}
\]

For conventional AM:

- \(m<1\): under-modulation.
- \(m=1\): 100% modulation.
- \(m>1\): over-modulation.

Over-modulation causes envelope distortion in conventional envelope detection.

### 6.2 AM Bandwidth

For a single-tone message signal:

\[
\boxed{BW=2f_m}
\]

The AM spectrum contains:

- Carrier frequency \(f_c\).
- Lower sideband \(f_c-f_m\).
- Upper sideband \(f_c+f_m\).

### 6.3 Advantages

- Relatively simple transmitter and receiver design.
- Easy envelope detection.
- Suitable for some broadcast applications.

### 6.4 Disadvantages

- More susceptible to amplitude noise.
- Conventional AM transmits significant carrier power.
- Power efficiency is limited.

## 7. Frequency Modulation

Frequency Modulation (FM) varies the instantaneous frequency of the carrier according to the message signal.

The carrier amplitude remains constant in ideal FM.

The modulation index is:

\[
\boxed{\beta=\frac{\Delta f}{f_m}}
\]

Where:

- \(\Delta f\) = peak frequency deviation.
- \(f_m\) = message frequency.

### 7.1 FM Characteristics

- Better resistance to amplitude noise than conventional AM.
- Constant-envelope transmission.
- Potentially wider bandwidth.
- Requires suitable modulation and demodulation circuits.

### 7.2 Carson's Rule

An approximate estimate of FM bandwidth is given by Carson's rule:

\[
\boxed{BW\approx2(\Delta f+f_m)}
\]

This estimate is widely used for practical FM systems.

## 8. Phase Modulation

Phase Modulation (PM) varies the instantaneous phase of the carrier according to the information signal.

The carrier amplitude remains constant in ideal PM.

For a sinusoidal message, the phase deviation is related to the amplitude of the message signal.

PM is closely related to FM because changes in phase over time correspond to instantaneous frequency changes.

Both are forms of angle modulation.

## 9. AM, FM and PM Comparison

| Property | AM | FM | PM |
|---|---|---|---|
| Carrier property varied | Amplitude | Frequency | Phase |
| Ideal carrier amplitude | Varies | Constant | Constant |
| Noise behaviour | More sensitive to amplitude noise | Better rejection of amplitude noise | Depends on phase disturbance |
| Bandwidth | Relatively narrow for conventional AM | Depends on deviation and message frequency | Depends on modulation and message characteristics |
| Main applications | AM broadcasting | FM broadcasting and radio links | Communication and digital modulation systems |

## 10. Digital Modulation

Digital modulation represents digital information by changing a carrier's properties.

Important techniques include:

### 10.1 Amplitude Shift Keying

Amplitude Shift Keying (ASK) represents digital symbols using different carrier amplitudes.

A simple binary ASK system may use:

- One amplitude for binary 1.
- Another amplitude, possibly zero, for binary 0.

### 10.2 Frequency Shift Keying

Frequency Shift Keying (FSK) represents digital symbols using different carrier frequencies.

For binary FSK:

- One frequency represents binary 0.
- Another frequency represents binary 1.

### 10.3 Phase Shift Keying

Phase Shift Keying (PSK) represents digital symbols using different carrier phases.

Binary PSK uses two phases separated by 180°.

### 10.4 Quadrature Amplitude Modulation

Quadrature Amplitude Modulation (QAM) uses combinations of amplitude and phase variations.

It can represent multiple bits per transmitted symbol.

Higher-order QAM increases the number of possible symbols but generally requires better signal quality for reliable detection.

## 11. Multiplexing

Multiplexing allows multiple information signals to share a common communication channel.

### 11.1 Frequency Division Multiplexing

Frequency Division Multiplexing (FDM) assigns different frequency bands to different signals.

### 11.2 Time Division Multiplexing

Time Division Multiplexing (TDM) assigns different time slots to different signals.

### 11.3 Wavelength Division Multiplexing

Wavelength Division Multiplexing (WDM) transmits multiple optical signals using different wavelengths through an optical fibre.

## 12. Noise and Interference

Noise is an unwanted electrical or electromagnetic disturbance that affects a communication signal.

Common noise sources include:

- Thermal noise.
- Shot noise.
- Atmospheric noise.
- Switching noise.
- Electromagnetic interference.

Noise may reduce the quality and reliability of received information.

### 12.1 Signal-to-Noise Ratio

Signal-to-Noise Ratio (SNR) compares signal power with noise power.

\[
\boxed{SNR=\frac{P_s}{P_n}}
\]

In decibels:

\[
\boxed{SNR_{dB}=10\log_{10}\left(\frac{P_s}{P_n}\right)}
\]

A larger SNR generally indicates a cleaner signal relative to noise.

## 13. Communication Bandwidth

Bandwidth describes the range of frequencies occupied by a signal or allocated to a communication channel.

For a frequency range:

\[
\boxed{BW=f_{upper}-f_{lower}}
\]

Bandwidth is an important factor in determining communication capacity.

The maximum theoretical data rate of an ideal band-limited channel with additive white Gaussian noise is described by Shannon's capacity theorem:

\[
\boxed{C=B\log_2(1+SNR)}
\]

Where:

- \(C\) = channel capacity in bits per second.
- \(B\) = bandwidth in hertz.
- \(SNR\) = linear signal-to-noise ratio.

## 14. Worked Numerical Examples

### Example 1: AM Modulation Index

**Given:**

A carrier has amplitude:

\[
A_c=10\,V
\]

The message amplitude is:

\[
A_m=6\,V
\]

Calculate the modulation index and percentage modulation.

**Formula:**

\[
m=\frac{A_m}{A_c}
\]

**Solution:**

\[
m=\frac{6}{10}
\]

\[
m=0.6
\]

Percentage modulation:

\[
0.6\times100=60\%
\]

**Final Answer:**

\[
\boxed{m=0.6}
\]

\[
\boxed{60\%\text{ modulation}}
\]

### Example 2: FM Bandwidth

**Given:**

An FM signal has:

\[
\Delta f=75\,kHz
\]

\[
f_m=15\,kHz
\]

Calculate its approximate bandwidth using Carson's rule.

**Formula:**

\[
BW\approx2(\Delta f+f_m)
\]

**Solution:**

\[
BW\approx2(75+15)
\]

\[
BW\approx180\,kHz
\]

**Final Answer:**

\[
\boxed{BW\approx180\,kHz}
\]

### Example 3: Signal-to-Noise Ratio

**Given:**

Signal power:

\[
P_s=100\,mW
\]

Noise power:

\[
P_n=1\,mW
\]

Calculate the SNR in decibels.

**Formula:**

\[
SNR_{dB}=10\log_{10}\left(\frac{P_s}{P_n}\right)
\]

**Solution:**

\[
SNR_{dB}=10\log_{10}\left(\frac{100}{1}\right)
\]

\[
SNR_{dB}=10\log_{10}(100)
\]

\[
SNR_{dB}=10(2)
\]

\[
SNR_{dB}=20\,dB
\]

**Final Answer:**

\[
\boxed{SNR=20\,dB}
\]

### Example 4: Shannon Channel Capacity

**Given:**

A communication channel has:

\[
B=1\,MHz
\]

\[
SNR=15
\]

Calculate the theoretical channel capacity.

**Formula:**

\[
C=B\log_2(1+SNR)
\]

**Solution:**

\[
C=10^6\log_2(16)
\]

Since:

\[
\log_2(16)=4
\]

Therefore:

\[
C=4\times10^6
\]

**Final Answer:**

\[
\boxed{C=4\,Mbps}
\]

## 15. Applications

Communication electronics is used in:

- Radio broadcasting.
- Television transmission.
- Mobile communication.
- Satellite communication.
- Wi-Fi and Bluetooth.
- Optical-fibre networks.
- Radar systems.
- Industrial telemetry.

## 16. Common Examination Traps

1. Modulation changes a carrier according to an information signal.
2. AM varies carrier amplitude.
3. FM varies instantaneous carrier frequency.
4. PM varies carrier phase.
5. Conventional AM can be distorted by over-modulation.
6. The conventional AM bandwidth for a single-tone message is twice the message frequency.
7. Carson's rule estimates practical FM bandwidth.
8. ASK changes amplitude.
9. FSK changes frequency.
10. PSK changes phase.
11. QAM combines amplitude and phase variations.
12. FDM separates signals by frequency.
13. TDM separates signals by time.
14. WDM separates optical channels by wavelength.
15. SNR is a ratio of signal power to noise power.
16. A larger SNR generally indicates better signal quality.
17. Shannon's capacity equation uses linear SNR, not SNR in decibels.
18. Channel bandwidth is not automatically equal to the data rate.

## Quiz

1. Which parameter is varied in conventional amplitude modulation?

   - [x] Carrier amplitude.
   - [ ] Carrier frequency.
   - [ ] Carrier phase only.
   - [ ] Channel resistance.

   > Amplitude modulation varies the carrier amplitude according to the information signal. The ideal carrier frequency and phase remain unchanged in conventional AM.

2. An FM signal has a peak frequency deviation of 50 kHz and a maximum message frequency of 10 kHz. What is its approximate bandwidth using Carson's rule?

   - [ ] 50 kHz.
   - [ ] 100 kHz.
   - [x] 120 kHz.
   - [ ] 200 kHz.

   > Carson's rule gives \(BW\approx2(\Delta f+f_m)=2(50+10)=120\) kHz.

3. Which multiplexing technique assigns separate time slots to different signals?

   - [ ] FDM.
   - [x] TDM.
   - [ ] WDM.
   - [ ] AM.

   > Time Division Multiplexing allocates different time intervals to separate information streams, allowing them to share a common communication channel.