---
title: Sorting Algorithms
level: intermediate
---

Sorting algorithms arrange data in a specified order, usually ascending or descending. Sorting is an important operation in computer science because organized data can make searching, analysis, and information processing more efficient.

## 1. Understanding Sorting

Sorting is the process of arranging elements according to a defined ordering rule.

Examples:

Ascending order:

```text
[2, 5, 8, 12, 19]
```

Descending order:

```text
[19, 12, 8, 5, 2]
```

Sorting can be performed on:
- Numbers.
- Names.
- Dates.
- Records.
- Objects with comparable attributes.

## 2. Bubble Sort

Bubble sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

The process continues until the collection is sorted.

Example:

```text
Initial: [5, 3, 8, 2]

Pass 1:   [3, 5, 2, 8]
Pass 2:   [3, 2, 5, 8]
Pass 3:   [2, 3, 5, 8]
```

The largest unsorted element moves toward the end during each pass.

## 3. Bubble Sort Algorithm

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
```

An optimized implementation can stop early if a complete pass performs no swaps.

## 4. Bubble Sort Complexity

| Case | Time Complexity |
| --- | --- |
| Best Case with Early Exit | O(n) |
| Average Case | O(n squared) |
| Worst Case | O(n squared) |
| Space Complexity | O(1) |

Bubble sort is simple but inefficient for large collections.

## 5. Selection Sort

Selection sort repeatedly identifies the smallest element in the unsorted portion and places it at the beginning of that portion.

Example:

```text
Initial: [29, 10, 14, 37]

Pass 1:   [10, 29, 14, 37]
Pass 2:   [10, 14, 29, 37]
Pass 3:   [10, 14, 29, 37]
```

Each pass places one element in its correct position.

## 6. Selection Sort Algorithm

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
```

Selection sort performs repeated minimum-element selection.

## 7. Selection Sort Complexity

| Case | Time Complexity |
| --- | --- |
| Best Case | O(n squared) |
| Average Case | O(n squared) |
| Worst Case | O(n squared) |
| Space Complexity | O(1) |

Selection sort performs relatively few swaps, but its comparison count remains quadratic.

## 8. Insertion Sort

Insertion sort builds a sorted portion of the collection one element at a time.

Each new element is inserted into its appropriate position among the previously sorted elements.

Example:

```text
Initial: [5, 2, 4, 1]

Step 1:   [2, 5, 4, 1]
Step 2:   [2, 4, 5, 1]
Step 3:   [1, 2, 4, 5]
```

It is particularly useful for small or nearly sorted collections.

## 9. Insertion Sort Algorithm

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
```

The algorithm shifts larger elements to create space for the current element.

## 10. Insertion Sort Complexity

| Case | Time Complexity |
| --- | --- |
| Best Case | O(n) |
| Average Case | O(n squared) |
| Worst Case | O(n squared) |
| Space Complexity | O(1) |

Insertion sort performs well when the input is already or nearly sorted.

## 11. Merge Sort

Merge sort is a divide-and-conquer sorting algorithm.

It divides the collection into smaller parts, sorts those parts, and merges them into a final sorted collection.

Main stages:

1. Divide the collection into halves.
2. Continue dividing until individual elements remain.
3. Merge smaller sorted collections.
4. Continue merging until the complete collection is sorted.

Merge sort has O(n log n) time complexity in its best, average, and worst cases.

Its standard array implementation requires O(n) auxiliary space.

## 12. Quick Sort

Quick sort is another divide-and-conquer sorting algorithm.

It selects a pivot element and partitions the collection so that smaller elements are placed on one side and larger elements on the other, according to the chosen partition scheme.

The algorithm then recursively sorts the resulting partitions.

Complexities:

- Best Case: O(n log n).
- Average Case: O(n log n).
- Worst Case: O(n squared).

The worst case can occur when partitions become highly unbalanced.

Quick sort is commonly implemented in-place, although recursive calls require additional stack space.

## 13. Heap Sort

Heap sort uses a binary heap to organize elements.

A max-heap places the largest value at its root.

The algorithm repeatedly:
1. Builds a max-heap.
2. Moves the largest element to the end.
3. Reduces the heap's active size.
4. Restores the heap property.

Its best, average, and worst-case time complexities are O(n log n).

Heap sort uses O(1) auxiliary array space in its standard iterative implementation.

## 14. Comparison of Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
| --- | --- | --- | --- |
| Bubble Sort | O(n) with early exit | O(n squared) | O(n squared) |
| Selection Sort | O(n squared) | O(n squared) | O(n squared) |
| Insertion Sort | O(n) | O(n squared) | O(n squared) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n squared) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |

## 15. Stable and Unstable Sorting

A stable sorting algorithm preserves the relative order of elements that have equal sorting keys.

For example, suppose two records have the same score but different names.

A stable sorting algorithm preserves their original relative order.

Common stable algorithms include:
- Bubble sort.
- Insertion sort.
- Merge sort in its standard stable implementation.

Common unstable algorithms include:
- Selection sort.
- Heap sort.
- Quick sort in its common in-place implementation.

Stability matters when sorting records using multiple fields.

## 16. In-Place Sorting

An in-place sorting algorithm performs its main work within the original collection and uses relatively little additional memory.

Examples include:
- Selection sort.
- Insertion sort.
- Heap sort.

Merge sort generally requires additional memory for array-based merging.

## 17. Choosing the Right Sorting Algorithm

- Bubble sort is useful mainly for learning sorting fundamentals.
- Selection sort is useful when minimizing swaps is important.
- Insertion sort works well for small or nearly sorted collections.
- Merge sort provides predictable O(n log n) performance.
- Quick sort is commonly efficient for practical general-purpose sorting.
- Heap sort guarantees O(n log n) time with low auxiliary array memory.

## Common Exam Traps

- Bubble sort compares adjacent elements.
- Selection sort repeatedly selects the smallest remaining element.
- Insertion sort builds a sorted portion incrementally.
- Merge sort follows divide-and-conquer.
- Quick sort uses a pivot and partitioning.
- Heap sort uses a binary heap.
- Merge sort has O(n log n) worst-case time complexity.
- Quick sort can have O(n squared) worst-case time complexity.
- Stability concerns the relative order of equal-key elements.
- In-place sorting concerns additional memory usage.

## Quiz

1. Which sorting algorithm repeatedly compares adjacent elements?
   - [ ] Selection sort
   - [x] Bubble sort
   - [ ] Merge sort
   - [ ] Heap sort

   > Bubble sort compares neighbouring elements and swaps them when necessary.

2. Which sorting algorithm follows the divide-and-conquer approach by dividing and merging sorted portions?
   - [ ] Insertion sort
   - [ ] Selection sort
   - [x] Merge sort
   - [ ] Bubble sort

   > Merge sort divides the collection into smaller parts and merges the sorted results.

3. What is the worst-case time complexity of standard quick sort?
   - [ ] O(1)
   - [ ] O(log n)
   - [ ] O(n log n)
   - [x] O(n squared)

   > Highly unbalanced partitions can cause quick sort to perform quadratic work.