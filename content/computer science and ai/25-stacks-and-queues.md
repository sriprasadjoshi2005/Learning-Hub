---
title: Stacks and Queues
level: intermediate
---

Stacks and queues are fundamental linear data structures. They organize elements according to specific rules and are widely used in operating systems, algorithms, programming language implementation, and application development.

## 1. Introduction to Stacks

A stack is a linear data structure that follows the Last In, First Out principle, commonly abbreviated as LIFO.

The most recently inserted element is the first one removed.

A useful real-world example is a stack of plates. The last plate placed on top is normally the first plate removed.

## 2. Stack Operations

Common stack operations include:

| Operation | Description |
| --- | --- |
| Push | Adds an element to the top |
| Pop | Removes the top element |
| Peek or Top | Returns the top element without removing it |
| isEmpty | Checks whether the stack is empty |
| Size | Returns the number of elements |

Example:

Suppose the stack contains:

```text
Bottom [10, 20, 30] Top
```

After pushing 40:

```text
Bottom [10, 20, 30, 40] Top
```

After one pop operation:

```text
Bottom [10, 20, 30] Top
```

## 3. Stack Overflow and Underflow

Stack overflow occurs when an attempt is made to insert an element into a full stack with a fixed capacity.

Stack underflow occurs when an attempt is made to remove an element from an empty stack.

These conditions must be handled to prevent invalid operations.

## 4. Stack Implementation

A stack can be implemented using:
- Arrays.
- Dynamic arrays.
- Linked lists.

Example using Python:

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack[-1])
```

The last inserted value is removed first.

## 5. Applications of Stacks

Stacks are used in:

### Function Calls

Programming languages use call stacks to manage function execution and return locations.

### Undo Operations

Text editors use stack-like behaviour to reverse recent actions.

### Expression Evaluation

Stacks help evaluate mathematical expressions and manage operators.

### Parentheses Matching

Compilers and interpreters use stacks to check balanced brackets.

### Backtracking

Stacks help algorithms return to previously visited states.

## 6. Introduction to Queues

A queue is a linear data structure that follows the First In, First Out principle, commonly abbreviated as FIFO.

The first inserted element is the first one removed.

A real-world example is a line of people waiting for service.

## 7. Queue Operations

Common queue operations include:

| Operation | Description |
| --- | --- |
| Enqueue | Adds an element at the rear |
| Dequeue | Removes an element from the front |
| Front | Returns the first element |
| Rear | Returns the last element |
| isEmpty | Checks whether the queue is empty |

Example:

```text
Front [10, 20, 30] Rear
```

After enqueueing 40:

```text
Front [10, 20, 30, 40] Rear
```

After one dequeue:

```text
Front [20, 30, 40] Rear
```

## 8. Types of Queues

### Simple Queue

Elements are inserted at the rear and removed from the front.

### Circular Queue

The final position connects logically to the first position.

This allows unused positions to be reused efficiently in a fixed-size array implementation.

### Priority Queue

Elements are removed according to priority rather than strictly according to insertion order.

### Double-Ended Queue

A deque allows insertion and deletion at both ends.

## 9. Queue Implementation

A queue can be implemented using arrays, linked lists, or specialized library structures.

Python provides `deque` in the `collections` module.

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue.popleft())
```

The first inserted element is removed first.

## 10. Applications of Queues

Queues are used in:

- Printer scheduling.
- CPU scheduling.
- Network packet processing.
- Customer service systems.
- Breadth-first search.
- Task scheduling.
- Message processing.

## 11. Stack vs Queue

| Feature | Stack | Queue |
| --- | --- | --- |
| Principle | LIFO | FIFO |
| Insertion | Top | Rear |
| Removal | Top | Front |
| Main Operations | Push and Pop | Enqueue and Dequeue |
| Example | Undo history | Printer queue |

## Common Exam Traps

- A stack follows LIFO.
- A queue follows FIFO.
- Push inserts an element into a stack.
- Pop removes the top element.
- Enqueue inserts an element into a queue.
- Dequeue removes the front element.
- A priority queue removes elements according to priority.
- A circular queue reuses available positions.

## Quiz

1. Which principle does a stack follow?
   - [ ] FIFO
   - [x] LIFO
   - [ ] Random access
   - [ ] Priority-based access only

   > A stack removes the most recently inserted element first.

2. Which operation removes an element from the front of a queue?
   - [ ] Push
   - [ ] Pop
   - [x] Dequeue
   - [ ] Enqueue

   > Dequeue removes the element at the front of a queue.

3. Which data structure is commonly used to implement undo functionality?
   - [ ] Graph
   - [ ] Queue
   - [x] Stack
   - [ ] Hash table

   > A stack can store recent actions so that the most recent action can be reversed first.