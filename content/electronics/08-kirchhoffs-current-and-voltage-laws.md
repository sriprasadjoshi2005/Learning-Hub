---
title: Kirchhoff's Current and Voltage Laws
level: intermediate
---

# Kirchhoff's Current and Voltage Laws

Complex electronic circuits often contain multiple interconnected branches and loops that cannot be analysed efficiently using simple series-parallel reduction alone. Kirchhoff's laws provide a systematic mathematical method for determining unknown currents and voltages in such networks.

Kirchhoff's Current Law (KCL) is based on conservation of electric charge, while Kirchhoff's Voltage Law (KVL) is based on conservation of energy in a lumped circuit model.

These laws are fundamental to circuit analysis and are used in transistor biasing, power supply design, sensor networks and electronic instrumentation.

This lesson develops KCL, KVL, sign conventions, node analysis, loop equations and practical applications. By the end, you will be able to formulate circuit equations, solve multi-branch networks and verify circuit behaviour using conservation principles.

## 1. Kirchhoff's Current Law

### 1.1 Statement of KCL

Kirchhoff's Current Law states that the algebraic sum of currents entering and leaving a node is zero.

$$\sum I=0$$

Equivalently:

$$\sum I_{in}=\sum I_{out}$$

### 1.2 Physical Principle

KCL follows from conservation of electric charge.

An ideal circuit node cannot continuously accumulate electric charge. Therefore, the total current entering a node must equal the total current leaving it.

### 1.3 Sign Convention

Choose a consistent sign convention:

- Currents entering a node: Positive.
- Currents leaving a node: Negative.

Then:

$$I_1+I_2-I_3-I_4=0$$

The opposite sign convention is equally valid if used consistently.

### 1.4 Example Node

```text
             I1 = 5 A
                |
                v
        I2 ---> NODE ----> I3
         2 A              4 A
                |
                v
               I4
```

Applying KCL:

$$I_1+I_2=I_3+I_4$$

$$5+2=4+I_4$$

$$I_4=3\text{ A}$$

## 2. Kirchhoff's Voltage Law

### 2.1 Statement of KVL

Kirchhoff's Voltage Law states that the algebraic sum of all voltage changes around any closed loop is zero.

$$\sum V=0$$

### 2.2 Physical Principle

KVL follows from conservation of energy.

A charge travelling around a closed path returns to its initial potential. The total energy gained from sources must equal the total energy lost in circuit elements, under the lumped-circuit assumptions.

### 2.3 Sign Convention

When traversing a loop:

- Moving from the negative to positive terminal of a source: Voltage rise.
- Moving from positive to negative terminal of a source: Voltage drop.
- Moving through a resistor in the direction of current: Voltage drop $IR$.
- Moving through a resistor opposite to current: Voltage rise $IR$.

### 2.4 Simple Loop

For a source $V_s$ and two series resistors:

$$V_s-I R_1-I R_2=0$$

Therefore:

$$V_s=I(R_1+R_2)$$

## 3. KCL and Node Equations

### 3.1 Node Voltage

Node voltage is the potential difference between a node and a selected reference node.

A common reference is ground, assigned 0 V.

### 3.2 Applying KCL Using Conductance

For a node voltage $V$ connected through resistors to known voltages $V_1,V_2,\ldots$:

$$\sum_k\frac{V-V_k}{R_k}=0$$

This is the foundation of nodal analysis.

### 3.3 Multiple Unknown Nodes

For circuits with several unknown node voltages, write one independent KCL equation for each non-reference node.

The resulting simultaneous equations can be solved using substitution, elimination or matrix methods.

## 4. KVL and Loop Equations

### 4.1 Loop Current

A loop current is an assumed current circulating around a chosen closed path.

For a single loop, KVL can produce one equation in one unknown current.

### 4.2 Shared Resistors

When two loop currents pass through a shared resistor, the resistor current depends on their relative directions.

For clockwise mesh currents $I_1$ and $I_2$, if both reference directions pass through the shared resistor in opposite directions:

$$I_R=I_1-I_2$$

The corresponding voltage drop in the first mesh is:

$$V_R=R(I_1-I_2)$$

### 4.3 Dependent and Independent Equations

A circuit may contain many loops, but not all loop equations are independent.

Redundant equations do not provide additional information.

The number of independent network equations depends on circuit topology.

## 5. Limits and Practical Interpretation

KCL and KVL are fundamental laws, but practical high-frequency circuits require care.

- At high frequencies, parasitic capacitance and inductance become important.
- Time-varying magnetic flux linking a loop can produce an induced EMF.
- Distributed transmission-line effects may make a simple lumped model inaccurate.

KCL remains valid when all relevant currents, including displacement current where required by the electromagnetic model, are accounted for.

The ordinary KVL form applies directly to lumped circuits without unaccounted time-varying magnetic flux linkage.

## 6. Mathematical Derivations and Numerical Examples

### Example 1: Applying KCL at a Node

**Given:**

At a node:

- 6 A enters.
- 2.5 A enters.
- 3 A leaves.
- An unknown current $I_x$ leaves.

Determine $I_x$.

**Formula:**

$$\sum I_{in}=\sum I_{out}$$

**Solution:**

1. Write incoming current:

   $$I_{in}=6+2.5=8.5\text{ A}$$

