---
title: Basic Circuit Analysis Using Equivalent Resistance and Network Reduction
level: intermediate
---

# Basic Circuit Analysis Using Equivalent Resistance and Network Reduction

Real electronic circuits often contain several resistors arranged in combinations that are not immediately obvious. Simplifying these networks into equivalent circuits makes it possible to calculate total current, voltage distribution, branch currents and power consumption efficiently.

Network reduction is the process of replacing a portion of a circuit with an electrically equivalent simpler network. The external behaviour of the reduced network remains unchanged at the terminals of interest.

This lesson consolidates series-parallel reduction, equivalent resistance, terminal behaviour, symmetry, balanced bridge networks and systematic circuit-solving techniques. It also introduces the distinction between simple series-parallel networks and more general resistor networks that require Kirchhoff's laws or network theorems.

By the end of this lesson, you will be able to reduce complex resistor networks, recognize balanced bridge conditions, determine equivalent resistance between terminals and choose an appropriate circuit-analysis method.

## 1. Equivalent Circuits

### 1.1 Definition

Two circuits are equivalent at a specified pair of terminals if they exhibit the same terminal voltage-current relationship under the conditions of interest.

For a purely resistive network, its equivalent resistance is the resistance that produces the same terminal behaviour as the original network.

$$R_{eq}=\frac{V_{terminal}}{I_{terminal}}$$

This relationship describes the equivalent resistance for a linear resistive network under a specified terminal test condition.

### 1.2 Purpose of Network Reduction

Network reduction is used to:

- Simplify circuit calculations.
- Determine total resistance.
- Calculate source current.
- Identify voltage and current distributions.
- Estimate power consumption.
- Simplify practical circuit design.

### 1.3 Equivalent Resistor Replacement

If a resistor network is replaced by an equivalent resistance, its external terminal behaviour remains unchanged.

However, internal branch currents and voltages are not automatically preserved by the replacement.

If internal quantities are needed, the original network must be restored mathematically after the total circuit has been analysed.

## 2. Systematic Series-Parallel Reduction

### 2.1 Identifying Series Combinations

Two resistors are in series when their common connecting node has no other branch connection.

Their equivalent resistance is:

$$R_{eq}=R_1+R_2$$

### 2.2 Identifying Parallel Combinations

Two resistors are in parallel when both their terminals connect to the same pair of nodes.

Their equivalent resistance is:

$$R_{eq}=\frac{R_1R_2}{R_1+R_2}$$

### 2.3 Reduction Strategy

A useful method is:

1. Redraw the circuit clearly.
2. Label all electrically distinct nodes.
3. Identify series and parallel groups.
4. Replace one group at a time.
5. Redraw the reduced circuit after every operation.
6. Repeat until the network is simplified.
7. Calculate total current and voltage.
8. Work backwards to obtain original branch quantities.

## 3. Special Parallel Relationships

### 3.1 Two Parallel Resistors

$$R_{eq}=\frac{R_1R_2}{R_1+R_2}$$

### 3.2 Three Parallel Resistors

$$R_{eq}=\frac{R_1R_2R_3}{R_1R_2+R_2R_3+R_3R_1}$$

### 3.3 Identical Parallel Resistors

For $n$ identical resistors:

$$R_{eq}=\frac{R}{n}$$

### 3.4 Conductance Method

Parallel combinations are often simpler using conductance.

$$G_{eq}=G_1+G_2+\cdots+G_n$$

Since:

$$G=\frac{1}{R}$$

This gives:

$$\frac{1}{R_{eq}}=\sum_i\frac{1}{R_i}$$

## 4. Open Circuits and Short Circuits

### 4.1 Open Circuit

An ideal open circuit has infinite resistance.

$$R\rightarrow\infty$$

Its current is zero for a finite applied voltage.

$$I=0$$

### 4.2 Short Circuit

An ideal short circuit has zero resistance.

$$R=0$$

Its voltage drop is zero for finite current.

A practical short circuit can produce extremely high current, limited by source and conductor impedances.

### 4.3 Effect on Resistor Networks

