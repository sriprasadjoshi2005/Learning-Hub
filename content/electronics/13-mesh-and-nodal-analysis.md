---
title: Mesh and Nodal Analysis
level: intermediate
---

# Mesh and Nodal Analysis

## Introduction

Mesh and nodal analysis are systematic methods used to determine unknown currents and voltages in electrical networks. They are especially useful when circuits contain several resistors, voltage sources, current sources, and interconnected branches.

Instead of simplifying every network into a single equivalent resistance, these methods apply Kirchhoff's voltage law and Kirchhoff's current law to establish simultaneous equations.

Mesh analysis focuses on currents circulating around independent loops in a planar circuit. Nodal analysis focuses on voltages at circuit nodes relative to a selected reference node.

Both methods are fundamental to electrical engineering, electronic circuit simulation, network design, and advanced circuit theory.

## 1. Fundamental Concepts

### 1.1 Branch

A branch is a portion of a circuit containing one or more elements connected between two nodes.

### 1.2 Node

A node is a point or continuous conducting region at which two or more circuit elements are connected.

### 1.3 Loop

A loop is any closed path in a circuit.

### 1.4 Mesh

A mesh is a loop that contains no other loop within it.

Mesh analysis is applicable directly to planar circuits.

### 1.5 Reference Node

A reference node is selected as the zero-voltage point.

Its voltage is defined as:

\[
V_{ref}=0
\]

Other node voltages are measured relative to this point.

## 2. Mesh Analysis

Mesh analysis is based on Kirchhoff's voltage law.

It assigns a current variable to each independent mesh and develops equations by summing the voltage changes around each mesh.

### 2.1 Mesh Current Direction

Mesh currents are usually assumed to flow clockwise.

The chosen direction is arbitrary. If the calculated current is negative, the actual current flows in the opposite direction.

### 2.2 Basic Two-Mesh Circuit

Consider two meshes sharing a resistor.

Let:
- \(I_1\) = clockwise current in mesh 1.
- \(I_2\) = clockwise current in mesh 2.
- \(R_1\) = resistor in mesh 1 only.
- \(R_2\) = resistor in mesh 2 only.
- \(R_3\) = shared resistor.

The current through the shared resistor, when measured in the direction of \(I_1\), is:

\[
I_1-I_2
\]

### 2.3 Mesh Equation for the First Loop

Applying Kirchhoff's voltage law:

\[
V_1=I_1R_1+(I_1-I_2)R_3
\]

Expanding:

\[
V_1=I_1R_1+I_1R_3-I_2R_3
\]

Rearranging:

\[
\boxed{(R_1+R_3)I_1-R_3I_2=V_1}
\]

### 2.4 Mesh Equation for the Second Loop

Similarly:

\[
V_2=I_2R_2+(I_2-I_1)R_3
\]

Expanding:

\[
V_2=I_2R_2+I_2R_3-I_1R_3
\]

Therefore:

\[
\boxed{-R_3I_1+(R_2+R_3)I_2=V_2}
\]

These two equations can be solved simultaneously.

## 3. General Mesh Analysis Procedure

1. Identify all independent meshes.
2. Assign a current to each mesh.
3. Choose a consistent direction, usually clockwise.
4. Apply Kirchhoff's voltage law to each mesh.
5. Express shared-resistor voltage drops using the difference between mesh currents.
6. Rearrange the equations.
7. Solve the simultaneous equations.
8. Interpret negative currents as currents flowing opposite to the assumed direction.

## 4. Mesh Analysis with Current Sources

When a current source is located in a branch belonging to only one mesh, the corresponding mesh current may be directly known.

For example, if a 3 A current source lies only in mesh 1 and points in the assumed mesh-current direction:

\[
I_1=3\text{ A}
\]

If its direction is opposite:

\[
I_1=-3\text{ A}
\]

### 4.1 Supermesh

