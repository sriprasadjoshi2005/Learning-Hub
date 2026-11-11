---
title: Algorithms, Flowcharts and Pseudocode
level: foundation
---

Algorithms, flowcharts and pseudocode are fundamental tools for designing and communicating computational solutions. They help programmers understand the logic of a problem before implementing it in a programming language.

## 1. Meaning of an Algorithm

An algorithm is a finite sequence of well-defined instructions designed to solve a problem or perform a task.

Example: Algorithm to calculate the sum of two numbers.

1. Start.
2. Read A and B.
3. Calculate SUM = A + B.
4. Display SUM.
5. Stop.

## 2. Characteristics of a Good Algorithm

A well-designed algorithm should have:

**Input:** Accepts zero or more inputs.

**Output:** Produces at least one result.

**Definiteness:** Each instruction must be clear and unambiguous.

**Finiteness:** Must terminate after a finite number of steps.

**Effectiveness:** Each instruction must be sufficiently basic and executable.

**Correctness:** Must produce the expected result for valid inputs.

## 3. Types of Algorithmic Control Structures

### Sequence

Instructions execute one after another in a defined order.

Example:

1. Read length.
2. Read width.
3. Calculate area.
4. Display area.

### Selection

A condition determines which instruction or branch executes.

Examples:

- IF.
- IF-ELSE.
- Nested IF.

### Iteration

A set of instructions is repeated.

Examples:

- FOR loop.
- WHILE loop.
- REPEAT-UNTIL loop.

## 4. Flowcharts

A flowchart is a graphical representation of an algorithm using standard symbols.

Important symbols:

| Symbol | Meaning |
|---|---|
| Oval | Start or End |
| Rectangle | Processing operation |
| Parallelogram | Input or Output |
| Diamond | Decision |
| Arrow | Direction of control flow |
| Circle | Connector |

Flowcharts help visualise the sequence of operations and decisions.

## 5. Pseudocode

Pseudocode is an informal, language-independent way of describing an algorithm using structured statements.

It resembles programming code but does not follow the strict syntax of a specific language.

Example:

BEGIN

    INPUT A
    INPUT B

    SUM = A + B

    OUTPUT SUM

END

## 6. Algorithm and Flowchart Comparison

| Algorithm | Flowchart |
|---|---|
| Written sequence of instructions | Graphical representation |
| Uses structured language | Uses standard symbols |
| Easy to write and modify | Helps visualise program logic |
| Suitable for describing detailed steps | Useful for understanding control flow |

## 7. Example: Checking Whether a Number Is Even or Odd

Pseudocode:

BEGIN

    INPUT N

    IF N MOD 2 = 0 THEN
        OUTPUT "Even"
    ELSE
        OUTPUT "Odd"
    END IF

END

The MOD operation calculates the remainder after division.

A number is even when its remainder after division by 2 is zero.

## 8. Example: Calculating a Factorial

The factorial of a positive integer N is the product of all positive integers from 1 to N.

For example:

5! = 5 x 4 x 3 x 2 x 1 = 120

Pseudocode:

BEGIN

    INPUT N
    FACTORIAL = 1

    FOR I = 1 TO N
        FACTORIAL = FACTORIAL x I
    END FOR

    OUTPUT FACTORIAL

END

For this algorithm, N must be a non-negative integer. The factorial of zero is 1.

## 9. Algorithm Testing

An algorithm should be tested using different types of inputs.

- Normal cases: Typical valid inputs.
- Boundary cases: Inputs at the limits of the accepted range.
- Invalid cases: Inputs outside the permitted range.
- Special cases: Values such as zero, negative numbers or repeated values where relevant.

## Common Exam Traps

- An algorithm must terminate after a finite number of steps.
- A diamond represents a decision in a standard flowchart.
- A rectangle represents processing.
- A parallelogram represents input or output.
- Pseudocode is not a specific programming language.
- Sequence, selection and iteration are fundamental control structures.
- Factorial of zero is 1.

## Quiz

1. Which property requires an algorithm to terminate after a finite number of steps?

- [ ] Definiteness.
- [ ] Effectiveness.
- [x] Finiteness.
- [ ] Portability.

> Finiteness ensures that an algorithm eventually terminates rather than continuing indefinitely.

2. Which flowchart symbol represents a decision?

- [ ] Rectangle.
- [ ] Oval.
- [ ] Parallelogram.
- [x] Diamond.

> The diamond represents a decision point, commonly involving a condition with alternative branches.

3. What is the value of 4 factorial?

- [ ] 12.
- [ ] 16.
- [x] 24.
- [ ] 32.

> 4! = 4 x 3 x 2 x 1 = 24.