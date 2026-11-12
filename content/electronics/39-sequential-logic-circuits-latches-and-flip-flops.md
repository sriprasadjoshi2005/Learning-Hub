---
title: Sequential Logic Circuits Including Latches and Flip-Flops
level: intermediate
---

# Sequential Logic Circuits Including Latches and Flip-Flops

Sequential logic circuits are digital circuits whose outputs depend on both present inputs and previously stored information.

Unlike combinational circuits, sequential circuits contain memory elements.

These circuits are essential in processors, counters, registers, communication systems, digital controllers, and computer memory.

The fundamental memory elements used in sequential logic are latches and flip-flops.

This lesson introduces sequential circuits, feedback, clock signals, SR latches, gated latches, D flip-flops, JK flip-flops, T flip-flops, triggering methods, and timing characteristics.

## 1. Introduction to Sequential Logic

A sequential circuit produces outputs based on:

- Present input values.
- Previously stored information.

Its behaviour can be represented as:

\[
Q_{next}=f(Q_{present},X)
\]

Where:

- \(Q_{next}\) = next state.
- \(Q_{present}\) = present state.
- \(X\) = present input.

The stored state allows a sequential circuit to remember information.

### 1.1 Difference Between Combinational and Sequential Circuits

| Property | Combinational circuit | Sequential circuit |
|---|---|---|
| Output depends on | Present inputs | Present inputs and previous state |
| Memory | Not required | Required |
| Feedback | Not normally required | Commonly used |
| Clock | Not generally required | May be required |
| Examples | Adders, decoders | Counters, registers, flip-flops |

## 2. Basic Memory Concept

A memory element stores a binary value.

A single binary storage element can hold:

\[
Q=0
\]

or:

\[
Q=1
\]

The complementary output is often available as:

\[
\overline Q
\]

A basic memory element must maintain its stored state until an appropriate input or control signal changes it.

## 3. SR Latch

An SR latch is a basic bistable memory circuit.

SR stands for:

- S: Set.
- R: Reset.

It can be constructed using two cross-coupled NOR gates or two cross-coupled NAND gates.

### 3.1 NOR-Based SR Latch

A NOR-based SR latch uses active-HIGH inputs.

Its inputs are S and R, and its outputs are Q and its complement.

### 3.2 Truth Table

| S | R | Next Q | Operation |
|---|---|---|---|
| 0 | 0 | Previous Q | Hold |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | Invalid | Forbidden condition |

### 3.3 Working Principle

**Set condition:**

When:

\[
S=1,\quad R=0
\]

the latch stores:

\[
Q=1
\]

**Reset condition:**

When:

\[
S=0,\quad R=1
\]

the latch stores:

\[
Q=0
\]

**Hold condition:**

When:

\[
S=0,\quad R=0
\]

the previous state is retained.

**Invalid condition:**

When:

\[
S=1,\quad R=1
\]

both outputs of the NOR latch are forced LOW, violating the normal complementary-output relationship.

This condition is avoided in normal operation.

## 4. NAND-Based SR Latch

A NAND-based SR latch uses active-LOW inputs.

Its inputs are commonly written as:

\[
\overline S,\quad\overline R
\]

### 4.1 Truth Table

| \(\overline S\) | \(\overline R\) | Operation |
|---|---|---|
| 1 | 1 | Hold |
| 0 | 1 | Set |
| 1 | 0 | Reset |
| 0 | 0 | Invalid |

The active input polarities are different from those of the NOR-based SR latch.

This distinction is important when analysing latch circuits.

## 5. Gated SR Latch

A gated SR latch includes an enable input.

The enable signal determines when the latch responds to the set and reset inputs.

When the enable is inactive, the stored state is maintained.

When the enable is active, the latch responds to its control inputs.

### 5.1 Applications

- Temporary data storage.
- Control circuits.
- Input synchronization structures.
- Basic memory circuits.

## 6. D Latch

A D latch is designed to eliminate the invalid input combination of the basic SR latch.

D stands for data.

It has:

- Data input D.
- Enable input E.
- Output Q.

### 6.1 Truth Table

