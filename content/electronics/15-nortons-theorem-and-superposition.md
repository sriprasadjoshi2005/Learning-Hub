---
title: Norton's Theorem and Superposition
level: intermediate
---

# Norton's Theorem and Superposition

## Introduction

Norton's theorem and the superposition theorem are important techniques for analysing linear electrical networks.

Norton's theorem simplifies a complicated linear two-terminal network into an equivalent current source connected in parallel with an equivalent resistance. It is closely related to Thevenin's theorem and provides an alternative representation of the same external circuit behaviour.

The superposition theorem provides a method for analysing circuits containing multiple independent sources. It determines the contribution of each independent source separately and combines the individual voltage or current contributions algebraically.

These methods are particularly useful in circuit design, signal analysis, power systems, and networks containing multiple sources.

## 1. Statement of Norton's Theorem

Norton's theorem states:

**Any linear bilateral two-terminal network containing independent sources and linear impedances can be replaced, as viewed from its output terminals, by an equivalent ideal current source \(I_N\) connected in parallel with an equivalent resistance \(R_N\).**

The equivalent circuit is:

```text
       ┌───────┬───────┐
       │       │       │
       ↑ IN   RN      RL
       │       │       │
       └───────┴───────┘
```

Where:
- \(I_N\) = Norton equivalent current.
- \(R_N\) = Norton equivalent resistance.
- \(R_L\) = load resistance.

The equivalent circuit produces the same external terminal voltage and load current as the original network.

## 2. Norton Equivalent Current

The Norton current is the short-circuit current measured at the output terminals.

\[
\boxed{I_N=I_{SC}}
\]

To determine it:

1. Remove the load.
2. Short the output terminals.
3. Calculate the current flowing through the short circuit.

This current is the Norton equivalent current.

## 3. Norton Equivalent Resistance

The Norton resistance is calculated by deactivating all independent sources and determining the equivalent resistance seen from the output terminals.

\[
\boxed{R_N=R_{eq}}
\]

The source-deactivation rules are:

| Independent source | Deactivated representation |
|---|---|
| Ideal voltage source | Short circuit |
| Ideal current source | Open circuit |

Dependent sources must remain active.

The resistance can also be determined using a test source when dependent sources are present.

## 4. Relationship Between Thevenin and Norton Equivalents

Thevenin and Norton equivalents represent the same linear two-terminal network.

Their relationship is:

\[
\boxed{V_{TH}=I_NR_N}
\]

And:

\[
\boxed{I_N=\frac{V_{TH}}{R_{TH}}}
\]

The equivalent resistances are equal:

\[
\boxed{R_{TH}=R_N}
\]

Therefore, a Thevenin equivalent can be transformed directly into a Norton equivalent and vice versa.

## 5. Load Current Using Norton's Equivalent

When a load resistance is connected in parallel with the Norton resistance, the source current divides between the two branches.

Using the current-divider rule:

\[
\boxed{I_L=I_N\frac{R_N}{R_N+R_L}}
\]

The load voltage is:

\[
\boxed{V_L=I_LR_L}
\]

Alternatively, using the parallel equivalent resistance:

\[
R_{eq}=R_N\parallel R_L
\]

\[
V_L=I_NR_{eq}
\]

Both methods produce the same result.

## 6. Step-by-Step Procedure for Norton's Theorem

1. Identify the output terminals.
2. Remove the load resistance.
3. Short the output terminals.
4. Calculate the short-circuit current to obtain \(I_N\).
5. Deactivate all independent sources.
6. Calculate the equivalent resistance seen from the output terminals to obtain \(R_N\).
7. Draw the Norton equivalent circuit.
8. Reconnect the load and calculate its current or voltage.

## 7. Superposition Theorem

### 7.1 Statement

The superposition theorem states:

**In a linear circuit containing multiple independent sources, the voltage or current in any element is the algebraic sum of the contributions produced by each independent source acting individually.**

When analysing one independent source:
- All other independent voltage sources are replaced by short circuits.
- All other independent current sources are replaced by open circuits.
- Dependent sources remain active.

### 7.2 Why Superposition Works

Linear circuits obey linear relationships between voltage, current, and circuit parameters.

If one source produces a current contribution \(I_1\), and another produces \(I_2\), the total response is:

\[
\boxed{I=I_1+I_2}
\]

Similarly, for voltage:

\[
\boxed{V=V_1+V_2}
\]

The contributions must be added algebraically, taking their directions and polarities into account.

## 8. Superposition Procedure

For a circuit containing several independent sources:

1. Select the voltage or current to be determined.
2. Keep one independent source active.
3. Deactivate all other independent sources.
4. Calculate the contribution of the active source.
5. Repeat for every independent source.
6. Add the individual contributions algebraically.
7. Interpret the sign of the final result.

### 8.1 Important Source-Deactivation Rules

| Source type | When deactivated |
|---|---|
| Ideal voltage source | Replace with short circuit |
| Ideal current source | Replace with open circuit |
| Dependent voltage source | Keep active |
| Dependent current source | Keep active |

A practical voltage source containing internal resistance retains that resistance when its ideal voltage source is deactivated.

Similarly, a practical current source retains its parallel internal resistance.

## 9. Superposition and Power

Superposition applies directly to linear voltages and currents.

However, power is not a linear quantity.

For a resistor:

\[
P=I^2R
\]

If two sources independently produce currents \(I_1\) and \(I_2\), the total power is:

\[
P=(I_1+I_2)^2R
\]

This is generally not equal to:

\[
I_1^2R+I_2^2R
\]

Therefore, individual power contributions must not simply be added using superposition.

First calculate the total voltage or current, then determine the actual power.

## 10. Worked Numerical Examples

