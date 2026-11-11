---
title: Number Systems and Binary Arithmetic
level: foundation
---

Computers represent and process information using binary digits. Understanding number systems and binary arithmetic is essential for studying computer architecture, digital logic and programming.

## 1. Meaning of a Number System

A number system is a method of representing numerical values using a collection of symbols and positional rules.

The base or radix determines the number of unique digits used.

Important number systems include:

| Number system | Base | Digits |
|---|---:|---|
| Binary | 2 | 0, 1 |
| Octal | 8 | 0–7 |
| Decimal | 10 | 0–9 |
| Hexadecimal | 16 | 0–9, A–F |

## 2. Decimal Number System

The decimal system is a base-10 positional number system.

For example:

347 = 3 x 100 + 4 x 10 + 7 x 1

Each digit represents a value determined by its position.

## 3. Binary Number System

Binary is a base-2 number system using only 0 and 1.

Each binary digit is called a bit.

Example:

1011 in binary:

1 x 8 + 0 x 4 + 1 x 2 + 1 x 1

= 8 + 0 + 2 + 1

= 11 in decimal.

## 4. Binary to Decimal Conversion

To convert binary into decimal:

1. Identify each digit's position from right to left.
2. Assign powers of 2 beginning with 2^0.
3. Multiply each digit by its positional value.
4. Add the results.

Example:

1101

= 1 x 8 + 1 x 4 + 0 x 2 + 1 x 1

= 13 in decimal.

## 5. Decimal to Binary Conversion

Repeatedly divide the decimal number by 2 and record the remainders.

Example: Convert 13 into binary.

13 / 2 = 6 remainder 1

6 / 2 = 3 remainder 0

3 / 2 = 1 remainder 1

1 / 2 = 0 remainder 1

Read the remainders from bottom to top.

Therefore:

13 = 1101 in binary.

## 6. Octal and Hexadecimal Systems

**Octal:** Uses eight digits from 0 to 7.

**Hexadecimal:** Uses sixteen symbols:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.

Hexadecimal digit values:

| Symbol | Decimal value |
|---|---:|
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |
| F | 15 |

Hexadecimal is useful because one hexadecimal digit represents exactly four binary bits.

## 7. Binary Arithmetic

### Binary Addition

| Operation | Result |
|---|---|
| 0 + 0 | 0 |
| 0 + 1 | 1 |
| 1 + 0 | 1 |
| 1 + 1 | 10 |

The result 10 means zero with a carry of one.

Example:

  101
+ 011
-----
 1000

### Binary Subtraction

| Operation | Result |
|---|---|
| 0 - 0 | 0 |
| 1 - 0 | 1 |
| 1 - 1 | 0 |
| 10 - 1 | 1 |

Borrowing is used when subtracting 1 from 0.

### Binary Multiplication

| Operation | Result |
|---|---|
| 0 x 0 | 0 |
| 0 x 1 | 0 |
| 1 x 0 | 0 |
| 1 x 1 | 1 |

## 8. Signed Number Representation

Computers can represent positive and negative integers using different methods.

Common methods include:

- Sign-magnitude representation.
- One's complement.
- Two's complement.

Two's complement is widely used because it allows addition and subtraction to be implemented efficiently within binary arithmetic systems.

## Common Exam Traps

- Binary uses only 0 and 1.
- Octal has base 8.
- Decimal has base 10.
- Hexadecimal has base 16.
- A hexadecimal digit corresponds to four binary bits.
- Binary 1010 represents decimal 10.
- Binary 1000 represents decimal 8.
- Remainders in repeated division must be read from bottom to top.

## Quiz

1. What is the decimal equivalent of binary 1011?

- [ ] 9.
- [ ] 10.
- [x] 11.
- [ ] 12.

> Binary 1011 equals 8 + 0 + 2 + 1, which gives decimal 11.

2. What is the base of the hexadecimal number system?

- [ ] 2.
- [ ] 8.
- [ ] 10.
- [x] 16.

> Hexadecimal uses sixteen symbols, from 0 to 9 and A to F.

3. What is the binary representation of decimal 10?

- [ ] 1001.
- [x] 1010.
- [ ] 1100.
- [ ] 1110.

> Decimal 10 equals 8 + 2, which is represented as binary 1010.