---
title: Transient Response of RC and RL Circuits
level: advanced
---

# Transient Response of RC and RL Circuits

## Introduction

Electrical circuits do not always operate under steady-state conditions. When a switch is operated, a source is connected or disconnected, or circuit conditions change, voltages and currents may vary over time before reaching a new steady state.

This temporary behaviour is known as the transient response.

Resistor-capacitor (RC) and resistor-inductor (RL) circuits are fundamental first-order circuits used to understand transient behaviour.

An RC circuit stores energy in an electric field, while an RL circuit stores energy in a magnetic field. Both exhibit exponential charging or current-response characteristics.

This lesson develops the differential equations governing RC and RL circuits, introduces time constants, examines charging and discharging processes, and solves numerical problems involving transient responses.

## 1. Introduction to Transient Response

A transient is the temporary change in circuit voltage or current following a change in operating conditions.

Examples include:

- A capacitor charging after a switch is closed.
- A capacitor discharging through a resistor.
- Current increasing in an inductor after a voltage is applied.
- Inductor current decreasing after a supply is removed.
- Voltage changes during switching operations.

The transient response eventually approaches a steady-state condition in a stable first-order circuit.

The total response is often expressed as:

\[
\boxed{\text{Total response}=\text{Transient response}+\text{Steady-state response}}
\]

The transient component decays with time in ordinary stable passive RC and RL circuits.

## 2. First-Order Circuits

A first-order circuit contains one independent energy-storage element.

Examples include:
- One capacitor with resistors.
- One inductor with resistors.

Its governing differential equation is generally first order.

The response contains one exponential term.

The general first-order response can be written as:

\[
\boxed{x(t)=x(\infty)+[x(0^+)-x(\infty)]e^{-t/\tau}}
\]

Where:
- \(x(t)\) = circuit variable at time \(t\).
- \(x(0^+)\) = value immediately after switching.
- \(x(\infty)\) = final steady-state value.
- \(\tau\) = time constant.

This form is useful for both RC and RL circuits.

## 3. Time Constant

The time constant determines how quickly a first-order circuit approaches its final value.

### 3.1 RC Time Constant

For an RC circuit:

\[
\boxed{\tau=RC}
\]

Where:
- \(R\) = resistance in ohms.
- \(C\) = capacitance in farads.
- \(\tau\) = time in seconds.

### 3.2 RL Time Constant

For an RL circuit:

\[
\boxed{\tau=\frac{L}{R}}
\]

Where:
- \(L\) = inductance in henries.
- \(R\) = resistance in ohms.
- \(\tau\) = time in seconds.

The resistance used in these expressions is the equivalent resistance seen by the energy-storage element with independent sources deactivated, considering the circuit's switching configuration.

## 4. RC Charging Circuit

Consider a resistor and capacitor connected in series with a DC voltage source.

Initially, assume the capacitor is uncharged.

When the switch is closed:
1. Current begins to flow.
2. The capacitor accumulates charge.
3. Capacitor voltage increases.
4. Circuit current decreases.
5. The capacitor approaches the supply voltage.

### 4.1 Derivation of the Charging Equation

Applying Kirchhoff's voltage law:

\[
V_s=v_R+v_C
\]

Using Ohm's law:

\[
v_R=iR
\]

For a capacitor:

\[
i=C\frac{dv_C}{dt}
\]

Substituting:

\[
V_s=RC\frac{dv_C}{dt}+v_C
\]

Rearranging:

\[
\frac{dv_C}{dt}=\frac{V_s-v_C}{RC}
\]

Solving the first-order differential equation with initial condition \(v_C(0)=0\):

\[
\boxed{v_C(t)=V_s(1-e^{-t/RC})}
\]

The capacitor voltage rises exponentially toward the supply voltage.

### 4.2 Charging Current

Using:

\[
i=C\frac{dv_C}{dt}
\]

Differentiate the charging equation:

\[
\boxed{i(t)=\frac{V_s}{R}e^{-t/RC}}
\]

The initial current is:

