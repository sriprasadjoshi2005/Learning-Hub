
---
title: Ohm's Law and Electrical Power
level: foundation
---

# Ohm's Law and Electrical Power

Ohm's law is one of the central relationships in electrical engineering. It connects voltage, current and resistance and provides the foundation for analysing many basic electronic circuits.

Electrical power describes the rate at which electrical energy is transferred or converted. In resistive components, electrical energy is commonly converted into heat, while in other devices it may be converted into light, sound, motion or stored energy.

This lesson develops Ohm's law, resistance characteristics, voltage-current graphs, electrical power, energy, heating effects and power ratings. It also introduces limitations of Ohm's law and distinguishes ohmic components from non-ohmic devices. By the end, you will be able to analyse resistive circuits, calculate power and energy, interpret V-I characteristics and evaluate component operating limits.

## 1. Ohm's Law

### 1.1 Statement of Ohm's Law

Ohm's law states that, for a conductor under constant physical conditions, the current through it is directly proportional to the potential difference across it.

$$V\propto I$$

Introducing a proportionality constant called resistance:

$$V=IR$$

Where:

- $V$ = voltage in volts.
- $I$ = current in amperes.
- $R$ = resistance in ohms.

This relationship applies to ohmic components when temperature and other relevant physical conditions remain constant.

### 1.2 Rearranged Forms

$$I=\frac{V}{R}$$

$$R=\frac{V}{I}$$

These forms allow calculation of any one quantity when the other two are known.

### 1.3 Physical Interpretation

For a fixed resistance:

$$I\propto V$$

Increasing voltage increases current proportionally.

For a fixed voltage:

$$I\propto\frac{1}{R}$$

Increasing resistance decreases current.

## 2. V-I Characteristics

### 2.1 Ohmic Conductor

An ohmic conductor has a linear voltage-current relationship under constant physical conditions.

$$V=IR$$

A graph of voltage against current is a straight line passing through the origin.

Its slope is:

$$\text{Slope}=\frac{\Delta V}{\Delta I}=R$$

### 2.2 Non-Ohmic Components

Some electronic devices do not have a constant resistance.

Examples include:

- Diodes.
- Transistors.
- Thermistors.
- Filament lamps.
- Varistors.

For these devices, current may not be directly proportional to voltage.

Their resistance may depend on temperature, voltage, current or operating region.

### 2.3 Static and Differential Resistance

Static resistance is:

$$R_{static}=\frac{V}{I}$$

Differential resistance is the local slope of the V-I characteristic:

$$r_d=\frac{dV}{dI}$$

These quantities are not necessarily equal for nonlinear components.

Differential resistance is especially useful when analysing small signal variations around a transistor or diode operating point.

## 3. Electrical Power

### 3.1 Definition

Electrical power is the rate of energy transfer.

$$P=\frac{dW}{dt}$$

For a circuit element using the passive sign convention:

$$P=VI$$

The SI unit is the watt.

### 3.2 Derivation of Resistive Power Equations

Starting with:

$$P=VI$$

Using Ohm's law:

$$V=IR$$

Substituting:

$$P=I(IR)$$

Therefore:

$$\boxed{P=I^2R}$$

Alternatively:

$$I=\frac{V}{R}$$

Substituting into $P=VI$:

$$P=V\left(\frac{V}{R}\right)$$

Therefore:

$$\boxed{P=\frac{V^2}{R}}$$

All three expressions are useful in resistive circuit analysis.

### 3.3 Power Absorbed and Supplied

Under the passive sign convention:

- Positive power means a component absorbs energy.
- Negative power means a component supplies energy.

A resistor normally absorbs electrical power and converts it into heat.

A battery can supply power during discharge and absorb power during charging.

## 4. Electrical Energy and Heating Effect

### 4.1 Electrical Energy

For constant power:

$$E=Pt$$

For constant DC voltage and current:

$$E=VIt$$

The SI unit is the joule.

### 4.2 Joule Heating

The heating effect of current is described by Joule's law:

$$H=I^2Rt$$

Where:

- $H$ = heat energy generated in joules.
- $I$ = current in amperes.
- $R$ = resistance in ohms.
- $t$ = time in seconds.

For an ideal resistor, electrical energy absorbed is converted into thermal energy.

### 4.3 Heating Dependence

At constant resistance and time:

$$H\propto I^2$$

Doubling current produces four times the heating.

At constant current and time:

$$H\propto R$$

Higher resistance produces greater heating.

## 5. Power Ratings and Efficiency

### 5.1 Component Power Rating

Every electronic component has an operating power limit.

A resistor rated at 0.25 W should not normally be operated continuously above that value under its specified conditions.

Excessive power dissipation can cause:

- Overheating.
- Resistance drift.
- Insulation damage.
- Component failure.
- Fire hazards.

### 5.2 Power Derating

A component's permitted power dissipation may decrease as ambient temperature increases.

Manufacturers provide derating curves to indicate allowable operating power under different thermal conditions.

### 5.3 Efficiency

Efficiency measures the fraction of input power converted into useful output power.

$$\eta=\frac{P_{out}}{P_{in}}\times100\%$$

For a system with 80 W useful output and 100 W input:

$$\eta=80\%$$

The remaining 20 W is lost or dissipated in other forms.

## 6. Mathematical Derivations and Numerical Examples

### Example 1: Current Through a Resistor

**Given:**

- Supply voltage = 18 V.
- Resistance = 600 $\Omega$.

Determine current and power dissipation.

**Formulas:**

$$I=\frac{V}{R}$$

$$P=VI$$

**Solution:**

1. Calculate current:

   $$I=\frac{18}{600}=0.03\text{ A}$$

