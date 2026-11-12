---
title: Voltage and Electromotive Force
level: foundation
---

# Voltage and Electromotive Force

Voltage is one of the most important quantities in electronic circuit analysis. It describes the difference in electric potential between two points and determines how much energy is transferred per unit charge as charge moves through a circuit element.

Electromotive force (EMF) is closely related to voltage but describes the energy supplied per unit charge by a source such as a battery or generator. Understanding the distinction between EMF, terminal voltage and potential difference is essential when analysing practical power supplies and electronic circuits.

This lesson develops the concept of electric potential, potential difference, EMF, internal resistance, terminal voltage, electrical work and voltage measurement. By the end, you will be able to calculate electrical energy transfer, analyse practical voltage sources and distinguish ideal sources from real sources.

## 1. Electric Potential and Potential Difference

### 1.1 Electric Potential

Electric potential at a point is the electric potential energy per unit positive test charge.

$$V=\frac{U}{q}$$

Where:

- $V$ = electric potential in volts.
- $U$ = electric potential energy in joules.
- $q$ = test charge in coulombs.

Electric potential is a scalar quantity.

Its value depends on the chosen reference point, commonly taken as zero potential at infinity for isolated charge distributions.

### 1.2 Potential Difference

Potential difference between two points is the change in electric potential per unit charge.

$$V_{AB}=V_A-V_B$$

It can also be related to the work done by the electric field:

$$V_A-V_B=\frac{W_{field}}{q}$$

Here, $W_{field}$ is the work done by the electric field on a positive test charge moving from A to B.

The SI unit is the volt.

$$1\text{ V}=1\text{ J/C}$$

### 1.3 Physical Meaning of Voltage

A potential difference of 5 V means that the electric potential energy difference is 5 joules per coulomb of charge.

For a charge magnitude of 2 C moving through a 5 V potential difference, the magnitude of energy transferred is:

$$W=QV$$

$$W=2\times5=10\text{ J}$$

The direction of energy transfer depends on the charge sign and whether work is done by or against the electric field.

## 2. Electromotive Force

### 2.1 Definition of EMF

Electromotive force is the energy supplied by a source per unit charge passing through it.

$$\mathcal{E}=\frac{W_{source}}{Q}$$

Where:

- $\mathcal{E}$ = electromotive force in volts.
- $W_{source}$ = energy supplied by the source in joules.
- $Q$ = charge in coulombs.

Despite its name, EMF is not a mechanical force. It is an energy-per-unit-charge quantity and has the same SI unit as voltage.

### 2.2 Sources of EMF

Common electrical sources include:

1. **Chemical sources:** Batteries convert chemical energy into electrical energy.
2. **Electromagnetic sources:** Generators produce EMF through electromagnetic induction.
3. **Photovoltaic sources:** Solar cells convert light energy into electrical energy.
4. **Thermoelectric sources:** Thermoelectric devices produce voltage from temperature differences.
5. **Piezoelectric sources:** Certain materials develop electric potential when mechanically stressed.

### 2.3 Ideal Voltage Source

An ideal voltage source maintains a constant terminal voltage regardless of the current drawn by the load.

Its internal resistance is zero.

$$V_{terminal}=\mathcal{E}$$

An ideal voltage source is a mathematical model. Real sources always have limitations.

## 3. Internal Resistance and Terminal Voltage

### 3.1 Practical Voltage Source

A practical battery can be represented by an ideal EMF source connected in series with an internal resistance.

```text
        Internal resistance
     +------/\/\/\/\------+
     |        r           |
     |                    |
     |      Ideal         |
     +------ EMF ---------+
              |
         External load
```

The internal resistance causes a voltage drop when current flows.

### 3.2 Terminal Voltage During Discharge

When a source supplies current to an external load:

$$V=\mathcal{E}-Ir$$

Where:

- $V$ = terminal voltage.
- $\mathcal{E}$ = EMF.
- $I$ = discharge current.
- $r$ = internal resistance.

The internal voltage drop is:

$$V_r=Ir$$

Therefore, terminal voltage is less than EMF during discharge.

### 3.3 Terminal Voltage During Charging

When current is driven into a practical source during charging:

$$V=\mathcal{E}+Ir$$

