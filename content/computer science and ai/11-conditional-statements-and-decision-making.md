---
title: Conditional Statements and Decision-Making
level: foundation
---

Conditional statements allow a program to make decisions based on whether specified conditions are true or false. They control the flow of execution and enable programs to respond differently to different inputs.

## 1. Meaning of Conditional Statements

A conditional statement evaluates an expression and executes instructions depending on its result.

Conditions generally produce Boolean values:

- True
- False

Example:

If a person's age is at least 18, the program may classify the person as an adult.

## 2. Comparison Operators

Comparison operators compare two values.

| Operator | Meaning | Example |
|---|---|---|
| == | Equal to | A == B |
| != | Not equal to | A != B |
| > | Greater than | A > B |
| < | Less than | A < B |
| >= | Greater than or equal to | A >= B |
| <= | Less than or equal to | A <= B |

The result of a comparison is generally Boolean.

## 3. IF Statement

The IF statement executes a block of instructions when a condition is true.

Pseudocode:

IF temperature > 30 THEN
    OUTPUT "Hot"
END IF

If the condition is false, the block is skipped.

## 4. IF-ELSE Statement

The IF-ELSE statement provides two alternative execution paths.

Pseudocode:

IF number MOD 2 = 0 THEN
    OUTPUT "Even"
ELSE
    OUTPUT "Odd"
END IF

Exactly one branch is selected according to the condition.

## 5. ELSE-IF Ladder

An ELSE-IF ladder evaluates multiple conditions in sequence.

Example:

IF marks >= 90 THEN
    OUTPUT "Grade A"
ELSE IF marks >= 75 THEN
    OUTPUT "Grade B"
ELSE IF marks >= 50 THEN
    OUTPUT "Grade C"
ELSE
    OUTPUT "Grade D"
END IF

The first condition that evaluates to true determines the selected branch.

## 6. Nested Conditional Statements

A nested conditional statement places one conditional statement inside another.

Example:

IF age >= 18 THEN
    IF has_license = TRUE THEN
        OUTPUT "Can drive"
    ELSE
        OUTPUT "License required"
    END IF
ELSE
    OUTPUT "Below required age"
END IF

Nested conditions are useful when one decision depends on another.

## 7. Logical Operators in Conditions

Logical operators combine or modify Boolean expressions.

| Operator | Meaning | True condition |
|---|---|---|
| AND | Both conditions must be true | TRUE AND TRUE |
| OR | At least one condition must be true | TRUE OR FALSE |
| NOT | Reverses a Boolean value | NOT FALSE |

Example:

IF age >= 18 AND has_license = TRUE THEN
    OUTPUT "Eligible to drive"
END IF

## 8. Short-Circuit Evaluation

Some programming languages evaluate logical expressions using short-circuit rules.

For an AND expression, if the first condition is false, the second condition may not need to be evaluated.

For an OR expression, if the first condition is true, the second condition may not need to be evaluated.

This can prevent unnecessary operations and avoid certain errors.

## 9. Switch or Match Statements

Some languages provide switch, case or match structures for selecting among multiple possible values.

Example:

MATCH choice:
    CASE 1:
        OUTPUT "Addition"
    CASE 2:
        OUTPUT "Subtraction"
    CASE 3:
        OUTPUT "Multiplication"
    DEFAULT:
        OUTPUT "Invalid choice"

These structures can make multi-branch decisions easier to organise.

## Common Exam Traps

- An IF statement executes its block only when the condition is true.
- ELSE provides an alternative branch.
- ELSE-IF conditions are evaluated in sequence.
- Nested conditions contain other conditional statements.
- AND requires both conditions to be true.
- OR requires at least one condition to be true.
- NOT reverses a Boolean value.
- Equality comparison and assignment are different operations.

## Quiz

1. Which operator checks whether two values are equal?

- [ ] =
- [x] ==
- [ ] !=
- [ ] >=

> The equality operator == compares two values, while = is commonly used for assignment.

2. What is the result of TRUE AND FALSE?

- [ ] TRUE.
- [x] FALSE.
- [ ] 1.
- [ ] Undefined.

> AND produces true only when both operands are true.

3. Which structure is most suitable for selecting one option from several possible values?

- [ ] A simple assignment statement.
- [ ] A single arithmetic expression.
- [x] A switch or match statement.
- [ ] A variable declaration.

> Switch or match structures organise multi-way selection based on the value of an expression.