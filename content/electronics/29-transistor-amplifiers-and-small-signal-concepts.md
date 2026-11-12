---
title: Transistor Amplifiers and Small-Signal Concepts
level: advanced
---

# Transistor Amplifiers and Small-Signal Concepts

A transistor amplifier is an electronic circuit that uses a transistor to increase the amplitude of an electrical signal.

Transistor amplifiers are used in audio systems, communication equipment, sensor interfaces, instrumentation, radio receivers, and many other electronic applications.

A transistor can amplify a signal when it is correctly biased in its forward-active region. The DC bias establishes the operating point, while the AC input causes small variations around that operating point.

This lesson introduces amplifier operation, voltage and current gain, coupling and bypass capacitors, small-signal models, hybrid-pi concepts, emitter degeneration, frequency response, and amplifier classes.

## 1. Introduction to Transistor Amplifiers

An amplifier receives an input signal and produces a larger output signal using energy supplied by a DC power source.

The transistor does not create energy. It controls the transfer of energy from the power supply to the output.

A basic transistor amplifier contains:

- A transistor.
- A DC power supply.
- Biasing components.
- Input coupling components.
- Output coupling components.
- Load resistance.

The transistor is usually biased in the forward-active region for linear amplification.

### 1.1 Signal Amplification

Suppose a small AC input voltage is applied to the base of a common-emitter transistor.

A small change in base-emitter voltage causes a change in base current.

This produces a larger change in collector current.

The collector resistor converts the current variation into a voltage variation.

The output voltage can therefore have a larger amplitude than the input voltage.

### 1.2 Amplifier Gain

Gain describes the relationship between output and input signals.

Voltage gain:

\[
A_v=\frac{V_{out}}{V_{in}}
\]

Current gain:

\[
A_i=\frac{I_{out}}{I_{in}}
\]

Power gain:

\[
A_p=\frac{P_{out}}{P_{in}}
\]

For small-signal analysis, gain is often expressed using changes in voltage or current:

\[
A_v=\frac{\Delta V_{out}}{\Delta V_{in}}
\]

The gain may be positive or negative depending on the phase relationship between input and output.

## 2. Common-Emitter Amplifier

The common-emitter configuration is widely used for voltage amplification.

A typical circuit contains:

- An NPN transistor.
- A collector resistor \(R_C\).
- An emitter resistor \(R_E\).
- Base biasing resistors.
- Input coupling capacitor.
- Output coupling capacitor.
- An emitter bypass capacitor, when required.

### 2.1 Basic Operation

The transistor is first biased at a suitable Q-point.

An AC signal is then applied to the base.

When the input voltage increases:

1. Base-emitter voltage increases.
2. Base current increases.
3. Collector current increases.
4. Voltage drop across the collector resistor increases.
5. Collector voltage decreases.

Therefore, the output voltage changes in the opposite direction to the input voltage.

The common-emitter amplifier produces approximately 180° phase inversion.

### 2.2 Collector Voltage

For a grounded-emitter circuit:

\[
V_C=V_{CC}-I_CR_C
\]

For a circuit with an emitter resistor:

\[
V_{CE}=V_{CC}-I_CR_C-I_ER_E
\]

These equations describe DC operating conditions.

## 3. Coupling Capacitors

Coupling capacitors transfer AC signals between circuit stages while preventing unwanted DC conditions from one stage affecting another.

### 3.1 Input Coupling Capacitor

The input coupling capacitor connects the signal source to the transistor input.

It:

- Allows the AC signal to pass.
- Blocks DC from the signal source.
- Helps preserve the transistor's bias point.

### 3.2 Output Coupling Capacitor

The output coupling capacitor transfers the amplified AC signal to the load.

It prevents the transistor's collector DC voltage from being applied directly to the load.

### 3.3 Capacitive Reactance

The magnitude of capacitive reactance is:

\[
X_C=\frac{1}{2\pi fC}
\]

Where:

- \(X_C\) = capacitive reactance in ohms.
- \(f\) = signal frequency in hertz.
- \(C\) = capacitance in farads.

At low frequencies, capacitive reactance increases.

Therefore, coupling capacitors can attenuate low-frequency signals if their capacitance is insufficient.

## 4. Emitter Bypass Capacitor

An emitter resistor provides negative feedback and improves DC stability.

However, it can also reduce AC voltage gain.

