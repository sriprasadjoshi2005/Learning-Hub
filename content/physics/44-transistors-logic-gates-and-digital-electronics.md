---
title: Transistors, Logic Gates and Digital Electronics
level: advanced
---

Transistors are fundamental components of modern electronic systems. They are used to amplify signals, switch electrical currents and form the building blocks of processors, memory devices and digital circuits.

Digital electronics uses discrete signal levels to represent and process information. Most modern digital systems use binary logic based on 0 and 1.

## 1. Introduction to Transistors

A transistor is a semiconductor device used primarily for amplification and electronic switching.

Two major transistor families are:

- Bipolar junction transistors (BJTs).
- Field-effect transistors (FETs).

A transistor can control a relatively large current using a smaller controlling signal.

## 2. Bipolar Junction Transistor

A BJT consists of three semiconductor regions.

Its terminals are:
- Emitter.
- Base.
- Collector.

There are two main types:

**NPN transistor:**

A p-type base is placed between two n-type regions.

**PNP transistor:**

An n-type base is placed between two p-type regions.

The emitter is heavily doped, the base is very thin and lightly doped, and the collector is designed to collect carriers and dissipate heat.

## 3. Transistor Currents

For a transistor operating in its usual active configuration:

\[
I_E=I_C+I_B
\]

Where:
- IE = emitter current.
- IC = collector current.
- IB = base current.

The common-base current gain is:

\[
\alpha=\frac{I_C}{I_E}
\]

The common-emitter current gain is:

\[
\beta=\frac{I_C}{I_B}
\]

For an idealised transistor in active operation:

\[
\beta=\frac{\alpha}{1-\alpha}
\]

These gains are related, but their numerical values are not identical.

## 4. Transistor Operating Regions

A BJT commonly operates in three important regions.

**Cut-off region:**

- The transistor is effectively switched off.
- Collector current is very small.

**Active region:**

- The base-emitter junction is forward biased.
- The collector-base junction is reverse biased.
- The transistor can amplify signals.

**Saturation region:**

- Both junctions are forward biased.
- The transistor is strongly switched on.
- Collector current is limited by the external circuit.

Switching circuits mainly use cut-off and saturation.

Amplifier circuits generally use the active region.

## 5. Transistor as a Switch

A transistor can operate as an electronic switch.

When the input signal is sufficiently low, the transistor enters cut-off.

When the input drives it into saturation, current flows through the load.

Applications include:
- LED control.
- Motor switching.
- Digital circuits.
- Relay drivers.
- Microcontroller outputs.

A suitable resistor or driver circuit is often needed to limit base current.

## 6. Transistor as an Amplifier

In the active region, a small change in base current can produce a larger change in collector current.

\[
\Delta I_C=\beta\Delta I_B
\]

For example, if:

\[
\beta=100
\]

and:

\[
\Delta I_B=20\ \mu A
\]

Then:

\[
\Delta I_C=100(20\ \mu A)
\]

\[
\boxed{\Delta I_C=2\text{ mA}}
\]

This illustrates current amplification.

The energy delivered to the amplified output comes from the transistor's external power supply, not from the input signal alone.

## 7. Field-Effect Transistors

A field-effect transistor controls current using an electric field.

Its three commonly used terminals are:
- Gate.
- Source.
- Drain.

The MOSFET is particularly important in modern integrated circuits.

A MOSFET may operate in:
- Cut-off.
- Linear or triode region.
- Saturation region.

The exact operating conditions depend on whether it is an enhancement-mode or depletion-mode device and whether it is n-channel or p-channel.

MOSFETs are widely used because they can provide high input resistance and efficient switching.

## 8. Integrated Circuits

An integrated circuit (IC) combines many electronic components on a single semiconductor chip.

It may contain:
- Transistors.
- Diodes.
- Resistors.
- Capacitors.
- Interconnections.

Examples include:
- Microprocessors.
- Memory chips.
- Operational amplifiers.
- Digital controllers.
- Communication chips.

Integrated circuits allow complex electronic systems to be made compact, fast and relatively inexpensive.

## 9. Introduction to Digital Electronics

Digital electronics represents information using discrete states.

Binary logic uses two symbols:

\[
0\quad\text{and}\quad1
\]

These states may correspond to different voltage ranges in a digital circuit.

The voltage representing logical 0 or 1 depends on the logic family and circuit design.

## 10. Basic Logic Gates

A logic gate performs a Boolean operation on one or more binary inputs.

### AND Gate

The output is 1 only when every input is 1.

\[
Y=A\cdot B
\]

### OR Gate

The output is 1 when at least one input is 1.

\[
Y=A+B
\]

