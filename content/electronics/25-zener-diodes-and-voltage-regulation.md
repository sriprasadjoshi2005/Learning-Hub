---
title: Zener Diodes and Voltage Regulation
level: intermediate
---

# Zener Diodes and Voltage Regulation

A Zener diode is a specially designed semiconductor diode intended to operate safely in its reverse-breakdown region.

Unlike an ordinary PN junction diode, which is generally operated in forward bias or below reverse breakdown, a Zener diode is designed to maintain a relatively stable voltage across its terminals when operating within its specified current range.

This property makes Zener diodes useful in voltage regulation, voltage references, overvoltage protection, and waveform-limiting circuits.

This lesson explains Zener diode construction, reverse-breakdown behaviour, voltage regulation, current calculations, power ratings, and practical circuit design.

## 1. Introduction to Zener Diodes

A Zener diode is a semiconductor device designed to operate in reverse bias beyond its breakdown voltage.

Its symbol resembles an ordinary diode symbol, but the cathode line is bent.

A simplified representation is:

    Anode                 Cathode
      |                      |
      ──────────|>|───────────
                 bent bar

A Zener diode is normally connected in reverse bias when used as a voltage regulator.

Its important characteristics include:

- Specified Zener voltage.
- Minimum operating current.
- Maximum operating current.
- Maximum power dissipation.
- Dynamic resistance.
- Temperature coefficient.

## 2. Zener Breakdown

When a PN junction diode is reverse-biased, a small reverse current flows.

As reverse voltage increases, the junction may eventually enter breakdown.

A Zener diode is designed so that this breakdown region can be used safely within specified electrical and thermal limits.

### 2.1 Zener Breakdown Mechanism

Zener breakdown occurs when the electric field across a heavily doped junction becomes sufficiently strong to allow electrons to tunnel through the energy barrier.

Important characteristics:

- Usually associated with heavily doped junctions.
- The depletion region is relatively narrow.
- Can occur at relatively low breakdown voltages.
- The electric field is extremely strong.

### 2.2 Avalanche Breakdown Mechanism

Avalanche breakdown occurs when accelerated charge carriers gain sufficient energy to produce additional electron-hole pairs through impact ionization.

Important characteristics:

- Often associated with more lightly doped junctions.
- The depletion region is comparatively wider.
- Carrier multiplication causes reverse current to increase sharply.

In practical Zener diodes, both mechanisms may contribute depending on the breakdown voltage.

### 2.3 Breakdown Voltage

The reverse voltage at which the diode enters its specified breakdown region is called the Zener voltage.

It is represented by:

\[
V_Z
\]

For example, a diode with a nominal Zener voltage of 5.1 V is designed to maintain approximately 5.1 V across itself at its specified test current and operating conditions.

The voltage is not perfectly constant under every current and temperature condition.

## 3. Zener Diode Characteristics

The current-voltage characteristic contains two important regions.

### 3.1 Forward-Bias Region

In forward bias, a Zener diode behaves approximately like an ordinary silicon diode.

A significant forward current flows when the forward voltage becomes sufficiently large.

### 3.2 Reverse-Bias Region

In reverse bias:

- A small leakage current flows before breakdown.
- At the breakdown voltage, reverse current increases rapidly.
- The voltage across the diode changes relatively little over a useful operating-current range.

This nearly constant-voltage behaviour is the basis of Zener regulation.

### 3.3 Simplified Characteristic

    Current I
       ↑
       |                         /
       |                       /
       |                     /
       |___________________/________→ Voltage V
       |
       |     Reverse leakage
       |-------------------------
       |          |
       |          |
       |          ↓
       |       Breakdown
       |       region

The reverse breakdown region is where the Zener diode is normally used for regulation.

## 4. Zener Diode as a Voltage Regulator

A Zener voltage regulator commonly consists of:

- An unregulated DC supply.
- A series resistor.
- A reverse-biased Zener diode.
- A load connected in parallel with the Zener diode.

The Zener diode maintains approximately constant load voltage while its current remains within the permitted operating range.

### 4.1 Circuit Arrangement

    V_in
      +
      |
      R_s
      |
      +───────────────+
      |               |
     Zener           R_L
      |               |
      +───────────────+
      |
     0 V

The Zener diode and load resistor are connected in parallel.

The Zener diode's cathode is connected towards the positive regulated output.

### 4.2 Working Principle

When the input voltage is sufficiently high:

1. Current flows through the series resistor.
2. The Zener diode enters reverse breakdown.
3. The Zener voltage remains approximately constant.
4. The load receives a regulated voltage.

The series resistor limits current and protects the Zener diode.

Without a suitable series resistor or another current-limiting mechanism, the Zener diode could be damaged by excessive current.

