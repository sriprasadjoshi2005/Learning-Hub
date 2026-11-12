---
title: Number Systems and Binary Arithmetic
level: foundation
---

# Number Systems and Binary Arithmetic

Digital electronic systems represent and process information using discrete values.

The binary number system is fundamental to digital electronics because electronic circuits can reliably represent two logical states using voltage levels.

Computers, microcontrollers, processors, memory devices, and digital communication systems all depend on binary representation.

This lesson introduces decimal, binary, octal, and hexadecimal number systems, number conversion, binary arithmetic, signed numbers, complements, and basic overflow concepts.

## 1. Introduction to Number Systems

A number system is a method of representing quantities using a set of symbols and rules.

A positional number system assigns a value to each digit according to its position.

The base, or radix, determines how many different digits are available.

Common number systems include:

| Number system | Base | Digits |
|---|---:|---|
| Decimal | 10 | 0–9 |
| Binary | 2 | 0, 1 |
| Octal | 8 | 0–7 |
| Hexadecimal | 16 | 0–9, A–F |

## 2. Decimal Number System

The decimal number system has base 10.

Each position represents a power of 10.

For example:

\[
5724=5(10^3)+7(10^2)+2(10^1)+4(10^0)
\]

Therefore:

\[
5724=5000+700+20+4
\]

Decimal is commonly used in everyday calculations and human-readable measurements.

## 3. Binary Number System

The binary number system has base 2.

It uses only two digits:

- 0.
- 1.

Each binary digit is called a bit.

The positions represent powers of 2.

For example:

\[
(1011)_2
\]

Expanding:

\[
=1(2^3)+0(2^2)+1(2^1)+1(2^0)
\]

\[
=8+0+2+1
\]

\[
\boxed{(1011)_2=(11)_{10}}
\]

## 4. Binary Place Values

The binary place values are:

| Position | Power of 2 | Decimal value |
|---|---:|---:|
| 0 | \(2^0\) | 1 |
| 1 | \(2^1\) | 2 |
| 2 | \(2^2\) | 4 |
| 3 | \(2^3\) | 8 |
| 4 | \(2^4\) | 16 |
| 5 | \(2^5\) | 32 |
| 6 | \(2^6\) | 64 |
| 7 | \(2^7\) | 128 |

For an \(n\)-bit unsigned number, the range is:

\[
\boxed{0\text{ to }2^n-1}
\]

For example, an 8-bit unsigned number can represent:

\[
0\text{ to }255
\]

## 5. Converting Binary to Decimal

Multiply each binary digit by its corresponding power of 2 and add the results.

### Example

Convert:

\[
(110101)_2
\]

to decimal.

Expansion:

\[
=1(32)+1(16)+0(8)+1(4)+0(2)+1(1)
\]

\[
=32+16+4+1
\]

\[
\boxed{(110101)_2=(53)_{10}}
\]

## 6. Converting Decimal to Binary

Repeatedly divide the decimal number by 2.

Record each remainder.

Read the remainders from bottom to top.

### Example

Convert \(45_{10}\) into binary.

| Division | Quotient | Remainder |
|---|---:|---:|
| 45 ÷ 2 | 22 | 1 |
| 22 ÷ 2 | 11 | 0 |
| 11 ÷ 2 | 5 | 1 |
| 5 ÷ 2 | 2 | 1 |
| 2 ÷ 2 | 1 | 0 |
| 1 ÷ 2 | 0 | 1 |

Reading upward:

\[
\boxed{(45)_{10}=(101101)_2}
\]

## 7. Octal Number System

The octal system has base 8.

Its digits are:

\[
0,1,2,3,4,5,6,7
\]

Each position represents a power of 8.

For example:

\[
(257)_8
\]

\[
=2(8^2)+5(8^1)+7(8^0)
\]

\[
=128+40+7
\]

\[
\boxed{(257)_8=(175)_{10}}
\]

### 7.1 Binary-to-Octal Conversion

Each octal digit corresponds to three binary bits.

| Octal digit | Binary |
|---|---|
| 0 | 000 |
| 1 | 001 |
| 2 | 010 |
| 3 | 011 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |

Group binary digits into sets of three, starting from the right.

Example:

\[
(1101011)_2
\]

