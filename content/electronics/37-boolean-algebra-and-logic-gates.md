---
title: Boolean Algebra and Logic Gates
level: foundation
---

# Boolean Algebra and Logic Gates

Digital electronic circuits operate using discrete logical states, commonly represented as binary 0 and binary 1.

Boolean algebra provides the mathematical rules used to describe and simplify these digital circuits.

Logic gates are the physical electronic circuits that perform Boolean operations.

They form the foundation of processors, memory devices, control systems, calculators, communication equipment, and other digital systems.

This lesson introduces Boolean variables, fundamental logic operations, logic-gate symbols, truth tables, Boolean laws, De Morgan's theorems, and circuit simplification.

## 1. Introduction to Boolean Algebra

Boolean algebra is a mathematical system in which variables have only two possible values:

\[
0\quad\text{or}\quad1
\]

These values commonly represent:

- Logic 0: LOW or FALSE.
- Logic 1: HIGH or TRUE.

In physical electronic circuits, these logical states are represented by voltage ranges.

The exact voltage levels depend on the logic family and supply voltage.

Boolean algebra is used to describe and simplify digital circuits.

## 2. Boolean Variables and Operations

A Boolean variable can take only one of two values.

For example:

\[
A\in\{0,1\}
\]

The basic Boolean operations are:

1. AND.
2. OR.
3. NOT.

Other gates can be constructed using combinations of these operations.

## 3. AND Operation

The AND operation produces an output of 1 only when every input is 1.

Boolean expression:

\[
\boxed{Y=A\cdot B}
\]

It may also be written as:

\[
Y=AB
\]

### Truth Table

| A | B | Y = A AND B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

For multiple inputs, the output is 1 only when all inputs are 1.

## 4. OR Operation

The OR operation produces an output of 1 when at least one input is 1.

Boolean expression:

\[
\boxed{Y=A+B}
\]

### Truth Table

| A | B | Y = A OR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

For multiple inputs, the output is 1 when one or more inputs are 1.

## 5. NOT Operation

The NOT operation produces the opposite of its input.

It is also called inversion or complementation.

Boolean expression:

\[
\boxed{Y=\overline{A}}
\]

### Truth Table

| A | Y = NOT A |
|---|---|
| 0 | 1 |
| 1 | 0 |

A NOT gate has one input and one output.

## 6. NAND Gate

A NAND gate is an AND gate followed by a NOT operation.

Boolean expression:

\[
\boxed{Y=\overline{AB}}
\]

### Truth Table

| A | B | Y = NAND |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The output is LOW only when all inputs are HIGH.

NAND is called a universal gate because any Boolean function can be implemented using only NAND gates.

## 7. NOR Gate

A NOR gate is an OR gate followed by a NOT operation.

Boolean expression:

\[
\boxed{Y=\overline{A+B}}
\]

### Truth Table

| A | B | Y = NOR |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

The output is HIGH only when every input is LOW.

NOR is also a universal gate.

## 8. XOR Gate

XOR means exclusive OR.

It produces an output of 1 when the inputs are different.

Boolean expression:

\[
\boxed{Y=A\oplus B}
\]

An equivalent Boolean expression is:

\[
Y=\overline{A}B+A\overline{B}
\]

### Truth Table

| A | B | Y = XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR is important in adders, parity circuits, and error-detection systems.

## 9. XNOR Gate

XNOR is the complement of XOR.

It produces an output of 1 when the inputs are equal.

Boolean expression:

\[
\boxed{Y=\overline{A\oplus B}}
\]

### Truth Table

| A | B | Y = XNOR |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

XNOR is useful in equality comparison circuits.

## 10. Summary of Logic Gates

| Gate | Boolean expression | Output condition for 1 |
|---|---|---|
| AND | \(AB\) | All inputs are 1 |
| OR | \(A+B\) | At least one input is 1 |
| NOT | \(\overline A\) | Input is 0 |
| NAND | \(\overline{AB}\) | At least one input is 0 |
| NOR | \(\overline{A+B}\) | All inputs are 0 |
| XOR | \(A\oplus B\) | Inputs are different |
| XNOR | \(\overline{A\oplus B}\) | Inputs are equal |

## 11. Fundamental Boolean Laws

Boolean algebra contains laws that simplify logical expressions.

### 11.1 Identity Laws

\[
A+0=A
\]

\[
A\cdot1=A
\]

### 11.2 Null Laws

\[
A+1=1
\]

\[
A\cdot0=0
\]

### 11.3 Idempotent Laws

\[
A+A=A
\]

\[
A\cdot A=A
\]

### 11.4 Complement Laws

\[
A+\overline A=1
\]

\[
A\cdot\overline A=0
\]

### 11.5 Involution Law

\[
\overline{\overline A}=A
\]

Taking the complement twice restores the original variable.

### 11.6 Commutative Laws

\[
A+B=B+A
\]

\[
AB=BA
\]

### 11.7 Associative Laws

\[
(A+B)+C=A+(B+C)
\]

\[
(AB)C=A(BC)
\]

### 11.8 Distributive Laws

\[
A(B+C)=AB+AC
\]

\[
A+BC=(A+B)(A+C)
\]

These laws are used to rearrange and simplify Boolean expressions.

## 12. Absorption Laws

Absorption laws eliminate redundant terms.

\[
\boxed{A+AB=A}
\]

Proof:

\[
A+AB=A(1+B)
\]

