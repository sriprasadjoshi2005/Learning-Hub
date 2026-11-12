---
title: Microprocessors and Microcontrollers
level: advanced
---

# Microprocessors and Microcontrollers

Microprocessors and microcontrollers are programmable electronic devices used to execute instructions and control digital systems.

They form the computational foundation of computers, smartphones, industrial equipment, automobiles, robots, and embedded devices.

Although both use processors to execute instructions, their architectures and intended applications are different.

This lesson introduces processor architecture, the CPU, instruction execution, buses, memory organization, microcontrollers, peripherals, interrupts, and the differences between microprocessors and microcontrollers.

## 1. Introduction to Microprocessors

A microprocessor is a programmable integrated circuit that primarily contains a central processing unit (CPU).

It executes instructions and performs arithmetic, logical, and control operations.

A microprocessor generally depends on external components for functions such as:

- Main memory.
- Input/output interfaces.
- Storage.
- Timers and communication peripherals.

A microprocessor is commonly used as the processing component of a larger computer system.

## 2. Central Processing Unit

The CPU is responsible for executing program instructions.

Its major functional units include:

1. Arithmetic Logic Unit.
2. Control Unit.
3. Registers.

### 2.1 Arithmetic Logic Unit

The Arithmetic Logic Unit (ALU) performs arithmetic and logical operations.

Examples:

- Addition.
- Subtraction.
- Comparison.
- AND.
- OR.
- XOR.
- Bit shifting.

### 2.2 Control Unit

The Control Unit coordinates processor operations.

It:

- Fetches instructions.
- Decodes instructions.
- Generates control signals.
- Coordinates data transfers.
- Controls the execution sequence.

### 2.3 Registers

Registers are small, high-speed storage locations inside the processor.

Common examples include:

- Program Counter.
- Instruction Register.
- Stack Pointer.
- Accumulator.
- General-purpose registers.
- Status or flag register.

## 3. Important Processor Registers

### 3.1 Program Counter

The Program Counter (PC) stores the address of the next instruction to be fetched.

It is updated during normal instruction execution and may change during branches, jumps, and interrupts.

### 3.2 Instruction Register

The Instruction Register holds the instruction currently being decoded or executed.

### 3.3 Stack Pointer

The Stack Pointer identifies the current position of the stack in memory.

The stack is commonly used for:

- Function calls.
- Return addresses.
- Temporary data.
- Saved processor states.

### 3.4 Status Register

The status register contains flags describing the result of certain operations.

Common flags include:

- Zero flag.
- Carry flag.
- Sign or negative flag.
- Overflow flag.

The exact flags depend on the processor architecture.

## 4. Instruction Cycle

A processor executes instructions through a sequence of operations.

The basic instruction cycle is commonly described as:

1. Fetch.
2. Decode.
3. Execute.
4. Store or write back, when required.

### 4.1 Fetch

The processor retrieves an instruction from memory using the address stored in the Program Counter.

### 4.2 Decode

The control unit interprets the instruction and determines the required operation.

### 4.3 Execute

The processor performs the operation using the ALU, registers, memory, or peripherals.

### 4.4 Write Back

The result is stored in a register or memory location when required.

Modern processors may overlap these stages using pipelining and other execution techniques.

## 5. Processor Architecture

Two classical instruction-set architecture approaches are:

### 5.1 CISC

Complex Instruction Set Computer architectures provide instructions that may perform relatively complex operations.

Characteristics may include:

- Rich instruction sets.
- Variable instruction lengths in many designs.
- Multiple addressing modes.
- Complex instruction decoding.

### 5.2 RISC

Reduced Instruction Set Computer architectures emphasize simpler instruction formats and operations.

Common characteristics include:

- Regular instruction formats.
- Large register sets in many designs.
- Load/store architecture.
- Efficient instruction decoding.

Modern processors may combine features from both approaches, so the distinction is not always absolute.

## 6. System Buses

A bus is a collection of signal lines used to transfer information between system components.

The three traditional bus categories are:

### 6.1 Address Bus

The address bus carries the address of the memory location or I/O location being accessed.

If a processor has \(n\) address lines, it can represent:

\[
\boxed{2^n\text{ distinct addresses}}
\]

assuming all address combinations are available.

### 6.2 Data Bus

The data bus transfers information between the processor, memory, and other devices.

A wider data bus can transfer more bits in one bus transaction, subject to the architecture and interface.

### 6.3 Control Bus

The control bus carries signals that coordinate system operations.

Examples include:

- Read.
- Write.
- Interrupt.
- Reset.
- Clock and control signals.

## 7. Memory Organization

Processors interact with several types of memory.

### 7.1 Cache Memory

Cache is high-speed memory used to reduce the average time required to access frequently used data and instructions.

Common cache levels include:

- L1.
- L2.
- L3.

### 7.2 Main Memory

Main memory stores programs and data currently being used by the processor.

In general-purpose computers, this is commonly DRAM.

### 7.3 Secondary Storage

Secondary storage retains information over longer periods.

Examples include:

- Solid-state drives.
- Hard disk drives.
- Flash storage.

## 8. Microcontrollers

A microcontroller is an integrated circuit designed for embedded control applications.

It typically combines a processor core with memory and peripheral interfaces on a single chip.

A microcontroller may contain:

- CPU.
- Flash program memory.
- SRAM.
- Timers and counters.
- GPIO pins.
- ADC.
- Communication interfaces.
- Interrupt controller.
- PWM modules.

The exact features depend on the device.

## 9. General-Purpose Input/Output

GPIO stands for General-Purpose Input/Output.

GPIO pins can be configured to interact with external electronic circuits.

### 9.1 Input Mode

A GPIO input reads an external logic signal.

Examples:

- Push buttons.
- Switches.
- Digital sensors.