The external charging voltage must overcome the source EMF and the internal resistive drop.

### 3.4 Open-Circuit Condition

When no current flows:

$$I=0$$

Therefore:

$$V=\mathcal{E}$$

The terminal voltage of an idealized practical source equals its EMF under open-circuit conditions.

## 4. Voltage Measurement

### 4.1 Voltmeter

A voltmeter measures the potential difference between two points.

It is connected in parallel with the component or circuit section being measured.

An ideal voltmeter has infinite input resistance so that it draws no current from the measured circuit.

### 4.2 Loading Effect

A practical voltmeter has finite input resistance.

When connected across a component, it forms a parallel resistance that may alter the original circuit voltage.

For a source resistance $R_s$ and voltmeter resistance $R_v$:

$$V_m=V_s\frac{R_v}{R_s+R_v}$$

A higher voltmeter input resistance reduces measurement error.

### 4.3 Ground Reference

In many electronic circuits, voltage is measured relative to a designated reference node called ground.

Ground is a circuit reference, not necessarily the same as the physical Earth connection.

## 5. Electric Potential Due to Point Charges

For a point charge:

$$V=\frac{kQ}{r}$$

Where:

- $Q$ = source charge.
- $r$ = distance from the charge.
- $k$ = Coulomb's constant.

For multiple point charges, potential is calculated by algebraically adding their individual contributions:

$$V_{total}=\sum_i\frac{kQ_i}{r_i}$$

Unlike electric force, electric potential is a scalar quantity.

## 6. Mathematical Derivations and Numerical Examples

### Example 1: Terminal Voltage of a Practical Battery

**Given:**

- Battery EMF = 12 V.
- Internal resistance = 0.4 $\Omega$.
- Discharge current = 2 A.

Determine terminal voltage.

**Formula:**

$$V=\mathcal{E}-Ir$$

**Solution:**

1. Calculate the internal voltage drop:

   $$V_r=2\times0.4=0.8\text{ V}$$

2. Subtract the internal voltage drop from EMF:

   $$V=12-0.8$$

   $$V=11.2\text{ V}$$

**Final Answer:**

The battery terminal voltage is **11.2 V** during discharge.

### Example 2: EMF and Internal Resistance from Two Measurements

**Given:**

A practical source produces:

- Terminal voltage 11.5 V at 1 A.
- Terminal voltage 10.5 V at 3 A.

Assume constant internal resistance.

Determine EMF and internal resistance.

**Formula:**

$$V=\mathcal{E}-Ir$$

**Solution:**

1. First measurement:

   $$11.5=\mathcal{E}-r$$

2. Second measurement:

   $$10.5=\mathcal{E}-3r$$

3. Subtract the second equation from the first:

   $$11.5-10.5=2r$$

   $$1=2r$$

   $$r=0.5\ \Omega$$

4. Substitute into the first equation:

   $$11.5=\mathcal{E}-0.5$$

   $$\mathcal{E}=12\text{ V}$$

**Final Answer:**

- EMF = **12 V**
- Internal resistance = **0.5 $\Omega$**

### Example 3: Voltmeter Loading Error

**Given:**

A 10 V source with an internal series resistance of 10 k$\Omega$ is measured using a voltmeter with an input resistance of 90 k$\Omega$.

Determine the measured voltage and percentage error relative to the unloaded source voltage.

**Formula:**

$$V_m=V_s\frac{R_v}{R_s+R_v}$$

**Solution:**

1. Identify the values:

   $$V_s=10\text{ V}$$

   $$R_s=10\text{ k}\Omega$$

   $$R_v=90\text{ k}\Omega$$

2. Calculate measured voltage:

   $$V_m=10\times\frac{90}{10+90}$$

   $$V_m=9\text{ V}$$

3. Calculate absolute error:

   $$\text{Error}=10-9=1\text{ V}$$

4. Calculate percentage error:

   $$\%\text{ Error}=\frac{1}{10}\times100=10\%$$

**Final Answer:**

The voltmeter indicates **9 V**, producing a **10% measurement error** due to loading.

## 7. Practical Applications

### 7.1 Battery Management

Battery monitoring circuits measure terminal voltage to estimate charge condition, detect abnormal operation and prevent excessive discharge.