A supermesh is formed when a current source lies in the common branch between two adjacent meshes.

The current-source branch is excluded from the combined KVL path.

The procedure is:

1. Combine the two adjacent meshes into one larger loop.
2. Apply KVL around the outer perimeter.
3. Write an additional equation based on the current source.
4. Solve the resulting equations.

If the source current flows in the direction of \(I_1\) and opposite to \(I_2\):

\[
\boxed{I_1-I_2=I_s}
\]

The exact sign depends on the chosen current directions and source-arrow orientation.

## 5. Nodal Analysis

Nodal analysis is based on Kirchhoff's current law.

It determines unknown node voltages by applying current conservation at each non-reference node.

### 5.1 Node Voltage Method

The voltage of a node is measured relative to the reference node.

For a resistor connected between two nodes:

\[
I=\frac{V_1-V_2}{R}
\]

Where \(V_1\) and \(V_2\) are the node voltages at its terminals.

If one terminal is connected to ground:

\[
I=\frac{V_1}{R}
\]

### 5.2 Basic Nodal Equation

Consider a node \(V_1\) connected:
- To a voltage source through \(R_1\).
- To ground through \(R_2\).
- To another node \(V_2\) through \(R_3\).

Applying KCL, taking currents leaving the node as positive:

\[
\frac{V_1-V_s}{R_1}+\frac{V_1}{R_2}+\frac{V_1-V_2}{R_3}=0
\]

This equation relates the unknown node voltages to the known source voltage and resistances.

## 6. General Nodal Analysis Procedure

1. Identify all circuit nodes.
2. Select a reference node.
3. Assign voltage variables to the remaining nodes.
4. Express each branch current using Ohm's law.
5. Apply KCL at every non-reference node.
6. Rearrange the equations into simultaneous equations.
7. Solve for the unknown node voltages.
8. Calculate branch currents from the voltage differences.

## 7. Nodal Analysis with Current Sources

Current sources are often convenient in nodal analysis.

Suppose a current source injects current \(I_s\) into a node connected to two resistors leading to ground.

Applying KCL:

\[
I_s=\frac{V}{R_1}+\frac{V}{R_2}
\]

Rearranging:

\[
\boxed{V=\frac{I_s}{1/R_1+1/R_2}}
\]

The denominator is the total conductance connected to the node.

## 8. Supernode

A supernode occurs when an ideal voltage source connects two non-reference nodes.

The voltage source directly establishes a relationship between the two node voltages.

For a voltage source \(V_s\) with positive terminal at node \(V_1\) and negative terminal at node \(V_2\):

\[
\boxed{V_1-V_2=V_s}
\]

The two nodes and voltage source are treated as one extended region for KCL.

The procedure is:

1. Identify the voltage source connecting the two non-reference nodes.
2. Enclose both nodes and the source in a supernode.
3. Apply KCL around the outer boundary.
4. Add the voltage-source constraint equation.
5. Solve the simultaneous equations.

## 9. Matrix Representation

Mesh and nodal equations can be expressed using matrices.

### 9.1 Mesh Matrix

For a two-mesh circuit:

\[
\begin{bmatrix}
R_1+R_3 & -R_3\\
-R_3 & R_2+R_3
\end{bmatrix}
\begin{bmatrix}
I_1\\
I_2
\end{bmatrix}
=
\begin{bmatrix}
V_1\\
V_2
\end{bmatrix}
\]

The diagonal terms represent the total resistance in each mesh.

The off-diagonal terms represent negative shared resistances.

### 9.2 Nodal Matrix

For a two-node resistive network:

\[
\begin{bmatrix}
G_{11} & -G_{12}\\
-G_{21} & G_{22}
\end{bmatrix}
\begin{bmatrix}
V_1\\
V_2
\end{bmatrix}
=
\begin{bmatrix}
I_1\\
I_2
\end{bmatrix}
\]

