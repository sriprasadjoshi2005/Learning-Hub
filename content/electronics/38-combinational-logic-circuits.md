---
title: Combinational Logic Circuits
level: intermediate
---

# Combinational Logic Circuits

Combinational logic circuits are digital circuits whose outputs depend only on their present input values.

They do not store previous input information.

These circuits are constructed using logic gates and are essential in arithmetic processing, data selection, code conversion, comparison, and digital control.

Important combinational circuits include:

- Half adders.
- Full adders.
- Half subtractors.
- Full subtractors.
- Multiplexers.
- Demultiplexers.
- Encoders.
- Decoders.
- Magnitude comparators.

## 1. Introduction to Combinational Logic

A combinational circuit consists of logic gates connected to produce one or more outputs.

Its behaviour is described by Boolean expressions or a truth table.

For a combinational circuit:

\[
Y=f(A,B,C,\ldots)
\]

The output depends on the current inputs.

There is no internal memory of earlier input states.

Examples include:

- Arithmetic circuits.
- Code converters.
- Multiplexers.
- Decoders.
- Digital comparators.

## 2. Half Adder

A half adder is a combinational circuit that adds two single-bit binary numbers.

It has:

- Two inputs: \(A\) and \(B\).
- Two outputs: Sum \(S\) and Carry \(C\).

### 2.1 Truth Table

| A | B | Sum | Carry |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

### 2.2 Boolean Expressions

The sum output is:

\[
\boxed{S=A\oplus B}
\]

The carry output is:

\[
\boxed{C=AB}
\]

A half adder can therefore be constructed using:

- One XOR gate.
- One AND gate.

### 2.3 Limitation

A half adder cannot accept a carry input from a previous stage.

This makes it insufficient by itself for general multibit addition.

## 3. Full Adder

A full adder adds three binary inputs:

- \(A\).
- \(B\).
- Carry input \(C_{in}\).

It produces:

- Sum \(S\).
- Carry output \(C_{out}\).

### 3.1 Truth Table

| A | B | \(C_{in}\) | S | \(C_{out}\) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

### 3.2 Sum Expression

\[
\boxed{S=A\oplus B\oplus C_{in}}
\]

### 3.3 Carry Expression

\[
\boxed{
C_{out}=AB+AC_{in}+BC_{in}
}
\]

An alternative expression is:

\[
C_{out}=AB+C_{in}(A\oplus B)
\]

### 3.4 Construction Using Two Half Adders

A full adder can be constructed using:

1. First half adder to add \(A\) and \(B\).
2. Second half adder to add the first sum and \(C_{in}\).
3. OR gate to combine the two carry outputs.

## 4. Binary Addition Using Full Adders

Multiple full adders can be connected in sequence.

The carry output of one stage becomes the carry input of the next stage.

This arrangement is called a ripple-carry adder.

For an \(n\)-bit addition, an \(n\)-stage ripple-carry adder can be used.

Its main disadvantage is propagation delay because the carry must travel through successive stages.

## 5. Half Subtractor

A half subtractor subtracts one binary bit from another.

It has:

- Minuend \(A\).
- Subtrahend \(B\).
- Difference \(D\).
- Borrow output \(B_{out}\).

### 5.1 Truth Table

| A | B | Difference | Borrow |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

### 5.2 Boolean Expressions

Difference:

\[
\boxed{D=A\oplus B}
\]

Borrow:

\[
\boxed{B_{out}=\overline A B}
\]

A half subtractor can be constructed using XOR, NOT, and AND gates.

## 6. Full Subtractor

A full subtractor subtracts two bits while considering an incoming borrow.

Inputs:

- Minuend \(A\).
- Subtrahend \(B\).
- Borrow input \(B_{in}\).

Outputs:

- Difference \(D\).
- Borrow output \(B_{out}\).

### 6.1 Difference Expression

\[
\boxed{D=A\oplus B\oplus B_{in}}
\]

### 6.2 Borrow Expression

\[
\boxed{
B_{out}=\overline A B+\overline A B_{in}+BB_{in}
}
\]

The full subtractor can be constructed using two half subtractors and an OR gate.

## 7. Multiplexers

A multiplexer, commonly called a MUX, selects one of several input signals and transfers the selected signal to a single output.

It is a data-selection circuit.

### 7.1 2-to-1 Multiplexer

A 2-to-1 multiplexer has:

- Two data inputs: \(I_0\) and \(I_1\).
- One select input: \(S\).
- One output: \(Y\).

Truth table:

| S | Y |
|---|---|
| 0 | \(I_0\) |
| 1 | \(I_1\) |

Boolean expression:

\[
\boxed{Y=\overline S I_0+SI_1}
\]

### 7.2 4-to-1 Multiplexer

A 4-to-1 multiplexer has:

- Four data inputs.
- Two select inputs.
- One output.

The number of select lines required for \(2^n\) inputs is:

\[
\boxed{n=\log_2 N}
\]

Where \(N\) is the number of data inputs.

For four inputs:

\[
n=\log_2 4=2
\]

### 7.3 Applications

- Data routing.
- Communication systems.
- Processor datapaths.
- Input selection.
- Implementing Boolean functions.

## 8. Demultiplexers

A demultiplexer, or DEMUX, performs the opposite function of a multiplexer.

It accepts one data input and routes it to one of several outputs.

For a 1-to-4 demultiplexer:

- One data input.
- Two select inputs.
- Four outputs.

