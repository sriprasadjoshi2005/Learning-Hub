---
title: Embedded Systems and Sensor Integration
level: advanced
---

# Embedded Systems and Sensor Integration

An embedded system is a computer-based electronic system designed to perform a specific function within a larger device or application.

Unlike general-purpose computers, embedded systems are usually designed around particular operational requirements such as timing, power consumption, reliability, cost, and physical size.

They are found in automobiles, medical devices, household appliances, industrial controllers, robots, communication equipment, and IoT products.

Sensors allow embedded systems to observe physical conditions and convert them into electrical signals that can be measured and processed.

This lesson introduces embedded-system architecture, hardware and software components, real-time operation, sensor classifications, transducers, signal conditioning, sensor interfacing, and practical design considerations.

## 1. Introduction to Embedded Systems

An embedded system combines hardware and software to perform a dedicated task.

Examples include:

- Washing-machine controllers.
- Vehicle engine-control units.
- Digital thermostats.
- Smart watches.
- Medical monitoring devices.
- Industrial automation controllers.
- Smart lighting systems.

An embedded system may operate independently or communicate with a larger network.

## 2. Main Components of an Embedded System

An embedded system commonly contains the following components.

### 2.1 Processing Unit

The processing unit executes instructions and controls the system.

It may be:

- A microcontroller.
- A microprocessor.
- A digital signal processor.
- A system-on-chip device.

### 2.2 Memory

Memory stores program instructions, configuration information, and operating data.

Common types include:

- Flash memory.
- SRAM.
- EEPROM.
- External memory devices.

### 2.3 Input Interfaces

Input interfaces receive information from sensors, switches, and other external devices.

### 2.4 Output Interfaces

Output interfaces control actuators, displays, motors, indicators, and communication devices.

### 2.5 Power Supply

The power supply provides suitable voltage and current to the system.

It may include:

- Voltage regulators.
- DC-DC converters.
- Battery-management circuits.
- Power-protection components.

## 3. Embedded-System Architecture

A basic embedded system can be represented as:

Physical environment → Sensors → Signal conditioning → Processor → Output driver → Actuator.

The processor executes programmed instructions using information received from its inputs.

It then generates outputs to control the physical system.

Feedback from the environment may allow the system to adjust its operation.

## 4. Classification of Embedded Systems

### 4.1 Standalone Embedded Systems

These systems perform a dedicated task without requiring a continuous connection to another computer.

Example: a digital weighing scale.

### 4.2 Real-Time Embedded Systems

These systems must respond to events within specified timing constraints.

Example: an automotive airbag control system.

### 4.3 Networked Embedded Systems

These systems communicate with other devices over wired or wireless networks.

Example: a network-connected industrial sensor.

### 4.4 Mobile Embedded Systems

These systems are designed for portable or battery-powered applications.

Example: a fitness tracker.

## 5. Real-Time Systems

A real-time system is a system in which correctness depends not only on the logical result but also on when the result is produced.

### 5.1 Hard Real-Time Systems

A hard real-time system must meet specified deadlines.

Missing a critical deadline may result in system failure.

Examples include:

- Certain flight-control functions.
- Critical medical control systems.
- Safety-critical automotive functions.

### 5.2 Soft Real-Time Systems

A soft real-time system should meet its deadlines, but occasional delays may reduce performance rather than cause complete system failure.

Examples include:

- Video streaming.
- Multimedia playback.
- Some user-interface operations.

## 6. Firmware

Firmware is software stored in non-volatile memory and used to control electronic hardware.

It commonly contains:

- Startup instructions.
- Peripheral initialization.
- Device-control routines.
- Communication functions.
- Interrupt handlers.
- Application logic.

Firmware is often written in C or C++, although other programming languages may also be used.

## 7. Sensors and Transducers

A sensor detects a physical quantity and produces a corresponding output.

A transducer converts energy from one form into another.

A sensor is commonly a type of transducer used for measurement.

Measured quantities include:

- Temperature.
- Pressure.
- Light intensity.
- Humidity.
- Distance.
- Acceleration.
- Magnetic field.
- Sound.
- Force.

## 8. Classification of Sensors

### 8.1 Temperature Sensors

Temperature sensors measure thermal conditions.

Examples:

- Thermistors.
- Thermocouples.
- Resistance Temperature Detectors.
- Semiconductor temperature sensors.

### 8.2 Light Sensors

Light sensors respond to incident light.

