---
title: Electronic Instrumentation and Measurement Systems
level: advanced
---

# Electronic Instrumentation and Measurement Systems

Electronic instrumentation deals with the measurement, monitoring, and analysis of electrical and physical quantities using electronic devices.

Measurement systems are essential in laboratories, manufacturing, medical equipment, power systems, communication networks, and scientific research.

In electronics, accurate measurement is necessary for circuit testing, troubleshooting, calibration, and performance verification.

This lesson introduces measurement systems, measurement errors, accuracy, precision, resolution, multimeters, oscilloscopes, signal generators, frequency counters, bridges, and instrument calibration.

## 1. Introduction to Electronic Instrumentation

An electronic measuring instrument converts a physical or electrical quantity into a form that can be observed, recorded, or analyzed.

Examples of measured quantities include:

- Voltage.
- Current.
- Resistance.
- Frequency.
- Capacitance.
- Inductance.
- Power.
- Temperature.
- Pressure.
- Time.

A measurement system commonly includes:

1. Measurand.
2. Sensor or input element.
3. Signal conditioning.
4. Processing or conversion.
5. Display or recording system.

## 2. Types of Measurement Systems

### 2.1 Analog Instruments

Analog instruments represent measured quantities using continuously varying indications.

Examples include:

- Moving-coil meters.
- Analog voltmeters.
- Analog ammeters.

### 2.2 Digital Instruments

Digital instruments display measured quantities as numerical values.

Examples include:

- Digital multimeters.
- Digital oscilloscopes.
- Frequency counters.
- Digital thermometers.

Digital instruments often provide convenient readings, but their accuracy still depends on calibration, resolution, and measurement conditions.

## 3. Measurement Characteristics

### 3.1 Accuracy

Accuracy indicates how close a measured value is to the true or accepted reference value.

### 3.2 Precision

Precision indicates the closeness of repeated measurements to one another.

### 3.3 Resolution

Resolution is the smallest change in a measured quantity that an instrument can distinguish.

### 3.4 Sensitivity

Sensitivity describes the change in instrument output for a given change in input.

### 3.5 Linearity

Linearity describes how closely an instrument follows an ideal proportional relationship over its operating range.

### 3.6 Repeatability

Repeatability describes the ability of an instrument to produce similar results under the same measurement conditions.

### 3.7 Range

Range specifies the minimum and maximum values that an instrument is designed to measure.

## 4. Measurement Errors

A measurement error is the difference between a measured value and a reference value.

\[
\boxed{e=x_m-x_r}
\]

Where:

- \(x_m\) = measured value.
- \(x_r\) = reference value.

### 4.1 Absolute Error

\[
\boxed{E_a=|x_m-x_r|}
\]

### 4.2 Relative Error

\[
\boxed{
E_r=\frac{|x_m-x_r|}{|x_r|}
}
\]

### 4.3 Percentage Error

\[
\boxed{
E_p=\frac{|x_m-x_r|}{|x_r|}\times100\%
}
\]

### 4.4 Systematic Errors

Systematic errors occur due to consistent measurement biases.

Possible causes include:

- Instrument calibration errors.
- Incorrect zero adjustment.
- Environmental influences.
- Measurement loading.
- Instrument design limitations.

### 4.5 Random Errors

Random errors arise from unpredictable variations in measurement conditions.

Examples include:

- Electrical noise.
- Small environmental fluctuations.
- Random signal variations.
- Reading uncertainty.

Repeated measurements and statistical analysis can help characterize random errors.

## 5. Digital Multimeter

A Digital Multimeter (DMM) is a commonly used instrument for measuring electrical quantities.

Typical functions include:

- DC voltage.
- AC voltage.
- DC current.
- AC current.
- Resistance.
- Continuity.
- Diode testing.
- Capacitance.
- Frequency.

The available functions depend on the particular instrument.

### 5.1 Voltage Measurement

A voltmeter is connected in parallel with the component or circuit section being measured.

An ideal voltmeter has infinite input resistance so that it draws no current.

A practical voltmeter has high but finite input resistance.

### 5.2 Current Measurement

An ammeter is connected in series with the circuit branch whose current is being measured.

An ideal ammeter has zero internal resistance.

A practical ammeter has a small internal resistance.

### 5.3 Resistance Measurement

Resistance is measured using an internal test source in the multimeter.

Resistance measurements should generally be made on a de-energized circuit, with suitable precautions against stored energy in capacitors and other components.

## 6. Oscilloscope