2. Write outgoing current:

   $$I_{out}=3+I_x$$

3. Equate:

   $$8.5=3+I_x$$

4. Solve:

   $$I_x=5.5\text{ A}$$

**Final Answer:**

The unknown current leaving the node is **5.5 A**.

### Example 2: Applying KVL to a Series Circuit

**Given:**

A 24 V source is connected in series with:

- $R_1=4\ \Omega$
- $R_2=8\ \Omega$

Determine current and voltage drops.

**Formula:**

$$24-4I-8I=0$$

**Solution:**

1. Combine resistance:

   $$24=12I$$

2. Calculate current:

   $$I=2\text{ A}$$

3. Voltage across the first resistor:

   $$V_1=2\times4=8\text{ V}$$

4. Voltage across the second resistor:

   $$V_2=2\times8=16\text{ V}$$

5. Verify:

   $$24-8-16=0$$

**Final Answer:**

- Current = **2 A**.
- First voltage drop = **8 V**.
- Second voltage drop = **16 V**.

### Example 3: Solving a Two-Node Circuit

**Given:**

An unknown node voltage $V$ is connected:

- To a 12 V node through 2 k$\Omega$.
- To ground through 4 k$\Omega$.
- To a 6 V node through 3 k$\Omega$.

Determine $V$.

**Formula:**

Apply KCL:

$$\frac{V-12}{2k}+\frac{V}{4k}+\frac{V-6}{3k}=0$$

**Solution:**

1. Multiply the equation by 12 k$\Omega$:

   $$6(V-12)+3V+4(V-6)=0$$

2. Expand:

   $$6V-72+3V+4V-24=0$$

3. Combine:

   $$13V-96=0$$

4. Solve:

   $$V=\frac{96}{13}$$

   $$V\approx7.385\text{ V}$$

**Final Answer:**

The unknown node voltage is approximately **7.385 V** relative to ground.

## 7. Practical Applications

### 7.1 Circuit Troubleshooting

KCL and KVL help identify unexpected current paths, incorrect connections and voltage drops.

### 7.2 Transistor Bias Networks

Node equations are used to determine transistor terminal voltages and currents.

### 7.3 Power Supply Networks

Kirchhoff's laws help analyse voltage regulation and current distribution.

### 7.4 Sensor Interfaces

Multi-branch sensor networks can be analysed using nodal equations.

### 7.5 Automated Circuit Simulation

Circuit simulators use network equations derived from Kirchhoff's laws to determine node voltages and branch currents.

## 8. Important Comparisons and Observations

| Feature | KCL | KVL |
|---|---|---|
| Governing principle | Conservation of charge | Conservation of energy |
| Applied to | Nodes | Closed loops |
| Main relationship | Sum of currents is zero | Sum of voltages is zero |
| Typical use | Nodal analysis | Loop or mesh analysis |
| Mathematical form | $\sum I=0$ | $\sum V=0$ |

### Important Observations

1. KCL must hold at every circuit node.
2. KVL must hold around every valid closed loop under the lumped-circuit assumptions.
3. Sign conventions are essential.
4. A negative calculated current means actual current flows opposite to the assumed reference direction.
5. A negative node voltage means the node is below the chosen reference.
6. Independent equations are sufficient; redundant equations do not add information.

## 9. Common Exam Traps

- **Reversing current directions:** KCL works with any consistent sign convention.
- **Ignoring resistor polarity:** The voltage drop depends on the assumed current direction.
- **Assuming a negative result is automatically incorrect:** It often indicates the actual direction is opposite to the chosen reference.
- **Confusing node and loop equations:** KCL applies at nodes; KVL applies around loops.
- **Writing too many redundant equations:** Only independent equations are needed.
- **Ignoring shared resistors:** Their current is the algebraic combination of relevant mesh currents.
- **Applying elementary KVL without considering induced EMF:** High-frequency and time-varying magnetic systems may require a more complete electromagnetic treatment.

## Quiz

1. At a circuit node, currents of 4 A and 7 A enter, while currents of 3 A and $I_x$ leave. What is $I_x$?

   - [ ] 4 A
   - [ ] 6 A
   - [x] 8 A
   - [ ] 14 A

   > By KCL, incoming current equals outgoing current. Therefore, $4+7=3+I_x$, giving $I_x=8\text{ A}$.

2. Which physical principle directly underlies Kirchhoff's Current Law?

   - [ ] Conservation of angular momentum.
   - [ ] Conservation of mechanical energy.
   - [x] Conservation of electric charge.
   - [ ] Conservation of magnetic flux.

   > KCL follows from charge conservation. In an ideal circuit node, charge does not continuously accumulate, so total incoming current equals total outgoing current.

3. A mesh analysis assumes clockwise currents of 3 A and 5 A in two adjacent meshes. A 4 $\Omega$ resistor is shared by the meshes, with the assumed mesh currents passing through it in opposite directions. What is the magnitude of the current through the shared resistor?

   - [ ] 5 A
   - [ ] 3 A
   - [x] 2 A
   - [ ] 8 A

   > The shared resistor current is the algebraic difference of the mesh currents: $|I_1-I_2|=|3-5|=2\text{ A}$. **Correction:** The options contain a duplicate 2 A answer. This question must be revised before use.