Group:

\[
001\ 101\ 011
\]

Convert each group:

\[
1\ 5\ 3
\]

Therefore:

\[
\boxed{(1101011)_2=(153)_8}
\]

## 8. Hexadecimal Number System

The hexadecimal system has base 16.

It uses:

\[
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
\]

The letters represent decimal values:

| Hexadecimal | Decimal |
|---|---:|
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |
| F | 15 |

For example:

\[
(2F)_{16}
\]

\[
=2(16)+15
\]

\[
=32+15
\]

\[
\boxed{(2F)_{16}=(47)_{10}}
\]

### 8.1 Binary-to-Hexadecimal Conversion

Each hexadecimal digit corresponds to four binary bits.

| Hexadecimal | Binary |
|---|---|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| A | 1010 |
| B | 1011 |
| C | 1100 |
| D | 1101 |
| E | 1110 |
| F | 1111 |

Group binary digits into sets of four, starting from the right.

Example:

\[
(10111100)_2
\]

Group:

\[
1011\ 1100
\]

Convert:

\[
B\ C
\]

Therefore:

\[
\boxed{(10111100)_2=(BC)_{16}}
\]

## 9. Binary Fractions

Binary numbers can also represent fractional values.

The positions to the right of the binary point represent negative powers of 2.

For example:

\[
(101.101)_2
\]

\[
=1(2^2)+0(2^1)+1(2^0)
+1(2^{-1})+0(2^{-2})+1(2^{-3})
\]

\[
=4+0+1+0.5+0+0.125
\]

\[
\boxed{(101.101)_2=(5.625)_{10}}
\]

## 10. Binary Addition

Binary addition follows four basic rules.

| Addition | Result |
|---|---|
| \(0+0\) | 0 |
| \(0+1\) | 1 |
| \(1+0\) | 1 |
| \(1+1\) | 10 |

The last rule produces a carry.

### Example

Add:

\[
1011_2+0110_2
\]

Working from right to left:

\[
\begin{array}{r}
1011\\
+0110\\
\hline
10001
\end{array}
\]

Therefore:

\[
\boxed{1011_2+0110_2=10001_2}
\]

Verification:

\[
11+6=17
\]

## 11. Binary Subtraction

The basic subtraction rules are:

| Subtraction | Result |
|---|---|
| \(0-0\) | 0 |
| \(1-0\) | 1 |
| \(1-1\) | 0 |
| \(0-1\) | Borrow required |

When subtracting \(0-1\), borrow from the next higher bit.

A borrowed binary 1 represents decimal 2 in the current column.

### Example

\[
1101_2-0101_2
\]

\[
\boxed{1000_2}
\]

Verification:

\[
13-5=8
\]

## 12. Binary Multiplication

Binary multiplication follows:

\[
0\times0=0
\]

\[
0\times1=0
\]

\[
1\times0=0
\]

\[
1\times1=1
\]

### Example

\[
101_2\times11_2
\]

\[
\begin{array}{r}
101\\
\times11\\
\hline
101\\
1010\\
\hline
1111
\end{array}
\]

Therefore:

\[
\boxed{101_2\times11_2=1111_2}
\]

Verification:

\[
5\times3=15
\]

## 13. Complements in Binary Arithmetic

Complements are used to represent negative numbers and simplify subtraction.

### 13.1 One's Complement

The one's complement is obtained by changing every 0 to 1 and every 1 to 0.

Example:

\[
10110010
\]

One's complement:

\[
01001101
\]

### 13.2 Two's Complement

Two's complement is obtained by:

1. Taking the one's complement.
2. Adding 1.

Example:

Original:

\[
00101100
\]

One's complement:

\[
11010011
\]

Add 1:

\[
11010100
\]

Therefore:

\[
\boxed{\text{Two's complement}=11010100}
\]

## 14. Signed Binary Numbers

An \(n\)-bit signed two's-complement number has the range:

\[
\boxed{-2^{n-1}\text{ to }2^{n-1}-1}
\]

For 8 bits:

\[
-128\text{ to }127
\]

The most significant bit indicates the sign in the usual two's-complement interpretation:

- 0 represents a non-negative number.
- 1 represents a negative number.

### 14.1 Representing a Negative Number

To represent \(-13\) using 8-bit two's complement:

Positive 13:

\[
00001101
\]

Invert:

\[
11110010
\]

Add 1:

\[
11110011
\]

Therefore:

\[
\boxed{-13=11110011_2}
\]

in 8-bit two's-complement representation.

## 15. Binary Overflow

Overflow occurs when an arithmetic result cannot be represented within the available number of bits.

For unsigned addition, a carry beyond the most significant bit indicates that the result exceeds the available range.

For signed two's-complement addition, overflow occurs when:

- Two positive numbers produce a negative result, or
- Two negative numbers produce a positive result.

A carry out alone does not determine signed overflow.

## 16. Worked Numerical Examples

### Example 1: Decimal to Binary and Hexadecimal

**Given:**

\[
(156)_{10}
\]

Convert into binary and hexadecimal.

**Solution:**

Binary conversion:

\[
156=128+16+8+4
\]

Therefore:

\[
156=10011100_2
\]

Group into four bits:

\[
1001\ 1100
\]

\[
1001=9,\quad1100=C
\]

Therefore:

\[
156=9C_{16}
\]

**Final Answer:**

\[
\boxed{156_{10}=10011100_2=9C_{16}}
\]

### Example 2: Two's-Complement Subtraction

**Given:**

\[
25-9
\]

Perform the subtraction using 8-bit two's complement.

**Solution:**

Represent 25:

\[
00011001
\]

Represent 9:

\[
00001001
\]

Take the two's complement of 9:

One's complement:

\[
11110110
\]

Add 1:

\[
11110111
\]

Add to 25:

\[
\begin{array}{r}
00011001\\
+11110111\\
\hline
00010000
\end{array}
\]

Discard the carry beyond eight bits.

**Final Answer:**

\[
\boxed{00010000_2=16_{10}}
\]

### Example 3: Signed Number Range

**Given:**

An 8-bit signed two's-complement representation.

Determine its minimum and maximum values.

**Formula:**

\[
-2^{n-1}\text{ to }2^{n-1}-1
\]

**Solution:**

For \(n=8\):

\[
-2^7\text{ to }2^7-1
\]

\[
-128\text{ to }127
\]

**Final Answer:**

\[
\boxed{-128\text{ to }127}
\]

## 17. Practical Applications

Binary and hexadecimal representations are used in:

- Processor instructions.
- Digital memory.
- Microcontroller programming.
- Machine-level data representation.
- Network addresses.
- Digital communication.
- Logic circuit design.
- Embedded systems.

Hexadecimal is especially useful because it represents four binary bits with one digit, making long binary values easier to read.

## 18. Common Examination Traps

1. Binary uses only 0 and 1.
2. The rightmost binary position represents \(2^0\).
3. Each hexadecimal digit corresponds to four binary bits.
4. Each octal digit corresponds to three binary bits.
5. Binary fractions use negative powers of 2.
6. The two's complement is the one's complement plus 1.
7. The 8-bit unsigned range is 0 to 255.
8. The 8-bit signed two's-complement range is -128 to 127.
9. Unsigned carry and signed overflow are not identical.
10. Hexadecimal A represents decimal 10.
11. Hexadecimal F represents decimal 15.
12. Leading zeros may be added to complete binary groups without changing the number.
13. Two's-complement subtraction is performed by adding the two's complement of the subtrahend.
14. The most significant bit has a negative weight in signed two's-complement representation.

## Quiz

1. What is the decimal equivalent of \(10110_2\)?

- [ ] 18.
- [x] 22.
- [ ] 24.
- [ ] 26.

> \(10110_2=1(16)+0(8)+1(4)+1(2)+0(1)=22\).

2. How many binary bits correspond to one hexadecimal digit?

- [ ] 2.
- [ ] 3.
- [x] 4.
- [ ] 8.

> Hexadecimal has base 16, and \(16=2^4\). Therefore, each hexadecimal digit represents exactly four binary bits.

3. What is the 8-bit two's-complement representation of -5?

- [ ] 00000101.
- [ ] 11111010.
- [x] 11111011.
- [ ] 10000101.

> Positive 5 is 00000101. Invert the bits to obtain 11111010, then add 1 to obtain 11111011.
