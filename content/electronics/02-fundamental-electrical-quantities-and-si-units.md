
---
title: Fundamental Electrical Quantities and SI Units
level: foundation
---

# Fundamental Electrical Quantities and SI Units

Electronics is fundamentally based on measurable electrical quantities such as charge, current, voltage, resistance, power and energy. Understanding these quantities and their relationships is essential before analysing electronic circuits or designing electrical systems.

Every electronic component operates according to physical principles that can be expressed mathematically. These principles require consistent units so that measurements, calculations and engineering specifications remain meaningful.

This lesson introduces the International System of Units (SI), fundamental electrical quantities, derived units, prefixes, dimensional analysis and the relationships between important electrical parameters. By the end of this lesson, you will be able to identify electrical quantities, convert between engineering prefixes, derive electrical units and check the dimensional correctness of circuit equations.

## 1. Introduction to Physical and Electrical Quantities

### 1.1 What Is a Physical Quantity?

A physical quantity is a measurable property of a physical system that can be expressed using a numerical value and an appropriate unit.

For example:

- Length = 5 metres.
- Mass = 2 kilograms.
- Time = 10 seconds.
- Electric current = 3 amperes.
- Voltage = 12 volts.

A physical measurement generally consists of:

$$Q = n \times u$$

Where:

- $Q$ = physical quantity.
- $n$ = numerical value.
- $u$ = unit.

For example:

$$V = 12 \times 1\text{ V} = 12\text{ V}$$

The numerical value alone is incomplete without its unit.

### 1.2 International System of Units

The International System of Units (SI) provides a globally standardized measurement system.

It contains seven base units.

| Fundamental Quantity | SI Unit | Symbol |
|---|---|---|
| Length | metre | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Thermodynamic temperature | kelvin | K |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

Electrical engineering uses several derived units constructed from these base units.

## 2. Fundamental Electrical Quantities

### 2.1 Electric Charge

Electric charge is a fundamental property of matter responsible for electrical interactions.

There are two types of electric charge:

- Positive charge, associated with protons.
- Negative charge, associated with electrons.

The SI unit of charge is the coulomb (C).

The magnitude of the elementary charge is:

$$e = 1.602176634 \times 10^{-19}\text{ C}$$

An electron carries charge $-e$, while a proton carries charge $+e$.

The total charge associated with $n$ elementary charges is:

$$Q = ne$$

For identical electrons, the signed charge is:

$$Q=-ne$$

### 2.2 Electric Current

Electric current describes the rate at which electric charge passes through a cross-section of a conductor.

$$I=\frac{dQ}{dt}$$

For constant current:

$$I=\frac{Q}{t}$$

The SI unit is the ampere (A).

One ampere corresponds to one coulomb of charge passing a cross-section per second.

$$1\text{ A}=1\text{ C/s}$$

### 2.3 Voltage or Electric Potential Difference

Voltage represents the difference in electric potential energy per unit charge between two points.

$$V=\frac{W}{Q}$$

Where:

- $V$ = potential difference in volts.
- $W$ = work or energy transferred in joules.
- $Q$ = charge in coulombs.

The SI unit is the volt (V).

$$1\text{ V}=1\text{ J/C}$$

A voltage difference provides the electrical driving force that can cause charge to move through a circuit.

### 2.4 Resistance

Electrical resistance measures how strongly a component opposes electric current.

For an ohmic component:

$$R=\frac{V}{I}$$

The SI unit is the ohm ($\Omega$).

$$1\ \Omega=1\text{ V/A}$$

Resistance depends on the material, dimensions, temperature and physical construction of a component.

### 2.5 Conductance

Conductance measures how easily electric current passes through a component.

It is the reciprocal of resistance:

$$G=\frac{1}{R}$$

The SI unit is the siemens (S).

$$1\text{ S}=1\text{ A/V}$$

A high conductance corresponds to a low resistance.

### 2.6 Electrical Power

