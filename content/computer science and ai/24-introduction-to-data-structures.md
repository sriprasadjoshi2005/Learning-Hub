---
title: Introduction to Data Structures
level: intermediate
---

A data structure is a method of organizing, storing, and managing data so that it can be accessed and modified efficiently. Data structures are fundamental to algorithms, software development, databases, and artificial intelligence.

## 1. Understanding Data Structures

Programs frequently process large collections of information.

Examples include:
- A list of student records.
- A collection of website users.
- A map of connected cities.
- A queue of customer requests.
- A hierarchy of folders.

The way information is organized influences how efficiently a program can search, insert, delete, and modify data.

## 2. Abstract Data Types

An Abstract Data Type, or ADT, describes a collection of values and the operations that can be performed on them without specifying the internal implementation.

Examples include:

| Abstract Data Type | Main Operations |
| --- | --- |
| List | Insert, delete, access |
| Stack | Push, pop, peek |
| Queue | Enqueue, dequeue |
| Set | Add, remove, membership test |
| Map | Insert, retrieve, delete key-value pairs |

An ADT describes behaviour, while a data structure describes how that behaviour is implemented.

## 3. Classification of Data Structures

Data structures can be classified into several categories.

### Primitive Data Structures

Primitive structures represent basic data values.

Examples:
- Integer.
- Float.
- Character.
- Boolean.

### Non-Primitive Data Structures

Non-primitive structures organize collections of values.

Examples:
- Arrays.
- Linked lists.
- Stacks.
- Queues.
- Trees.
- Graphs.
- Hash tables.

## 4. Linear Data Structures

Linear data structures organize elements in a sequential arrangement.

Examples include:

- Arrays.
- Linked lists.
- Stacks.
- Queues.

Each element is generally arranged before or after another element according to the structure's organization.

## 5. Non-Linear Data Structures

Non-linear data structures organize elements using hierarchical or network-like relationships.

Examples include:

- Trees.
- Graphs.

A tree represents hierarchical relationships, while a graph represents connections between entities.

## 6. Static and Dynamic Data Structures

### Static Data Structures

Static data structures have a size that is fixed or predetermined during their relevant allocation period.

An array with a fixed capacity is a common example.

Advantages:
- Predictable memory requirements.
- Direct indexing in arrays.
- Simple implementation in many situations.

Limitations:
- Capacity may be insufficient.
- Unused allocated space may be wasted.
- Resizing may require additional operations.

### Dynamic Data Structures

Dynamic data structures can grow or shrink during program execution.

Examples include:
- Linked lists.
- Dynamic arrays.
- Trees.
- Graphs.

Advantages:
- Flexible memory usage.
- Adaptability to changing data sizes.
- Useful for unpredictable collections.

## 7. Common Data Structure Operations

| Operation | Meaning |
| --- | --- |
| Traversal | Visiting elements |
| Searching | Finding a required element |
| Insertion | Adding an element |
| Deletion | Removing an element |
| Sorting | Arranging elements in an order |
| Updating | Modifying an existing value |
| Accessing | Retrieving an element |

The efficiency of these operations depends on the selected structure and implementation.

## 8. Introduction to Time Complexity

Time complexity describes how an algorithm's running time grows as the input size increases.

It is commonly expressed using Big O notation.

Important complexity classes include:

| Complexity | Name | General Behaviour |
| --- | --- | --- |
| O(1) | Constant | Does not grow with input size |
| O(log n) | Logarithmic | Grows slowly |
| O(n) | Linear | Grows proportionally |
| O(n log n) | Linearithmic | Common in efficient sorting |
| O(n²) | Quadratic | Grows rapidly |
| O(2^n) | Exponential | Grows very rapidly |

These expressions describe growth rates rather than exact execution times.

## 9. Space Complexity

Space complexity describes how memory requirements grow with input size.

An algorithm may use additional memory for:
- Temporary variables.
- Auxiliary arrays.
- Recursive function calls.
- Data structures.
- Intermediate results.

An efficient algorithm should consider both time and memory requirements.

## 10. Choosing the Right Data Structure

The choice depends on the operations an application performs most frequently.

Examples:

| Requirement | Suitable Structure |
| --- | --- |
| Fast indexed access | Array |
| Last-in, first-out processing | Stack |
| First-in, first-out processing | Queue |
| Hierarchical information | Tree |
| Network connections | Graph |
| Key-based lookup | Hash table |
| Sequential dynamic storage | Linked list |

No single data structure is ideal for every application.

## Common Exam Traps

- An ADT describes operations and behaviour, not necessarily implementation.
- Arrays, linked lists, stacks, and queues are linear structures.
- Trees and graphs are non-linear structures.
- Static structures have fixed or predetermined capacity.
- Dynamic structures can change size.
- Time complexity and space complexity measure different resource requirements.
- Big O notation describes growth behaviour, not exact execution time.

## Quiz

1. Which of the following is a non-linear data structure?
   - [ ] Array
   - [ ] Stack
   - [ ] Queue
   - [x] Tree

   > Trees organize information hierarchically rather than in a single sequential arrangement.

2. Which complexity represents constant-time behaviour?
   - [ ] O(n)
   - [x] O(1)
   - [ ] O(n squared)
   - [ ] O(2^n)

   > O(1) indicates that the operation's growth does not depend on input size.

3. What does an Abstract Data Type primarily describe?
   - [ ] The physical size of computer memory
   - [ ] The programming language used
   - [x] The values and operations supported by a data type
   - [ ] The speed of a processor

   > An ADT specifies what operations are available without requiring a particular internal implementation.