---
title: Voltage and Current Dividers
level: intermediate
---

# Voltage and Current Dividers

## Introduction

Voltage and current dividers are fundamental circuit-analysis techniques used to determine how voltage and current are distributed among resistive components.

In a series circuit, the same current flows through every component, while the supply voltage is divided according to the resistance values. In a parallel circuit, every branch has the same voltage, while the total current divides among the branches according to their resistances.

These principles are widely used in sensor circuits, biasing networks, measurement systems, reference-voltage generation, and electronic signal conditioning.

This lesson develops the voltage-divider and current-divider equations, explains their derivations, examines loading effects, and applies the techniques to practical circuit problems.

## 1. Voltage Divider Principle

A voltage divider is a circuit arrangement in which a supply voltage is distributed across two or more series-connected resistors.

The current through all series resistors is identical.

Consider two resistors connected in series across a voltage source.

```text
       + Vs -
         |
        R1
         |
         A
         |
        R2
         |
         |
        0 V
```

The output voltage may be measured across either resistor or across a combination of them.

## 2. Derivation of the Voltage Divider Rule

Consider two resistors \(R_1\) and \(R_2\) connected in series across a source voltage \(V_s\).

The total resistance is:

\[
R_T=R_1+R_2
\]

Using Ohm's law:

\[
I=\frac{V_s}{R_1+R_2}
\]

The voltage across the first resistor is:

\[
V_1=IR_1
\]

Substituting the current:

\[
V_1=\frac{V_s}{R_1+R_2}R_1
\]

Therefore:

\[
\boxed{V_1=V_s\frac{R_1}{R_1+R_2}}
\]

Similarly:

\[
V_2=IR_2
\]

\[
\boxed{V_2=V_s\frac{R_2}{R_1+R_2}}
\]

For any number of series resistors:

\[
\boxed{V_k=V_s\frac{R_k}{R_T}}
\]

Where \(R_T\) is the total series resistance and \(R_k\) is the resistor across which the voltage is measured.

## 3. Important Properties of Voltage Dividers

### 3.1 Voltage Proportionality

The voltage across a resistor is directly proportional to its resistance.

A larger resistance receives a larger share of the total voltage in a series circuit.

### 3.2 Conservation of Voltage

The sum of all individual voltage drops equals the supply voltage.

\[
V_s=V_1+V_2+\cdots+V_n
\]

### 3.3 Resistance Ratio

For two series resistors:

\[
\frac{V_1}{V_2}=\frac{R_1}{R_2}
\]

This relationship is useful when designing a circuit to obtain a desired output voltage.

## 4. Loaded Voltage Divider

A voltage divider becomes loaded when an additional load resistance is connected across its output terminals.

The load resistance changes the effective resistance of the lower divider branch.

Consider a voltage divider consisting of \(R_1\) and \(R_2\), with a load \(R_L\) connected across \(R_2\).

The effective lower resistance is:

\[
R_{eq}=R_2\parallel R_L
\]

\[
R_{eq}=\frac{R_2R_L}{R_2+R_L}
\]

The output voltage becomes:

\[
\boxed{V_o=V_s\frac{R_{eq}}{R_1+R_{eq}}}
\]

Substituting:

\[
\boxed{
V_o=V_s
\frac{R_2\parallel R_L}
{R_1+(R_2\parallel R_L)}
}
\]

### 4.1 Loading Effect

When a load is connected, the output voltage generally decreases compared with the unloaded voltage.

This occurs because the effective resistance of the lower branch decreases.

A voltage divider is less affected by loading when the load resistance is much larger than the divider's output resistance.

A common design approximation is:

\[
R_L\geq10R_{out}
\]

This is a practical guideline rather than a universal requirement.

## 5. Voltage Divider Design

A voltage divider can be designed to produce a required output voltage.

For an unloaded two-resistor divider:

\[
V_o=V_s\frac{R_2}{R_1+R_2}
\]

Rearranging:

\[
\frac{V_o}{V_s}=\frac{R_2}{R_1+R_2}
\]

Therefore:

\[
V_oR_1=R_2(V_s-V_o)
\]

\[
\boxed{R_1=R_2\frac{V_s-V_o}{V_o}}
\]

This equation can be used to select suitable resistor values.

## 6. Current Divider Principle

A current divider is a parallel circuit arrangement in which the total current divides among multiple branches.

All parallel branches have the same voltage.

The branch current depends on the resistance of that branch.

Consider two resistors connected in parallel.

```text
             It
             |
       +-----+-----+
       |           |
      R1          R2
       |           |
       +-----+-----+
             |
             |
```

The total current divides into \(I_1\) and \(I_2\).

## 7. Derivation of the Current Divider Rule

For two parallel resistors:

\[
I_T=I_1+I_2
\]

The voltage across each resistor is equal.

Therefore:

\[
I_1R_1=I_2R_2
\]

Using the current-divider relationship:

\[
\boxed{I_1=I_T\frac{R_2}{R_1+R_2}}
\]

Similarly:

\[
\boxed{I_2=I_T\frac{R_1}{R_1+R_2}}
\]

Notice that the current through a resistor depends on the resistance of the other branch in the numerator.

This is because current divides inversely with resistance.

### 7.1 General Current Divider Rule

For multiple parallel resistors, the current through branch \(k\) is:

\[
\boxed{
I_k=I_T
\frac{1/R_k}
{\sum_{i=1}^{n}(1/R_i)}
}
\]

Where:
- \(I_k\) = current through branch \(k\).
- \(I_T\) = total current.
- \(R_k\) = resistance of branch \(k\).
- \(n\) = number of parallel branches.

## 8. Conductance Form of the Current Divider

Conductance is the reciprocal of resistance.

\[
G=\frac{1}{R}
\]

The current divider can therefore be expressed as:

\[
\boxed{I_k=I_T\frac{G_k}{G_T}}
\]

Where:

\[
G_T=G_1+G_2+\cdots+G_n
\]

This form is particularly convenient when several parallel branches are present.

## 9. Comparison of Voltage and Current Dividers

| Property | Voltage divider | Current divider |
|---|---|---|
| Circuit arrangement | Series | Parallel |
| Common quantity | Current | Voltage |
| Divided quantity | Voltage | Current |
| Distribution | Directly proportional to resistance | Inversely proportional to resistance |
| Main application | Obtaining a required voltage | Obtaining branch currents |

## 10. Worked Numerical Examples

### Example 1: Basic Voltage Divider

**Given:**

- Supply voltage = 24 V
- \(R_1=4\ \Omega\)
- \(R_2=8\ \Omega\)

**Find:** Voltage across each resistor.

**Solution:**

Total resistance:

\[
R_T=4+8=12\ \Omega
\]

Circuit current:

\[
I=\frac{24}{12}=2\text{ A}
\]

Voltage across \(R_1\):

\[
V_1=IR_1=2\times4
\]

\[
\boxed{V_1=8\text{ V}}
\]

Voltage across \(R_2\):

\[
V_2=IR_2=2\times8
\]

\[
\boxed{V_2=16\text{ V}}
\]

Verification:

\[
V_1+V_2=8+16=24\text{ V}
\]

### Example 2: Loaded Voltage Divider

**Given:**

- Supply voltage = 12 V
- \(R_1=2\text{ k}\Omega\)
- \(R_2=4\text{ k}\Omega\)
- \(R_L=4\text{ k}\Omega\)

The load is connected across \(R_2\).

**Find:** Actual output voltage.

**Solution:**

Effective lower resistance:

\[
R_{eq}=R_2\parallel R_L
\]

\[
R_{eq}=\frac{4\times4}{4+4}
\]

\[
R_{eq}=2\text{ k}\Omega
\]

Output voltage:

\[
V_o=12\times\frac{2}{2+2}
\]

\[
\boxed{V_o=6\text{ V}}
\]

Without the load, the output would have been:

\[
V_o=12\times\frac{4}{2+4}=8\text{ V}
\]

The load reduces the output voltage from 8 V to 6 V.

