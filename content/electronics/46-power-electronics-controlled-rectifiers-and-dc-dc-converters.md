---
title: Power Electronics Including Controlled Rectifiers and DC-DC Converters
level: advanced
---

# Power Electronics Including Controlled Rectifiers and DC-DC Converters

Power electronics is the branch of electronics concerned with converting, controlling, and regulating electrical power using semiconductor devices.

It is essential in electric vehicles, renewable-energy systems, industrial motor drives, battery chargers, power supplies, and energy-storage systems.

Power electronic converters change electrical energy from one form into another while controlling important quantities such as voltage, current, frequency, and power.

This lesson introduces power semiconductor devices, rectifiers, controlled rectifiers, DC-DC converters, inverters, switching techniques, efficiency, and practical power-electronic applications.

## 1. Introduction to Power Electronics

Power electronics uses semiconductor devices as controlled switches to regulate electrical energy.

The main objectives are:

- AC-to-DC conversion.
- DC-to-DC conversion.
- DC-to-AC conversion.
- AC-to-AC conversion.
- Voltage regulation.
- Current control.
- Motor speed control.

Power converters are designed to operate efficiently while satisfying electrical and thermal limits.

## 2. Power Semiconductor Devices

Important semiconductor devices used in power electronics include:

### 2.1 Power Diodes

Power diodes allow current to flow primarily in one direction.

They are commonly used in:

- Rectifiers.
- Freewheeling circuits.
- Protection circuits.

### 2.2 Thyristors

A thyristor is a semiconductor switching device that can be triggered into conduction.

The Silicon Controlled Rectifier (SCR) is a widely studied thyristor.

An SCR has three terminals:

- Anode.
- Cathode.
- Gate.

A gate pulse can initiate conduction when the device is forward-biased.

Once conducting, a conventional SCR remains on until its current falls below the holding-current requirement, subject to its operating conditions.

### 2.3 Power MOSFETs

Power MOSFETs are voltage-controlled semiconductor switching devices.

They are widely used in high-frequency switching applications.

### 2.4 Insulated-Gate Bipolar Transistors

An Insulated-Gate Bipolar Transistor (IGBT) combines MOS-gate control with bipolar conduction characteristics.

IGBTs are commonly used in medium- and high-power conversion applications.

## 3. Power Converter Classification

| Converter | Input | Output | Main purpose |
|---|---|---|---|
| Rectifier | AC | DC | AC-to-DC conversion |
| DC-DC converter | DC | DC | Change DC voltage level |
| Inverter | DC | AC | DC-to-AC conversion |
| AC voltage controller | AC | Controlled AC | Control AC voltage |
| Cycloconverter | AC | AC at another frequency | AC frequency conversion |

## 4. Rectifiers

A rectifier converts alternating current into unidirectional current.

Rectifiers are commonly used in DC power supplies and battery-charging circuits.

### 4.1 Half-Wave Rectifier

A half-wave rectifier uses one diode to conduct during one half-cycle of an AC input.

During the other half-cycle, the diode blocks current.

For an ideal sinusoidal input with peak value \(V_m\):

\[
\boxed{V_{DC}=\frac{V_m}{\pi}}
\]

### 4.2 Full-Wave Rectifier

A full-wave rectifier uses both half-cycles of the AC input to produce a unidirectional output.

Common arrangements include:

- Centre-tapped rectifier.
- Bridge rectifier.

For an ideal full-wave rectified sine wave:

\[
\boxed{V_{DC}=\frac{2V_m}{\pi}}
\]

The output ripple frequency is twice the AC input frequency.

## 5. Controlled Rectifiers

A controlled rectifier uses controllable semiconductor devices to regulate the average DC output.

SCRs are commonly used in traditional controlled rectifier circuits.

Unlike an uncontrolled diode rectifier, a controlled rectifier can adjust its output by changing the firing angle.

### 5.1 Firing Angle

The firing angle, represented by \(\alpha\), is the electrical angle measured from the relevant AC reference point to the instant an SCR is triggered.

Changing the firing angle changes the conduction interval and average output voltage.

### 5.2 Single-Phase Half-Wave Controlled Rectifier

For an ideal single-phase half-wave controlled rectifier with a resistive load:

\[
\boxed{
V_{DC}=\frac{V_m}{2\pi}(1+\cos\alpha)
}
\]

Where:

- \(V_m\) = peak input voltage.
- \(\alpha\) = firing angle.