## 5. Current Relationships in a Zener Regulator

The current flowing through the series resistor divides into two branches:

- Zener current.
- Load current.

By Kirchhoff's current law:

\[
I_S=I_Z+I_L
\]

Where:

- \(I_S\) = series resistor current.
- \(I_Z\) = Zener current.
- \(I_L\) = load current.

The series resistor current is:

\[
I_S=\frac{V_{in}-V_Z}{R_S}
\]

The load current is:

\[
I_L=\frac{V_Z}{R_L}
\]

Therefore:

\[
\boxed{I_Z=\frac{V_{in}-V_Z}{R_S}-\frac{V_Z}{R_L}}
\]

This equation is valid when the Zener diode is operating in breakdown and the output voltage is approximately \(V_Z\).

## 6. Conditions for Proper Regulation

A Zener diode must operate within a permitted current range.

### 6.1 Minimum Zener Current

The Zener current must be sufficiently large to keep the diode in its useful breakdown region.

The minimum specified current is often represented by:

\[
I_{Z(min)}
\]

### 6.2 Maximum Zener Current

The Zener current must not exceed the maximum permitted value.

The maximum value depends on the power rating and voltage of the diode.

### 6.3 Zener Power Dissipation

The power dissipated by the Zener diode is:

\[
P_Z=V_ZI_Z
\]

Therefore:

\[
I_{Z(max)}=\frac{P_{Z(max)}}{V_Z}
\]

Where:

- \(P_{Z(max)}\) = maximum permitted Zener power.
- \(V_Z\) = nominal Zener voltage.

The operating current must satisfy:

\[
I_{Z(min)}\leq I_Z\leq I_{Z(max)}
\]

The diode must also remain within its temperature and thermal limits.

## 7. Designing a Zener Regulator

A suitable series resistor must be selected to maintain regulation under the expected input-voltage and load-current variations.

For the minimum input voltage and maximum load current, enough current must remain for the Zener diode to regulate.

The design condition is:

\[
\frac{V_{in(min)}-V_Z}{R_S}
\geq I_{L(max)}+I_{Z(min)}
\]

Rearranging:

\[
\boxed{R_S\leq
\frac{V_{in(min)}-V_Z}
{I_{L(max)}+I_{Z(min)}}}
\]

The maximum Zener current must also be checked at maximum input voltage and minimum load current.

For a fixed load resistor:

\[
I_{Z(max,actual)}
=
\frac{V_{in(max)}-V_Z}{R_S}
-I_{L(min)}
\]

The chosen resistor must ensure that the resulting Zener power remains within the device rating.

## 8. Line Regulation and Load Regulation

### 8.1 Line Regulation

Line regulation describes the ability of a regulator to maintain a stable output voltage when the input voltage changes.

A Zener regulator compensates for input variations by changing its Zener current.

When input voltage increases:

- Series resistor current increases.
- Zener current generally increases.
- Output voltage remains approximately constant.

### 8.2 Load Regulation

Load regulation describes the ability of a regulator to maintain its output voltage when load current changes.

When load current increases:

- More current flows through the load.
- Less current remains for the Zener diode.
- The output remains regulated as long as the Zener current stays above its minimum operating value.

If the load current becomes too high, the Zener current may fall below the required value.

The diode then leaves its regulation region and the output voltage may decrease.

## 9. Dynamic Resistance of a Zener Diode

A real Zener diode does not have perfectly constant voltage.

Its voltage changes slightly when the current changes.

The small-signal or dynamic resistance is:

\[
r_Z=\frac{\Delta V_Z}{\Delta I_Z}
\]

A lower dynamic resistance generally indicates better voltage stability over the operating region.

For small changes:

\[
\Delta V_Z\approx r_Z\Delta I_Z
\]

This relationship helps estimate output variation caused by changing Zener current.

## 10. Worked Numerical Examples

### Example 1: Zener Regulator Current

**Given:**

- Input voltage: \(V_{in}=12\,V\).
- Zener voltage: \(V_Z=5.1\,V\).
- Series resistance: \(R_S=330\,\Omega\).
- Load resistance: \(R_L=1\,k\Omega\).

Assume the Zener diode is operating in breakdown.

Calculate the series current, load current, and Zener current.

**Formula:**

\[
I_S=\frac{V_{in}-V_Z}{R_S}
\]

\[
I_L=\frac{V_Z}{R_L}
\]

\[
I_Z=I_S-I_L
\]

**Solution:**

Series current:

\[
I_S=\frac{12-5.1}{330}
\]

\[
I_S=\frac{6.9}{330}
\]

\[
I_S=20.91\,mA
\]

Load current:

\[
I_L=\frac{5.1}{1000}
\]

\[
I_L=5.1\,mA
\]

Zener current:

\[
I_Z=20.91-5.1
\]

\[
I_Z=15.81\,mA
\]

**Final Answer:**

\[
\boxed{I_S=20.91\,mA}
\]

\[
\boxed{I_L=5.1\,mA}
\]

\[
\boxed{I_Z=15.81\,mA}
\]

### Example 2: Zener Power Dissipation

**Given:**

- Zener voltage: \(V_Z=6.2\,V\).
- Zener current: \(I_Z=25\,mA\).

Calculate the power dissipated by the Zener diode.

**Formula:**

\[
P_Z=V_ZI_Z
\]

**Solution:**

\[
P_Z=6.2\times25\times10^{-3}
\]

\[
P_Z=0.155\,W
\]

**Final Answer:**

\[
\boxed{P_Z=155\,mW}
\]

The selected Zener diode must have a power rating greater than the calculated dissipation, with suitable thermal and design margins.

### Example 3: Selecting a Series Resistor

**Given:**

- Minimum input voltage: \(V_{in(min)}=10\,V\).
- Zener voltage: \(V_Z=5\,V\).
- Maximum load current: \(I_{L(max)}=20\,mA\).
- Required minimum Zener current: \(I_{Z(min)}=5\,mA\).

Calculate the maximum permitted series resistance.

**Formula:**

\[
R_S\leq
\frac{V_{in(min)}-V_Z}
{I_{L(max)}+I_{Z(min)}}
\]

**Solution:**

\[
R_S\leq
\frac{10-5}{20\times10^{-3}+5\times10^{-3}}
\]

\[
R_S\leq\frac{5}{0.025}
\]

\[
R_S\leq200\,\Omega
\]

**Final Answer:**

\[
\boxed{R_S\leq200\,\Omega}
\]

A practical resistor value must also be checked under maximum input voltage and minimum load current to ensure that the Zener diode does not exceed its maximum current or power rating.

## 11. Zener Diode as a Voltage Reference

A voltage reference provides a stable voltage for other circuit sections.

Zener diodes are often used as simple voltage references.

Applications include:

- Comparator reference inputs.
- Basic regulator circuits.
- Measurement equipment.
- Overvoltage detection.
- Power supply protection.

Precision voltage references may use more advanced semiconductor structures because ordinary Zener diodes have temperature coefficients, dynamic resistance, and noise.

## 12. Zener Diode as a Protection Device

A Zener diode can limit the voltage across a circuit.

If the applied voltage exceeds the intended limit, the diode enters breakdown and conducts current.

This can help protect sensitive components.

However, the surrounding circuit must safely handle the resulting current and power.

For fast transient protection, specialised devices such as TVS diodes are often more appropriate.

## 13. Limitations of Zener Regulators

Although Zener regulators are simple, they have limitations:

1. They can waste power through continuous current flow.
2. Their output voltage is not perfectly constant.
3. Their regulation range is limited.
4. They are less efficient for large load currents.
5. Temperature affects their characteristics.
6. They require a suitable current-limiting element.
7. They are generally less suitable than dedicated regulators for high-power applications.

## 14. Common Examination Traps

1. A Zener diode is normally used in reverse breakdown when regulating voltage.
2. The series resistor limits current; it is not optional in a basic shunt regulator.
3. Zener current is the difference between series current and load current.
4. The Zener diode and load are connected in parallel.
5. Zener voltage is approximately constant only within the specified operating range.
6. Maximum power dissipation must not be exceeded.
7. Increasing load current generally reduces the Zener current.
8. Increasing input voltage generally increases Zener current.
9. A Zener diode does not produce an exactly constant voltage under all conditions.
10. Zener breakdown and avalanche breakdown are different physical mechanisms.

## Quiz

1. How is a Zener diode normally connected when used as a voltage regulator?

- [ ] In forward bias without a series resistor.
- [x] In reverse bias with a suitable current-limiting resistor.
- [ ] In series with the load in forward bias.
- [ ] With both terminals connected to ground.

> A Zener regulator uses the reverse-breakdown region of the diode. A series resistor limits current and protects the diode from excessive power dissipation.

2. A Zener regulator has a series current of 30 mA and a load current of 18 mA. What is the Zener current?

- [ ] 48 mA.
- [ ] 30 mA.
- [x] 12 mA.
- [ ] 18 mA.

> By Kirchhoff's current law, \(I_S=I_Z+I_L\). Therefore, \(I_Z=30-18=12\,mA\).

3. A 5.6 V Zener diode carries 20 mA. Calculate its power dissipation.

- [ ] 11.2 W.
- [ ] 0.0112 W.
- [x] 0.112 W.
- [ ] 2.8 W.

> \(P_Z=V_ZI_Z=5.6\times0.020=0.112\,W\), which is 112 mW.