- A resistor in series with an open circuit interrupts the entire series path.
- A short circuit connected in parallel with a resistor bypasses that resistor.
- An open parallel branch carries no current.
- A shorted branch may cause excessive source current.

## 5. Symmetry in Resistor Networks

Symmetry can simplify some resistor networks.

If a network is geometrically and electrically symmetrical, certain nodes may have equal potentials.

When two nodes have the same potential, a resistor connected between them has zero voltage across it and therefore carries zero current.

However, symmetry must be established from the actual circuit connections and component values, not merely from how the diagram looks.

## 6. Balanced Wheatstone Bridge

A Wheatstone bridge contains four resistive arms arranged in a bridge configuration.

It is commonly used to measure unknown resistance.

```text
              A
             / \
           R1   R2
           /     \
          B---G---C
           \     /
           R3   R4
             \ /
              D
```

Here, a galvanometer or detector is connected between B and C.

The bridge is balanced when no current flows through the detector.

Therefore:

$$V_B=V_C$$

The balance condition is:

$$\frac{R_1}{R_2}=\frac{R_3}{R_4}$$

Equivalently:

$$R_1R_4=R_2R_3$$

This relationship is useful for determining an unknown resistance.

## 7. Limitations of Simple Network Reduction

Not every resistor network can be simplified using only series and parallel formulas.

A network may contain:

- Multiple interconnected branches.
- Bridge connections.
- Shared resistors.
- Multiple independent voltage sources.
- Nodes with complex connectivity.

In these cases, Kirchhoff's laws and more advanced network theorems are required.

Two common transformations are:

- Delta-to-star conversion.
- Star-to-delta conversion.

These transformations will be explored in greater depth when studying advanced circuit network analysis.

## 8. Mathematical Derivations and Numerical Examples

### Example 1: Multi-Stage Series-Parallel Network

**Given:**

A 30 V source supplies:

- A 5 $\Omega$ resistor in series with
- A parallel network containing 10 $\Omega$ and 15 $\Omega$ resistors.

Determine total resistance, source current and branch currents.

**Solution:**

1. Calculate parallel resistance:

   $$R_p=\frac{10\times15}{10+15}$$

   $$R_p=6\ \Omega$$

2. Calculate total resistance:

   $$R_{eq}=5+6=11\ \Omega$$

3. Calculate source current:

   $$I=\frac{30}{11}$$

   $$I\approx2.727\text{ A}$$

4. Calculate voltage across the 5 $\Omega$ resistor:

   $$V_1=2.727\times5$$

   $$V_1\approx13.636\text{ V}$$

5. Calculate voltage across the parallel network:

   $$V_p=30-13.636$$

   $$V_p\approx16.364\text{ V}$$

6. Determine branch currents:

   $$I_{10}=\frac{16.364}{10}=1.636\text{ A}$$

   $$I_{15}=\frac{16.364}{15}=1.091\text{ A}$$

7. Verify:

   $$1.636+1.091=2.727\text{ A}$$

**Final Answer:**

- Equivalent resistance = **11 $\Omega$**.
- Source current = **2.727 A**.
- 10 $\Omega$ branch current = **1.636 A**.
- 15 $\Omega$ branch current = **1.091 A**.

### Example 2: Unknown Resistance in a Balanced Wheatstone Bridge

**Given:**

A Wheatstone bridge is balanced with:

- $R_1=100\ \Omega$
- $R_2=200\ \Omega$
- $R_3=150\ \Omega$
- Unknown resistance $R_4$

Determine $R_4$.

**Formula:**

$$\frac{R_1}{R_2}=\frac{R_3}{R_4}$$

Rearranging:

$$R_4=\frac{R_2R_3}{R_1}$$

**Solution:**

1. Substitute:

   $$R_4=\frac{200\times150}{100}$$

2. Calculate:

   $$R_4=300\ \Omega$$

**Final Answer:**

The unknown resistance is **300 $\Omega$**.

### Example 3: Equivalent Resistance Using Conductance

**Given:**

Four resistors are connected in parallel:

- 100 $\Omega$
- 200 $\Omega$
- 300 $\Omega$
- 600 $\Omega$

Determine the equivalent resistance.

**Formula:**

