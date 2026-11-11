---
title: Fundamental Programming Exercises
level: foundation
---

Programming exercises help develop the ability to translate mathematical and logical problems into executable instructions. This lesson introduces common beginner problems involving arithmetic, conditions, loops and basic algorithms.

## 1. Addition of Two Numbers

Problem: Read two numbers and calculate their sum.

Pseudocode:

BEGIN
    INPUT A
    INPUT B

    SUM = A + B

    OUTPUT SUM
END

This exercise introduces input, assignment, arithmetic and output.

## 2. Area of a Rectangle

The area of a rectangle is:

AREA = LENGTH x WIDTH

Pseudocode:

BEGIN
    INPUT LENGTH
    INPUT WIDTH

    AREA = LENGTH x WIDTH

    OUTPUT AREA
END

Both dimensions should use compatible units.

## 3. Checking Even or Odd Numbers

A number is even if it is divisible by 2 without a remainder.

Pseudocode:

BEGIN
    INPUT N

    IF N MOD 2 = 0 THEN
        OUTPUT "Even"
    ELSE
        OUTPUT "Odd"
    END IF
END

The MOD operator returns the remainder after division.

## 4. Finding the Largest of Three Numbers

Pseudocode:

BEGIN
    INPUT A, B, C

    LARGEST = A

    IF B > LARGEST THEN
        LARGEST = B
    END IF

    IF C > LARGEST THEN
        LARGEST = C
    END IF

    OUTPUT LARGEST
END

The algorithm also works when two or more values are equal.

## 5. Calculating Factorial

Factorial is defined for non-negative integers.

N! = N x (N - 1) x ... x 2 x 1

Special case:

0! = 1

Pseudocode:

BEGIN
    INPUT N
    FACTORIAL = 1

    FOR I = 1 TO N
        FACTORIAL = FACTORIAL x I
    END FOR

    OUTPUT FACTORIAL
END

For negative inputs, the algorithm should reject the input because ordinary integer factorial is not defined for negative integers.

## 6. Generating a Multiplication Table

Pseudocode:

BEGIN
    INPUT N

    FOR I = 1 TO 10
        OUTPUT N x I
    END FOR
END

This exercise demonstrates repeated multiplication using a loop.

## 7. Checking Prime Numbers

A prime number is an integer greater than 1 that has exactly two positive divisors: 1 and itself.

Pseudocode:

BEGIN
    INPUT N

    IF N <= 1 THEN
        OUTPUT "Not prime"
    ELSE
        PRIME = TRUE

        FOR I = 2 TO FLOOR(SQRT(N))
            IF N MOD I = 0 THEN
                PRIME = FALSE
                BREAK
            END IF
        END FOR

        IF PRIME = TRUE THEN
            OUTPUT "Prime"
        ELSE
            OUTPUT "Not prime"
        END IF
    END IF
END

Checking divisors only up to the square root is sufficient because factors occur in pairs.

## 8. Reversing a Number

Pseudocode:

BEGIN
    INPUT N
    REVERSED = 0

    WHILE N > 0
        DIGIT = N MOD 10
        REVERSED = REVERSED x 10 + DIGIT
        N = FLOOR(N / 10)
    END WHILE

    OUTPUT REVERSED
END

This version assumes a non-negative integer input and does not preserve leading zeros.

## 9. Finding the Sum of Digits

Pseudocode:

BEGIN
    INPUT N
    SUM = 0

    WHILE N > 0
        DIGIT = N MOD 10
        SUM = SUM + DIGIT
        N = FLOOR(N / 10)
    END WHILE

    OUTPUT SUM
END

For example, the sum of digits of 352 is:

3 + 5 + 2 = 10.

## 10. Fibonacci Sequence

The Fibonacci sequence begins with 0 and 1. Each subsequent term is the sum of the previous two terms.

Sequence:

0, 1, 1, 2, 3, 5, 8, 13, ...

Pseudocode:

BEGIN
    INPUT N

    A = 0
    B = 1

    FOR I = 1 TO N
        OUTPUT A

        TEMP = A + B
        A = B
        B = TEMP
    END FOR
END

This algorithm generates the first N terms.

## Common Exam Traps

- The factorial of zero is 1.
- Negative integers are not prime.
- The number 1 is neither prime nor composite.
- The Fibonacci sequence starts with 0 and 1 in this convention.
- MOD returns the remainder.
- Integer division may discard the fractional part.
- A prime-testing algorithm can stop after checking divisors up to the square root.

## Quiz

1. What is the factorial of zero?

- [ ] 0.
- [ ] Undefined.
- [x] 1.
- [ ] 10.

> Zero factorial is defined as 1, which is important in combinatorics and mathematical identities.

2. Which of the following is a prime number?

- [ ] 1.
- [ ] 21.
- [x] 17.
- [ ] 27.

> Seventeen has exactly two positive divisors: 1 and 17.

3. Which operation is used to obtain the remainder after integer division?

- [ ] Multiplication.
- [ ] Exponentiation.
- [ ] Integer square root.
- [x] Modulo.

> The modulo operation returns the remainder after division.