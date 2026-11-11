---
title: Introduction to Programming Concepts
level: foundation
---

Programming is the process of writing instructions that tell a computer how to perform specific tasks. Programming languages provide structured ways to express algorithms and communicate operations to computer systems.

## 1. Meaning of Programming

Programming involves:

- Understanding a problem.
- Designing an algorithm.
- Writing source code.
- Translating or interpreting the code.
- Executing the program.
- Testing and debugging the result.

A program is a set of instructions written to perform a particular task.

## 2. Programming Languages

Programming languages allow humans to express computational instructions.

They can be broadly classified into three levels.

### Machine Language

Machine language consists of binary instructions directly understood by a processor.

Characteristics:

- Uses binary representations.
- Hardware-dependent.
- Difficult for humans to read and write.
- Does not require translation into another programming language before execution.

### Assembly Language

Assembly language uses symbolic instructions and names instead of writing every instruction directly in binary.

An assembler translates assembly language into machine code.

### High-Level Languages

High-level languages use syntax and structures that are more understandable to humans.

Examples:

- Python.
- C.
- C++.
- Java.
- JavaScript.

They generally require a compiler, interpreter or another execution system.

## 3. Compiler and Interpreter

### Compiler

A compiler translates source code into another representation, commonly machine code or intermediate code.

In many compiled workflows, translation occurs before the resulting program is executed.

### Interpreter

An interpreter executes a program through an execution environment that processes its instructions or intermediate representation.

The exact implementation differs between languages and platforms.

| Compiler | Interpreter |
|---|---|
| Commonly translates code before execution | Commonly processes code during execution |
| May generate a separate executable or intermediate representation | Often relies on an execution environment |
| Can support extensive optimisation | Can provide interactive execution |
| Example: C compilation workflow | Example: Traditional Python execution workflow |

Modern programming environments may combine compilation, interpretation and just-in-time compilation.

## 4. Basic Programming Elements

### Variables

A variable is a named storage location or reference used to hold information during program execution.

Example:

AGE = 20

### Constants

A constant represents a value that is intended not to change during a particular program execution or according to the language's constant rules.

Example:

PI = 3.14159

### Data Types

Data types define the kind of values that can be represented and the operations that can be performed on them.

Common types include:

- Integer.
- Floating-point number.
- Character.
- String.
- Boolean.

### Operators

Operators perform operations on values.

Examples:

- Arithmetic operators.
- Comparison operators.
- Logical operators.
- Assignment operators.

## 5. Programming Paradigms

A programming paradigm is a general approach to organising and writing programs.

### Procedural Programming

Organises programs around procedures or functions that perform defined tasks.

Examples include C and procedural programming in Python.

### Object-Oriented Programming

Organises programs around objects containing data and related behaviour.

Examples include Java, C++ and Python.

### Functional Programming

Emphasises functions, expressions and techniques that minimise changes to program state.

Examples include Haskell and functional programming features in Python and JavaScript.

## 6. Syntax and Semantics

**Syntax:** The rules governing how program instructions must be written.

**Semantics:** The meaning or behaviour of those instructions.

A program may contain valid syntax but still produce an incorrect result because its logic is wrong.

## 7. Errors in Programming

### Syntax Errors

Occur when code violates the language's grammatical rules.

### Runtime Errors

Occur during program execution.

Examples include division by zero and attempts to access unavailable resources.

### Logical Errors

Occur when a program executes but produces an incorrect result.

Example:

A program calculates the area of a rectangle using:

AREA = LENGTH + WIDTH

The correct operation is multiplication.

## 8. Debugging and Testing

Debugging is the process of identifying, analysing and correcting errors in a program.

Testing checks whether software behaves as expected.

Common testing approaches include:

- Unit testing.
- Integration testing.
- System testing.
- Acceptance testing.

## Common Exam Traps

- Machine language consists of binary instructions.
- An assembler translates assembly language.
- A compiler translates source code into another representation.
- An interpreter executes code through an execution environment.
- Syntax errors differ from logical errors.
- A program can execute successfully and still produce incorrect output.
- A variable is not necessarily a constant.
- Programming paradigms describe approaches to organising programs.

## Quiz

1. Which language uses binary instructions directly understood by a processor?

- [ ] Python.
- [ ] Java.
- [x] Machine language.
- [ ] SQL.

> Machine language represents processor instructions in binary form.

2. What is the main purpose of an assembler?

- [ ] Convert Python programs into Java.
- [x] Translate assembly language into machine code.
- [ ] Manage computer memory.
- [ ] Design graphical user interfaces.

> An assembler converts symbolic assembly instructions into machine instructions.

3. A program executes without errors but calculates an incorrect result. What type of error is most likely responsible?

- [ ] Syntax error.
- [ ] Hardware error.
- [x] Logical error.
- [ ] Network error.

> A logical error occurs when the program's instructions execute but do not produce the intended result.