Here:
- Diagonal terms represent total conductance connected to each node.
- Off-diagonal terms represent negative conductance directly connecting the nodes.
- The right-hand side represents net current injected into each node.

For ordinary reciprocal resistor networks:

\[
G_{12}=G_{21}
\]

## 10. Choosing Between Mesh and Nodal Analysis

| Feature | Mesh analysis | Nodal analysis |
|---|---|---|
| Main law | KVL | KCL |
| Unknowns | Mesh currents | Node voltages |
| Particularly convenient with | Voltage sources | Current sources |
| Main equations | Voltage equations | Current equations |
| Special technique | Supermesh | Supernode |
| Direct applicability | Planar circuits | General lumped networks |

The most efficient method usually has fewer independent unknowns.

## 11. Worked Numerical Examples

### Example 1: Two-Mesh Analysis

**Given:**

A two-mesh circuit has:
- \(R_1=4\ \Omega\)
- \(R_2=6\ \Omega\)
- Shared resistance \(R_3=2\ \Omega\)
- First source \(V_1=12\text{ V}\)
- Second source \(V_2=6\text{ V}\)

Both source polarities support the assumed clockwise mesh directions.

**Find:** Mesh currents.

**Solution:**

First mesh:

\[
(4+2)I_1-2I_2=12
\]

\[
6I_1-2I_2=12
\]

Second mesh:

\[
-2I_1+(6+2)I_2=6
\]

\[
-2I_1+8I_2=6
\]

Multiply the first equation by 4:

\[
24I_1-8I_2=48
\]

Multiply the second equation by 1:

\[
-2I_1+8I_2=6
\]

Adding:

\[
22I_1=54
\]

\[
\boxed{I_1=2.455\text{ A}}
\]

Substitute into the first equation:

\[
6(2.455)-2I_2=12
\]

\[
I_2=1.364\text{ A}
\]

**Final Answer:**

\[
\boxed{I_1=2.455\text{ A}}
\]

\[
\boxed{I_2=1.364\text{ A}}
\]

Shared resistor current:

\[
I_3=I_1-I_2
\]

\[
\boxed{I_3=1.091\text{ A}}
\]

### Example 2: Nodal Analysis with Two Unknown Nodes

**Given:**

- A 10 V source connects to node \(V_1\) through a 2 Ω resistor.
- Node \(V_1\) connects to ground through 4 Ω.
- Node \(V_1\) connects to node \(V_2\) through 2 Ω.
- Node \(V_2\) connects to ground through 4 Ω.

**Find:** Both node voltages.

**Solution:**

At node \(V_1\):

\[
\frac{V_1-10}{2}+\frac{V_1}{4}+\frac{V_1-V_2}{2}=0
\]

Multiplying by 4:

\[
2V_1-20+V_1+2V_1-2V_2=0
\]

\[
5V_1-2V_2=20
\]

At node \(V_2\):

\[
\frac{V_2-V_1}{2}+\frac{V_2}{4}=0
\]

Multiplying by 4:

\[
2V_2-2V_1+V_2=0
\]

\[
-2V_1+3V_2=0
\]

From the second equation:

\[
V_2=\frac{2V_1}{3}
\]

Substitute into the first:

\[
5V_1-\frac{4V_1}{3}=20
\]

\[
\frac{11V_1}{3}=20
\]

\[
\boxed{V_1=5.455\text{ V}}
\]

Therefore:

\[
\boxed{V_2=3.636\text{ V}}
\]

### Example 3: Nodal Analysis with a Current Source

**Given:**

- A 6 A current source injects current into a node.
- The node connects to ground through 3 Ω and 6 Ω resistors in parallel.

**Find:** Node voltage and branch currents.

**Solution:**

Applying KCL:

\[
6=\frac{V}{3}+\frac{V}{6}
\]

\[
6=\frac{2V+V}{6}
\]

\[
36=3V
\]

\[
\boxed{V=12\text{ V}}
\]

