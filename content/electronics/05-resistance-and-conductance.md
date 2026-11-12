
---
title: Resistance and Conductance
level: foundation
---

# Resistance and Conductance

Resistance and conductance determine how easily electric current flows through an electronic component. They are fundamental to circuit design because they influence current distribution, voltage drops, power dissipation and signal behaviour.

A resistor is one of the most widely used electronic components. It is used to limit current, establish voltage levels, set transistor operating points, form filters and protect sensitive devices.

This lesson examines the physical origin of resistance, resistivity, conductivity, the geometry of conductors, temperature dependence, resistor classifications, power ratings and conductance. By the end, you will be able to calculate resistance from material properties, analyse temperature effects, select appropriate resistor values and understand non-ideal resistive behaviour.

## 1. Electrical Resistance

### 1.1 Definition

Electrical resistance is the property of a material or component that opposes electric current.

For an ohmic component:

$$R=\frac{V}{I}$$

Where:

- $R$ = resistance in ohms.
- $V$ = voltage across the component.
- $I$ = current through the component.

The SI unit is the ohm ($\Omega$).

$$1\ \Omega=1\text{ V/A}$$

A resistance of 100 $\Omega$ produces a voltage drop of 100 V when a current of 1 A flows through it, provided the component remains ohmic under those conditions.

### 1.2 Physical Origin of Resistance

In a metallic conductor, electrons move through a lattice of atoms and interact with lattice vibrations, impurities and defects.

These interactions scatter charge carriers and limit their directed motion.

The result is electrical resistance.

Important factors include:

- Material composition.
- Temperature.
- Conductor length.
- Cross-sectional area.
- Material defects and impurities.

## 2. Resistivity and Conductivity

### 2.1 Resistivity

Resistivity is an intrinsic material property that describes how strongly a material opposes current flow.

For a uniform conductor:

$$R=\rho\frac{L}{A}$$

Where:

- $R$ = resistance in ohms.
- $\rho$ = resistivity in $\Omega\text{m}$.
- $L$ = conductor length in metres.
- $A$ = cross-sectional area in m².

Rearranging:

$$\rho=\frac{RA}{L}$$

The SI unit of resistivity is ohm-metre ($\Omega\text{m}$).

### 2.2 Effect of Length

Resistance is directly proportional to length:

$$R\propto L$$

If conductor length doubles while material and cross-sectional area remain unchanged, resistance doubles.

### 2.3 Effect of Cross-Sectional Area

Resistance is inversely proportional to cross-sectional area:

$$R\propto\frac{1}{A}$$

If cross-sectional area doubles, resistance becomes half.

A thicker wire therefore generally has lower resistance than a thinner wire of the same material and length.

### 2.4 Conductivity

Conductivity is the reciprocal of resistivity.

$$\sigma=\frac{1}{\rho}$$

The SI unit is siemens per metre (S/m).

A highly conductive material has low resistivity.

## 3. Conductance

Conductance measures the ease with which current flows through a component.

$$G=\frac{1}{R}$$

The SI unit is siemens (S).

For an ohmic component:

$$G=\frac{I}{V}$$

Conductance is useful in circuit analysis, especially when working with parallel networks and nodal analysis.

### 3.1 Resistance and Conductance Relationship

| Resistance | Conductance |
|---|---|
| Opposition to current | Ease of current flow |
| $R=V/I$ | $G=I/V$ |
| Unit: $\Omega$ | Unit: S |
| Increases when conductance decreases | Increases when resistance decreases |

## 4. Temperature Dependence of Resistance

### 4.1 Metallic Conductors

For many metals over a limited temperature range:

$$R_T=R_0[1+\alpha(T-T_0)]$$

Where:

- $R_T$ = resistance at temperature $T$.
- $R_0$ = resistance at reference temperature $T_0$.
- $\alpha$ = temperature coefficient of resistance in K$^{-1}$.

Most pure metals have a positive temperature coefficient.

Their resistance generally increases as temperature rises.

### 4.2 Negative Temperature Coefficient

Some materials, particularly thermistors designed with negative temperature coefficients, exhibit decreasing resistance as temperature increases.

These are called NTC thermistors.

### 4.3 Positive Temperature Coefficient

PTC thermistors are designed so that resistance increases with temperature, sometimes very sharply over a specified temperature range.

### 4.4 Superconductivity

