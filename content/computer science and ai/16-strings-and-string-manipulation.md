---
title: Strings and String Manipulation
level: intermediate
---

A string is a sequence of characters used to represent textual information. String manipulation involves operations such as searching, comparing, extracting, joining and transforming text.

## 1. Meaning of a String

A string represents a sequence of characters.

Examples:

"Computer Science"

"Artificial Intelligence"

"Programming123"

A string may contain letters, numbers, spaces and symbols.

## 2. String Length

String length refers to the number of characters in a string according to the language's string representation.

Example:

TEXT = "COMPUTER"

LENGTH(TEXT) = 8

Some languages count Unicode characters differently depending on whether they use bytes, code points or grapheme clusters.

## 3. String Indexing

Indexing accesses individual characters using their positions.

Many programming languages use zero-based indexing.

Example:

TEXT = "HELLO"

| Index | Character |
|---:|---|
| 0 | H |
| 1 | E |
| 2 | L |
| 3 | L |
| 4 | O |

Other languages or systems may use different indexing conventions.

## 4. String Slicing

Slicing extracts a portion of a string.

Example:

TEXT = "COMPUTER"

TEXT[0:4] = "COMP"

In Python-style slicing, the starting index is included and the ending index is excluded.

## 5. String Concatenation

Concatenation joins two or more strings.

Example:

FIRST = "Computer"
SECOND = "Science"

RESULT = FIRST + " " + SECOND

Output:

Computer Science

## 6. String Comparison

String comparison determines whether two strings are equal or establishes their ordering according to the language's comparison rules.

Examples:

- Equality.
- Inequality.
- Lexicographic comparison.

Case sensitivity depends on the operation and programming language.

## 7. Common String Operations

| Operation | Purpose |
|---|---|
| LENGTH | Finds string length |
| UPPERCASE | Converts letters to uppercase |
| LOWERCASE | Converts letters to lowercase |
| CONCATENATE | Joins strings |
| SUBSTRING | Extracts part of a string |
| REPLACE | Replaces selected content |
| FIND | Locates a substring |
| SPLIT | Divides a string into parts |
| TRIM | Removes selected surrounding whitespace |

Exact function names vary between programming languages.

## 8. String Immutability

In languages with immutable strings, a string cannot be changed directly after creation.

An operation that appears to modify a string creates a new string instead.

Python strings are immutable.

For example:

TEXT = "HELLO"

TEXT = TEXT + " WORLD"

The second statement creates a new string value and assigns it to TEXT.

## 9. String Traversal

String traversal means visiting characters one by one.

Pseudocode:

TEXT = "HELLO"

FOR EACH CHARACTER IN TEXT
    OUTPUT CHARACTER
END FOR

This technique is useful for:

- Counting vowels.
- Reversing text.
- Searching for characters.
- Validating input.
- Analysing words.

## 10. Basic String Algorithms

### Counting Vowels

Pseudocode:

COUNT = 0

FOR EACH CHARACTER IN TEXT
    IF CHARACTER IS A VOWEL THEN
        COUNT = COUNT + 1
    END IF
END FOR

### Reversing a String

Pseudocode:

REVERSED = EMPTY STRING

FOR I = LENGTH(TEXT) - 1 DOWN TO 0
    REVERSED = REVERSED + TEXT[I]
END FOR

### Palindrome Checking

A palindrome is a sequence that reads the same forward and backward under a defined comparison rule.

Examples:

LEVEL

MADAM

A comparison may ignore case or spaces if the problem requires it.

## Common Exam Traps

- A string is a sequence of characters.
- String length and highest index are not necessarily equal.
- Zero-based indexing starts at index 0.
- In Python-style slicing, the ending index is excluded.
- Concatenation joins strings.
- Immutable strings cannot be modified directly.
- Palindrome checking depends on the comparison rules specified by the problem.

## Quiz

1. What is the index of the first character in a zero-based string?

- [ ] 1.
- [x] 0.
- [ ] -1.
- [ ] 2.

> Zero-based indexing assigns index 0 to the first character.

2. What is the result of concatenating "DATA" and "BASE"?

- [ ] DATA BASE only.
- [ ] DATAB.
- [x] DATABASE.
- [ ] BASEDATA.

> Concatenation joins the character sequences in the specified order.

3. Which statement describes an immutable string?

- [ ] A string that must contain only numbers.
- [ ] A string that cannot be printed.
- [x] A string that cannot be directly modified after creation.
- [ ] A string that always has zero length.

> Immutable strings cannot be altered in place; operations produce new string values instead.