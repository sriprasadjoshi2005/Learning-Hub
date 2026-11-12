---
title: Thevenin's Theorem
level: intermediate
---

# Thevenin's Theorem

## Introduction

Thevenin's theorem is a fundamental network-analysis technique that simplifies a complicated linear electrical network into an equivalent voltage source connected in series with an equivalent resistance.

Instead of repeatedly analysing an entire circuit whenever the load changes, the original network can be replaced by a simpler equivalent model at the load terminals.

This technique is particularly useful in analysing electronic circuits, power-delivery networks, sensor interfaces, and systems in which the load resistance varies.

The lesson develops the theorem, derives its equivalent model, explains the calculation of Thevenin voltage and resistance, examines dependent sources, and solves numerical problems.

## 1. Statement of Thevenin's Theorem

Thevenin's theorem states:

**Any linear bilateral two-terminal network containing independent sources and linear impedances can be replaced, as viewed from its output terminals, by an equivalent ideal voltage source \(V_{TH}\) connected in series with an equivalent resistance \(R_{TH}\).**

The equivalent circuit is:

```text
       RTH
  +───/\/\/─────+ 
  |             |
 (VTH)          RL
  |             |
  +─────────────+
```

Where:
- \(V_{TH}\) = Thevenin equivalent voltage.
- \(R_{TH}\) = Thevenin equivalent resistance.
- \(R_L\) = load resistance.

The equivalent circuit produces the same terminal voltage and load current as the original network for any permissible load connected to those terminals.

## 2. Thevenin Equivalent Voltage

The Thevenin voltage is the open-circuit voltage measured across the load terminals after removing the load.

\[
\boxed{V_{TH}=V_{OC}}
\]

The load must be disconnected while calculating this voltage.

The original network remains active, including its independent sources.

### 2.1 Why Open-Circuit Voltage?

When the load is disconnected, no current flows through the load terminals.

The voltage measured across those terminals is the voltage available to an external load.

This voltage becomes the ideal source voltage in the Thevenin equivalent model.

## 3. Thevenin Equivalent Resistance

The Thevenin resistance is the resistance seen looking into the network from the load terminals after independent sources have been deactivated.

### 3.1 Deactivating Independent Sources

For an ideal independent voltage source:

\[
V_s=0
\]

A zero-voltage ideal source is equivalent to a short circuit.

For an ideal independent current source:

\[
I_s=0
\]

A zero-current ideal source is equivalent to an open circuit.

Therefore:

| Independent source | Deactivated representation |
|---|---|
| Ideal voltage source | Short circuit |
| Ideal current source | Open circuit |

All resistors remain in the circuit.

### 3.2 Calculation of Thevenin Resistance

After deactivating the independent sources:

1. Remove the load.
2. Replace ideal voltage sources with short circuits.
3. Replace ideal current sources with open circuits.
4. Calculate the equivalent resistance viewed from the load terminals.

\[
\boxed{R_{TH}=R_{eq}}
\]

The result is the Thevenin resistance.

## 4. Thevenin's Theorem Using Open-Circuit and Short-Circuit Measurements

For a linear network containing only independent sources:

\[
V_{TH}=V_{OC}
\]

If the short-circuit current is known:

\[
I_{SC}=\frac{V_{TH}}{R_{TH}}
\]

Therefore:

\[
\boxed{R_{TH}=\frac{V_{OC}}{I_{SC}}}
\]

This method is useful when open-circuit voltage and short-circuit current are available.

It should not be applied blindly to circuits with nonlinear elements or certain dependent-source configurations.

## 5. Step-by-Step Procedure

To determine the Thevenin equivalent of a circuit:

1. Identify the two terminals across which the load is connected.
2. Remove the load resistance.
3. Calculate the open-circuit voltage across the terminals.
4. Deactivate all independent sources.
5. Calculate the equivalent resistance seen from the terminals.
6. Construct the equivalent voltage source in series with the calculated resistance.
7. Reconnect the load and calculate its current or voltage.

## 6. Thevenin's Theorem with Dependent Sources

Dependent sources must not be deactivated because their values depend on other circuit variables.

A common method is to apply a test voltage or test current at the output terminals.

If a test voltage \(V_t\) produces a test current \(I_t\), then:

\[
\boxed{R_{TH}=\frac{V_t}{I_t}}
\]

The dependent sources remain active during this calculation.

The independent sources are deactivated when determining the resistance, but dependent sources remain in the network.

## 7. Thevenin Equivalent with Multiple Independent Sources

A network may contain several independent voltage and current sources.

The Thevenin voltage can be calculated using:

- Nodal analysis.
- Mesh analysis.
- Kirchhoff's laws.
- Superposition.

All sources must be treated according to the circuit's actual connections and polarities.

When using superposition, the individual source contributions are calculated with the other independent sources deactivated.

## 8. Load Current and Load Voltage

Once the Thevenin equivalent is obtained, the original network becomes a simple series circuit.

The load current is:

\[
\boxed{I_L=\frac{V_{TH}}{R_{TH}+R_L}}
\]

The load voltage is:

\[
\boxed{V_L=I_LR_L}
\]

Alternatively:

\[
\boxed{V_L=V_{TH}\frac{R_L}{R_{TH}+R_L}}
\]

The power delivered to the load is:

\[
\boxed{P_L=I_L^2R_L}
\]

## 9. Worked Numerical Examples

### Example 1: Basic Thevenin Equivalent

**Given:**

- Supply voltage = 12 V.
- \(R_1=4\ \Omega\).
- \(R_2=8\ \Omega\).
- The output terminals are across \(R_2\).