An emitter bypass capacitor is connected in parallel with the emitter resistor to reduce its effect on AC signals.

### 4.1 Working Principle

At DC:

- The capacitor behaves approximately as an open circuit after charging.
- The emitter resistor remains active.
- DC bias stability is maintained.

At sufficiently high signal frequencies:

- Capacitor reactance becomes small.
- AC current can pass through the capacitor.
- The emitter resistor is partially bypassed for AC.
- Voltage gain increases.

### 4.2 Design Consideration

The bypass capacitor must be selected so that its reactance is sufficiently low over the intended signal-frequency range.

However, complete bypassing is not always desirable.

Leaving some emitter resistance unbypassed can improve linearity and reduce distortion.

## 5. Small-Signal Analysis

A transistor amplifier operates around a DC Q-point.

When a small AC signal is applied, transistor currents and voltages vary slightly around that operating point.

Small-signal analysis examines these variations.

The transistor's non-linear characteristics can be approximated by a linear model over a sufficiently small range.

This makes it easier to calculate voltage gain, current gain, and input resistance.

### 5.1 DC and AC Components

A transistor voltage can be expressed as:

\[
v_{BE}(t)=V_{BEQ}+v_{be}(t)
\]

Where:

- \(V_{BEQ}\) = DC base-emitter voltage at the Q-point.
- \(v_{be}(t)\) = small AC variation.

Similarly:

\[
i_C(t)=I_{CQ}+i_c(t)
\]

Where:

- \(I_{CQ}\) = DC collector current.
- \(i_c(t)\) = small AC collector-current variation.

The total instantaneous quantity is the sum of its DC and AC components.

## 6. Transconductance

Transconductance measures how much collector current changes in response to a small change in base-emitter voltage.

For a BJT operating in the forward-active region:

\[
\boxed{g_m=\frac{I_{CQ}}{V_T}}
\]

Where:

- \(g_m\) = transconductance in siemens.
- \(I_{CQ}\) = quiescent collector current.
- \(V_T\) = thermal voltage.

At room temperature:

\[
V_T\approx25.85\,mV
\]

Transconductance increases when collector bias current increases.

### 6.1 Small-Signal Collector Current

For small changes:

\[
i_c\approx g_mv_{be}
\]

Where:

- \(i_c\) = small-signal collector current.
- \(v_{be}\) = small-signal base-emitter voltage.

This equation is fundamental to BJT small-signal analysis.

## 7. Hybrid-Pi Model

The hybrid-pi model is a small-signal equivalent circuit used to analyse transistor amplifiers.

Its important parameters include:

- \(r_\pi\): small-signal resistance between base and emitter.
- \(g_m\): transconductance.
- \(r_o\): small-signal output resistance.

The simplified model represents the base-emitter input using \(r_\pi\) and the collector current using a controlled current source.

### 7.1 Base-Emitter Small-Signal Resistance

The hybrid-pi input resistance is approximately:

\[
\boxed{r_\pi=\frac{\beta}{g_m}}
\]

Substituting:

\[
g_m=\frac{I_{CQ}}{V_T}
\]

Therefore:

\[
\boxed{r_\pi=\frac{\beta V_T}{I_{CQ}}}
\]

Where:

- \(r_\pi\) = small-signal base-emitter resistance.
- \(\beta\) = common-emitter current gain.
- \(I_{CQ}\) = quiescent collector current.

### 7.2 Output Resistance

The transistor's small-signal output resistance is approximately:

\[
r_o\approx\frac{V_A}{I_{CQ}}
\]

Where:

- \(V_A\) = Early voltage.
- \(I_{CQ}\) = quiescent collector current.

This approximation models the effect of the Early effect, which causes collector current to vary slightly with collector-emitter voltage.

The output resistance is not always included in basic amplifier calculations.

## 8. Voltage Gain of a Common-Emitter Amplifier

For a simplified common-emitter amplifier with:

- Emitter at AC ground.
- Negligible transistor output resistance.
- No unbypassed emitter resistance.
- A collector load represented by \(R_C\parallel R_L\).

The approximate voltage gain is:

\[
\boxed{A_v\approx-g_m(R_C\parallel R_L)}
\]

Where:

- \(A_v\) = voltage gain.
- \(g_m\) = transistor transconductance.
- \(R_C\) = collector resistor.
- \(R_L\) = load resistance.

The negative sign represents phase inversion.