### 9.2 Output Mode

A GPIO output drives an external signal.

Examples:

- LEDs.
- Control signals.
- Relay driver inputs.
- Digital enable lines.

GPIO pins have electrical limits, including maximum current and permitted voltage.

External driver circuits may be required for larger loads.

## 10. Timers and Counters

Microcontrollers commonly contain hardware timers and counters.

They are used for:

- Measuring time intervals.
- Generating periodic events.
- Producing PWM signals.
- Counting external pulses.
- Measuring input signal frequency.

Hardware timers allow these operations to occur without continuously executing software instructions.

## 11. Analog-to-Digital and Digital-to-Analog Interfaces

### 11.1 Analog-to-Digital Converter

An Analog-to-Digital Converter (ADC) converts an analog voltage into a digital numerical representation.

The digital output depends on:

- Resolution.
- Reference voltage.
- Input voltage.
- Sampling process.

### 11.2 Digital-to-Analog Converter

A Digital-to-Analog Converter (DAC) converts a digital value into a corresponding analog output.

DACs are used in:

- Audio systems.
- Signal generation.
- Control systems.
- Instrumentation.

## 12. Interrupts

An interrupt is a signal or event that requests the processor's attention.

When an interrupt is accepted, the processor temporarily changes its normal execution flow to handle the event.

The interrupt service routine (ISR) contains the instructions used to respond.

Common interrupt sources include:

- Timer overflow.
- External switches.
- Communication events.
- ADC conversion completion.
- Hardware faults.

Interrupts allow systems to respond to events without continuously polling every device.

## 13. Microprocessor vs Microcontroller

| Property | Microprocessor | Microcontroller |
|---|---|---|
| Main purpose | General-purpose processing | Embedded control |
| CPU | Usually central component | Integrated into the device |
| Memory | Often external or separately packaged | Commonly integrated |
| Peripherals | Often external or chipset-based | Commonly integrated |
| System complexity | Can be relatively high | Often compact |
| Typical applications | Computers and high-performance systems | Appliances, sensors, controllers |

The distinction is based on typical architecture and intended use rather than an absolute rule.

## 14. Worked Numerical Examples

### Example 1: Addressable Memory

**Given:**

A processor has 20 address lines.

Calculate the number of distinct addresses it can represent.

**Formula:**

\[
N=2^n
\]

**Solution:**

\[
N=2^{20}
\]

\[
N=1,048,576
\]

**Final Answer:**

\[
\boxed{1,048,576\text{ addresses}}
\]

### Example 2: ADC Resolution

**Given:**

An ideal 10-bit ADC uses a reference voltage of:

\[
V_{ref}=5\,V
\]

Calculate its number of output codes and approximate voltage step size.

**Formula:**

\[
N=2^n
\]

\[
\text{Step size}\approx\frac{V_{ref}}{2^n}
\]

**Solution:**

Number of output codes:

\[
N=2^{10}=1024
\]

Approximate step size:

\[
\Delta V=\frac{5}{1024}
\]

\[
\Delta V\approx0.004883\,V
\]

\[
\Delta V\approx4.883\,mV
\]

**Final Answer:**

\[
\boxed{1024\text{ output codes}}
\]

\[
\boxed{\Delta V\approx4.883\,mV}
\]

### Example 3: Timer Frequency

**Given:**

A timer receives a 16 MHz clock and uses a prescaler of 64.

Calculate the timer clock frequency.

**Formula:**

\[
f_{timer}=\frac{f_{clock}}{\text{Prescaler}}
\]

**Solution:**

\[
f_{timer}=\frac{16\,MHz}{64}
\]

\[
f_{timer}=0.25\,MHz
\]

\[
f_{timer}=250\,kHz
\]

**Final Answer:**

\[
\boxed{250\,kHz}
\]

## 15. Applications

Microprocessors and microcontrollers are used in:

- Computers.
- Smartphones.
- Automotive control.
- Industrial automation.
- Robotics.
- Home appliances.
- Medical devices.
- Communication equipment.
- IoT systems.

## 16. Common Examination Traps

1. The ALU performs arithmetic and logical operations.
2. The Control Unit coordinates instruction execution.
3. The Program Counter stores the address of the next instruction.
4. The Instruction Register holds the current instruction.
5. The address bus carries addresses.
6. The data bus transfers data.
7. The control bus coordinates operations.
8. An \(n\)-bit address bus represents up to \(2^n\) addresses.
9. A microcontroller generally integrates a processor, memory, and peripherals.
10. GPIO pins can operate as inputs or outputs.
11. An ADC converts analog information into digital representation.
12. A DAC converts digital values into analog signals.
13. An interrupt requests processor attention.
14. An ISR handles a particular interrupt event.
15. Timers can generate events and measure intervals without continuous software polling.

## Quiz

1. Which processor register stores the address of the next instruction?

   - [ ] Instruction Register.
   - [x] Program Counter.
   - [ ] Accumulator.
   - [ ] Status Register.

   > The Program Counter contains the address used to fetch the next instruction. It changes during normal execution and may be modified by branches, jumps, and interrupts.

2. What is the main architectural characteristic of a typical microcontroller?

   - [ ] It contains only an ALU.
   - [ ] It requires an external processor for every operation.
   - [x] It integrates a processor, memory, and peripherals into one device.
   - [ ] It can process only analog signals.

   > A microcontroller combines processing, storage, and peripheral functions on a single integrated circuit, making it suitable for compact embedded control systems.

3. A processor has 16 address lines. How many distinct addresses can it represent?

   - [ ] 16.
   - [ ] 256.
   - [x] 65,536.
   - [ ] 1,000,000.

   > The number of address combinations is \(2^n\). Therefore, \(2^{16}=65,536\) distinct addresses can be represented.