### Example 3: Basic Current Divider

**Given:**

- Total current = 12 A
- \(R_1=3\ \Omega\)
- \(R_2=6\ \Omega\)

**Find:** Current through each resistor.

**Solution:**

Current through \(R_1\):

\[
I_1=12\times\frac{6}{3+6}
\]

\[
\boxed{I_1=8\text{ A}}
\]

Current through \(R_2\):

\[
I_2=12\times\frac{3}{3+6}
\]

\[
\boxed{I_2=4\text{ A}}
\]

Verification:

\[
I_1+I_2=8+4=12\text{ A}
\]

### Example 4: Current Division Among Three Branches

**Given:**

- Total current = 18 A
- \(R_1=2\ \Omega\)
- \(R_2=3\ \Omega\)
- \(R_3=6\ \Omega\)

**Find:** Branch currents.

**Solution:**

Total conductance:

\[
G_T=\frac12+\frac13+\frac16
\]

\[
G_T=1\text{ S}
\]

Current through the first branch:

\[
I_1=18\times\frac{1/2}{1}
\]

\[
\boxed{I_1=9\text{ A}}
\]

Second branch:

\[
I_2=18\times\frac{1/3}{1}
\]

\[
\boxed{I_2=6\text{ A}}
\]

Third branch:

\[
I_3=18\times\frac{1/6}{1}
\]

\[
\boxed{I_3=3\text{ A}}
\]

Verification:

\[
9+6+3=18\text{ A}
\]

## 11. Practical Applications

Voltage and current dividers are used in:

- Sensor signal conditioning.
- Battery-voltage monitoring.
- Transistor biasing networks.
- Reference-voltage generation.
- Potentiometer circuits.
- Measurement instruments.
- Current-sharing networks.
- Electronic control systems.

A resistive voltage divider is often used to scale a voltage to a range suitable for an analogue-to-digital converter.

However, its output impedance and loading behaviour must be considered when selecting component values.

## 12. Common Exam Traps

1. **Reversing the voltage-divider numerator:** The resistor across which the voltage is measured must appear in the numerator.

2. **Reversing the current-divider numerator:** For two branches, the current through \(R_1\) uses \(R_2\) in the numerator.

3. **Ignoring loading:** A load connected across a divider resistor changes the effective branch resistance.

4. **Adding parallel resistances directly:** Parallel resistances must be combined using reciprocal relationships.

5. **Forgetting conservation:** The sum of divider voltages must equal the supply voltage, and the sum of branch currents must equal total current.

6. **Confusing direct and inverse proportionality:** Series voltage division is directly proportional to resistance, whereas parallel current division is inversely proportional to resistance.

7. **Mixing units:** Convert kΩ to Ω or use consistent units throughout a calculation.

## Quiz

1. A 30 V supply is connected across two series resistors of 5 Ω and 10 Ω. What is the voltage across the 10 Ω resistor?

   - [ ] 5 V
   - [ ] 10 V
   - [x] 20 V
   - [ ] 25 V

   > The voltage-divider rule gives \(V_2=30\times10/(5+10)=20\) V. The larger resistor receives the larger voltage drop in a series circuit.

2. A total current of 15 A enters two parallel resistors of 4 Ω and 8 Ω. What is the current through the 4 Ω resistor?

   - [x] 10 A
   - [ ] 5 A
   - [ ] 7.5 A
   - [ ] 12 A

   > The current-divider rule gives \(I_1=15\times8/(4+8)=10\) A. The lower-resistance branch receives the larger current.

3. An unloaded voltage divider produces 8 V across its lower resistor. A load is then connected in parallel with that resistor. Assuming the source and upper resistor remain unchanged, what generally happens to the output voltage?

   - [ ] It increases because the load draws additional current.
   - [ ] It remains exactly 8 V under all loading conditions.
   - [x] It decreases because the effective lower-branch resistance decreases.
   - [ ] It becomes equal to the supply voltage.

   > Adding a parallel load reduces the effective resistance of the lower divider branch. This decreases its share of the total voltage and produces a lower output voltage.