\[
\boxed{i(0^+)=\frac{V_s}{R}}
\]

The final current is:

\[
\boxed{i(\infty)=0}
\]

### 4.3 Resistor Voltage

Since:

\[
v_R=V_s-v_C
\]

\[
\boxed{v_R(t)=V_se^{-t/RC}}
\]

The resistor voltage decreases exponentially.

## 5. RC Discharging Circuit

A charged capacitor can discharge through a resistor when the supply is disconnected and a closed discharge path is provided.

The capacitor releases its stored energy through the resistor.

Applying KVL:

\[
v_R+v_C=0
\]

Using:

\[
i=C\frac{dv_C}{dt}
\]

The resulting differential equation gives:

\[
\boxed{v_C(t)=V_0e^{-t/RC}}
\]

Where \(V_0\) is the initial capacitor voltage.

The magnitude of discharge current is:

\[
\boxed{|i(t)|=\frac{V_0}{R}e^{-t/RC}}
\]

The actual current direction is opposite to the charging-current direction under the same reference convention.

## 6. RC Charging and Discharging Characteristics

The capacitor charging voltage is:

\[
v_C(t)=V_s(1-e^{-t/\tau})
\]

The discharging voltage is:

\[
v_C(t)=V_0e^{-t/\tau}
\]

The approximate response at different time intervals is:

| Time | Charging voltage | Discharging voltage |
|---|---:|---:|
| \(0\tau\) | 0% | 100% |
| \(1\tau\) | 63.2% | 36.8% |
| \(2\tau\) | 86.5% | 13.5% |
| \(3\tau\) | 95.0% | 5.0% |
| \(4\tau\) | 98.2% | 1.8% |
| \(5\tau\) | 99.3% | 0.7% |

After approximately five time constants, the transient is generally considered practically complete.

## 7. Initial and Final Conditions of a Capacitor

An ideal capacitor voltage cannot change instantaneously if the current remains finite.

Therefore:

\[
\boxed{v_C(0^+)=v_C(0^-)}
\]

The voltage immediately after switching equals the voltage immediately before switching.

### 7.1 Initially Uncharged Capacitor

At the instant of connection to a DC source, an initially uncharged ideal capacitor behaves like a short circuit in terms of its initial voltage.

Its voltage is zero at \(t=0^+\).

As time passes, it charges.

### 7.2 Fully Charged Capacitor

At DC steady state:

\[
\frac{dv_C}{dt}=0
\]

Therefore:

\[
i_C=0
\]

An ideal capacitor behaves as an open circuit at steady state.

## 8. RL Transient Response

An RL circuit consists of a resistor and inductor connected in a network.

When a DC voltage is applied, current does not immediately reach its final value because the inductor opposes changes in current.

### 8.1 RL Current Growth

Consider a series RL circuit connected to a DC voltage source.

Applying KVL:

\[
V_s=Ri+L\frac{di}{dt}
\]

Rearranging:

\[
\frac{di}{dt}+\frac{R}{L}i=\frac{V_s}{L}
\]

For an initially unenergised inductor, the solution is:

\[
\boxed{i(t)=\frac{V_s}{R}(1-e^{-tR/L})}
\]

Since:

\[
\tau=\frac{L}{R}
\]

The equation becomes:

\[
\boxed{i(t)=\frac{V_s}{R}(1-e^{-t/\tau})}
\]

### 8.2 Inductor Voltage During Current Growth

The inductor voltage is:

\[
v_L=L\frac{di}{dt}
\]

Differentiating the current equation:

\[
\boxed{v_L(t)=V_se^{-t/\tau}}
\]

Initially:

\[
v_L(0^+)=V_s
\]

At steady state:

\[
v_L(\infty)=0
\]

The resistor voltage increases as the inductor voltage decreases.

## 9. RL Current Decay

When the source is removed from a series RL circuit while a closed current path remains, the inductor releases its stored magnetic energy through the resistance.

Applying KVL:

\[
L\frac{di}{dt}+Ri=0
\]

Solving:

\[
\boxed{i(t)=I_0e^{-Rt/L}}
\]

Or:

\[
\boxed{i(t)=I_0e^{-t/\tau}}
\]

Where \(I_0\) is the initial current.

The inductor current cannot change instantaneously:

\[
\boxed{i_L(0^+)=i_L(0^-)}
\]

The current gradually approaches zero.

## 10. Initial and Final Conditions of an Inductor

An ideal inductor current cannot change instantaneously under finite applied voltage.

Therefore:

\[
\boxed{i_L(0^+)=i_L(0^-)}
\]

### 10.1 Initially Unenergised Inductor

If the initial current is zero:

\[
i_L(0^-)=0
\]

Then:

\[
i_L(0^+)=0
\]

The current starts from zero and increases according to the applied circuit conditions.

### 10.2 Inductor at DC Steady State

For constant current:

\[
\frac{di}{dt}=0
\]

Therefore:

\[
v_L=0
\]

An ideal inductor behaves as a short circuit under DC steady-state conditions.

A practical inductor retains its winding resistance.

## 11. Comparing RC and RL Transients

| Property | RC circuit | RL circuit |
|---|---|---|
| Energy-storage element | Capacitor | Inductor |
| Stored energy | Electric field | Magnetic field |
| Time constant | \(RC\) | \(L/R\) |
| Continuous state variable | Capacitor voltage | Inductor current |
| Initial ideal behaviour when unenergised | Short circuit | Open circuit |
| Final DC steady-state behaviour | Open circuit | Short circuit |
| Charging or growth response | Exponential | Exponential |

## 12. General First-Order Response Formula

For a variable that moves from an initial value to a final value:

\[
\boxed{x(t)=x_f+(x_0-x_f)e^{-t/\tau}}
\]

This equation is particularly useful because it avoids deriving a separate expression for every circuit.

Examples:

For capacitor voltage:

\[
v_C(t)=V_f+(V_0-V_f)e^{-t/RC}
\]

For inductor current:

\[
i_L(t)=I_f+(I_0-I_f)e^{-tR/L}
\]

The initial and final values must be determined from the actual circuit.

## 13. Worked Numerical Examples

### Example 1: RC Charging

**Given:**

- Supply voltage = 10 V.
- Resistance = 20 kΩ.
- Capacitance = 50 μF.
- Initial capacitor voltage = 0 V.

**Find:** Time constant and capacitor voltage after one time constant.

**Solution:**

Time constant:

\[
\tau=RC
\]

\[
\tau=20,000\times50\times10^{-6}
\]

\[
\boxed{\tau=1\text{ s}}
\]

At \(t=\tau\):

\[
v_C=V_s(1-e^{-1})
\]

\[
v_C=10(1-0.3679)
\]

\[
\boxed{v_C\approx6.32\text{ V}}
\]

### Example 2: RC Discharging

**Given:**

- Initial capacitor voltage = 12 V.
- Resistance = 10 kΩ.
- Capacitance = 100 μF.
- Time = 2 seconds.

**Find:** Remaining capacitor voltage.

**Solution:**

Time constant:

\[
\tau=RC
\]

\[
\tau=10,000\times100\times10^{-6}
\]

\[
\tau=1\text{ s}
\]

Discharging equation:

\[
v_C(t)=V_0e^{-t/\tau}
\]

\[
v_C(2)=12e^{-2}
\]

\[
\boxed{v_C\approx1.624\text{ V}}
\]

### Example 3: RL Current Growth

**Given:**

- Supply voltage = 24 V.
- Resistance = 12 Ω.
- Inductance = 6 H.
- Initial current = 0 A.

**Find:** Time constant and current after one time constant.

**Solution:**

\[
\tau=\frac{L}{R}
\]

\[
\tau=\frac{6}{12}
\]

\[
\boxed{\tau=0.5\text{ s}}
\]

Final steady-state current:

\[
I_f=\frac{V_s}{R}
\]

\[
I_f=\frac{24}{12}=2\text{ A}
\]

At one time constant:

\[
i=I_f(1-e^{-1})
\]

\[
i=2(0.6321)
\]

\[
\boxed{i\approx1.264\text{ A}}
\]

### Example 4: RL Current Decay

**Given:**

- Initial current = 5 A.
- Inductance = 2 H.
- Resistance = 4 Ω.
- Time = 1 second.

**Find:** Remaining current.

**Solution:**

Time constant:

\[
\tau=\frac{L}{R}
\]

\[
\tau=\frac{2}{4}=0.5\text{ s}
\]

Current decay:

\[
i(t)=I_0e^{-t/\tau}
\]

\[
i(1)=5e^{-1/0.5}
\]

\[
i(1)=5e^{-2}
\]

\[
\boxed{i\approx0.677\text{ A}}
\]

### Example 5: Determining Capacitance from a Required Time Constant

**Given:**

- Required time constant = 0.2 s.
- Resistance = 40 kΩ.

**Find:** Required capacitance.

**Formula:**

\[
\tau=RC
\]

Rearranging:

\[
C=\frac{\tau}{R}
\]

**Solution:**

\[
C=\frac{0.2}{40,000}
\]

\[
C=5\times10^{-6}\text{ F}
\]

\[
\boxed{C=5\ \mu\text{F}}
\]

## 14. Practical Applications

Transient-response analysis is used in:

- Timing circuits.
- Signal delay networks.
- Power-supply startup circuits.
- Switching regulators.
- Relay and solenoid protection.
- Pulse-shaping circuits.
- Reset circuits.
- Sensor response networks.
- Filter design.
- Electronic switching systems.

### 14.1 RC Timing

An RC network can generate a time delay because the capacitor voltage changes gradually.

This principle is used in simple timers and reset circuits.

### 14.2 RL Switching

Inductors store magnetic energy and resist current changes.

This property is important in switching power supplies and motor-control circuits.

### 14.3 Protection Circuits

When inductive loads are switched off, the inductor may generate a high voltage.

Flyback diodes and snubber circuits provide controlled paths for stored energy.

## 15. Common Exam Traps

1. **Using the wrong time constant:** RC circuits use \(RC\), while RL circuits use \(L/R\).

2. **Assuming capacitor voltage changes instantaneously:** Ideal capacitor voltage is continuous.

3. **Assuming inductor current changes instantaneously:** Ideal inductor current is continuous.

4. **Confusing initial and final conditions:** Determine the circuit conditions immediately before and long after switching.

5. **Forgetting the exponential sign:** Charging uses \(1-e^{-t/\tau}\); discharging uses \(e^{-t/\tau}\).

6. **Using the wrong resistance:** The resistance must be the equivalent resistance seen by the storage element in the relevant switching configuration.

7. **Treating five time constants as mathematically infinite:** It is approximately complete, not exactly complete.

8. **Ignoring switching paths:** An inductor requires a current path when its stored energy is released.

## Quiz

1. An RC circuit has a resistance of 10 kΩ and capacitance of 100 μF. What is its time constant?

   - [ ] 0.1 s
   - [x] 1 s
   - [ ] 10 s
   - [ ] 100 s

   > The RC time constant is \(\tau=RC=10,000\times100\times10^{-6}=1\) second.

2. In an initially uncharged ideal RC charging circuit, approximately what percentage of the final capacitor voltage is reached after one time constant?

   - [ ] 36.8%
   - [ ] 50%
   - [x] 63.2%
   - [ ] 100%

   > The charging equation is \(v_C=V_s(1-e^{-t/\tau})\). At \(t=\tau\), the fraction is \(1-e^{-1}\approx0.632\), or 63.2%.

3. A charged ideal inductor is disconnected from its original supply but retains a closed resistive current path. Which quantity must remain continuous immediately after switching?

   - [ ] Inductor voltage
   - [ ] Resistor voltage
   - [x] Inductor current
   - [ ] Resistor power

   > An ideal inductor cannot undergo an instantaneous current change under finite voltage. Its current immediately after switching equals its current immediately before switching.