### NOT Gate

The output is the complement of the input.

\[
Y=\overline{A}
\]

## 11. Universal Logic Gates

NAND and NOR gates are called universal gates because any Boolean function can be implemented using only NAND gates or only NOR gates.

**NAND:**

\[
Y=\overline{A\cdot B}
\]

**NOR:**

\[
Y=\overline{A+B}
\]

Universal gates are important for digital circuit design.

## 12. XOR and XNOR Gates

**Exclusive OR (XOR):**

Produces 1 when the two inputs are different.

\[
Y=A\oplus B
\]

**Exclusive NOR (XNOR):**

Produces 1 when the two inputs are equal.

\[
Y=\overline{A\oplus B}
\]

These gates are frequently used in arithmetic and comparison circuits.

## 13. Truth Tables

Truth tables describe the output of a logic gate for every possible input combination.

For two-input gates:

| A | B | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

## 14. Boolean Algebra

Boolean algebra is the mathematical system used to simplify logical expressions.

Important identities include:

\[
A+0=A
\]

\[
A\cdot1=A
\]

\[
A+1=1
\]

\[
A\cdot0=0
\]

\[
A+\overline A=1
\]

\[
A\cdot\overline A=0
\]

## 15. De Morgan's Theorems

De Morgan's theorems are fundamental rules for transforming Boolean expressions.

First theorem:

\[
\overline{A\cdot B}=\overline A+\overline B
\]

Second theorem:

\[
\overline{A+B}=\overline A\cdot\overline B
\]

These identities are useful when converting circuits between NAND and NOR implementations.

## 16. Combinational Logic Circuits

A combinational circuit has outputs determined only by its current inputs.

Examples include:
- Adders.
- Subtractors.
- Multiplexers.
- Demultiplexers.
- Encoders.
- Decoders.

### Half Adder

A half adder adds two binary digits.

Inputs: A and B.

Sum:

\[
S=A\oplus B
\]

Carry:

\[
C=A\cdot B
\]

### Full Adder

A full adder adds three binary inputs: A, B and carry-in.

Sum:

\[
S=A\oplus B\oplus C_{\mathrm{in}}
\]

Carry-out:

\[
C_{\mathrm{out}}=AB+AC_{\mathrm{in}}+BC_{\mathrm{in}}
\]

## 17. Sequential Logic Circuits

A sequential circuit depends on both current inputs and stored previous states.

It contains memory elements.

Examples include:
- Flip-flops.
- Registers.
- Counters.
- Memory circuits.

A clock signal commonly coordinates state changes in synchronous sequential circuits.

## 18. Flip-Flops

A flip-flop is a bistable digital circuit capable of storing one bit.

Important types include:
- SR flip-flop.
- JK flip-flop.
- D flip-flop.
- T flip-flop.

A D flip-flop transfers its D input to its output at the active clock edge.

It is widely used in registers and memory structures.

## 19. Worked Numerical Example

A common-emitter transistor has a current gain:

\[
\beta=120
\]

If the base current is:

\[
I_B=25\ \mu A
\]

Calculate the collector current, assuming active-region operation.

\[
I_C=\beta I_B
\]

\[
I_C=120(25\ \mu A)
\]

\[
\boxed{I_C=3\text{ mA}}
\]

The emitter current is:

\[
I_E=I_C+I_B
\]

\[
I_E=3.025\text{ mA}
\]

## Common Exam Traps

- A BJT has emitter, base and collector terminals.
- A MOSFET is a field-effect transistor.
- The base current is generally much smaller than collector current in a common-emitter BJT.
- A transistor amplifier operates in the active region.
- A transistor switch commonly operates in cut-off and saturation.
- NAND and NOR are universal gates.
- XOR gives 1 when inputs differ.
- A combinational circuit does not require stored previous states.
- Sequential circuits contain memory elements.

## Quiz

1. In a BJT, the relationship between emitter, collector and base currents is:

- [ ] IE = IC - IB
- [x] IE = IC + IB
- [ ] IB = IE + IC
- [ ] IC = IE + IB

> The emitter current divides into collector current and base current. Therefore, IE = IC + IB.

2. Which of the following is a universal logic gate?

- [ ] AND only
- [ ] XOR only
- [x] NAND
- [ ] NOT only

> NAND gates can be combined to construct NOT, AND, OR and more complex Boolean functions.

3. A circuit whose output depends on stored previous states as well as current inputs is:

- [ ] Purely combinational
- [ ] A simple resistor network
- [x] Sequential logic
- [ ] A passive filter only

> Sequential circuits contain memory elements, so their outputs can depend on the history of the input signals.