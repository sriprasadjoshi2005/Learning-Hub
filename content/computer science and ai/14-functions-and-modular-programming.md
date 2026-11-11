---
title: Functions and Modular Programming
level: foundation
---

Functions are reusable blocks of code designed to perform specific tasks. Modular programming divides a large program into smaller independent components, making software easier to understand, test and maintain.

## 1. Meaning of a Function

A function is a named block of instructions that performs a particular operation.

A function may:

- Accept input values.
- Perform calculations.
- Execute logical operations.
- Return a result.
- Be called multiple times.

Example:

FUNCTION ADD(A, B)
    RETURN A + B
END FUNCTION

Calling ADD(5, 3) returns 8.

## 2. Function Declaration and Function Call

**Function declaration or definition:** Establishes the function's name, parameters and implementation.

**Function call:** Requests the execution of a function.

Example:

FUNCTION SQUARE(N)
    RETURN N x N
END FUNCTION

RESULT = SQUARE(4)

The result is 16.

## 3. Parameters and Arguments

A parameter is a variable specified in a function definition.

An argument is the actual value supplied when the function is called.

Example:

FUNCTION MULTIPLY(A, B)
    RETURN A x B
END FUNCTION

MULTIPLY(3, 5)

Here, A and B are parameters, while 3 and 5 are arguments.

## 4. Return Values

A return statement sends a result from a function back to the calling code.

Example:

FUNCTION AREA(LENGTH, WIDTH)
    RETURN LENGTH x WIDTH
END FUNCTION

RESULT = AREA(6, 4)

The function returns 24.

Some functions perform actions without returning an explicit value.

## 5. Local and Global Variables

**Local variable:** Declared within a function or local scope and generally accessible only within that scope.

**Global variable:** Defined in a broader scope and may be accessible from multiple parts of a program, depending on language rules.

Excessive use of global variables can make programs harder to test and maintain.

## 6. Types of Functions

Functions may be classified according to their parameters and return values.

| Type | Description |
|---|---|
| No parameters, no return value | Performs an operation without accepting or returning a value |
| Parameters, no return value | Accepts input and performs an action |
| No parameters, return value | Produces a result without receiving arguments |
| Parameters and return value | Accepts input and returns a result |

## 7. Modular Programming

Modular programming divides software into smaller modules.

A module is a logical unit responsible for a particular part of the program.

Advantages include:

- Code reusability.
- Easier debugging.
- Better organisation.
- Simpler testing.
- Improved maintenance.
- Reduced duplication.

## 8. Recursion and Functions

A recursive function calls itself to solve smaller versions of a problem.

Example:

FUNCTION FACTORIAL(N)
    IF N = 0 THEN
        RETURN 1
    ELSE
        RETURN N x FACTORIAL(N - 1)
    END IF
END FUNCTION

The base case stops recursion.

Without an appropriate base case, recursion may continue indefinitely until available execution resources are exhausted.

## 9. Function Libraries

A function library contains reusable functions that programmers can use without implementing every operation themselves.

Examples include:

- Mathematical libraries.
- String-processing libraries.
- Date and time libraries.
- File-processing libraries.

## Common Exam Traps

- Parameters are defined in a function declaration.
- Arguments are supplied during a function call.
- A return statement sends a result to the caller.
- Local variables have limited scope.
- Global variables have broader scope.
- Modular programming divides a large program into smaller components.
- Recursive functions require a suitable base case.

## Quiz

1. What is an argument in a function call?

- [ ] The function's return type.
- [x] A value supplied to a function when it is called.
- [ ] The name of a programming language.
- [ ] A variable that must always be global.

> Arguments are the actual values passed to a function during execution.

2. What is the main advantage of modular programming?

- [ ] It eliminates the need for testing.
- [ ] It prevents every possible runtime error.
- [x] It improves organisation, reuse and maintainability.
- [ ] It makes all programs execute in constant time.

> Dividing programs into modules makes individual components easier to understand, test and maintain.

3. What prevents a recursive function from continuing indefinitely?

- [ ] A global variable.
- [ ] A function library.
- [x] A base case.
- [ ] A comment.

> A base case defines when recursion should stop.