2. Convert into milliamperes:

   $$I=30\text{ mA}$$

3. Calculate power:

   $$P=18\times0.03$$

   $$P=0.54\text{ W}$$

**Final Answer:**

- Current = **30 mA**.
- Power dissipation = **0.54 W**.

A resistor rated at 0.5 W would be insufficient under these conditions without exceeding its rating.

### Example 2: Heating Energy in a Resistor

**Given:**

A 20 $\Omega$ resistor carries a current of 1.5 A for 4 minutes.

Determine the electrical energy converted into heat.

**Formula:**

$$H=I^2Rt$$

**Solution:**

1. Convert time:

   $$t=4\times60=240\text{ s}$$

2. Substitute:

   $$H=(1.5)^2\times20\times240$$

3. Calculate:

   $$H=2.25\times20\times240$$

   $$H=10,800\text{ J}$$

**Final Answer:**

The resistor converts **10.8 kJ** of electrical energy into heat.

### Example 3: Resistor Selection from Power Dissipation

**Given:**

A resistor must carry 25 mA continuously from a 12 V source. Determine the resistance and minimum theoretical power dissipation.

**Solution:**

1. Convert current:

   $$I=0.025\text{ A}$$

2. Calculate resistance:

   $$R=\frac{V}{I}=\frac{12}{0.025}$$

   $$R=480\ \Omega$$

3. Calculate power:

   $$P=VI=12\times0.025$$

   $$P=0.30\text{ W}$$

4. A 0.25 W resistor is below the calculated dissipation.

5. A 0.5 W resistor is the next common rating that exceeds the theoretical value, although additional thermal margin may be desirable.

**Final Answer:**

- Required resistance = **480 $\Omega$**.
- Calculated power dissipation = **0.30 W**.
- A suitable resistor must have a rating above 0.30 W, with appropriate derating and safety margin.

## 7. Practical Applications

### 7.1 LED Current Limiting

A series resistor controls LED current.

The approximate resistor value is:

$$R=\frac{V_s-V_f}{I_f}$$

Where:

- $V_s$ = supply voltage.
- $V_f$ = LED forward voltage.
- $I_f$ = desired LED current.

### 7.2 Heating Elements

Electric heaters use resistive elements to convert electrical energy into heat.

### 7.3 Battery and Power Supply Design

Power calculations determine current limits, component ratings and expected energy consumption.

### 7.4 Electronic Protection

Current-limiting resistors reduce the risk of excessive current through sensitive devices.

### 7.5 Amplifier Design

Power calculations help determine transistor dissipation, thermal requirements and amplifier efficiency.

## 8. Important Comparisons and Observations

### 8.1 Ohmic and Non-Ohmic Devices

| Characteristic | Ohmic Device | Non-Ohmic Device |
|---|---|---|
| V-I relationship | Linear under specified conditions | Nonlinear |
| Resistance | Constant under fixed conditions | Varies with operating point |
| Graph | Straight line through origin | Generally curved |
| Examples | Fixed resistor | Diode, thermistor and filament lamp |

### 8.2 Electrical Power Equations

| Equation | Most Useful When |
|---|---|
| $P=VI$ | Voltage and current are known |
| $P=I^2R$ | Current and resistance are known |
| $P=V^2/R$ | Voltage and resistance are known |

### 8.3 Important Observations

1. Ohm's law requires constant physical conditions.
2. Resistance is the slope of a voltage-versus-current graph for an ohmic resistor.
3. Differential resistance describes local nonlinear behaviour.
4. Electrical power is energy transferred per unit time.
5. Doubling current through a fixed resistor produces four times the power.
6. Component power ratings must include appropriate thermal margin.
7. Electrical efficiency is never greater than 100% for a passive energy-conversion process.

## 9. Common Exam Traps

- **Applying Ohm's law universally:** Diodes and many other devices are nonlinear.
- **Confusing voltage and current graph slopes:** On a V-I graph with voltage on the vertical axis, slope is resistance. On an I-V graph, slope is conductance.
- **Forgetting squared current:** Resistor power is proportional to $I^2$.
- **Using minutes in Joule's law:** Convert time into seconds to obtain energy in joules.
- **Ignoring component ratings:** A correct resistance value does not guarantee a safe power rating.
- **Assuming all input power becomes useful output:** Some energy is dissipated as heat and other losses.
- **Confusing static and differential resistance:** They describe different properties of nonlinear components.

## Quiz

1. A 750 $\Omega$ resistor is connected across a 15 V supply. What is its power dissipation?

   - [ ] 0.15 W
   - [x] 0.30 W
   - [ ] 0.45 W
   - [ ] 0.60 W

   > Using $P=V^2/R$, $P=15^2/750=225/750=0.30\text{ W}$.

2. A nonlinear electronic component has a curved voltage-current characteristic. Which resistance quantity represents the local slope of its V-I curve at a particular operating point?

   - [ ] Static resistance, $V/I$
   - [x] Differential resistance, $dV/dI$
   - [ ] Conductance, $I/V$, at all operating points
   - [ ] Power dissipation, $VI$

   > Differential resistance is defined by $r_d=dV/dI$. It represents the local change in voltage for a small change in current around an operating point. Static resistance is the ratio $V/I$.

3. A fixed resistor dissipates 5 W when carrying a current of 1 A. If its current increases to 3 A while resistance remains constant, what is its new power dissipation?

   - [ ] 15 W
   - [ ] 25 W
   - [x] 45 W
   - [ ] 60 W

   > For a fixed resistor, $P=I^2R$. Increasing current from 1 A to 3 A increases power by a factor of $3^2=9$. Therefore, the new power is $5\times9=45\text{ W}$.