The select inputs determine which output receives the input data.

### 8.1 Applications

- Data distribution.
- Communication systems.
- Memory selection.
- Digital control.

## 9. Encoders

An encoder converts one active input among several inputs into a coded binary output.

For example, a simple 4-to-2 encoder has four input lines and two output lines.

If only one input is active at a time:

| Active input | Binary output |
|---|---|
| \(D_0\) | 00 |
| \(D_1\) | 01 |
| \(D_2\) | 10 |
| \(D_3\) | 11 |

A basic encoder requires a valid single active input.

If multiple inputs may be active simultaneously, a priority encoder is used to select the highest-priority input.

## 10. Decoders

A decoder converts a binary input code into a corresponding active output line.

For a 2-to-4 decoder, there are:

- Two binary input lines.
- Four output lines.

### 10.1 Truth Table

| A | B | \(Y_0\) | \(Y_1\) | \(Y_2\) | \(Y_3\) |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

This is an active-HIGH decoder.

### 10.2 Applications

- Memory address decoding.
- Display systems.
- Instruction decoding.
- Digital selection circuits.

## 11. Magnitude Comparator

A magnitude comparator compares two binary numbers and determines their relationship.

For two numbers \(A\) and \(B\), it may produce three outputs:

- \(A>B\).
- \(A=B\).
- \(A<B\).

For a one-bit comparator:

\[
A>B=A\overline B
\]

\[
A<B=\overline A B
\]

\[
A=B=\overline{A\oplus B}
\]

These outputs are mutually exclusive for a valid comparison.

## 12. Combinational Circuit Design Procedure

A systematic design process is:

1. Identify the required inputs and outputs.
2. Define the circuit's behaviour.
3. Construct the truth table.
4. Derive Boolean expressions.
5. Simplify the expressions.
6. Select suitable logic gates.
7. Draw the logic circuit.
8. Verify all input combinations.

This process is used in practical digital circuit design.

## 13. Worked Numerical Examples

### Example 1: Full Adder

**Given:**

\[
A=1,\quad B=1,\quad C_{in}=1
\]

Calculate sum and carry output.

**Formula:**

\[
S=A\oplus B\oplus C_{in}
\]

\[
C_{out}=AB+AC_{in}+BC_{in}
\]

**Solution:**

Sum:

\[
S=1\oplus1\oplus1
\]

\[
S=0\oplus1=1
\]

Carry:

\[
C_{out}=(1)(1)+(1)(1)+(1)(1)
\]

\[
C_{out}=1+1+1=1
\]

In Boolean algebra, OR of any number of 1 values is 1.

**Final Answer:**

\[
\boxed{S=1,\quad C_{out}=1}
\]

### Example 2: Multiplexer Output

**Given:**

A 4-to-1 multiplexer has:

\[
I_0=0,\quad I_1=1,\quad I_2=1,\quad I_3=0
\]

Select inputs:

\[
S_1=1,\quad S_0=0
\]

Determine the output.

**Solution:**

The select combination 10 selects input \(I_2\).

Therefore:

\[
Y=I_2
\]

\[
\boxed{Y=1}
\]

### Example 3: Number of Select Lines

**Given:**

A multiplexer has 16 data inputs.

Calculate the number of select lines.

**Formula:**

\[
n=\log_2N
\]

**Solution:**

\[
n=\log_2 16
\]

\[
n=4
\]

**Final Answer:**

\[
\boxed{4\text{ select lines}}
\]

## 14. Practical Applications

Combinational circuits are used in:

- Arithmetic logic units.
- Processor datapaths.
- Memory address decoding.
- Data communication.
- Digital measurement systems.
- Display controllers.
- Code conversion.
- Digital control equipment.

## 15. Common Examination Traps

1. Combinational outputs depend only on present inputs.
2. A half adder has no carry input.
3. A full adder has a carry input.
4. XOR produces the sum bit in half and full adders.
5. AND produces the half-adder carry.
6. A half subtractor has no borrow input.
7. A full subtractor includes a borrow input.
8. A multiplexer selects one of several inputs.
9. A demultiplexer distributes one input to a selected output.
10. An encoder converts active input information into a binary code.
11. A decoder converts a binary code into an active output.
12. A 4-to-1 multiplexer requires two select lines.
13. A 16-to-1 multiplexer requires four select lines.
14. A basic encoder assumes only one active input unless priority behaviour is specified.
15. A magnitude comparator determines whether one binary number is greater than, equal to, or less than another.

## 16. Quiz

### Question 1

What is the main difference between a half adder and a full adder?

- [ ] A half adder has two outputs, while a full adder has one.
- [x] A full adder accepts a carry input, while a half adder does not.
- [ ] A full adder cannot produce a carry output.
- [ ] A half adder performs subtraction.

> **Explanation:** A full adder adds three input bits, including a carry from a previous stage. A half adder adds only two input bits.

### Question 2

How many select lines are required for a 16-to-1 multiplexer?

- [ ] 2.
- [ ] 3.
- [x] 4.
- [ ] 16.

> **Explanation:** The number of select lines is \(\log_2N\). For 16 inputs, \(\log_2 16=4\).

### Question 3

Which circuit converts a binary input code into one of several active output lines?

- [ ] Encoder.
- [ ] Multiplexer.
- [x] Decoder.
- [ ] Full subtractor.

> **Explanation:** A decoder accepts a binary code and activates the corresponding output line. It is commonly used in memory selection and address decoding.