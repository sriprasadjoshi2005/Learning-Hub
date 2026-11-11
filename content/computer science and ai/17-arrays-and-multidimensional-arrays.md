---
title: Arrays and Multidimensional Arrays
level: intermediate
---

An array is a data structure used to store a collection of elements under a common variable name. Arrays allow efficient access to elements using their positions or indices.

## 1. Meaning of an Array

An array stores multiple values in an organised sequence.

Example:

MARKS = [75, 82, 91, 68, 88]

Instead of creating five separate variables, an array stores all five values together.

Traditional arrays commonly store elements of the same data type, although some languages provide flexible array-like structures.

## 2. Array Indexing

Array indexing identifies the position of an element.

For a zero-based array:

MARKS = [75, 82, 91, 68, 88]

| Index | Value |
|---:|---:|
| 0 | 75 |
| 1 | 82 |
| 2 | 91 |
| 3 | 68 |
| 4 | 88 |

The number of elements is called the array length.

For an array with n elements using zero-based indexing, valid indices range from 0 to n - 1.

## 3. Array Traversal

Traversal means accessing each element of an array.

Pseudocode:

FOR I = 0 TO LENGTH(ARRAY) - 1
    OUTPUT ARRAY[I]
END FOR

Traversal is useful for searching, counting and calculating aggregate values.

## 4. Insertion and Deletion

**Insertion:** Adding an element to an array.

**Deletion:** Removing an element from an array.

In a fixed-size array, insertion and deletion may require shifting existing elements.

In dynamic arrays, the storage capacity may change when necessary.

## 5. Searching in Arrays

### Linear Search

Linear search checks elements sequentially until the target is found or the array ends.

Its worst-case time complexity is O(n).

### Binary Search

Binary search repeatedly divides the search interval into halves.

It requires the input array to be sorted.

Its time complexity is O(log n).

## 6. One-Dimensional Arrays

A one-dimensional array stores elements in a single sequence.

Example:

TEMPERATURE = [28, 30, 29, 31, 27]

It may represent temperature readings collected over five days.

## 7. Two-Dimensional Arrays

A two-dimensional array organises elements into rows and columns.

Example:

MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

The element at row 1 and column 2 is 6 when using zero-based indexing.

Two-dimensional arrays are commonly used to represent matrices and tables.

## 8. Multidimensional Arrays

Arrays with more than two dimensions are called multidimensional arrays.

Examples include:

- Three-dimensional scientific data.
- Image and video data.
- Simulation grids.
- Tensor representations in machine learning.

## 9. Array Operations

Common operations include:

- Accessing an element.
- Updating an element.
- Traversing the array.
- Searching for an element.
- Sorting elements.
- Inserting elements.
- Deleting elements.
- Combining arrays.

## 10. Advantages and Limitations

Advantages:

- Organised storage.
- Direct index-based access.
- Convenient traversal.
- Suitable for mathematical processing.

Limitations:

- Fixed-size arrays may have limited flexibility.
- Insertion and deletion may require shifting elements.
- Accessing invalid indices can cause errors.
- Traditional arrays generally require compatible element types.

## Common Exam Traps

- Arrays store collections of elements.
- Zero-based arrays begin at index 0.
- The last valid index is n - 1.
- Binary search requires sorted data.
- Linear search does not require sorted data.
- A two-dimensional array contains rows and columns.
- Array traversal means visiting elements systematically.

## Quiz

1. What is the last valid index of a zero-based array containing 10 elements?

- [ ] 10.
- [ ] 8.
- [x] 9.
- [ ] 11.

> A zero-based array of length 10 has indices from 0 through 9.

2. Which searching algorithm requires sorted input?

- [ ] Linear search.
- [ ] Sequential search.
- [x] Binary search.
- [ ] Unordered traversal.

> Binary search depends on sorted order to eliminate half of the remaining search interval at each step.

3. What is a two-dimensional array commonly used to represent?

- [ ] A single Boolean value.
- [ ] Only one character.
- [x] A structure of rows and columns.
- [ ] A computer network connection.

> Two-dimensional arrays organise values into a tabular arrangement of rows and columns.