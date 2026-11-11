---
title: Debugging, Testing and Code Quality
level: intermediate
---

Debugging and testing are essential software development activities. Debugging helps identify and correct defects, while testing evaluates whether a program behaves according to its requirements.

## 1. Understanding Debugging

Debugging is the systematic process of identifying, locating, analyzing, and correcting errors in a program.

A defect or bug is a flaw that causes software to behave incorrectly.

Common causes include:
- Incorrect algorithms.
- Invalid assumptions.
- Incorrect variable values.
- Boundary-condition mistakes.
- Incorrect data handling.
- Unexpected user input.

## 2. Debugging Process

A systematic debugging process usually involves:

1. Reproducing the problem.
2. Identifying the conditions that cause it.
3. Locating the relevant section of code.
4. Investigating variable values and execution flow.
5. Correcting the underlying problem.
6. Testing the correction.
7. Checking that other features still work.

Changing code without understanding the cause can introduce additional defects.

## 3. Debugging Techniques

### Print Debugging

Temporary output statements reveal variable values and program progress.

```python
number = 15
print("Current number:", number)
```

### Breakpoints

A breakpoint pauses program execution at a selected line.

Developers can inspect:
- Variable values.
- Function calls.
- Execution order.
- Program state.

### Step-by-Step Execution

Debuggers commonly provide:

- Step Into: Enter a function call.
- Step Over: Execute a function without entering its internal statements.
- Step Out: Continue execution until the current function returns.
- Continue: Resume execution until another breakpoint or termination.

## 4. Software Testing

Software testing evaluates whether a program satisfies specified requirements and behaves correctly.

Testing can reveal defects, but it cannot prove that a program is completely free of errors.

## 5. Types of Software Testing

| Testing Type | Purpose |
| --- | --- |
| Unit Testing | Tests individual functions or components |
| Integration Testing | Tests interactions between components |
| System Testing | Tests the complete application |
| Acceptance Testing | Checks whether requirements are satisfied |
| Regression Testing | Checks whether new changes break existing features |
| Performance Testing | Evaluates speed, stability, and resource usage |

## 6. Test Cases

A test case specifies an input, execution conditions, and an expected result.

Example: Testing an even-or-odd function.

| Input | Expected Result |
| --- | --- |
| 4 | Even |
| 7 | Odd |
| 0 | Even |
| -6 | Even |

Good test cases include normal values, boundary values, and invalid inputs.

## 7. Boundary Value Analysis

Boundary value analysis focuses on values near the limits of an accepted input range.

Suppose an application accepts ages from 18 to 60.

Useful test values include:

- 17: Below the minimum.
- 18: Minimum accepted value.
- 19: Just above the minimum.
- 59: Just below the maximum.
- 60: Maximum accepted value.
- 61: Above the maximum.

Boundary testing is useful because many programming errors occur near limits.

## 8. Equivalence Partitioning

Equivalence partitioning divides input data into groups expected to behave similarly.

Suppose a system accepts marks from 0 to 100.

The input can be divided into three partitions:

- Invalid values below 0.
- Valid values from 0 to 100.
- Invalid values above 100.

Instead of testing every possible value, representative values are selected from each partition.

## 9. Code Quality

Code quality describes how readable, maintainable, reliable, and efficient a program is.

Important characteristics include:

- Readability: Code is easy to understand.
- Maintainability: Code is easy to modify.
- Reliability: Code behaves consistently.
- Reusability: Components can be used again.
- Efficiency: Resources are used appropriately.
- Testability: Code can be tested effectively.

## 10. Clean Code Practices

Good programming practices include:

- Use meaningful variable and function names.
- Divide large programs into smaller functions.
- Avoid unnecessary repetition.
- Keep functions focused on specific tasks.
- Use consistent formatting.
- Handle errors appropriately.
- Write useful documentation.
- Remove unnecessary code.

## 11. Automated Testing

Automated testing uses software tools to execute test cases and compare actual results with expected results.

For example, Python provides the `unittest` module.

```python
import unittest

def add(a, b):
    return a + b

class AdditionTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

if __name__ == "__main__":
    unittest.main()
```

Automated testing is particularly useful when applications are modified frequently.

## Common Exam Traps

- Debugging identifies and corrects defects; testing evaluates program behaviour.
- Unit testing focuses on individual components.
- Integration testing examines interactions between components.
- Regression testing checks whether existing functionality still works after changes.
- Boundary value analysis concentrates on input limits.
- Testing can reveal defects but cannot guarantee their complete absence.

## Quiz

1. What is the primary purpose of debugging?
   - [ ] To design a database
   - [x] To identify and correct program defects
   - [ ] To increase screen resolution
   - [ ] To translate programming languages

   > Debugging investigates errors and corrects their underlying causes.

2. Which testing technique focuses on values near the limits of an accepted input range?
   - [ ] Integration testing
   - [ ] Regression testing
   - [x] Boundary value analysis
   - [ ] Performance testing

   > Boundary value analysis checks values at and around input boundaries.

3. Which testing method checks whether recent changes have broken previously working features?
   - [ ] Unit testing
   - [ ] Acceptance testing
   - [ ] System testing
   - [x] Regression testing

   > Regression testing verifies that existing functionality continues to work after modifications.