Since:

\[
1+B=1
\]

Therefore:

\[
A+AB=A
\]

Another absorption law is:

\[
\boxed{A(A+B)=A}
\]

These identities are especially useful in circuit simplification.

## 13. De Morgan's Theorems

De Morgan's theorems describe how complements interact with AND and OR operations.

### 13.1 First Theorem

The complement of an AND expression is equal to the OR of the individual complements.

\[
\boxed{\overline{AB}=\overline A+\overline B}
\]

### 13.2 Second Theorem

The complement of an OR expression is equal to the AND of the individual complements.

\[
\boxed{\overline{A+B}=\overline A\cdot\overline B}
\]

### 13.3 Importance

De Morgan's theorems are used to:

- Simplify Boolean expressions.
- Convert AND operations into NAND structures.
- Convert OR operations into NOR structures.
- Design circuits using universal gates.

## 14. Universal Gates

A universal gate can be used by itself to construct any Boolean function.

NAND and NOR are universal gates.

### 14.1 Implementing NOT Using NAND

Connect both NAND inputs to the same variable:

\[
Y=\overline{AA}
\]

Since:

\[
AA=A
\]

Therefore:

\[
Y=\overline A
\]

### 14.2 Implementing AND Using NAND

First produce:

\[
X=\overline{AB}
\]

Then invert the result using another NAND gate:

\[
Y=\overline{XX}
\]

Therefore:

\[
Y=AB
\]

### 14.3 Implementing OR Using NAND

Using De Morgan's theorem:

\[
A+B=\overline{\overline A\cdot\overline B}
\]

The two inputs can first be inverted using NAND gates, and a third NAND gate combines them.

This demonstrates how a complete logic system can be built from NAND gates alone.

## 15. Boolean Expression Simplification

Boolean expressions can often be reduced to fewer terms and gates.

### Example

Simplify:

\[
Y=AB+A\overline B
\]

Factor out \(A\):

\[
Y=A(B+\overline B)
\]

Using the complement law:

\[
B+\overline B=1
\]

Therefore:

\[
Y=A(1)
\]

\[
\boxed{Y=A}
\]

The original circuit can be replaced by a direct connection from input \(A\) to the output.

## 16. Worked Numerical Examples

### Example 1: Evaluate a Boolean Expression

**Given:**

\[
Y=A\overline B+BC
\]

For:

\[
A=1,\quad B=0,\quad C=1
\]

Calculate \(Y\).

**Solution:**

First:

\[
\overline B=1
\]

Then:

\[
A\overline B=(1)(1)=1
\]

And:

\[
BC=(0)(1)=0
\]

Therefore:

\[
Y=1+0
\]

\[
\boxed{Y=1}
\]

### Example 2: Simplify a Boolean Expression

**Given:**

\[
Y=A+AB+\overline A B
\]

Simplify the expression.

**Solution:**

Using absorption:

\[
A+AB=A
\]

Therefore:

\[
Y=A+\overline A B
\]

Using the distributive identity:

\[
A+\overline A B=(A+\overline A)(A+B)
\]

Since:

\[
A+\overline A=1
\]

Then:

\[
Y=1(A+B)
\]

\[
\boxed{Y=A+B}
\]

### Example 3: Determine an XOR Output

**Given:**

\[
Y=A\oplus B
\]

For:

\[
A=1,\quad B=0
\]

**Solution:**

XOR produces 1 when inputs are different.

Since:

\[
1\neq0
\]

**Final Answer:**

\[
\boxed{Y=1}
\]

## 17. Applications of Logic Gates

Logic gates are used in:

- Arithmetic circuits.
- Digital controllers.
- Microprocessors.
- Memory circuits.
- Data comparison.
- Error detection.
- Digital communication.
- Automatic control systems.

They are the basic building blocks from which more complex digital systems are constructed.

## 18. Common Examination Traps

1. Boolean variables have only two possible values.
2. AND produces 1 only when all inputs are 1.
3. OR produces 1 when at least one input is 1.
4. NOT reverses the input.
5. NAND is the complement of AND.
6. NOR is the complement of OR.
7. XOR produces 1 for different input values.
8. XNOR produces 1 for equal input values.
9. NAND and NOR are universal gates.
10. \(A+AB=A\) is an absorption identity.
11. \(A+\overline A=1\).
12. \(A\overline A=0\).
13. De Morgan's theorems interchange AND and OR when taking complements.
14. Boolean addition does not mean ordinary arithmetic addition.
15. Boolean multiplication does not mean ordinary arithmetic multiplication.

## Quiz

1. What is the output of an XOR gate when both inputs are 1?

- [ ] 1.
- [x] 0.
- [ ] 2.
- [ ] Undefined.

> XOR produces 1 only when its inputs are different. Since both inputs are 1, they are equal, so the output is 0.

2. Which of the following is a universal logic gate?

- [ ] AND only.
- [ ] OR only.
- [x] NAND.
- [ ] XOR only.

> NAND is a universal gate because NOT, AND, OR, and any other Boolean function can be constructed using NAND gates alone. NOR is also universal.

3. Which expression is equivalent to \(\overline{A+B}\)?

- [ ] \(\overline A+\overline B\).
- [x] \(\overline A\cdot\overline B\).
- [ ] \(AB\).
- [ ] \(A+B\).

> De Morgan's second theorem states that the complement of an OR operation equals the AND of the individual complements.