This expression assumes an ideal SCR and a resistive load under the standard half-wave circuit conditions.

### 5.3 Single-Phase Fully Controlled Bridge Rectifier

For an ideal single-phase fully controlled bridge with continuous load current:

\[
\boxed{
V_{DC}=\frac{2V_m}{\pi}\cos\alpha
}
\]

This expression assumes ideal devices and continuous conduction.

The average output can become negative for firing angles greater than 90° under the appropriate continuous-current operating conditions, allowing inverter operation when the DC-side circuit supports it.

## 6. DC-DC Converters

A DC-DC converter changes one DC voltage level into another.

It commonly uses semiconductor switching devices, inductors, capacitors, and control circuitry.

Important converter types include:

- Buck converter.
- Boost converter.
- Buck-boost converter.

## 7. Buck Converter

A buck converter produces an output voltage lower than its input voltage under normal operating conditions.

It is also called a step-down converter.

An ideal buck converter operating in continuous conduction mode has:

\[
\boxed{V_o=DV_{in}}
\]

Where:

- \(V_o\) = output voltage.
- \(V_{in}\) = input voltage.
- \(D\) = duty cycle.

The duty cycle is:

\[
\boxed{D=\frac{T_{ON}}{T}}
\]

For an ideal converter:

\[
0\leq D\leq1
\]

Increasing the duty cycle increases the average output voltage.

## 8. Boost Converter

A boost converter produces an output voltage greater than its input voltage under normal operating conditions.

It is also called a step-up converter.

For an ideal boost converter operating in continuous conduction mode:

\[
\boxed{V_o=\frac{V_{in}}{1-D}}
\]

As the duty cycle increases, the ideal output voltage increases.

Practical converters are limited by semiconductor ratings, losses, control constraints, and component parasitics.

## 9. Buck-Boost Converter

A buck-boost converter can produce an output magnitude either lower or higher than its input voltage.

For the classical inverting buck-boost converter operating ideally in continuous conduction mode:

\[
\boxed{\frac{V_o}{V_{in}}=-\frac{D}{1-D}}
\]

The negative sign indicates that the output polarity is reversed relative to the input reference.

Other non-inverting buck-boost topologies are also available.

## 10. Pulse-Width Modulation

Pulse-Width Modulation (PWM) controls the average power delivered to a load by varying the duration of the switching pulse.

The duty cycle is the fraction of one switching period for which the switch remains ON.

\[
\boxed{D=\frac{T_{ON}}{T_{ON}+T_{OFF}}}
\]

PWM is widely used in:

- DC-DC converters.
- Motor speed control.
- LED brightness control.
- Inverters.
- Switching power supplies.

## 11. Inverters

An inverter converts DC electrical power into AC electrical power.

Applications include:

- Solar power systems.
- Uninterruptible power supplies.
- Electric vehicle drives.
- Variable-frequency motor drives.

Inverters use controlled semiconductor switches to generate an alternating output.

Common output waveforms include:

- Square wave.
- Modified waveform.
- Pulse-width-modulated waveform.
- Sinusoidal waveform after suitable filtering.

## 12. Switching Losses and Conduction Losses

Power electronic devices experience losses during operation.

### 12.1 Conduction Losses

Conduction losses occur when current flows through a device that has a non-zero voltage drop or resistance.

For a simplified resistive conduction model:

\[
P_{cond}=I^2R
\]

### 12.2 Switching Losses

Switching losses occur during transitions between ON and OFF states.

During switching transitions, voltage and current may overlap for a short interval.

Increasing switching frequency can increase switching losses, although it may reduce the size of passive components.

## 13. Converter Efficiency

Efficiency measures the fraction of input power delivered as useful output power.

\[
\boxed{
\eta=\frac{P_{out}}{P_{in}}\times100\%
}
\]

A higher efficiency indicates lower power loss for the same output power.

Converter efficiency is affected by:

- Semiconductor conduction losses.
- Switching losses.
- Magnetic losses.
- Capacitor losses.
- Gate-drive losses.
- Control-circuit consumption.

## 14. Thermal Management

Power semiconductor devices generate heat during operation.

Excessive temperature can reduce reliability and damage components.

Thermal management methods include:

- Heat sinks.
- Cooling fans.
- Thermal interface materials.
- Appropriate PCB copper areas.
- Thermal monitoring.
- Proper device selection.

The junction temperature must remain within the device's specified operating limits.

## 15. Worked Numerical Examples