$$G_{eq}=\sum_i\frac{1}{R_i}$$

$$R_{eq}=\frac{1}{G_{eq}}$$

**Solution:**

1. Calculate individual conductances:

   $$G_1=0.01\text{ S}$$

   $$G_2=0.005\text{ S}$$

   $$G_3=0.003333\text{ S}$$

   $$G_4=0.001667\text{ S}$$

2. Add conductances:

   $$G_{eq}=0.01+0.005+0.003333+0.001667$$

   $$G_{eq}=0.020\text{ S}$$

3. Calculate equivalent resistance:

   $$R_{eq}=\frac{1}{0.020}$$

   $$R_{eq}=50\ \Omega$$

**Final Answer:**

The equivalent resistance is **50 $\Omega$**.

## 9. Practical Applications

### 9.1 Circuit Design

Engineers simplify resistor networks before selecting component values and analysing power consumption.

### 9.2 Resistance Measurement

Wheatstone bridge circuits accurately measure small resistance changes.

### 9.3 Fault Detection

Short and open circuit analysis helps identify damaged components and wiring faults.

### 9.4 Sensor Systems

Resistive sensors are often incorporated into bridge networks for accurate measurement.

### 9.5 Power Distribution

Equivalent resistance calculations help determine total load and source current.

## 10. Important Comparisons and Observations

### 10.1 Network Types

| Network | Equivalent Resistance |
|---|---|
| Series | $R_1+R_2+\cdots$ |
| Parallel | Reciprocal sum |
| Identical parallel resistors | $R/n$ |
| Balanced Wheatstone bridge | Determined by bridge balance condition |

### 10.2 Important Observations

1. Equivalent resistance describes terminal behaviour.
2. Internal branch currents must be recovered from the original network.
3. Parallel resistance is smaller than the smallest positive branch resistance.
4. Series resistance is greater than any individual positive resistance.
5. A balanced bridge has zero detector current.
6. Symmetry can simplify networks when equal-potential conditions are established.
7. Not all networks are reducible using basic series-parallel formulas.

## 11. Common Exam Traps

- **Combining resistors based on visual appearance:** Electrical node connections determine series and parallel relationships.
- **Forgetting to redraw reduced circuits:** This can cause incorrect assumptions about connectivity.
- **Using a bridge formula without checking balance:** The Wheatstone balance condition applies only when detector current is zero.
- **Assuming symmetry without proof:** Equal-looking branches do not guarantee equal potentials if component values differ.
- **Treating an open circuit as zero resistance:** An ideal open has infinite resistance.
- **Treating a short circuit as infinite resistance:** An ideal short has zero resistance.
- **Assuming every network can be reduced using series and parallel combinations:** More general network-analysis methods are sometimes required.

## Quiz

1. A 6 $\Omega$ resistor is connected in series with a parallel combination of 12 $\Omega$ and 4 $\Omega$. What is the total equivalent resistance?

   - [ ] 7 $\Omega$
   - [ ] 8 $\Omega$
   - [x] 9 $\Omega$
   - [ ] 10 $\Omega$

   > The parallel combination is $(12\times4)/(12+4)=48/16=3\ \Omega$. Adding the series resistance gives $6+3=9\ \Omega$.

2. In a balanced Wheatstone bridge, what is the potential difference across the galvanometer connected between the two middle junctions?

   - [ ] Equal to the supply voltage.
   - [ ] Half the supply voltage.
   - [x] Zero.
   - [ ] Dependent only on galvanometer resistance.

   > A balanced bridge has equal potentials at the two detector junctions. Therefore, the potential difference is zero and no current flows through an ideal galvanometer branch.

3. A balanced Wheatstone bridge has $R_1=80\ \Omega$, $R_2=120\ \Omega$ and $R_3=200\ \Omega$. What is the unknown resistance $R_4$?

   - [ ] 150 $\Omega$
   - [ ] 240 $\Omega$
   - [x] 300 $\Omega$
   - [ ] 400 $\Omega$

   > The balance condition is $R_1/R_2=R_3/R_4$. Rearranging gives $R_4=R_2R_3/R_1=(120\times200)/80=300\ \Omega$.