### 7.2 Voltage Regulation

Voltage regulators maintain a relatively constant output voltage despite changes in input voltage or load current.

### 7.3 Solar Energy Systems

Photovoltaic cells generate EMF when exposed to light. Multiple cells are connected to obtain the required voltage and current.

### 7.4 Electronic Measurement

Voltmeters, digital multimeters and oscilloscopes measure potential differences in electronic circuits.

### 7.5 Power Supplies

Regulated power supplies convert incoming electrical energy into stable DC voltage levels suitable for electronic components.

## 8. Important Comparisons and Observations

### 8.1 EMF and Terminal Voltage

| Characteristic | EMF | Terminal Voltage |
|---|---|---|
| Meaning | Energy supplied per unit charge by source | Potential difference across source terminals |
| Unit | Volt | Volt |
| Symbol | $\mathcal{E}$ | $V$ |
| Ideal source | Equal to terminal voltage | Equal to EMF |
| Practical source during discharge | Generally greater | Reduced by internal voltage drop |

### 8.2 Ideal and Practical Voltage Sources

| Characteristic | Ideal Source | Practical Source |
|---|---|---|
| Internal resistance | Zero | Nonzero |
| Terminal voltage | Constant | Depends on load current |
| Power capability | Unlimited in ideal model | Limited |
| Physical realization | Theoretical model | Real batteries and supplies |

### 8.3 Important Observations

1. EMF and voltage have the same SI unit but different physical meanings.
2. EMF describes energy supplied per unit charge.
3. Terminal voltage changes with load current in a practical source.
4. Internal resistance causes power dissipation inside a source.
5. A voltmeter must have high input resistance to minimize loading.
6. Ground is a reference node and is not automatically Earth.

## 9. Common Exam Traps

- **Treating EMF as a mechanical force:** EMF is energy supplied per unit charge.
- **Assuming terminal voltage always equals EMF:** This is true for an ideal source or an open-circuit practical source, not generally during discharge.
- **Using the wrong internal-resistance equation:** During discharge, $V=\mathcal{E}-Ir$; during charging, $V=\mathcal{E}+Ir$.
- **Connecting a voltmeter in series:** A voltmeter is connected in parallel.
- **Ignoring voltmeter loading:** Finite input resistance can alter the measured voltage.
- **Confusing ground with Earth:** Circuit ground is a reference node and may or may not be physically earthed.
- **Ignoring polarity:** Voltage between A and B is the negative of voltage between B and A.

## Quiz

1. A practical battery has an EMF of 15 V and internal resistance of 0.5 $\Omega$. If it supplies 4 A, what is its terminal voltage?

   - [ ] 17 V
   - [ ] 15 V
   - [x] 13 V
   - [ ] 11 V

   > During discharge, $V=\mathcal{E}-Ir=15-(4\times0.5)=13\text{ V}$. The internal voltage drop is 2 V.

2. A voltmeter is connected across a resistor in an electronic circuit. Why should its input resistance be very high?

   - [ ] To increase the current through the resistor.
   - [ ] To increase the power consumed by the circuit.
   - [x] To minimize the current drawn by the meter and reduce loading error.
   - [ ] To force the resistor voltage to zero.

   > A voltmeter is connected in parallel. Its input resistance forms an additional parallel path. A very high input resistance minimizes the current drawn by the meter and makes the measured voltage closer to the original circuit voltage.

3. A source produces terminal voltages of 9.6 V at 2 A and 9.0 V at 5 A while discharging. Assuming constant internal resistance, what are its EMF and internal resistance?

   - [ ] 9.6 V and 0.20 $\Omega$
   - [x] 10.0 V and 0.20 $\Omega$
   - [ ] 10.0 V and 0.40 $\Omega$
   - [ ] 11.0 V and 0.20 $\Omega$

   > Using $V=\mathcal{E}-Ir$, the two equations are $9.6=\mathcal{E}-2r$ and $9.0=\mathcal{E}-5r$. Subtraction gives $0.6=3r$, so $r=0.2\ \Omega$. Substitution gives $\mathcal{E}=9.6+(2\times0.2)=10.0\text{ V}$.