The parallel combination is:

\[
R_C\parallel R_L=
\frac{R_CR_L}{R_C+R_L}
\]

A lower effective collector load generally reduces voltage gain.

## 9. Emitter Degeneration

Emitter degeneration refers to leaving an emitter resistor unbypassed for AC operation.

It introduces negative feedback.

### 9.1 Effects

Emitter degeneration generally:

- Reduces voltage gain.
- Improves linearity.
- Reduces distortion.
- Makes gain less sensitive to transistor parameter variations.
- Can improve input resistance.

It is often used when predictable amplifier behaviour is more important than obtaining the maximum possible gain.

### 9.2 Approximate Gain

For a simplified circuit with an unbypassed emitter resistor:

\[
A_v\approx
-\frac{R_C\parallel R_L}
{r_e+R_E}
\]

Where:

- \(r_e\) = approximate intrinsic emitter resistance.
- \(R_E\) = unbypassed emitter resistance.

This approximation assumes sufficiently large beta and other simplifying conditions.

The intrinsic emitter resistance is approximately:

\[
r_e\approx\frac{V_T}{I_E}
\]

At room temperature, it is often approximated as:

\[
r_e\approx\frac{26\,mV}{I_E}
\]

with \(I_E\) expressed in amperes.

## 10. Frequency Response of a Transistor Amplifier

Frequency response describes how amplifier gain changes with signal frequency.

A practical transistor amplifier does not provide identical gain at every frequency.

Its response is commonly divided into three regions.

### 10.1 Low-Frequency Region

At low frequencies:

- Coupling capacitor reactance becomes larger.
- Emitter bypass capacitor reactance becomes larger.
- Signal attenuation increases.

The amplifier gain decreases.

### 10.2 Mid-Frequency Region

In the mid-frequency region:

- Coupling capacitors behave approximately as short circuits for AC.
- Bypass capacitors provide effective bypassing.
- Internal transistor capacitances have relatively little influence.

The gain is approximately constant.

### 10.3 High-Frequency Region

At high frequencies:

- Internal transistor capacitances become significant.
- Wiring capacitance affects the signal.
- Transit-time effects become important.
- Gain decreases.

### 10.4 Bandwidth

The bandwidth is the difference between upper and lower cutoff frequencies.

\[
\boxed{BW=f_H-f_L}
\]

Where:

- \(f_H\) = upper cutoff frequency.
- \(f_L\) = lower cutoff frequency.

The cutoff frequencies are commonly defined at the points where voltage gain falls to approximately 0.707 of its midband value.

This corresponds to a power reduction of one-half, or approximately -3 dB.

## 11. Amplifier Classes

Amplifiers can also be classified according to how long their active devices conduct during an input cycle.

### 11.1 Class A

The transistor conducts throughout the entire input cycle.

Conduction angle:

\[
360^\circ
\]

Characteristics:

- Good linearity.
- Low distortion when properly designed.
- Relatively low efficiency.
- Continuous device current.

### 11.2 Class B

The transistor conducts for approximately half of the input cycle.

Conduction angle:

\[
180^\circ
\]

Characteristics:

- Higher efficiency than Class A.
- Often uses a complementary push-pull arrangement.
- Can suffer from crossover distortion.

### 11.3 Class AB

The transistor conducts for more than half but less than the entire cycle.

Conduction angle:

\[
180^\circ<\theta<360^\circ
\]

Characteristics:

- Reduced crossover distortion compared with Class B.
- Efficiency generally higher than Class A.
- Common in audio output stages.

### 11.4 Class C

The transistor conducts for less than half of the input cycle.

Conduction angle:

\[
\theta<180^\circ
\]

Characteristics:

- High efficiency in suitable applications.
- Strongly non-linear output current.
- Often used with tuned circuits in radio-frequency applications.

## 12. Worked Numerical Examples

### Example 1: Transconductance

**Given:**

- Quiescent collector current: \(I_{CQ}=2\,mA\).
- Thermal voltage: \(V_T=25.85\,mV\).

Calculate the transistor transconductance.

**Formula:**

\[
g_m=\frac{I_{CQ}}{V_T}
\]

**Solution:**

Convert units:

\[
I_{CQ}=0.002\,A
\]

\[
V_T=0.02585\,V
\]

Substitute:

\[
g_m=\frac{0.002}{0.02585}
\]

\[
g_m\approx0.07737\,S
\]

