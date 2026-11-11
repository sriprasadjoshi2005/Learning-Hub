---
title: Algorithm Analysis and Big O Notation
level: advanced
---

Algorithm analysis is the study of an algorithm's efficiency in terms of execution time and memory usage. It helps developers compare different solutions and select algorithms that perform well as input sizes increase.

## 1. Understanding Algorithm Analysis

An algorithm is a finite sequence of well-defined instructions used to solve a problem.

Two algorithms may produce the same result but require different amounts of time and memory.

Algorithm analysis evaluates these differences.

The two major measures are:

- Time complexity: Describes how the number of operations grows with input size.
- Space complexity: Describes how memory requirements grow with input size.

## 2. Input Size

Input size represents the amount of data processed by an algorithm.

It is commonly represented by n.

Examples:

- For an array, n may represent the number of elements.
- For a string, n may represent the number of characters.
- For a graph, V may represent vertices and E may represent edges.
- For a matrix, n may represent its dimensions.

The choice of input-size variable depends on the problem.

## 3. Time Complexity

Time complexity describes how the number of computational operations changes as the input size increases.

It does not necessarily represent the actual time measured in seconds.

Example:

```python
def display_values(values):
    for value in values:
        print(value)
```

If the collection contains n elements, the loop executes n times.

Its time complexity is O(n).

## 4. Best, Average and Worst Cases

An algorithm may perform differently depending on the input.

### Best Case

The minimum amount of work required for an input of a particular size.

For linear search, the best case occurs when the target is the first element.

### Average Case

The expected amount of work over a specified distribution of inputs.

For linear search under a common uniform-position assumption, the average number of comparisons grows proportionally to n.

### Worst Case

The maximum amount of work required for an input of a particular size.

For linear search, the worst case occurs when the target is at the end or is absent.

## 5. Asymptotic Notations

Asymptotic notation describes algorithm growth as input size becomes large.

### Big O Notation

Big O provides an asymptotic upper bound on a function's growth.

It is commonly used to express worst-case complexity.

Example:

An algorithm that performs approximately 3n + 5 operations has O(n) complexity.

### Big Omega Notation

Big Omega provides an asymptotic lower bound.

It describes a growth rate that an algorithm or function does not fall below, under the stated conditions.

### Big Theta Notation

Big Theta provides a tight asymptotic bound.

A function belongs to Theta(n) when its growth is bounded both above and below by constant multiples of n for sufficiently large n.

## 6. Common Complexity Classes

| Complexity | Name | Example |
| --- | --- | --- |
| O(1) | Constant | Accessing an array element by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n squared) | Quadratic | Basic nested-loop comparison |
| O(n cubed) | Cubic | Certain triple-nested loops |
| O(2^n) | Exponential | Brute-force subset enumeration |
| O(n!) | Factorial | Generating all permutations |

These classes describe growth rates, not exact execution times.

## 7. Analysing Loops

A single loop that processes n elements commonly has O(n) complexity.

Example:

```python
for i in range(n):
    print(i)
```

Two independent nested loops, each running n times, commonly produce O(n squared) complexity.

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The inner statement executes n multiplied by n times.

## 8. Consecutive Loops

Consider:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

The total number of iterations is 2n.

Its complexity is O(n), because constant factors are ignored in asymptotic analysis.

## 9. Logarithmic Complexity

An algorithm has logarithmic complexity when its problem size is repeatedly reduced by a constant factor.

Example:

```python
while n > 1:
    n = n // 2
```

The number of iterations grows approximately as log base 2 of n.

Binary search follows this general pattern.

## 10. Space Complexity

Space complexity describes the memory required by an algorithm.

It may include:

- Input storage.
- Auxiliary data structures.
- Temporary variables.
- Recursive call-stack memory.
- Output storage, depending on the analysis convention.

Example:

```python
def calculate_sum(values):
    total = 0

    for value in values:
        total += value

    return total
```

The algorithm uses a constant amount of additional working memory, excluding the input.

Its auxiliary space complexity is O(1).

## 11. Recursive Complexity

Recursive algorithms require analysis of both repeated operations and function calls.

Example:

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

The function makes n recursive calls up to a constant difference.

Its time complexity is O(n), and its recursive stack space is O(n).

## 12. Comparing Algorithms

Suppose two algorithms solve the same problem.

- Algorithm A takes O(n) time.
- Algorithm B takes O(n squared) time.

For small inputs, their performance may appear similar.

As n increases, the quadratic algorithm generally requires much more work.

This is why algorithmic efficiency becomes increasingly important for large datasets.

## 13. Amortized Analysis

Amortized analysis studies the average cost of operations over a sequence of operations, without relying on a probability distribution.

For example, dynamic arrays occasionally resize and copy their contents.

A resizing operation may be expensive, but most insertions are inexpensive.

The amortized insertion cost is commonly O(1) for a dynamic array that grows geometrically.

## 14. Practical Considerations

Big O notation is useful, but it does not describe every performance factor.

Actual execution can also depend on:

- Hardware.
- Programming language.
- Compiler optimizations.
- Memory access patterns.
- Data distribution.
- Implementation details.
- Constant factors.

Algorithm analysis provides a theoretical foundation, while benchmarking measures practical performance.

## Common Exam Traps

- Big O represents an asymptotic upper bound, not an exact operation count.
- Big Omega represents a lower bound.
- Big Theta represents a tight bound.
- Constant factors are ignored in asymptotic simplification.
- Two consecutive O(n) loops still produce O(n) complexity.
- Two nested loops commonly produce O(n squared) complexity.
- Repeatedly halving a problem commonly produces O(log n) complexity.
- Recursive algorithms may require additional call-stack memory.
- Time complexity and space complexity measure different resources.

## Quiz

1. What is the time complexity of two consecutive loops, each executing n times?
   - [ ] O(1)
   - [x] O(n)
   - [ ] O(n squared)
   - [ ] O(log n)

   > The total work is 2n, and constant factors are ignored, giving O(n).

2. Which notation represents a tight asymptotic bound?
   - [ ] Big O
   - [ ] Big Omega
   - [x] Big Theta
   - [ ] Big Delta

   > Big Theta bounds a function both above and below asymptotically.

3. What is the auxiliary space complexity of a recursive factorial implementation with n recursive calls?
   - [ ] O(1)
   - [ ] O(log n)
   - [x] O(n)
   - [ ] O(n squared)

   > Each recursive call occupies space on the call stack, producing linear stack usage.