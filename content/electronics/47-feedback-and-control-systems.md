---
title: Feedback and Control Systems
level: advanced
---

# Feedback and Control Systems

Control systems are designed to regulate the behaviour of physical processes and electronic devices.

They are used to maintain temperature, control motor speed, regulate voltage, stabilize position, and automate industrial processes.

Feedback is an important concept in control engineering because it allows a system to measure its output and adjust its behaviour according to the difference between the desired and actual outputs.

This lesson introduces open-loop and closed-loop systems, feedback principles, transfer functions, stability, system response, proportional-integral-derivative control, and practical electronic control applications.

## 1. Introduction to Control Systems

A control system is an arrangement of components designed to manage the behaviour of another system.

Examples include:

- Room temperature controllers.
- Motor speed controllers.
- Automatic voltage regulators.
- Industrial process controllers.
- Aircraft control systems.
- Robotic positioning systems.

A control system generally includes:

- Reference input.
- Controller.
- Plant or process.
- Output.
- Feedback path, when applicable.

## 2. Open-Loop Control Systems

An open-loop control system performs an action without measuring its output and using that measurement to correct the action.

The controller operates according to a predetermined command.

### 2.1 Example

A basic electric heater operated using a timer is an open-loop system.

The heater runs for a specified duration without measuring the actual room temperature.

### 2.2 Advantages

- Simple design.
- Low cost.
- Easy implementation.
- Generally fewer components.

### 2.3 Disadvantages

- Cannot automatically correct disturbances.
- Output accuracy depends on system conditions.
- Performance may change when the load changes.

## 3. Closed-Loop Control Systems

A closed-loop control system measures its output and uses feedback to adjust its operation.

The actual output is compared with the desired reference input.

The difference is called the error signal.

\[
\boxed{e(t)=r(t)-y(t)}
\]

Where:

- \(r(t)\) = reference input.
- \(y(t)\) = measured output.
- \(e(t)\) = error signal.

The controller uses the error to determine the required corrective action.

### 3.1 Example

A thermostat measures room temperature and compares it with the desired temperature.

If the room is too cold, the heater is activated.

If the room becomes sufficiently warm, the controller reduces or stops heating.

### 3.2 Advantages

- Corrects deviations automatically.
- Can reduce the effect of disturbances.
- Improves regulation and accuracy when properly designed.

### 3.3 Disadvantages

- More complex than open-loop control.
- Requires sensors and feedback paths.
- Poor design can cause oscillation or instability.

## 4. Open-Loop and Closed-Loop Comparison

| Property | Open-loop | Closed-loop |
|---|---|---|
| Feedback | Absent | Present |
| Output measurement | Not used for correction | Used for correction |
| Complexity | Usually lower | Usually higher |
| Disturbance correction | Limited | Possible |
| Stability concerns | Generally simpler | Requires stability analysis |
| Example | Timer-based heater | Thermostat |

## 5. Negative Feedback

Negative feedback occurs when a portion of the output is subtracted from the reference input.

The error is:

\[
e=r-Hy
\]

Where:

- \(r\) = reference input.
- \(H\) = feedback transfer function.
- \(y\) = output.

Negative feedback can improve:

- Accuracy.
- Stability margins when properly designed.
- Disturbance rejection.
- Bandwidth.
- Sensitivity to component variations.

However, excessive feedback or unsuitable phase behaviour can produce instability.

## 6. Positive Feedback

Positive feedback occurs when the feedback signal reinforces the reference input.

It is used in certain circuits and systems, including:

- Oscillators.
- Schmitt triggers.
- Regenerative circuits.

Positive feedback can increase gain and produce switching or oscillatory behaviour.

It must be designed carefully because uncontrolled positive feedback can cause instability.

## 7. Transfer Functions

A transfer function describes the relationship between a system's output and input in the Laplace domain under specified initial conditions, commonly taken as zero.

\[
\boxed{G(s)=\frac{Y(s)}{X(s)}}
\]

Where:

- \(G(s)\) = transfer function.
- \(Y(s)\) = output in the Laplace domain.
- \(X(s)\) = input in the Laplace domain.

Transfer functions are widely used in linear time-invariant control-system analysis.

## 8. Closed-Loop Transfer Function

Consider a negative-feedback system with:

- Forward-path transfer function \(G(s)\).
- Feedback transfer function \(H(s)\).

The closed-loop transfer function is:

\[
\boxed{
T(s)=\frac{G(s)}{1+G(s)H(s)}
}
\]

For unity feedback:

\[
H(s)=1
\]

Therefore:

\[
\boxed{
T(s)=\frac{G(s)}{1+G(s)}
}
\]

The expression assumes the standard negative-feedback configuration.

## 9. System Response

A control system's response describes how its output changes when an input is applied.

Important response characteristics include:

### 9.1 Rise Time

Rise time is the time required for the output to rise between specified lower and upper percentages of its final value.

The exact definition depends on the engineering convention.

### 9.2 Settling Time

Settling time is the time required for the output to enter and remain within a specified tolerance band around its final value.

### 9.3 Overshoot

Overshoot is the amount by which the response exceeds its final value during a transient response.

### 9.4 Steady-State Error

Steady-state error is the difference between the reference and output after transient effects have sufficiently decayed.

For unity feedback:

\[
e_{ss}=\lim_{t\to\infty}[r(t)-y(t)]
\]

when the limit exists.

## 10. Stability

A stable control system produces a bounded response under the specified stability conditions.

An unstable system may exhibit growing oscillations or an output that increases without bound.

Stability is influenced by:

- System poles.
- Feedback gain.
- Time delays.
- Component parameters.
- Phase shift.
- System dynamics.