Certain materials exhibit zero DC electrical resistance below a critical temperature under suitable magnetic-field and current conditions.

This phenomenon is called superconductivity.

It is distinct from ordinary low-resistance metallic conduction.

## 5. Types of Resistors

### 5.1 Fixed Resistors

Fixed resistors have a nominal resistance that is not intended to be adjusted during normal operation.

Common types include:

- Carbon composition.
- Carbon film.
- Metal film.
- Metal oxide film.
- Wire-wound.
- Thick-film and thin-film resistors.

### 5.2 Variable Resistors

Variable resistors allow resistance to be adjusted.

Examples:

- Potentiometers.
- Rheostats.
- Trimmers.

A potentiometer commonly has three terminals and can be used as a voltage divider.

A rheostat is generally used as a two-terminal variable resistance.

### 5.3 Special Resistors

| Component | Behaviour | Application |
|---|---|---|
| LDR | Resistance decreases with light intensity | Light sensing |
| NTC thermistor | Resistance decreases with temperature | Temperature measurement |
| PTC thermistor | Resistance increases with temperature | Protection and temperature sensing |
| Varistor | Resistance decreases strongly at high voltage | Surge protection |
| Strain gauge | Resistance changes with mechanical strain | Force and pressure measurement |

## 6. Resistor Ratings and Specifications

### 6.1 Nominal Resistance

The nominal resistance is the specified intended resistance value.

### 6.2 Tolerance

Tolerance specifies the permitted deviation from the nominal resistance under stated conditions.

For a resistor:

$$R_{actual}=R_{nominal}(1\pm\text{tolerance})$$

A 1 k$\Omega$ resistor with 5% tolerance may have a resistance between:

$$950\ \Omega\leq R\leq1050\ \Omega$$

### 6.3 Power Rating

A resistor must not dissipate more power than its rated limit under the specified environmental and thermal conditions.

Common ratings include:

- 0.125 W.
- 0.25 W.
- 0.5 W.
- 1 W.
- 2 W.

### 6.4 Voltage Rating

Some resistors also have maximum working-voltage limits.

Even when calculated power is below the rated power, excessive voltage can cause insulation breakdown or other failure.

## 7. Mathematical Derivations and Numerical Examples

### Example 1: Resistance of a Copper Wire

**Given:**

- Length, $L=20\text{ m}$.
- Cross-sectional area, $A=1.5\text{ mm}^2$.
- Resistivity of copper, $\rho=1.68\times10^{-8}\ \Omega\text{m}$.

Determine the resistance at the specified reference temperature.

**Formula:**

$$R=\rho\frac{L}{A}$$

**Solution:**

1. Convert area:

   $$A=1.5\times10^{-6}\text{ m}^2$$

2. Substitute:

   $$R=\frac{(1.68\times10^{-8})(20)}{1.5\times10^{-6}}$$

3. Calculate:

   $$R=0.224\ \Omega$$

**Final Answer:**

The wire resistance is approximately **0.224 $\Omega$**.

### Example 2: Temperature-Dependent Resistance

**Given:**

A metallic resistor has:

- Resistance at 20°C = 100 $\Omega$.
- Temperature coefficient, $\alpha=0.004/^\circ\text{C}$.
- Final temperature = 80°C.

Determine the final resistance using the linear approximation.

**Formula:**

$$R_T=R_0[1+\alpha(T-T_0)]$$

**Solution:**

1. Determine temperature difference:

   $$\Delta T=80-20=60^\circ\text{C}$$

2. Substitute:

   $$R_T=100[1+(0.004)(60)]$$

3. Calculate:

   $$R_T=100(1+0.24)$$

   $$R_T=124\ \Omega$$

**Final Answer:**

The resistance increases to **124 $\Omega$**.

### Example 3: Resistor Tolerance and Power Rating

**Given:**

A 2.2 k$\Omega$ resistor has 5% tolerance and is connected across 12 V.

Determine its permitted resistance range and maximum possible power dissipation under the stated voltage.

**Solution:**

1. Convert nominal resistance:

   $$R=2200\ \Omega$$

2. Calculate tolerance:

   $$0.05\times2200=110\ \Omega$$

3. Determine resistance range:

   $$R_{min}=2200-110=2090\ \Omega$$

   $$R_{max}=2200+110=2310\ \Omega$$

