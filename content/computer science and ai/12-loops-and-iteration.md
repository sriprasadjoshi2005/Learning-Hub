---
title: Loops and Iteration
level: foundation
---

Loops are programming structures that repeatedly execute a block of instructions. They reduce code repetition and are essential for processing collections, performing calculations and implementing algorithms.

## 1. Meaning of Iteration

Iteration is the repeated execution of a set of instructions.

For example, displaying numbers from 1 to 5 requires repeating an output operation.

Without a loop, the output instruction would need to be written multiple times.

## 2. FOR Loop

A FOR loop is commonly used when the number of repetitions is known or determined by a sequence.

Pseudocode:

FOR I = 1 TO 5
    OUTPUT I
END FOR

Output:

1
2
3
4
5

A loop variable controls the repetition.

## 3. WHILE Loop

A WHILE loop repeatedly executes a block as long as its condition remains true.

Pseudocode:

I = 1

WHILE I <= 5
    OUTPUT I
    I = I + 1
END WHILE

The condition is checked before each iteration.

If the condition is false initially, the loop body may not execute at all.

## 4. DO-WHILE or REPEAT-UNTIL Loop

A post-test loop checks its condition after executing the loop body.

Example:

I = 1

DO
    OUTPUT I
    I = I + 1
WHILE I <= 5

The loop body executes at least once.

In REPEAT-UNTIL structures, repetition continues until the specified condition becomes true.

## 5. Entry-Controlled and Exit-Controlled Loops

| Entry-controlled loop | Exit-controlled loop |
|---|---|
| Condition checked before execution | Condition checked after execution |
| May execute zero times | Executes at least once |
| Examples: FOR and WHILE | Example: DO-WHILE |

## 6. Nested Loops

A nested loop is a loop placed inside another loop.

Example:

FOR I = 1 TO 3
    FOR J = 1 TO 2
        OUTPUT I, J
    END FOR
END FOR

The inner loop completes its iterations for every iteration of the outer loop.

If the outer loop executes 3 times and the inner loop executes 2 times, the inner operation executes 6 times.

## 7. Loop Control Statements

**BREAK:** Terminates the nearest enclosing loop immediately.

**CONTINUE:** Skips the remaining instructions in the current iteration and proceeds to the next iteration.

These statements provide additional control over repetition.

## 8. Infinite Loops

An infinite loop occurs when a loop continues indefinitely because its termination condition is never satisfied.

Example:

I = 1

WHILE I > 0
    OUTPUT I
END WHILE

The value of I never changes, so the condition remains true.

Infinite loops may be intentional in certain systems, but accidental infinite loops are programming errors.

## 9. Loop Applications

Loops are used for:

- Calculating sums and averages.
- Searching through data.
- Sorting collections.
- Processing files.
- Generating multiplication tables.
- Repeating user input validation.
- Implementing numerical algorithms.

## 10. Time Complexity of Simple Loops

A loop that executes n times and performs a constant amount of work per iteration generally has linear time complexity.

Its complexity is O(n).

Two nested loops that each execute n times generally perform approximately n squared operations.

Their complexity is O(n^2).

## Common Exam Traps

- FOR loops are useful for controlled repetition.
- WHILE checks its condition before execution.
- DO-WHILE executes its body at least once.
- BREAK terminates a loop.
- CONTINUE skips the current iteration's remaining statements.
- Nested loops multiply iteration counts when both ranges are fixed.
- A loop may execute zero times if its entry condition is initially false.

## Quiz

1. Which loop structure guarantees at least one execution of its body?

- [ ] FOR.
- [ ] WHILE.
- [x] DO-WHILE.
- [ ] IF-ELSE.

> A DO-WHILE loop checks its condition after executing the body, so the body runs at least once.

2. What is the purpose of the BREAK statement?

- [ ] Restart the program.
- [ ] Skip only one output statement.
- [x] Terminate the nearest enclosing loop.
- [ ] Declare a new variable.

> BREAK immediately exits the nearest enclosing loop.

3. What is the general time complexity of a loop that performs constant work for n iterations?

- [ ] O(1).
- [x] O(n).
- [ ] O(log n).
- [ ] O(n^2).

> A constant amount of work repeated n times results in linear time complexity.