Examples:

- Light-dependent resistors.
- Photodiodes.
- Phototransistors.
- Digital light sensors.

### 8.3 Pressure Sensors

Pressure sensors convert pressure into an electrical signal.

They are used in:

- Industrial process control.
- Weather systems.
- Automotive applications.
- Medical equipment.

### 8.4 Motion and Acceleration Sensors

Accelerometers measure acceleration.

Gyroscopes measure angular velocity.

These sensors are commonly combined in inertial measurement units.

Applications include:

- Navigation.
- Robotics.
- Smartphones.
- Stabilization systems.

### 8.5 Distance Sensors

Distance sensors estimate the distance between the sensor and an object.

Common technologies include:

- Ultrasonic sensing.
- Infrared sensing.
- Time-of-flight optical sensing.
- Laser ranging.

## 9. Active and Passive Sensors

### 9.1 Active Sensors

Active sensors require an external excitation or emit energy to measure a physical quantity, depending on the sensor type.

Examples include:

- Ultrasonic distance sensors.
- Radar sensors.
- Active optical ranging systems.

### 9.2 Passive Sensors

Passive sensors detect naturally occurring energy or changes in a physical property without actively transmitting a measurement signal.

Examples include:

- Thermocouples.
- Photodiodes operating as light detectors.
- Passive infrared sensors.

The active/passive classification depends on the sensing mechanism and is not identical to the powered/unpowered classification.

## 10. Analog and Digital Sensors

### 10.1 Analog Sensors

Analog sensors produce continuously varying output signals.

Examples:

- Analog temperature sensors.
- Thermistors.
- LDR circuits.
- Analog pressure sensors.

Their outputs may require amplification, filtering, and ADC conversion.

### 10.2 Digital Sensors

Digital sensors provide information in digital form.

They may contain internal signal conditioning and ADC circuitry.

Some digital sensors communicate using I2C, SPI, or other protocols.

## 11. Sensor Characteristics

Important sensor characteristics include:

### 11.1 Range

The range is the interval of physical values that the sensor can measure.

### 11.2 Sensitivity

Sensitivity describes the change in output per unit change in the measured quantity.

For a linear sensor:

\[
\boxed{S=\frac{\Delta y}{\Delta x}}
\]

Where:

- \(\Delta y\) = change in output.
- \(\Delta x\) = change in measured input.

### 11.3 Accuracy

Accuracy describes how close a measurement is to the true or accepted reference value.

### 11.4 Precision

Precision describes the closeness of repeated measurements to one another.

### 11.5 Resolution

Resolution is the smallest change in input that can be distinguished by the measurement system.

### 11.6 Linearity

Linearity describes how closely the sensor output follows an ideal linear relationship with its input.

### 11.7 Response Time

Response time describes how quickly the sensor reacts to a change in the measured quantity.

## 12. Signal Conditioning

Sensor outputs are not always suitable for direct processing.

Signal conditioning modifies the signal so that it can be measured reliably.

Common operations include:

- Amplification.
- Filtering.
- Attenuation.
- Linearization.
- Isolation.
- Level shifting.
- Impedance matching.

For example, a small sensor voltage may be amplified using an operational amplifier before being applied to an ADC.

## 13. Sensor Calibration

Calibration compares a sensor's output with a known reference.

It helps identify measurement errors and establish a relationship between output and actual physical quantity.

Calibration may involve:

1. Applying known reference values.
2. Recording sensor outputs.
3. Comparing measured and reference values.
4. Determining correction factors.
5. Applying calibration to future measurements.

Calibration does not automatically remove every source of uncertainty.

## 14. Actuators

An actuator converts an electrical control signal into a physical action.

Examples include:

- DC motors.
- Servo motors.
- Solenoids.
- Relays.
- Heating elements.
- Valves.
- Piezoelectric actuators.

A sensor observes the environment, while an actuator changes it.

## 15. Feedback in Embedded Systems

A feedback system measures the result of an action and uses that information to adjust future control.

For example, a temperature controller may:

1. Measure the current temperature.
2. Compare it with a desired temperature.
3. Calculate the difference.
4. Control a heater.
5. Measure the temperature again.

This process repeats to maintain the desired operating condition.

## 16. Low-Power Embedded Design

Many embedded systems operate using batteries.

Power consumption can be reduced through:

- Low-power microcontrollers.
- Reduced clock frequency when high performance is unnecessary.
- Sleep and standby modes.
- Efficient voltage regulation.
- Peripheral shutdown.
- Reduced wireless transmission.
- Event-driven operation.

Power optimization must preserve the timing and functionality required by the application.

## 17. Worked Numerical Examples

### Example 1: Sensor Sensitivity

**Given:**

A temperature sensor produces:

\[
0.5\,V
\]

at \(20^\circ C\), and:

\[
1.5\,V
\]

at \(40^\circ C\).

Calculate its average sensitivity over this interval.

**Formula:**

\[
S=\frac{\Delta V}{\Delta T}
\]

**Solution:**

\[
\Delta V=1.5-0.5=1\,V
\]

\[
\Delta T=40-20=20^\circ C
\]

\[
S=\frac{1}{20}
\]

\[
S=0.05\,V/^\circ C
\]

**Final Answer:**

\[
\boxed{S=50\,mV/^\circ C}
\]

### Example 2: ADC Resolution for a Sensor

**Given:**

A sensor produces an output from 0 V to 3.3 V.

A 12-bit ADC measures this voltage.

Calculate the approximate voltage step size.

**Formula:**

\[
\Delta V\approx\frac{V_{ref}}{2^n}
\]

**Solution:**

\[
\Delta V=\frac{3.3}{2^{12}}
\]

\[
\Delta V=\frac{3.3}{4096}
\]

\[
\Delta V\approx0.0008057\,V
\]

\[
\Delta V\approx0.806\,mV
\]

**Final Answer:**

\[
\boxed{\Delta V\approx0.806\,mV}
\]

### Example 3: Measurement Error

**Given:**

A temperature reference indicates:

\[
T_{reference}=50^\circ C
\]

A sensor indicates:

\[
T_{measured}=48^\circ C
\]

Calculate the absolute error and percentage error relative to the reference.

**Formula:**

\[
\text{Absolute error}=|T_{measured}-T_{reference}|
\]

\[
\text{Percentage error}=
\frac{\text{Absolute error}}{T_{reference}}\times100
\]

**Solution:**

\[
\text{Absolute error}=|48-50|=2^\circ C
\]

\[
\text{Percentage error}=\frac{2}{50}\times100
\]

\[
=4\%
\]

**Final Answer:**

\[
\boxed{2^\circ C\text{ absolute error}}
\]

\[
\boxed{4\%\text{ percentage error}}
\]

## 18. Applications

Embedded systems and sensor integration are used in:

- Smart homes.
- Automotive systems.
- Industrial automation.
- Medical monitoring.
- Robotics.
- Environmental monitoring.
- Agriculture.
- Consumer electronics.
- IoT networks.

## 19. Common Examination Traps

1. An embedded system is designed for a particular application or set of functions.
2. Firmware controls the hardware of an embedded device.
3. A sensor detects a physical quantity.
4. A transducer converts energy from one form to another.
5. Sensitivity is the change in output per unit change in input.
6. Accuracy and precision are different concepts.
7. Resolution is the smallest distinguishable measurement change.
8. Analog sensors produce continuously varying outputs.
9. Digital sensors provide digital information.
10. Signal conditioning prepares a sensor signal for reliable processing.
11. Calibration compares measurements with known references.
12. An actuator produces physical action.
13. Hard real-time systems have strict deadline requirements.
14. Soft real-time systems can tolerate some deadline misses with degraded performance.
15. Low-power design is particularly important in battery-powered systems.

## Quiz

1. Which characteristic describes the change in sensor output for a unit change in the measured quantity?

   - [ ] Accuracy.
   - [ ] Precision.
   - [x] Sensitivity.
   - [ ] Response time.

   > Sensitivity is defined as the ratio of output change to input change. For a linear sensor, it is commonly expressed as output units per unit of the measured physical quantity.

2. Which component converts an electrical control signal into physical movement?

   - [ ] ADC.
   - [ ] Sensor.
   - [x] Actuator.
   - [ ] Memory register.

   > An actuator converts a control signal into physical action. Motors, solenoids, valves, and relays are examples of actuating devices.

3. What is the main requirement of a hard real-time system?

   - [ ] It must always use wireless communication.
   - [ ] It must operate without a processor.
   - [x] It must meet specified timing deadlines.
   - [ ] It must use only analog sensors.

   > Hard real-time systems have strict timing requirements. Missing a critical deadline can cause system failure even if the calculated result is logically correct.