| E | D | Next Q |
|---|---|---|
| 0 | X | Previous Q |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Here, X means that the input may be either 0 or 1.

### 6.2 Working Principle

When the enable signal is HIGH, the output follows the data input.

When the enable signal is LOW, the previous output is retained.

A D latch is therefore level-sensitive.

## 7. Flip-Flops

A flip-flop is a bistable storage element that commonly responds to a clock transition.

Unlike a level-sensitive latch, an edge-triggered flip-flop changes its stored state only at a specified clock edge.

The two common triggering edges are:

- Positive edge: transition from 0 to 1.
- Negative edge: transition from 1 to 0.

Flip-flops are fundamental components of synchronous digital systems.

## 8. D Flip-Flop

A D flip-flop stores the value present at its data input when the active clock edge occurs.

Its characteristic equation is:

\[
\boxed{Q_{next}=D}
\]

### 8.1 Truth Table

For a positive-edge-triggered D flip-flop:

| Clock condition | D | Next Q |
|---|---|---|
| Rising edge | 0 | 0 |
| Rising edge | 1 | 1 |
| No active edge | X | Previous Q |

### 8.2 Applications

- Data storage.
- Registers.
- Pipeline stages.
- Digital delay circuits.
- Synchronization circuits.

## 9. JK Flip-Flop

The JK flip-flop is a modified SR flip-flop that removes the forbidden input condition.

Its inputs are J and K.

### 9.1 Truth Table

| J | K | Next Q | Operation |
|---|---|---|---|
| 0 | 0 | Previous Q | Hold |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | Complement of previous Q | Toggle |

### 9.2 Characteristic Equation

\[
\boxed{Q_{next}=J\overline Q+\overline KQ}
\]

### 9.3 Toggle Operation

When:

\[
J=K=1
\]

the output changes to its opposite state at the active clock edge.

If:

\[
Q=0
\]

then:

\[
Q_{next}=1
\]

If:

\[
Q=1
\]

then:

\[
Q_{next}=0
\]

This makes the JK flip-flop useful in counter circuits.

## 10. T Flip-Flop

A T flip-flop is called a toggle flip-flop.

It has one input T.

### 10.1 Truth Table

| T | Next Q | Operation |
|---|---|---|
| 0 | Previous Q | Hold |
| 1 | Complement of previous Q | Toggle |

### 10.2 Characteristic Equation

\[
\boxed{Q_{next}=T\oplus Q}
\]

A T flip-flop can be constructed from a JK flip-flop by connecting:

\[
J=K=T
\]

### 10.3 Applications

- Binary counters.
- Frequency division.
- Sequential control circuits.

## 11. Clock Signals

A clock is a periodic digital signal used to coordinate operations in a synchronous system.

A clock alternates between logic LOW and logic HIGH.

Important clock parameters include:

- Clock period.
- Clock frequency.
- Duty cycle.
- Rising edge.
- Falling edge.

### 11.1 Clock Frequency

\[
\boxed{f=\frac{1}{T}}
\]

Where:

- \(f\) = clock frequency.
- \(T\) = clock period.

### 11.2 Duty Cycle

Duty cycle is the percentage of one clock period for which the signal remains HIGH.

\[
\boxed{
D=\frac{T_{HIGH}}{T}\times100\%
}
\]

A 50% duty-cycle clock spends equal time in HIGH and LOW states.

## 12. Timing Parameters

Flip-flops have timing requirements that must be satisfied for reliable operation.

### 12.1 Setup Time

Setup time is the minimum interval for which the data input must remain stable before the active clock edge.

### 12.2 Hold Time

Hold time is the minimum interval for which the data input must remain stable after the active clock edge.

### 12.3 Propagation Delay

Propagation delay is the time between the active clock transition and the corresponding output transition.

### 12.4 Metastability

Metastability may occur when setup or hold requirements are violated.

The output may temporarily remain at an intermediate voltage or take an unusually long time to settle to a valid logic state.

Metastability is an important concern when transferring asynchronous signals into synchronous digital systems.

## 13. Asynchronous Set and Reset

Some flip-flops provide additional control inputs called asynchronous set and reset.

These inputs can change the output without waiting for a clock edge.