Electrical power describes the rate at which electrical energy is transferred or converted.

$$P=\frac{dW}{dt}$$

For a DC circuit element:

$$P=VI$$

Using Ohm's law, alternative expressions are:

$$P=I^2R$$

$$P=\frac{V^2}{R}$$

The SI unit is the watt (W).

$$1\text{ W}=1\text{ J/s}$$

### 2.7 Electrical Energy

Electrical energy is the total energy transferred over a period.

$$E=Pt$$

For constant DC voltage and current:

$$E=VIt$$

The SI unit is the joule (J).

Electrical energy is also commonly measured in kilowatt-hours (kWh).

$$1\text{ kWh}=3.6\times10^6\text{ J}$$

## 3. Derived Electrical Units

Derived units are constructed by combining SI base units.

| Quantity | Relationship | SI Unit | Unit Symbol |
|---|---|---|---|
| Charge | $Q=It$ | Coulomb | C |
| Voltage | $V=W/Q$ | Volt | V |
| Resistance | $R=V/I$ | Ohm | $\Omega$ |
| Conductance | $G=1/R$ | Siemens | S |
| Capacitance | $C=Q/V$ | Farad | F |
| Inductance | $L=V/(di/dt)$ | Henry | H |
| Power | $P=VI$ | Watt | W |
| Energy | $E=Pt$ | Joule | J |
| Frequency | $f=1/T$ | Hertz | Hz |

### 3.1 Capacitance

Capacitance measures the ability of a component to store electric charge per unit potential difference.

$$C=\frac{Q}{V}$$

The SI unit is the farad (F).

$$1\text{ F}=1\text{ C/V}$$

### 3.2 Inductance

Inductance describes the property of a circuit element that opposes changes in current through the voltage induced across it.

$$V_L=L\frac{di}{dt}$$

The SI unit is the henry (H).

$$1\text{ H}=1\text{ V}\cdot\text{s/A}$$

### 3.3 Frequency

Frequency measures the number of complete cycles of a periodic signal per second.

$$f=\frac{1}{T}$$

Where $T$ is the time period in seconds.

The SI unit is the hertz (Hz).

$$1\text{ Hz}=1\text{ cycle/s}$$

## 4. SI Prefixes and Engineering Notation

Electronic circuits frequently use extremely small and extremely large values. SI prefixes simplify their representation.

| Prefix | Symbol | Power of Ten | Example |
|---|---|---|---|
| Tera | T | $10^{12}$ | 1 THz |
| Giga | G | $10^9$ | 1 GHz |
| Mega | M | $10^6$ | 1 M$\Omega$ |
| Kilo | k | $10^3$ | 1 k$\Omega$ |
| Base unit | — | $10^0$ | 1 A |
| Milli | m | $10^{-3}$ | 1 mA |
| Micro | $\mu$ | $10^{-6}$ | 1 $\mu$F |
| Nano | n | $10^{-9}$ | 1 nF |
| Pico | p | $10^{-12}$ | 1 pF |
| Femto | f | $10^{-15}$ | 1 fF |

### 4.1 Important Prefix Conversions

$$1\text{ k}\Omega=1000\ \Omega$$

$$1\text{ M}\Omega=10^6\ \Omega$$

$$1\text{ mA}=10^{-3}\text{ A}$$

$$1\ \mu\text{A}=10^{-6}\text{ A}$$

$$1\text{ nF}=10^{-9}\text{ F}$$

$$1\text{ pF}=10^{-12}\text{ F}$$

**Important distinction:** Capitalization matters. The symbol M represents mega, while m represents milli. Therefore, 1 mA and 1 MA differ by a factor of one billion.

## 5. Dimensional Analysis of Electrical Quantities

Dimensional analysis checks whether mathematical equations are consistent with physical dimensions.

The fundamental dimensions used in basic electrical engineering include:

- Mass: $[M]$
- Length: $[L]$
- Time: $[T]$
- Electric current: $[I]$