**Final Answer:**

\[
\boxed{g_m\approx77.37\,mS}
\]

### Example 2: Hybrid-Pi Input Resistance

**Given:**

- Current gain: \(\beta=100\).
- Transconductance: \(g_m=40\,mS\).

Calculate \(r_\pi\).

**Formula:**

\[
r_\pi=\frac{\beta}{g_m}
\]

**Solution:**

Convert:

\[
g_m=0.04\,S
\]

Substitute:

\[
r_\pi=\frac{100}{0.04}
\]

\[
r_\pi=2500\,\Omega
\]

**Final Answer:**

\[
\boxed{r_\pi=2.5\,k\Omega}
\]

### Example 3: Common-Emitter Voltage Gain

**Given:**

- Transconductance: \(g_m=0.04\,S\).
- Collector resistance: \(R_C=4\,k\Omega\).
- Load resistance: \(R_L=4\,k\Omega\).
- Emitter is at AC ground.
- Neglect transistor output resistance.

Calculate the approximate voltage gain.

**Formula:**

\[
A_v\approx-g_m(R_C\parallel R_L)
\]

**Solution:**

Calculate the parallel resistance:

\[
R_C\parallel R_L=
\frac{4000\times4000}{4000+4000}
\]

\[
R_C\parallel R_L=2000\,\Omega
\]

Calculate gain:

\[
A_v=-0.04\times2000
\]

\[
A_v=-80
\]

**Final Answer:**

\[
\boxed{A_v\approx-80}
\]

The negative sign indicates approximately 180° phase inversion.

## 13. Practical Applications

### 13.1 Audio Amplification

Transistor amplifiers increase the amplitude of microphone, instrument, and audio signals.

### 13.2 Sensor Signal Conditioning

Small electrical signals from sensors can be amplified before measurement or conversion.

### 13.3 Radio-Frequency Amplification

Transistor stages amplify weak signals received by communication systems.

### 13.4 Instrumentation

Amplifiers increase small voltage variations from measurement circuits.

### 13.5 Multistage Amplifiers

Several amplifier stages can be connected to obtain the required overall gain, bandwidth, and impedance characteristics.

## 14. Common Examination Traps

1. A transistor amplifier requires an appropriate DC Q-point.
2. The DC operating point and AC signal are separate components of the total instantaneous signal.
3. A common-emitter amplifier normally produces phase inversion.
4. Coupling capacitors block DC while transferring AC.
5. An emitter bypass capacitor increases AC gain by reducing AC degeneration.
6. The emitter resistor remains important for DC stability even when bypassed for AC.
7. Transconductance is measured in siemens.
8. Hybrid-pi resistance \(r_\pi\) is approximately \(\beta/g_m\).
9. Loading reduces the effective collector resistance and can reduce voltage gain.
10. The negative sign in common-emitter voltage gain represents phase inversion.
11. Bandwidth is \(f_H-f_L\), not \(f_H+f_L\).
12. The -3 dB cutoff corresponds to approximately 0.707 of the midband voltage gain.
13. Class A conducts throughout the cycle.
14. Class B has an ideal conduction angle of 180°.
15. High gain does not automatically mean high efficiency or low distortion.

## 15. Quiz

### Question 1

What does transistor transconductance represent?

- [ ] The ratio of collector voltage to emitter voltage.
- [x] The change in collector current per unit change in base-emitter voltage.
- [ ] The ratio of input power to output power.
- [ ] The total DC resistance of the collector.

> **Explanation:** Transconductance is \(g_m=\Delta I_C/\Delta V_{BE}\) for small variations. At the Q-point, it is approximately \(I_{CQ}/V_T\) for a BJT.

### Question 2

A transistor has \(\beta=120\) and \(g_m=60\,mS\). What is its approximate hybrid-pi resistance?

- [ ] 0.5 Ω.
- [ ] 60 Ω.
- [x] 2 kΩ.
- [ ] 7.2 kΩ.

> **Explanation:** \(r_\pi=\beta/g_m=120/0.06=2000\,\Omega=2\,k\Omega\).

### Question 3

Which amplifier class has an ideal conduction angle of 180°?

- [ ] Class A.
- [x] Class B.
- [ ] Class AB.
- [ ] Class C.

> **Explanation:** A Class B amplifier's active device conducts for approximately half of the input cycle, corresponding to 180°.