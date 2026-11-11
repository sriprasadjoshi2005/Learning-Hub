---
title: Computer Architecture and the CPU
level: foundation
---

Computer architecture describes the organisation and operation of a computer system. It explains how the processor, memory, storage and input/output components work together to execute instructions.

## 1. Basic Organisation of a Computer

A computer system generally contains:

1. Input Unit.
2. Central Processing Unit.
3. Memory Unit.
4. Output Unit.
5. Secondary Storage.

The CPU is responsible for executing program instructions and coordinating many processing operations.

## 2. Central Processing Unit

The Central Processing Unit (CPU) is commonly described as the brain of a computer.

Its major components include:

**Arithmetic Logic Unit (ALU):**
- Performs arithmetic operations.
- Performs logical comparisons.
- Executes operations such as addition, subtraction, AND and OR.

**Control Unit (CU):**
- Directs instruction execution.
- Coordinates operations between computer components.
- Generates control signals.

**Registers:**
- Small, extremely fast storage locations inside the processor.
- Temporarily hold instructions, addresses and data.

## 3. Important CPU Registers

| Register | Function |
|---|---|
| Program Counter (PC) | Holds the address of the next instruction |
| Instruction Register (IR) | Holds the current instruction |
| Memory Address Register (MAR) | Holds a memory address |
| Memory Data Register (MDR) | Holds data being transferred to or from memory |
| Accumulator | Holds intermediate arithmetic or logical results |

Register names and arrangements vary between processor architectures.

## 4. Instruction Cycle

The CPU executes instructions through a repeated process commonly described as the instruction cycle.

### Fetch

The processor retrieves an instruction from memory.

### Decode

The control unit interprets the instruction and determines the required operation.

### Execute

The processor performs the specified operation.

### Store

The result may be written to a register or memory.

This is commonly called the fetch-decode-execute cycle.

## 5. Von Neumann Architecture

The Von Neumann architecture is based on the stored-program concept.

Its main characteristics include:

- Instructions and data share the same memory.
- The CPU fetches instructions from memory.
- Instructions are generally executed sequentially unless control flow changes.
- Input and output devices communicate with the processing system.

A limitation is the Von Neumann bottleneck, which occurs because instructions and data compete for shared communication pathways.

## 6. Harvard Architecture

Harvard architecture uses separate storage and pathways for instructions and data.

| Von Neumann | Harvard |
|---|---|
| Shared instruction and data memory | Separate instruction and data memories |
| Shared communication pathway in the basic model | Separate pathways |
| Simpler unified memory arrangement | Allows simultaneous instruction and data access in suitable designs |

Many modern processors use modified or hybrid approaches.

## 7. CPU Performance

CPU performance depends on several factors:

- Clock frequency.
- Number of cores.
- Instruction set architecture.
- Cache size and efficiency.
- Memory performance.
- Processor design.
- Workload characteristics.

Clock frequency is measured in hertz, commonly gigahertz.

A higher clock frequency does not automatically mean a processor is faster in every task.

## Common Exam Traps

- The ALU performs arithmetic and logical operations.
- The Control Unit coordinates instruction execution.
- Registers are located inside the CPU.
- The Program Counter stores the address of the next instruction.
- The Instruction Register holds the current instruction.
- Von Neumann architecture uses shared instruction and data memory in its basic form.
- Clock speed alone does not determine overall computer performance.

## Quiz

1. Which CPU component performs arithmetic and logical operations?

- [ ] Control Unit.
- [ ] Program Counter.
- [x] Arithmetic Logic Unit.
- [ ] Memory Address Register.

> The ALU performs calculations and logical comparisons during instruction execution.

2. Which register holds the address of the next instruction?

- [ ] Instruction Register.
- [x] Program Counter.
- [ ] Accumulator.
- [ ] Memory Data Register.

> The Program Counter identifies the memory location from which the next instruction should be fetched.

3. What is a defining characteristic of basic Von Neumann architecture?

- [ ] Instructions and data must be stored on separate physical devices.
- [ ] The CPU does not require memory.
- [x] Instructions and data share the same memory.
- [ ] Every instruction must be executed simultaneously.

> The stored-program concept allows instructions and data to occupy the same memory system.