### Example 1: Buck Converter

**Given:**

An ideal buck converter has:

\[
V_{in}=24\,V
\]

\[
D=0.5
\]

Calculate the output voltage.

**Formula:**

\[
V_o=DV_{in}
\]

**Solution:**

\[
V_o=0.5\times24
\]

\[
V_o=12\,V
\]

**Final Answer:**

\[
\boxed{V_o=12\,V}
\]

### Example 2: Boost Converter

**Given:**

An ideal boost converter has:

\[
V_{in}=12\,V
\]

\[
D=0.6
\]

Calculate its output voltage.

**Formula:**

\[
V_o=\frac{V_{in}}{1-D}
\]

**Solution:**

\[
V_o=\frac{12}{1-0.6}
\]

\[
V_o=\frac{12}{0.4}
\]

\[
V_o=30\,V
\]

**Final Answer:**

\[
\boxed{V_o=30\,V}
\]

### Example 3: Converter Efficiency

**Given:**

A power converter receives:

\[
P_{in}=200\,W
\]

Its output power is:

\[
P_{out}=180\,W
\]

Calculate its efficiency and power loss.

**Formula:**

\[
\eta=\frac{P_{out}}{P_{in}}\times100\%
\]

\[
P_{loss}=P_{in}-P_{out}
\]

**Solution:**

\[
\eta=\frac{180}{200}\times100
\]

\[
\eta=90\%
\]

Power loss:

\[
P_{loss}=200-180
\]

\[
P_{loss}=20\,W
\]

**Final Answer:**

\[
\boxed{\eta=90\%}
\]

\[
\boxed{P_{loss}=20\,W}
\]

### Example 4: PWM Duty Cycle

**Given:**

A switching converter has:

\[
T_{ON}=30\,\mu s
\]

\[
T_{OFF}=70\,\mu s
\]

Calculate its duty cycle.

**Formula:**

\[
D=\frac{T_{ON}}{T_{ON}+T_{OFF}}
\]

**Solution:**

\[
D=\frac{30}{30+70}
\]

\[
D=\frac{30}{100}=0.3
\]

**Final Answer:**

\[
\boxed{D=30\%}
\]

## 16. Applications

Power electronics is used in:

- Electric vehicles.
- Solar photovoltaic systems.
- Wind-energy conversion.
- Battery chargers.
- Industrial motor drives.
- UPS systems.
- Switched-mode power supplies.
- Renewable-energy storage.
- Railway traction.

## 17. Common Examination Traps

1. A rectifier converts AC into DC.
2. An inverter converts DC into AC.
3. A buck converter reduces DC voltage.
4. A boost converter increases DC voltage.
5. A buck-boost converter can change output magnitude and, in its classical inverting form, reverse polarity.
6. An SCR is a controlled semiconductor device.
7. The firing angle controls the triggering instant of an SCR.
8. PWM controls the switching duty cycle.
9. Duty cycle is the ratio of ON time to total switching period.
10. Ideal buck and boost equations assume continuous conduction mode.
11. Practical converter outputs differ from ideal predictions because of losses and component limitations.
12. Switching frequency can influence switching losses.
13. Conduction losses occur while current flows through semiconductor devices.
14. Efficiency is output power divided by input power.
15. Thermal management is essential in high-power electronic systems.

## Quiz

1. Which converter is primarily used to reduce a DC input voltage?

   - [ ] Boost converter.
   - [x] Buck converter.
   - [ ] Inverter.
   - [ ] Uncontrolled AC regulator.

   > An ideal buck converter operates as a step-down DC-DC converter. Its continuous-conduction voltage relationship is \(V_o=DV_{in}\), where the duty cycle is less than or equal to one.

2. What does the firing angle of an SCR-controlled rectifier determine?

   - [ ] The physical size of the SCR.
   - [ ] The AC supply frequency.
   - [x] The triggering instant of the SCR relative to the AC reference.
   - [ ] The resistance of the load.

   > The firing angle specifies when the gate pulse triggers the SCR during the AC cycle. Changing it changes the conduction interval and therefore the average output voltage.

3. A converter receives 100 W and delivers 85 W. What is its efficiency?

   - [ ] 15%.
   - [ ] 50%.
   - [x] 85%.
   - [ ] 100%.

   > Efficiency is \(\eta=(P_{out}/P_{in})\times100=(85/100)\times100=85\%\). The remaining 15 W is lost within the converter.