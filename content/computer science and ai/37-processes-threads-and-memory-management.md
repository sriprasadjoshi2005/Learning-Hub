---
title: Processes, Threads and Memory Management
level: advanced
---

Processes, threads, and memory management are fundamental operating-system concepts. They determine how programs execute, share processor resources, and use available memory.

## 1. Understanding a Process

A process is a program in execution.

It includes more than the program's source code.

A process may contain:

- Executable instructions.
- A process identifier.
- Current execution state.
- Memory allocations.
- CPU register values.
- Open files.
- Other operating-system resources.

A single program can have multiple running processes.

## 2. Process States

A process moves through different states during execution.

Common states include:

| State | Meaning |
| --- | --- |
| New | Process is being created |
| Ready | Process is waiting for CPU allocation |
| Running | Process is currently executing |
| Waiting or Blocked | Process is waiting for an event or resource |
| Terminated | Process has completed or been stopped |

A process does not necessarily execute continuously. The operating system schedules and coordinates its execution.

## 3. Process Control Block

A Process Control Block, or PCB, is an operating-system data structure containing information required to manage a process.

It commonly stores:

- Process identifier.
- Process state.
- Program counter.
- CPU registers.
- Scheduling information.
- Memory-management information.
- I/O status.
- Resource information.

The PCB helps the operating system track and manage individual processes.

## 4. CPU Scheduling

CPU scheduling determines which ready process receives processor time.

The scheduler selects processes according to a scheduling policy.

Common scheduling algorithms include:

### First Come, First Served

Processes execute in the order they arrive.

It is simple but can cause long waiting times when a lengthy process executes before shorter ones.

### Shortest Job First

Selects the process with the shortest expected CPU burst.

It can reduce average waiting time under suitable assumptions, but estimating execution time may be difficult.

### Priority Scheduling

Selects processes according to assigned priority.

A problem called starvation can occur when low-priority processes wait indefinitely.

### Round Robin

Each process receives a fixed time slice called a time quantum.

After its quantum expires, an unfinished process moves to the back of the ready queue.

Round Robin is commonly associated with time-sharing systems.

## 5. Scheduling Performance Measures

Important scheduling measures include:

- Waiting time: Time spent waiting in the ready queue.
- Turnaround time: Total time from submission to completion.
- Response time: Time from submission until the first response or execution.
- CPU utilization: Proportion of time the processor is busy.
- Throughput: Number of completed processes per unit time.

A scheduling algorithm may optimize some measures while affecting others.

## 6. Context Switching

A context switch occurs when the CPU stops executing one process or thread and switches to another.

The operating system saves the current execution context and restores the context of the selected process or thread.

Context switching enables multitasking but introduces overhead.

## 7. Understanding Threads

A thread is an execution unit within a process.

A process may contain one or multiple threads.

Threads belonging to the same process commonly share:

- Process memory.
- Program code.
- Global data.
- Open resources.

Each thread maintains its own execution state, including its stack and processor context.

## 8. Processes vs Threads

| Feature | Process | Thread |
| --- | --- | --- |
| Definition | Program in execution | Execution unit within a process |
| Address Space | Generally separate | Shares process address space |
| Resource Ownership | Owns process resources | Uses process resources |
| Creation Cost | Generally higher | Generally lower |
| Communication | Often requires IPC mechanisms | Can communicate through shared memory |
| Failure Impact | Usually isolated from other processes | Can affect the entire process |

Threads improve responsiveness and can support parallel execution on multicore processors.

## 9. Concurrency and Parallelism

### Concurrency

Concurrency means multiple tasks make progress during overlapping periods.

They may take turns using a single processor.

### Parallelism

Parallelism means multiple tasks execute at the same time on different processing resources.

A multicore processor can support parallel execution.

Concurrency does not necessarily imply parallelism.

## 10. Race Conditions and Synchronization

A race condition occurs when the outcome of a program depends on the unpredictable timing or ordering of concurrent operations.

Example:

Two threads attempt to increment the same shared variable.

If both read the original value before either writes the updated value, one increment may be lost.

Synchronization mechanisms help coordinate access to shared resources.

Common mechanisms include:

- Mutex locks.
- Semaphores.
- Monitors.
- Condition variables.

## 11. Memory Management

Memory management controls how computer memory is allocated, tracked, protected, and released.

The operating system manages memory so that multiple processes can execute safely.

Important responsibilities include:

- Allocating memory.
- Releasing memory.
- Tracking available memory.
- Protecting process memory.
- Supporting virtual memory.

## 12. Virtual Memory

Virtual memory provides each process with an abstraction of its own address space.

It allows programs to use an address space that is not limited to the amount of physical RAM currently allocated to them.

Virtual memory is commonly implemented using paging and sometimes segmentation-related mechanisms.

## 13. Paging

Paging divides virtual memory into fixed-size pages and physical memory into fixed-size frames.

Pages can be mapped to available physical frames.

A page table records these mappings.

Paging helps avoid external fragmentation associated with variable-sized contiguous allocation.

However, it can produce internal fragmentation, particularly in the final allocated page.

## 14. Page Faults

A page fault occurs when a process accesses a virtual page that does not currently have the required mapping in physical memory.

The operating system handles the fault.

Depending on the situation, it may:

1. Check whether the memory access is valid.
2. Locate the required page.
3. Obtain a free frame or select a page for replacement.
4. Load the required page.
5. Update the page table.
6. Resume the interrupted instruction.

A page fault is not necessarily an error. It is a normal part of virtual memory operation.

## 15. Page Replacement Algorithms

When physical memory has no available frame, an operating system may need to replace an existing page.

Important algorithms include:

### FIFO

Replaces the page that has been in memory the longest.

### Least Recently Used

Replaces the page that has not been accessed for the longest time.

### Optimal Page Replacement

Replaces the page whose next use is farthest in the future.

Optimal replacement is mainly a theoretical benchmark because future memory references are generally unknown.

## 16. Memory Fragmentation

### Internal Fragmentation

Occurs when allocated memory contains unused space within the allocated region.

### External Fragmentation

Occurs when free memory is divided into separated blocks, making it difficult to allocate a sufficiently large contiguous region.

Paging reduces external fragmentation in physical-memory allocation, although other forms of memory-management overhead remain.

## Common Exam Traps

- A process is a program in execution.
- A thread is an execution unit within a process.
- Threads in the same process generally share an address space.
- A PCB stores process-management information.
- Round Robin uses a time quantum.
- A context switch saves and restores execution context.
- Concurrency does not necessarily mean parallel execution.
- A race condition depends on the ordering of concurrent operations.
- Paging divides virtual memory into pages and physical memory into frames.
- A page fault does not necessarily indicate an invalid memory access.
- FIFO and LRU are page-replacement algorithms.

## Quiz

1. Which scheduling algorithm uses a fixed time quantum?
   - [ ] First Come, First Served
   - [ ] Shortest Job First
   - [x] Round Robin
   - [ ] Static memory allocation

   > Round Robin allocates a time slice to each process in the ready queue.

2. What does a page fault indicate?
   - [ ] The processor has stopped permanently.
   - [x] A required virtual-memory page needs to be handled because it is not currently available through the required physical mapping.
   - [ ] The operating system has been deleted.
   - [ ] A program has necessarily encountered a syntax error.

   > A page fault triggers operating-system handling to resolve a virtual-memory access.

3. Which mechanism helps prevent uncontrolled simultaneous access to shared resources?
   - [ ] Compiler
   - [ ] Cache
   - [x] Mutex
   - [ ] File extension

   > A mutex provides mutual exclusion so that protected shared operations are not performed simultaneously by multiple threads.