4. Power is:

   $$P=\frac{V^2}{R}$$

5. Maximum power occurs at minimum resistance:

   $$P_{max}=\frac{12^2}{2090}$$

   $$P_{max}\approx0.0689\text{ W}$$

**Final Answer:**

- Resistance range = **2.09 k$\Omega$ to 2.31 k$\Omega$**.
- Maximum calculated dissipation = **68.9 mW**.

A suitably rated resistor should be selected with adequate thermal margin and consideration of its voltage rating.

## 8. Practical Applications

### 8.1 Current Limiting

Resistors limit current through LEDs and other sensitive components.

### 8.2 Voltage Division

Resistor networks generate smaller voltages from a larger supply voltage.

### 8.3 Transistor Biasing

Resistors establish transistor operating points and help stabilize amplifier circuits.

### 8.4 Temperature Measurement

Thermistors convert temperature changes into resistance changes that can be measured electronically.

### 8.5 Protection

Special resistor types and resistive elements can help limit surge current and protect electronic systems.

## 9. Important Comparisons and Observations

### 9.1 Resistance and Resistivity

| Resistance | Resistivity |
|---|---|
| Property of a particular component | Intrinsic material property |
| Depends on geometry and material | Depends primarily on material and temperature |
| Unit: $\Omega$ | Unit: $\Omega\text{m}$ |
| $R=\rho L/A$ | $\rho=RA/L$ |

### 9.2 Conductance and Conductivity

| Conductance | Conductivity |
|---|---|
| Reciprocal of component resistance | Reciprocal of material resistivity |
| Unit: S | Unit: S/m |
| Depends on component geometry | Material property |
| $G=1/R$ | $\sigma=1/\rho$ |

### 9.3 Important Observations

1. Resistance depends on material and geometry.
2. Resistivity is a material property, not a geometric property.
3. Longer conductors have higher resistance.
4. Larger cross-sectional areas reduce resistance.
5. Most metallic conductors have positive temperature coefficients.
6. Resistor tolerance affects actual circuit behaviour.
7. Power rating and voltage rating must both be considered.

## 10. Common Exam Traps

- **Confusing resistance with resistivity:** Resistance belongs to a particular component; resistivity describes the material.
- **Forgetting area conversion:** Convert mm² to m² before using SI resistivity.
- **Reversing the geometry relationship:** Resistance increases with length and decreases with cross-sectional area.
- **Ignoring temperature:** Resistance can change significantly with temperature.
- **Assuming tolerance is always symmetrical in actual manufacturing:** The stated tolerance specifies the permitted range, but the actual value is not necessarily uniformly distributed.
- **Selecting a resistor using only nominal power:** Thermal derating and voltage limits must also be considered.
- **Confusing conductivity and conductance:** Conductivity is measured in S/m, while conductance is measured in S.

## Quiz

1. A copper conductor has a length of 10 m and cross-sectional area of 2 mm². If its resistivity is $1.7\times10^{-8}\ \Omega\text{m}$, what is its resistance?

   - [ ] 0.017 $\Omega$
   - [x] 0.085 $\Omega$
   - [ ] 0.17 $\Omega$
   - [ ] 0.85 $\Omega$

   > Convert area: $2\text{ mm}^2=2\times10^{-6}\text{ m}^2$. Using $R=\rho L/A$, $R=(1.7\times10^{-8}\times10)/(2\times10^{-6})=0.085\ \Omega$.

2. A uniform metallic wire is stretched to twice its original length without changing its volume. Assuming resistivity remains constant, what happens to its resistance?

   - [ ] It doubles.
   - [ ] It becomes half.
   - [x] It becomes four times larger.
   - [ ] It remains unchanged.

   > Resistance is $R=\rho L/A$. With constant volume, $AL$ is constant. Doubling length makes area half. Therefore, the new resistance is $\rho(2L)/(A/2)=4R$.

3. A 1 k$\Omega$ resistor with 10% tolerance is connected across an ideal 10 V source. What is the maximum possible power dissipation due to the tolerance range?

   - [ ] 0.0826 W
   - [ ] 0.100 W
   - [x] 0.111 W
   - [ ] 0.122 W

   > Maximum power occurs at minimum resistance. The minimum resistance is $1000(1-0.10)=900\ \Omega$. Therefore, $P_{max}=V^2/R=100/900=0.1111\text{ W}$.
