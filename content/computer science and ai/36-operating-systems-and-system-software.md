---
title: Operating Systems and System Software
level: foundation
---

An operating system is system software that manages computer hardware and provides services to application programs. It acts as an intermediary between users, applications, and the physical components of a computer.

## 1. Understanding an Operating System

An operating system controls and coordinates the major activities of a computer.

It provides an environment in which applications can execute without requiring every application to manage hardware independently.

Common operating systems include:

- Microsoft Windows.
- Linux.
- macOS.
- Android.
- iOS.

## 2. Main Functions of an Operating System

An operating system performs several important functions.

### Process Management

Manages running programs and allocates processor time.

### Memory Management

Controls memory allocation and tracks the memory used by processes.

### File Management

Organizes files and directories and manages access to stored information.

### Device Management

Coordinates communication with hardware devices such as keyboards, printers, and storage drives.

### Security and Access Control

Controls user permissions and protects system resources.

### User Interface

Provides methods through which users interact with the computer.

## 3. Types of Operating Systems

### Batch Operating System

Processes groups of jobs without requiring continuous interaction from the user during execution.

### Multiprogramming Operating System

Keeps multiple programs in memory so that the processor can work on another program when one is waiting for an operation.

### Multitasking Operating System

Allows multiple tasks to make progress through processor scheduling.

### Multiuser Operating System

Supports multiple users accessing system resources.

### Multiprocessing Operating System

Uses multiple processing units or cores to execute tasks.

### Real-Time Operating System

Provides predictable responses within specified timing constraints.

Real-time systems are important in industrial control, robotics, medical equipment, and embedded applications.

### Distributed Operating System

Coordinates resources and activities across multiple connected computers.

## 4. Kernel

The kernel is the central component of an operating system.

It manages important system resources and provides core services.

Its responsibilities commonly include:

- Process scheduling.
- Memory management.
- Device communication.
- Interrupt handling.
- System-call handling.
- Resource protection.

The kernel operates with privileged access to hardware and system resources.

## 5. User Mode and Kernel Mode

Modern operating systems commonly distinguish between two execution modes.

### User Mode

Applications execute with restricted permissions.

They cannot directly perform every privileged hardware operation.

### Kernel Mode

The operating-system kernel executes with elevated privileges.

It can access protected system resources and perform privileged operations.

This separation improves security and system stability.

## 6. System Calls

A system call is a controlled interface through which a program requests a service from the operating system.

Examples include:

- Creating a process.
- Opening a file.
- Reading data.
- Writing data.
- Allocating memory.
- Communicating with devices.

A system call allows an application to request privileged services without directly controlling hardware.

## 7. Types of System Software

System software supports the operation and management of a computer.

Examples include:

- Operating systems.
- Device drivers.
- Language translators.
- System utilities.
- Firmware.
- System libraries.

## 8. Language Translators

Programming languages require suitable translation or execution mechanisms.

### Compiler

A compiler translates source code into another form, commonly machine code or an intermediate representation.

### Interpreter

An interpreter executes programs through an interpretation process.

Actual implementation strategies differ between languages and runtime environments.

### Assembler

An assembler translates assembly language into machine code or object code.

## 9. Device Drivers

A device driver is software that allows an operating system to communicate with a hardware device.

Examples include drivers for:

- Graphics cards.
- Printers.
- Network adapters.
- Audio devices.
- Storage controllers.

Drivers provide device-specific functionality through operating-system interfaces.

## 10. Booting Process

Booting is the process of starting a computer and loading its operating system.

A simplified sequence is:

1. Power is supplied to the computer.
2. Firmware begins execution.
3. Hardware initialization and checks are performed.
4. A bootloader is located and executed.
5. The bootloader loads the operating-system kernel.
6. The kernel initializes essential system components.
7. System services and user interfaces become available.

The exact sequence depends on the computer architecture and firmware configuration.

## 11. Open-Source and Proprietary Operating Systems

### Open-Source Operating Systems

Their source code is available under licenses that permit specified forms of inspection, modification, and redistribution.

Linux distributions are common examples.

### Proprietary Operating Systems

Their source code and distribution rights are controlled by their owners.

Windows and macOS are examples of proprietary operating systems.

## 12. Importance of Operating Systems

Operating systems make general-purpose computing possible by coordinating hardware, managing resources, and providing common services to applications.

Without an operating system, application developers would need to manage many hardware-specific operations themselves.

## Common Exam Traps

- The operating system is system software.
- The kernel is the central component of an operating system.
- System calls allow applications to request operating-system services.
- User mode has restricted privileges.
- Kernel mode has elevated privileges.
- A compiler translates source code.
- An assembler translates assembly language.
- Device drivers enable communication with hardware.
- Real-time systems are designed around timing requirements.

## Quiz

1. What is the central component of an operating system?
   - [ ] Text editor
   - [ ] Web browser
   - [x] Kernel
   - [ ] Spreadsheet

   > The kernel manages core operating-system functions and system resources.

2. Which interface allows an application to request services from the operating system?
   - [ ] HTML
   - [ ] CSS
   - [x] System call
   - [ ] Spreadsheet formula

   > System calls provide a controlled interface for requesting operating-system services.

3. Which software allows an operating system to communicate with a hardware device?
   - [ ] Database schema
   - [ ] Web server
   - [ ] Compiler
   - [x] Device driver

   > A device driver provides the software interface required to operate a hardware device.