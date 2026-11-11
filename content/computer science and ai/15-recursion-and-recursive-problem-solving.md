---
title: Recursion and Recursive Problem-Solving
level: intermediate
---

Recursion is a programming technique in which a function calls itself to solve a problem by reducing it into smaller instances of the same problem. It is widely used in mathematical algorithms, tree processing and divide-and-conquer techniques.

## 1. Meaning of Recursion

A recursive function solves a problem by calling itself with a smaller or simpler input.

A recursive solution generally contains:

1. Base case.
2. Recursive case.
3. Progress toward the base case.

The base case terminates the recursive process.

## 2. Base Case and Recursive Case

**Base case:** Defines the simplest situation that can be solved directly.

**Recursive case:** Reduces the current problem into a smaller problem.

Example: Factorial.

FUNCTION FACTORIAL(N)

    IF N = 0 THEN
        RETURN 1
    ELSE
        RETURN N x FACTORIAL(N - 1)
    END IF

END FUNCTION

For positive N:

N! = N x (N - 1)!

The base case is:

0! = 1.

## 3. Recursive Execution

Consider FACTORIAL(4).

The calls are:

FACTORIAL(4)
= 4 x FACTORIAL(3)
= 4 x 3 x FACTORIAL(2)
= 4 x 3 x 2 x FACTORIAL(1)
= 4 x 3 x 2 x 1 x FACTORIAL(0)

Since FACTORIAL(0) = 1:

FACTORIAL(4) = 24.

## 4. Call Stack

A call stack stores information about active function calls.

Each recursive call generally creates a new stack frame containing information such as:

- Function parameters.
- Local variables.
- Return addresses.
- Execution state.

When a function completes, its stack frame is removed.

Excessive recursion can cause stack overflow.

## 5. Direct and Indirect Recursion

**Direct recursion:** A function calls itself directly.

**Indirect recursion:** One function calls another function, which eventually calls the first function.

Example of indirect recursion:

FUNCTION A()
    CALL B()
END FUNCTION

FUNCTION B()
    CALL A()
END FUNCTION

Without a stopping condition, both forms can continue indefinitely.

## 6. Recursion and Iteration

| Recursion | Iteration |
|---|---|
| Uses repeated function calls | Uses loops |
| Relies on the call stack | Usually uses loop-control variables |
| Can express tree and divide-and-conquer problems naturally | Often suitable for straightforward repetition |
| May introduce function-call overhead | Often has lower overhead for simple repetition |
| Requires a termination condition | Requires a loop termination condition |

Both approaches can solve many of the same problems.

## 7. Recursive Fibonacci Sequence

The Fibonacci sequence can be defined recursively:

F(0) = 0

F(1) = 1

F(n) = F(n - 1) + F(n - 2), for n >= 2.

Pseudocode:

FUNCTION FIBONACCI(N)

    IF N = 0 THEN
        RETURN 0
    ELSE IF N = 1 THEN
        RETURN 1
    ELSE
        RETURN FIBONACCI(N - 1) + FIBONACCI(N - 2)
    END IF

END FUNCTION

This simple recursive implementation repeats many calculations.

Its running time grows exponentially with N.

## 8. Tail Recursion

Tail recursion occurs when the recursive call is the final operation performed by the function.

Some programming languages or compilers can optimise certain tail-recursive functions.

However, tail-call optimisation is not guaranteed in every language or execution environment.

## 9. Applications of Recursion

- Tree traversal.
- Graph algorithms.
- Factorial calculations.
- Fibonacci calculations.
- Binary search.
- Merge sort.
- Quick sort.
- Directory traversal.
- Divide-and-conquer algorithms.

## Common Exam Traps

- Every valid recursive solution needs an appropriate stopping condition.
- The base case terminates recursion.
- Recursive calls are generally managed using the call stack.
- Direct recursion involves a function calling itself.
- Indirect recursion involves multiple functions calling one another.
- Naive recursive Fibonacci has exponential time complexity.
- Recursion and iteration are alternative problem-solving approaches.

## Quiz

1. Which component of a recursive function prevents endless self-calling?

- [ ] Parameter.
- [ ] Return type.
- [x] Base case.
- [ ] Global variable.

> The base case identifies when the problem is sufficiently simple to return a result without another recursive call.

2. What generally stores information about active recursive function calls?

- [ ] Heap storage.
- [ ] Secondary storage.
- [ ] CPU cache only.
- [x] Call stack.

> The call stack stores function execution information, including local state and return addresses.

3. What is the main performance problem of the naive recursive Fibonacci algorithm?

- [ ] It cannot calculate positive integers.
- [ ] It always requires a database.
- [x] It repeats many calculations and has exponential running time.
- [ ] It cannot use a base case.

> The naive recursive method recalculates the same Fibonacci values many times, causing exponential growth in execution time.