An oscilloscope displays electrical signals as a function of time.

It is one of the most important instruments used in electronics testing.

A typical oscilloscope can display:

- Waveform shape.
- Amplitude.
- Time period.
- Frequency.
- Phase difference.
- Rise time.
- Fall time.
- Transient behaviour.

### 6.1 Vertical Scale

The vertical scale is commonly expressed in volts per division.

It determines how much voltage is represented by each vertical grid division.

### 6.2 Horizontal Scale

The horizontal scale is commonly expressed in seconds per division.

It determines the time represented by each horizontal grid division.

### 6.3 Triggering

Triggering stabilizes the waveform display by defining the condition at which waveform acquisition or display begins.

Common trigger sources include:

- Input channels.
- External trigger.
- Internal trigger signals.

### 6.4 Probe Attenuation

Oscilloscope probes may use attenuation settings such as 1× and 10×.

The oscilloscope configuration must match the probe setting for accurate amplitude measurements.

## 7. Function Generator

A function generator produces electrical signals with selected waveform shapes and parameters.

Common waveforms include:

- Sine waves.
- Square waves.
- Triangle waves.
- Ramp waves.
- Pulse signals.

Important settings include:

- Frequency.
- Amplitude.
- DC offset.
- Duty cycle.
- Waveform type.

Function generators are used to test amplifiers, filters, oscillators, and communication circuits.

## 8. Frequency Counter

A frequency counter measures the frequency of a periodic signal.

It commonly counts the number of signal cycles occurring during a known time interval.

The frequency is:

\[
\boxed{f=\frac{N}{T_g}}
\]

Where:

- \(N\) = number of counted cycles.
- \(T_g\) = gate time.

A longer gate time generally improves basic counting resolution but increases measurement time.

## 9. Wheatstone Bridge

A Wheatstone bridge is a circuit used to measure an unknown resistance by balancing two resistive branches.

At balance, the galvanometer or detector current is zero.

For a common bridge arrangement:

\[
\boxed{\frac{R_1}{R_2}=\frac{R_3}{R_x}}
\]

Therefore:

\[
\boxed{R_x=\frac{R_2R_3}{R_1}}
\]

The exact ratio depends on the resistor labeling and bridge arrangement.

Wheatstone bridges are also used with resistive sensors.

## 10. Kelvin Bridge

A Kelvin double bridge is used for measuring very low resistance values.

It reduces the influence of lead and contact resistance through a suitable four-terminal arrangement.

Applications include:

- Measuring shunt resistors.
- Testing electrical contacts.
- Measuring low-resistance conductors.
- Testing busbars.

## 11. LCR Meter

An LCR meter measures:

- Inductance.
- Capacitance.
- Resistance.

Depending on the instrument, it may also measure:

- Impedance.
- Dissipation factor.
- Quality factor.
- Equivalent series resistance.

It is useful for testing passive components and electronic circuits.

## 12. Loading Effect

Loading effect occurs when a measuring instrument changes the behaviour of the circuit being measured.

For example, a voltmeter connected across a high-resistance circuit may draw enough current to alter the measured voltage.

A voltmeter with higher input resistance generally reduces this effect.

Similarly, an ammeter with lower internal resistance reduces the voltage drop introduced into the circuit.

## 13. Instrument Calibration

Calibration compares an instrument's readings against a known reference standard.

The purpose is to determine measurement deviations and establish whether the instrument meets its specified performance.

Calibration may involve:

1. Selecting an appropriate reference standard.
2. Applying known input values.
3. Recording instrument readings.
4. Calculating deviations.
5. Documenting calibration results.
6. Applying corrections where appropriate.

Calibration does not mean that every measurement is automatically exact.

## 14. Safety in Electronic Measurements

Measurement procedures must account for electrical hazards.

Important precautions include:

- Selecting the correct instrument range.
- Using correctly rated probes.
- Checking probe insulation.
- Connecting current meters in series.
- Connecting voltage meters in parallel.
- Avoiding resistance measurements on energized circuits.
- Respecting instrument voltage and category ratings.
- Discharging capacitors safely before handling.
- Avoiding exposed live conductors.

Mains and high-energy measurements require appropriate training and correctly rated equipment.

## 15. Worked Numerical Examples

### Example 1: Percentage Measurement Error

**Given:**

Reference voltage:

\[
V_r=10\,V
\]

Measured voltage:

\[
V_m=9.8\,V
\]

Calculate the percentage error.

**Formula:**

