---
title: Exception Handling and Error Management
level: intermediate
---

Exception handling is a programming technique used to detect and manage errors that occur while a program is running. It prevents unexpected failures from terminating a program and allows developers to provide meaningful error messages or alternative actions.

## 1. Errors and Exceptions

An error is a problem that prevents a program from working correctly.

Common categories include:

| Error Type | Description | Example |
| --- | --- | --- |
| Syntax Error | Violation of programming language rules | Missing closing bracket |
| Runtime Error | Occurs during program execution | Division by zero |
| Logical Error | Program runs but produces an incorrect result | Using addition instead of multiplication |
| Compilation Error | Prevents source code from being compiled | Invalid type declaration |

An exception is an event that interrupts the normal flow of program execution.

Examples include:
- Dividing a number by zero.
- Accessing an invalid array index.
- Opening a file that does not exist.
- Converting invalid text into a number.

## 2. Exception Handling

Exception handling allows a program to respond to runtime problems instead of stopping unexpectedly.

Common exception-handling constructs include:

- `try`: Contains statements that may produce an exception.
- `except` or `catch`: Handles an exception.
- `finally`: Contains statements that execute whether an exception occurs or not.
- `raise` or `throw`: Explicitly generates an exception.

## 3. Try and Except Blocks

A try block contains potentially problematic code. If an exception occurs, control moves to an appropriate exception handler.

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

Different exception handlers can respond to different types of errors.

## 4. Handling Multiple Exceptions

A program may encounter several kinds of exceptions.

Multiple handlers allow each exception to be managed separately.

Example:

```python
try:
    values = [10, 20, 30]
    index = int(input("Enter an index: "))
    print(values[index])
except ValueError:
    print("The index must be an integer.")
except IndexError:
    print("The selected index does not exist.")
```

A general exception handler can catch unexpected exceptions, but specific handlers should generally be preferred.

## 5. Finally Block

A finally block executes whether an exception occurs or not.

It is commonly used for cleanup operations such as closing files and releasing resources.

Example:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Operation completed.")
```

Resource-management mechanisms such as `with` in Python are often safer for file handling.

## 6. Raising Exceptions

Programmers can deliberately generate exceptions when an invalid condition occurs.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Raising exceptions helps enforce valid input and program rules.

## 7. Custom Exceptions

Custom exceptions are user-defined exception classes created for specific application requirements.

Example:

```python
class InsufficientBalanceError(Exception):
    pass

balance = 500
withdrawal = 800

if withdrawal > balance:
    raise InsufficientBalanceError("Insufficient balance.")
```

Custom exceptions make application errors easier to identify and manage.

## 8. Exception Propagation

Exception propagation occurs when an exception moves through function calls until a suitable handler is found.

If no handler catches the exception, the program may terminate with an error report.

Example:

```python
def calculate():
    return 10 / 0

def execute():
    calculate()

try:
    execute()
except ZeroDivisionError:
    print("An arithmetic error occurred.")
```

The exception originates in `calculate()` and propagates through `execute()` to the handler.

## 9. Best Practices

- Catch specific exceptions whenever possible.
- Avoid using exceptions to control ordinary program flow.
- Provide useful error messages.
- Validate input before processing it.
- Release resources properly.
- Avoid silently ignoring exceptions.
- Create custom exceptions when application-specific errors need to be represented.

## Common Exam Traps

- Syntax errors and runtime exceptions are not the same.
- A finally block is intended for cleanup and normally executes even when an exception occurs.
- Raising an exception and handling an exception are different operations.
- A custom exception is defined by the programmer.
- Exception propagation allows errors to move through function calls.

## Quiz

1. Which block contains code that may generate an exception?
   - [ ] except
   - [x] try
   - [ ] finally
   - [ ] raise

   > The try block contains statements that may produce exceptions.

2. Which block is generally used for cleanup operations?
   - [ ] except
   - [ ] raise
   - [x] finally
   - [ ] return

   > The finally block is designed for operations that should run regardless of whether an exception occurs.

3. What happens when an exception is not handled anywhere in a program?
   - [ ] It automatically becomes a comment.
   - [ ] It is always ignored.
   - [x] It may terminate program execution.
   - [ ] It is converted into a variable.

   > An unhandled exception can terminate execution and produce an error report.