Depending on the device:

- Asynchronous set forces Q to 1.
- Asynchronous reset forces Q to 0.

Their active polarity and simultaneous-input behaviour depend on the specific device.

They are commonly used to initialize digital systems into a known state.

## 14. Comparison of Latches and Flip-Flops

| Property | Latch | Flip-flop |
|---|---|---|
| Triggering | Level-sensitive | Usually edge-triggered |
| Control | Enable | Clock |
| Output behaviour | Can follow input while enabled | Changes at active clock edge |
| Typical use | Data holding and gating | Synchronous storage |
| Timing requirements | Depend on enable behaviour | Setup and hold around clock edge |

## 15. Worked Numerical Examples

### Example 1: D Flip-Flop State

**Given:**

A positive-edge-triggered D flip-flop has:

- Present output: \(Q=0\).
- Data input: \(D=1\).

A rising clock edge occurs.

Determine the next output.

**Formula:**

\[
Q_{next}=D
\]

**Solution:**

At the rising clock edge:

\[
Q_{next}=1
\]

**Final Answer:**

\[
\boxed{Q_{next}=1}
\]

### Example 2: JK Flip-Flop

**Given:**

- Present state: \(Q=1\).
- \(J=1\).
- \(K=1\).

Determine the next state.

**Formula:**

When:

\[
J=K=1
\]

the flip-flop toggles.

**Solution:**

The complement of the present state is:

\[
\overline Q=0
\]

Therefore:

\[
Q_{next}=0
\]

**Final Answer:**

\[
\boxed{Q_{next}=0}
\]

### Example 3: Clock Period

**Given:**

A digital system operates at:

\[
f=20\,MHz
\]

Calculate the clock period.

**Formula:**

\[
T=\frac{1}{f}
\]

**Solution:**

\[
T=\frac{1}{20\times10^6}
\]

\[
T=50\times10^{-9}\,s
\]

\[
T=50\,ns
\]

**Final Answer:**

\[
\boxed{T=50\,ns}
\]

## 16. Practical Applications

Sequential circuits are used in:

- Processor registers.
- Digital counters.
- Memory systems.
- Communication interfaces.
- Clock synchronization.
- Digital controllers.
- State machines.
- Embedded systems.

## 17. Common Examination Traps

1. Sequential circuits depend on present inputs and stored state.
2. Combinational circuits do not require memory.
3. An SR latch has set and reset inputs.
4. A NOR-based SR latch uses active-HIGH inputs.
5. A NAND-based SR latch commonly uses active-LOW inputs.
6. A D latch is level-sensitive.
7. An edge-triggered flip-flop responds to a clock transition.
8. A D flip-flop stores the data input at its active clock edge.
9. A JK flip-flop toggles when J and K are both 1.
10. A T flip-flop toggles when T is 1.
11. Setup time is measured before the active clock edge.
12. Hold time is measured after the active clock edge.
13. Metastability can occur when timing requirements are violated.
14. Asynchronous controls can act independently of the clock.
15. The clock period is the reciprocal of clock frequency.

## Quiz

1. Which flip-flop toggles its output when both J and K are HIGH?

- [ ] D flip-flop.
- [ ] SR latch.
- [x] JK flip-flop.
- [ ] Non-inverting buffer.

> When J and K are both 1, a JK flip-flop complements its previous output at the active clock edge.

2. What is the main difference between a latch and an edge-triggered flip-flop?

- [ ] A latch cannot store information.
- [x] A latch is level-sensitive, while an edge-triggered flip-flop responds to a clock edge.
- [ ] A flip-flop has no output.
- [ ] A latch always requires two clock inputs.

> A latch can respond throughout an active enable level, whereas an edge-triggered flip-flop changes state at a specified clock transition.

3. A flip-flop has a setup time of 5 ns and a hold time of 2 ns. What do these values represent?

- [ ] Output voltage limits.
- [ ] Maximum clock frequency and duty cycle.
- [x] Required data stability intervals before and after the active clock edge.
- [ ] The time required to power the circuit.

> Setup time specifies how long the data must be stable before the active edge. Hold time specifies how long it must remain stable afterward.