Current through 3 Ω:

\[
I_1=\frac{12}{3}=4\text{ A}
\]

Current through 6 Ω:

\[
I_2=\frac{12}{6}=2\text{ A}
\]

Verification:

\[
I_1+I_2=4+2=6\text{ A}
\]

### Example 4: Mesh Analysis with a Shared Resistor

**Given:**

- First mesh resistance excluding shared branch = 5 Ω.
- Second mesh resistance excluding shared branch = 7 Ω.
- Shared resistance = 3 Ω.
- First source = 20 V.
- Second source = 10 V.

**Find:** Mesh currents.

**Solution:**

First mesh:

\[
(5+3)I_1-3I_2=20
\]

\[
8I_1-3I_2=20
\]

Second mesh:

\[
-3I_1+(7+3)I_2=10
\]

\[
-3I_1+10I_2=10
\]

Multiply the first equation by 10:

\[
80I_1-30I_2=200
\]

Multiply the second equation by 3:

\[
-9I_1+30I_2=30
\]

Adding:

\[
71I_1=230
\]

\[
\boxed{I_1=3.239\text{ A}}
\]

Substituting:

\[
8(3.239)-3I_2=20
\]

\[
\boxed{I_2=1.304\text{ A}}
\]

Shared branch current:

\[
I_3=I_1-I_2
\]

\[
\boxed{I_3=1.935\text{ A}}
\]

## 12. Practical Applications

Mesh and nodal analysis are used in:

- Complex resistor-network analysis.
- Electronic circuit design.
- Transistor bias-network analysis.
- Power distribution calculations.
- Operational amplifier circuit analysis.
- Circuit simulation software.
- Network modelling and engineering problem solving.

Nodal analysis is especially useful in many computer-based circuit solvers because node-voltage equations can be systematically assembled into matrices.

## 13. Common Exam Traps

1. **Incorrect shared-resistor current:** The voltage drop across a resistor shared by two meshes depends on the difference between mesh currents.

2. **Inconsistent current directions:** Choose directions first and maintain them throughout the equations.

3. **Incorrect source polarity:** A voltage rise and voltage drop must be assigned according to the direction of traversal.

4. **Confusing nodes with meshes:** Nodal analysis determines node voltages, whereas mesh analysis determines loop currents.

5. **Forgetting the supermesh constraint:** A current source between two meshes requires an additional current relationship.

6. **Forgetting the supernode constraint:** A voltage source between two non-reference nodes requires a voltage relationship.

7. **Incorrect reference-node selection:** All node voltages must be measured relative to the same reference.

8. **Assuming negative results are invalid:** A negative current or voltage indicates that the actual direction or polarity is opposite to the assumed one.

## Quiz

1. Two clockwise mesh currents of 5 A and 2 A flow through adjacent meshes sharing a 4 Ω resistor. What is the current through the shared resistor in the direction of the first mesh current?

   - [ ] 7 A
   - [ ] 2 A
   - [x] 3 A
   - [ ] 5 A

   > The shared branch current is the algebraic difference between the mesh currents: \(I_1-I_2=5-2=3\) A.

2. Which circuit-analysis method is generally more convenient when a network contains several independent current sources?

   - [ ] Mesh analysis in every case
   - [x] Nodal analysis
   - [ ] Source transformation is compulsory
   - [ ] Equivalent resistance alone

   > Nodal analysis uses KCL and treats current sources naturally as current injections or withdrawals at nodes. This often reduces the number of equations.

3. A current source is connected between two non-reference nodes. Which technique is required to handle the voltage-source constraint associated with this arrangement in nodal analysis?

   - [ ] Supermesh
   - [ ] Voltage divider
   - [x] Supernode
   - [ ] Current divider

   > A voltage source between two non-reference nodes creates a supernode. KCL is applied around the supernode boundary, and an additional voltage constraint relates the node voltages.