For continuous-time linear time-invariant systems, the locations of closed-loop poles are central to determining internal stability.

## 11. PID Controller

A Proportional-Integral-Derivative (PID) controller is widely used in industrial control systems.

It combines three control actions.

### 11.1 Proportional Control

Proportional control produces an output proportional to the present error.

\[
\boxed{u_P(t)=K_Pe(t)}
\]

Where \(K_P\) is the proportional gain.

Increasing proportional gain generally makes the response more aggressive, but excessive gain may cause overshoot or instability.

### 11.2 Integral Control

Integral control depends on the accumulated error over time.

\[
\boxed{
u_I(t)=K_I\int_0^t e(\tau)d\tau
}
\]

Integral action can eliminate steady-state error for suitable systems, but excessive integral action may cause overshoot and slow recovery.

### 11.3 Derivative Control

Derivative control depends on the rate of change of error.

\[
\boxed{
u_D(t)=K_D\frac{de(t)}{dt}
}
\]

Derivative action can improve damping and help reduce overshoot.

It is sensitive to measurement noise, so practical systems often filter the derivative term.

### 11.4 Complete PID Equation

\[
\boxed{
u(t)=K_Pe(t)+K_I\int_0^t e(\tau)d\tau
+K_D\frac{de(t)}{dt}
}
\]

## 12. Sensors and Actuators in Control Systems

A sensor measures the physical output or condition of a system.

An actuator changes the physical behaviour of the system.

Examples:

| Control application | Sensor | Actuator |
|---|---|---|
| Temperature control | Temperature sensor | Heater |
| Motor speed control | Encoder or speed sensor | Motor drive |
| Position control | Position sensor | Servo motor |
| Pressure control | Pressure sensor | Control valve |
| Light control | Light sensor | LED driver |

The sensor provides feedback, while the actuator implements the control action.

## 13. Practical Electronic Control Systems

### 13.1 Voltage Regulation

A voltage regulator measures output voltage and adjusts its operation to maintain a desired value.

### 13.2 Motor Speed Control

A controller measures motor speed and adjusts the drive signal to maintain the required speed.

### 13.3 Temperature Control

A controller compares measured temperature with a setpoint and regulates a heating or cooling element.

### 13.4 Position Control

A position-control system compares the desired position with the measured position and drives a motor to reduce the error.

## 14. Worked Numerical Examples

### Example 1: Feedback Error

**Given:**

A temperature controller has:

\[
T_{reference}=30^\circ C
\]

\[
T_{measured}=26^\circ C
\]

Calculate the error.

**Formula:**

\[
e=r-y
\]

**Solution:**

\[
e=30-26
\]

\[
e=4^\circ C
\]

**Final Answer:**

\[
\boxed{e=4^\circ C}
\]

The controller must act to increase the temperature.

### Example 2: Closed-Loop Gain

**Given:**

A negative-feedback system has:

\[
G=100
\]

\[
H=0.1
\]

Calculate the closed-loop gain.

**Formula:**

\[
T=\frac{G}{1+GH}
\]

**Solution:**

\[
T=\frac{100}{1+(100)(0.1)}
\]

\[
T=\frac{100}{11}
\]

\[
T\approx9.09
\]

**Final Answer:**

\[
\boxed{T\approx9.09}
\]

### Example 3: Proportional Controller Output

**Given:**

A proportional controller has:

\[
K_P=5
\]

\[
e=2
\]

Calculate the proportional control output.

**Formula:**

\[
u_P=K_Pe
\]

**Solution:**

\[
u_P=5\times2
\]

\[
u_P=10
\]

**Final Answer:**

\[
\boxed{u_P=10}
\]

## 15. Applications

Feedback and control systems are used in:

- Industrial automation.
- Robotics.
- Electric motor drives.
- Automotive control.
- Aerospace systems.
- Power supplies.
- Temperature regulation.
- Process industries.
- Renewable-energy systems.

## 16. Common Examination Traps

1. Open-loop systems do not use output feedback for correction.
2. Closed-loop systems use measured output.
3. Error is the difference between the reference and feedback signal.
4. Negative feedback subtracts the feedback signal from the reference.
5. Positive feedback reinforces the input.
6. Negative feedback can improve regulation but does not automatically guarantee stability.
7. A transfer function describes an input-output relationship in the Laplace domain.
8. Closed-loop gain depends on both forward and feedback paths.
9. Overshoot is different from steady-state error.
10. Settling time describes how quickly the response remains within a specified tolerance band.
11. Integral control acts on accumulated error.
12. Derivative control acts on the rate of change of error.
13. Excessive controller gain can cause undesirable behaviour.
14. Sensors measure conditions, while actuators produce physical actions.
15. A PID controller combines proportional, integral, and derivative actions.

## Quiz

1. Which control system uses measured output to correct its operation?

   - [ ] Open-loop system.
   - [x] Closed-loop system.
   - [ ] Uncontrolled system.
   - [ ] Passive circuit only.

   > A closed-loop system measures its output, compares it with the reference, and uses the resulting error signal to determine corrective action.

2. Which PID control action depends on the accumulated error over time?

   - [ ] Proportional.
   - [x] Integral.
   - [ ] Derivative.
   - [ ] Switching.

   > Integral control evaluates the accumulated error through integration. It can eliminate steady-state error in suitable systems when properly tuned.

3. What is the main purpose of negative feedback in a control system?

   - [ ] To reinforce the reference signal.
   - [ ] To eliminate the need for sensors.
   - [x] To compare and correct deviations between the reference and feedback signals.
   - [ ] To guarantee instability.

   > Negative feedback subtracts the feedback signal from the reference. The controller uses the resulting error to reduce deviations and regulate the system.