**Find:** Thevenin equivalent voltage and resistance.

**Solution:**

The open-circuit voltage is the voltage across \(R_2\).

Using the voltage-divider rule:

\[
V_{TH}=12\times\frac{8}{4+8}
\]

\[
\boxed{V_{TH}=8\text{ V}}
\]

To calculate Thevenin resistance, deactivate the 12 V source by replacing it with a short circuit.

The two resistors are now parallel as seen from the output terminals.

\[
R_{TH}=\frac{4\times8}{4+8}
\]

\[
\boxed{R_{TH}=2.667\ \Omega}
\]

**Final Answer:**

\[
\boxed{V_{TH}=8\text{ V}}
\]

\[
\boxed{R_{TH}=2.667\ \Omega}
\]

### Example 2: Calculating Load Current

**Given:**

The Thevenin equivalent from Example 1 is connected to:

\[
R_L=5\ \Omega
\]

**Find:** Load current and load voltage.

**Solution:**

Load current:

\[
I_L=\frac{8}{2.667+5}
\]

\[
\boxed{I_L\approx1.043\text{ A}}
\]

Load voltage:

\[
V_L=I_LR_L
\]

\[
V_L=1.043\times5
\]

\[
\boxed{V_L\approx5.217\text{ V}}
\]

### Example 3: Finding Thevenin Resistance Using Short-Circuit Current

**Given:**

- Open-circuit voltage = 20 V.
- Short-circuit current = 4 A.

**Find:** Thevenin resistance.

**Formula:**

\[
R_{TH}=\frac{V_{OC}}{I_{SC}}
\]

**Solution:**

\[
R_{TH}=\frac{20}{4}
\]

\[
\boxed{R_{TH}=5\ \Omega}
\]

### Example 4: Thevenin Equivalent of a Loaded Divider Network

**Given:**

- Source voltage = 24 V.
- Upper resistor = 6 Ω.
- Lower resistor = 12 Ω.
- Load resistance = 8 Ω connected across the lower resistor.

**Find:** Load current using Thevenin's theorem.

**Step 1: Remove the load.**

The open-circuit voltage is:

\[
V_{TH}=24\times\frac{12}{6+12}
\]

\[
\boxed{V_{TH}=16\text{ V}}
\]

**Step 2: Calculate Thevenin resistance.**

Deactivate the voltage source.

\[
R_{TH}=6\parallel12
\]

\[
R_{TH}=\frac{6\times12}{6+12}
\]

\[
\boxed{R_{TH}=4\ \Omega}
\]

**Step 3: Reconnect the load.**

\[
I_L=\frac{16}{4+8}
\]

\[
\boxed{I_L=1.333\text{ A}}
\]

**Step 4: Calculate load voltage.**

\[
V_L=1.333\times8
\]

\[
\boxed{V_L=10.667\text{ V}}
\]

## 10. Practical Applications

Thevenin's theorem is used in:

- Battery and power-supply modelling.
- Electronic circuit simplification.
- Sensor output analysis.
- Load variation studies.
- Transistor circuit modelling.
- Power-system calculations.
- Circuit simulation and troubleshooting.

For example, a sensor connected to different measurement devices can be represented using a Thevenin equivalent to examine how each device loads the sensor.

## 11. Important Comparisons and Observations

| Quantity | Meaning |
|---|---|
| \(V_{TH}\) | Open-circuit voltage at the output terminals |
| \(R_{TH}\) | Equivalent resistance seen from the output terminals |
| \(I_L\) | Current through the connected load |
| \(V_L\) | Voltage across the load |
| \(I_{SC}\) | Short-circuit current at the output terminals |

Important observations:

- Thevenin voltage is calculated with the load removed.
- Thevenin resistance is calculated with independent sources deactivated.
- Dependent sources remain active.
- The equivalent model is valid at the selected output terminals.
- The load can be changed without repeating the entire original network analysis.

## 12. Common Exam Traps

1. **Leaving the load connected while calculating open-circuit voltage:** The load must be removed.

2. **Replacing a voltage source with an open circuit:** An ideal voltage source is short-circuited when deactivated.

3. **Replacing a current source with a short circuit:** An ideal current source is opened when deactivated.

4. **Deactivating dependent sources:** Dependent sources must remain active.

5. **Confusing Thevenin voltage with load voltage:** They are equal only under open-circuit conditions.

6. **Ignoring source polarity:** Thevenin voltage must retain the correct polarity.

7. **Using the wrong equivalent resistance:** Calculate the resistance seen specifically from the chosen output terminals.

## Quiz

1. A linear network has an open-circuit voltage of 18 V and a short-circuit current of 3 A. What is its Thevenin resistance?

   - [ ] 3 Ω
   - [ ] 9 Ω
   - [x] 6 Ω
   - [ ] 54 Ω

   > Thevenin resistance is \(R_{TH}=V_{OC}/I_{SC}=18/3=6\ \Omega\).

2. While determining Thevenin resistance, how should an ideal independent current source be treated?

   - [ ] Replace it with a short circuit.
   - [ ] Replace it with a voltage source.
   - [x] Replace it with an open circuit.
   - [ ] Leave it connected without modification.

   > Deactivating an ideal current source means setting its current to zero. A zero-current source is equivalent to an open circuit.

3. A Thevenin equivalent consists of a 12 V source in series with 4 Ω. A 2 Ω load is connected across the output. What is the load voltage?

   - [ ] 12 V
   - [ ] 8 V
   - [x] 4 V
   - [ ] 2 V

   > The load current is \(I_L=12/(4+2)=2\) A. The voltage across the 2 Ω load is \(V_L=2\times2=4\) V.