### 5.1 Dimensions of Charge

Since:

$$Q=It$$

Therefore:

$$[Q]=[I][T]$$

### 5.2 Dimensions of Voltage

Voltage is energy per unit charge.

$$V=\frac{W}{Q}$$

The dimensional formula for energy is:

$$[W]=[M][L]^2[T]^{-2}$$

Therefore:

$$[V]=[M][L]^2[T]^{-3}[I]^{-1}$$

### 5.3 Dimensions of Resistance

Using:

$$R=\frac{V}{I}$$

Therefore:

$$[R]=[M][L]^2[T]^{-3}[I]^{-2}$$

### 5.4 Dimensions of Power

$$P=VI$$

Therefore:

$$[P]=[M][L]^2[T]^{-3}$$

### 5.5 Why Dimensional Analysis Matters

Dimensional analysis is useful for:

1. Detecting incorrect equations.
2. Verifying derived mathematical expressions.
3. Converting between units.
4. Understanding physical relationships.
5. Identifying possible forms of equations.

However, dimensional correctness alone does not prove that an equation is physically correct. Numerical constants and mathematical functions must also be established through physical laws or derivations.

## 6. Mathematical Derivations and Numerical Examples

### Example 1: Calculating Charge from Current

**Given:**

- Current, $I=250\text{ mA}$
- Time, $t=4\text{ minutes}$

Determine the total charge transferred.

**Formula:**

$$Q=It$$

**Solution:**

1. Convert current into amperes:

   $$I=250\times10^{-3}=0.25\text{ A}$$

2. Convert time into seconds:

   $$t=4\times60=240\text{ s}$$

3. Calculate charge:

   $$Q=0.25\times240$$

   $$Q=60\text{ C}$$

**Final Answer:**

The total charge transferred is **60 C**.

### Example 2: Electrical Power and Energy Consumption

**Given:**

An electronic heating element operates at:

- Voltage, $V=24\text{ V}$
- Current, $I=2.5\text{ A}$
- Operating time, $t=3\text{ hours}$

Determine its power and energy consumption.

**Formulas:**

$$P=VI$$

$$E=Pt$$

**Solution:**

1. Calculate power:

   $$P=24\times2.5=60\text{ W}$$

2. Convert power into kilowatts:

   $$P=0.060\text{ kW}$$

3. Calculate energy:

   $$E=0.060\times3$$

   $$E=0.18\text{ kWh}$$

4. Convert energy into joules:

   $$E=0.18\times3.6\times10^6$$

   $$E=648,000\text{ J}$$

**Final Answer:**

- Power = **60 W**
- Energy consumption = **0.18 kWh**
- Energy in joules = **648 kJ**

### Example 3: Determining Resistance Using Dimensional and Electrical Relationships

**Given:**

A component has:

- Voltage across it = 12 V
- Current through it = 40 mA

Determine its resistance and conductance.

**Formulas:**

$$R=\frac{V}{I}$$

$$G=\frac{1}{R}$$

**Solution:**

1. Convert current:

   $$I=40\times10^{-3}=0.040\text{ A}$$

2. Calculate resistance:

   $$R=\frac{12}{0.040}=300\ \Omega$$

3. Calculate conductance:

   $$G=\frac{1}{300}$$

   $$G=0.003333\text{ S}$$

4. Express conductance in millisiemens:

   $$G=3.333\text{ mS}$$

**Final Answer:**

- Resistance = **300 $\Omega$**
- Conductance = **3.333 mS**

## 7. Practical Applications

### 7.1 Component Selection

Engineers use SI units and engineering prefixes to select components with appropriate electrical ratings.

A resistor may be specified as 4.7 k$\Omega$, while a capacitor may be specified as 100 nF.

Incorrect unit interpretation can result in selecting components with unsuitable values.

### 7.2 Power Supply Design

Power supply circuits require accurate voltage, current and power calculations to ensure that connected electronic devices operate within safe limits.