### Example 1: Finding Norton Equivalent from a Thevenin Equivalent

**Given:**

- Thevenin voltage = 24 V.
- Thevenin resistance = 8 Ω.

**Find:** Norton equivalent.

**Solution:**

\[
I_N=\frac{V_{TH}}{R_{TH}}
\]

\[
I_N=\frac{24}{8}
\]

\[
\boxed{I_N=3\text{ A}}
\]

The resistance remains unchanged:

\[
\boxed{R_N=8\ \Omega}
\]

### Example 2: Load Current Using Norton's Theorem

**Given:**

- Norton current = 5 A.
- Norton resistance = 10 Ω.
- Load resistance = 15 Ω.

**Find:** Load current.

**Solution:**

Using the current-divider rule:

\[
I_L=I_N\frac{R_N}{R_N+R_L}
\]

\[
I_L=5\times\frac{10}{10+15}
\]

\[
I_L=5\times0.4
\]

\[
\boxed{I_L=2\text{ A}}
\]

Load voltage:

\[
V_L=2\times15
\]

\[
\boxed{V_L=30\text{ V}}
\]

### Example 3: Superposition with Two Voltage Sources

**Given:**

Two ideal voltage sources are connected through separate resistors to a common node.

- Source 1 = 12 V through 2 Ω.
- Source 2 = 6 V through 4 Ω.
- A 4 Ω resistor connects the common node to ground.

**Find:** Common-node voltage.

**Solution:**

First consider the 12 V source alone.

Deactivate the 6 V source by replacing it with a short circuit.

The two resistors connected from the node to ground are 4 Ω and 4 Ω in parallel.

\[
R_p=4\parallel4=2\ \Omega
\]

The contribution from the 12 V source is:

\[
V_1=12\times\frac{2}{2+2}
\]

\[
V_1=6\text{ V}
\]

Now consider the 6 V source alone.

Deactivate the 12 V source.

The 2 Ω resistor and 4 Ω load resistor are in parallel:

\[
R_p=2\parallel4
\]

\[
R_p=\frac{8}{6}=1.333\ \Omega
\]

The contribution from the 6 V source is:

\[
V_2=6\times\frac{1.333}{4+1.333}
\]

\[
V_2=1.5\text{ V}
\]

Total node voltage:

\[
V=V_1+V_2
\]

\[
\boxed{V=7.5\text{ V}}
\]

### Example 4: Superposition with Opposing Contributions

**Given:**

A circuit has two sources producing opposing contributions to the current through a resistor.

- First source contribution = 4 A in the chosen positive direction.
- Second source contribution = 1.5 A in the opposite direction.

**Find:** Total current.

**Solution:**

Choose the first direction as positive.

\[
I=4+(-1.5)
\]

\[
\boxed{I=2.5\text{ A}}
\]

The positive result indicates that the actual current flows in the direction of the first contribution.

## 11. Comparison of Thevenin and Norton Theorems

| Feature | Thevenin | Norton |
|---|---|---|
| Equivalent source | Voltage source | Current source |
| Resistance connection | Series | Parallel |
| Source value | Open-circuit voltage | Short-circuit current |
| Equivalent resistance | \(R_{TH}\) | \(R_N\) |
| Relationship | \(V_{TH}=I_NR_N\) | \(I_N=V_{TH}/R_{TH}\) |

## 12. Limitations of Superposition

Superposition has important limitations:

1. It applies to linear circuits.
2. It cannot be directly applied to nonlinear devices operating in nonlinear regions.
3. Power cannot be calculated by independently adding the power contributions of each source.
4. It can become computationally lengthy when a circuit contains many independent sources.
5. Dependent sources must remain active.

## 13. Practical Applications

Norton's theorem is useful in:
- Current-source circuit modelling.
- Parallel-network simplification.
- Sensor and measurement circuit analysis.
- Load-current calculations.
- Electronic circuit design.

Superposition is useful in:
- Multi-source signal analysis.
- Amplifier input analysis.
- AC circuit calculations.
- Power-system network studies.
- Separating DC bias and small-signal contributions in linearised circuit models.

## 14. Common Exam Traps

1. **Confusing Norton current with open-circuit current:** Norton current is the short-circuit current.

2. **Changing resistance incorrectly:** Thevenin and Norton equivalent resistances have the same value.

3. **Deactivating dependent sources:** Dependent sources must remain active.

4. **Incorrect source deactivation:** Voltage sources become short circuits; current sources become open circuits.

5. **Ignoring direction:** Superposition contributions must be added algebraically.

6. **Applying superposition directly to power:** Calculate the total current or voltage first, then determine power.

7. **Forgetting practical source resistance:** Internal resistance remains when the ideal source is deactivated.

## Quiz

1. A network has a Thevenin voltage of 30 V and a Thevenin resistance of 6 Ω. What is its Norton current?

   - [ ] 180 A
   - [ ] 6 A
   - [x] 5 A
   - [ ] 0.2 A

   > Norton current is \(I_N=V_{TH}/R_{TH}=30/6=5\) A.

2. When applying superposition to a circuit, what should be done with an ideal independent voltage source that is temporarily deactivated?

   - [ ] Replace it with an open circuit.
   - [x] Replace it with a short circuit.
   - [ ] Replace it with a current source.
   - [ ] Leave it active at its original voltage.

   > A deactivated ideal voltage source has zero voltage, which is equivalent to a short circuit.

3. Two independent sources produce currents of 7 A and 3 A through a resistor in opposite directions. What is the actual current magnitude?

   - [ ] 10 A
   - [ ] 7 A
   - [x] 4 A
   - [ ] 21 A

   > Superposition requires algebraic addition. Taking the 7 A direction as positive gives \(I=7-3=4\) A.