\[
E_p=\frac{|V_m-V_r|}{|V_r|}\times100\%
\]

**Solution:**

\[
E_p=\frac{|9.8-10|}{10}\times100
\]

\[
E_p=\frac{0.2}{10}\times100
\]

\[
E_p=2\%
\]

**Final Answer:**

\[
\boxed{2\%}
\]

### Example 2: Oscilloscope Frequency Measurement

**Given:**

One complete waveform cycle occupies 4 horizontal divisions.

The time scale is:

\[
2\,ms/division
\]

Calculate the time period and frequency.

**Formula:**

\[
T=(\text{Divisions})(\text{Time per division})
\]

\[
f=\frac{1}{T}
\]

**Solution:**

\[
T=4\times2\,ms
\]

\[
T=8\,ms
\]

Convert to seconds:

\[
T=0.008\,s
\]

Therefore:

\[
f=\frac{1}{0.008}
\]

\[
f=125\,Hz
\]

**Final Answer:**

\[
\boxed{T=8\,ms}
\]

\[
\boxed{f=125\,Hz}
\]

### Example 3: Wheatstone Bridge

**Given:**

A balanced Wheatstone bridge has:

\[
R_1=100\,\Omega
\]

\[
R_2=200\,\Omega
\]

\[
R_3=150\,\Omega
\]

Calculate the unknown resistance \(R_x\).

**Formula:**

\[
R_x=\frac{R_2R_3}{R_1}
\]

**Solution:**

\[
R_x=\frac{200\times150}{100}
\]

\[
R_x=300\,\Omega
\]

**Final Answer:**

\[
\boxed{R_x=300\,\Omega}
\]

### Example 4: Frequency Counter

**Given:**

A frequency counter records 5000 cycles during a gate time of:

\[
T_g=0.1\,s
\]

Calculate the frequency.

**Formula:**

\[
f=\frac{N}{T_g}
\]

**Solution:**

\[
f=\frac{5000}{0.1}
\]

\[
f=50,000\,Hz
\]

**Final Answer:**

\[
\boxed{f=50\,kHz}
\]

## 16. Applications

Electronic instrumentation is used in:

- Electronics laboratories.
- Semiconductor testing.
- Industrial measurement.
- Medical instrumentation.
- Electrical power systems.
- Communication testing.
- Manufacturing quality control.
- Scientific research.

## 17. Common Examination Traps

1. Accuracy describes closeness to a reference value.
2. Precision describes consistency between repeated measurements.
3. Resolution is the smallest distinguishable change.
4. A voltmeter is connected in parallel.
5. An ammeter is connected in series.
6. An ideal voltmeter has infinite input resistance.
7. An ideal ammeter has zero internal resistance.
8. An oscilloscope displays voltage as a function of time.
9. The oscilloscope's time scale determines the time represented by each horizontal division.
10. Probe attenuation settings must match the oscilloscope configuration.
11. A function generator produces test signals.
12. A frequency counter measures periodic signal frequency.
13. A Wheatstone bridge is used to determine an unknown resistance.
14. A Kelvin bridge is suitable for very low resistance measurements.
15. Loading effect occurs when the instrument alters the measured circuit.
16. Calibration compares readings against known references.
17. Resistance measurements should not be performed on an energized circuit.
18. Instrument range and safety ratings must be checked before measurements.

## Quiz

1. How should a voltmeter be connected to measure the voltage across a resistor?

   - [ ] In series with the resistor.
   - [x] In parallel with the resistor.
   - [ ] Across the power supply only.
   - [ ] In place of the resistor.

   > A voltmeter measures the potential difference between two points, so it is connected in parallel with the component. Its high input resistance helps minimize circuit loading.

2. Which instrument is most suitable for observing the shape of a time-varying electrical signal?

   - [ ] Ammeter.
   - [ ] Wheatstone bridge.
   - [x] Oscilloscope.
   - [ ] LCR meter.

   > An oscilloscope displays an electrical waveform as a function of time. It allows the user to examine amplitude, period, frequency, transitions, and transient behaviour.

3. What is the primary purpose of a Wheatstone bridge?

   - [ ] To measure high-frequency signals.
   - [x] To determine an unknown resistance using a balanced bridge.
   - [ ] To generate sinusoidal signals.
   - [ ] To convert AC into DC.

   > A Wheatstone bridge determines an unknown resistance by balancing two resistive branches. At balance, the detector current is zero and the resistor ratios provide the unknown resistance.