### 7.3 Battery Capacity

Battery capacity is commonly expressed in ampere-hours (Ah).

For example, a battery rated at 2 Ah can ideally deliver 2 A for one hour under its specified operating conditions.

Actual capacity depends on discharge rate, temperature, battery chemistry and cutoff voltage.

### 7.4 Signal Processing

Frequency and time period are essential when analysing oscillators, filters, communication systems and digital clock circuits.

### 7.5 Electronic Instrumentation

Multimeters and oscilloscopes measure voltage, current, resistance, frequency and other electrical parameters using standardized units.

## 8. Important Comparisons and Observations

### 8.1 Electrical Quantities

| Quantity | Meaning | Unit | Important Relationship |
|---|---|---|---|
| Charge | Quantity of electricity | C | $Q=It$ |
| Current | Rate of charge flow | A | $I=dQ/dt$ |
| Voltage | Energy per unit charge | V | $V=W/Q$ |
| Resistance | Opposition to current | $\Omega$ | $R=V/I$ |
| Conductance | Ease of current flow | S | $G=1/R$ |
| Power | Rate of energy transfer | W | $P=VI$ |
| Energy | Total transferred energy | J | $E=Pt$ |

### 8.2 Important Observations

1. Electrical current is measured in amperes, not coulombs.
2. Charge is measured in coulombs, not amperes.
3. Voltage represents energy per unit charge.
4. Power represents the rate of energy transfer.
5. Energy depends on both power and operating time.
6. SI prefixes must be handled carefully during calculations.
7. Dimensional analysis is a verification technique, not a replacement for physical derivation.

## 9. Common Exam Traps

- **Confusing current and charge:** Current is the rate of charge flow, whereas charge is the total quantity transferred.
- **Using minutes instead of seconds:** SI calculations involving current and charge generally require time in seconds.
- **Confusing milli and mega:** Milli is $10^{-3}$, while mega is $10^6$.
- **Using the wrong power expression:** $P=I^2R$ and $P=V^2/R$ apply to an ohmic resistance under the relevant operating conditions.
- **Confusing energy and power:** A 100 W device operating for 2 hours consumes 200 Wh, not 100 Wh.
- **Ignoring dimensional consistency:** Both sides of a physically valid equation must have compatible dimensions.
- **Assuming 1 Ah equals 1 joule:** Ampere-hour measures electric charge capacity; joule measures energy.

## Quiz

1. A constant current of 350 mA flows through an electronic component for 8 minutes. What total charge passes through the component?

   - [ ] 84 C
   - [x] 168 C
   - [ ] 280 C
   - [ ] 1,680 C

   > Convert the current: $350\text{ mA}=0.35\text{ A}$. Convert time: $8\times60=480\text{ s}$. Therefore, $Q=It=0.35\times480=168\text{ C}$.

2. Which of the following correctly represents the SI base dimensions of electrical resistance?

   - [ ] $[M][L]^2[T]^{-2}[I]^{-1}$
   - [ ] $[M][L]^2[T]^{-3}[I]^{-1}$
   - [x] $[M][L]^2[T]^{-3}[I]^{-2}$
   - [ ] $[M][L]^2[T]^{-3}[I]^{-3}$

   > Resistance is $R=V/I$. The dimensions of voltage are $[M][L]^2[T]^{-3}[I]^{-1}$. Dividing by current introduces another factor of $[I]^{-1}$, giving $[M][L]^2[T]^{-3}[I]^{-2}$.

3. A 48 V electronic device draws 750 mA continuously for 4 hours. What is the total electrical energy consumed?

   - [ ] 36 Wh
   - [ ] 72 Wh
   - [x] 144 Wh
   - [ ] 192 Wh

   > Convert current into amperes: $0.75\text{ A}$. Power is $P=VI=48\times0.75=36\text{ W}$. Energy is $E=Pt=36\times4=144\text{ Wh}$. In kilowatt-hours, this is 0.144 kWh.
