---
title: Searching Algorithms
level: intermediate
---

Searching algorithms are methods used to locate specific information within a collection of data. They are essential in databases, information retrieval, software applications, and artificial intelligence.

## 1. Understanding Searching

Searching is the process of determining whether a target element exists in a collection and identifying its position when found.

Examples include:
- Finding a student record.
- Locating a word in a dictionary.
- Searching for a product.
- Finding a value in an array.
- Retrieving information from a database.

A searching algorithm should be selected according to the data organization and application requirements.

## 2. Linear Search

Linear search examines elements one by one until the target is found or the collection is exhausted.

It does not require the data to be sorted.

Example:

Consider the array:

```text
[12, 25, 8, 40, 17]
```

Search for 40.

Steps:

1. Compare 40 with 12.
2. Compare 40 with 25.
3. Compare 40 with 8.
4. Compare 40 with 40.
5. The target is found.

## 3. Linear Search Algorithm

```python
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
```

The algorithm returns the index of the target or -1 if it is absent.

## 4. Linear Search Complexity

| Case | Time Complexity |
| --- | --- |
| Best Case | O(1) |
| Average Case | O(n) |
| Worst Case | O(n) |
| Space Complexity | O(1) |

The best case occurs when the target is the first element.

The worst case occurs when the target is last or absent.

## 5. Binary Search

Binary search is an efficient searching algorithm that repeatedly divides the search interval into two halves.

It requires the data to be sorted.

Example:

```text
[10, 20, 30, 40, 50, 60, 70]
```

Search for 60.

Steps:

1. Examine the middle element, 40.
2. Since 60 is greater than 40, discard the left half.
3. Examine the middle of the remaining interval.
4. Compare 60 with 60.
5. The target is found.

## 6. Binary Search Algorithm

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

The algorithm repeatedly narrows the search interval.

## 7. Binary Search Complexity

| Case | Time Complexity |
| --- | --- |
| Best Case | O(1) |
| Average Case | O(log n) |
| Worst Case | O(log n) |
| Iterative Space Complexity | O(1) |

Binary search is efficient because it eliminates approximately half of the remaining search interval at each step.

## 8. Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
| --- | --- | --- |
| Data Requirement | Sorted or unsorted | Sorted |
| Search Method | Sequential | Repeated halving |
| Best Time | O(1) | O(1) |
| Worst Time | O(n) | O(log n) |
| Implementation | Simple | Requires interval management |
| Suitable For | Small or unsorted collections | Large sorted collections |

## 9. Recursive Binary Search

Binary search can also be implemented recursively.

Example:

```python
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, target)

    return binary_search_recursive(arr, mid + 1, high, target)
```

Recursive binary search repeatedly calls itself with a smaller search interval.

Its time complexity is O(log n), while its auxiliary space complexity is O(log n) because of recursive calls.

## 10. Hash-Based Searching

Hash-based searching uses a hash function to transform a key into an index or location in a hash table.

A hash table stores information using key-value associations or indexed buckets.

Average-case search time is commonly O(1), assuming a suitable hash function and effective collision management.

However, the worst-case search time can be O(n) when many keys collide.

## 11. Hash Collisions

A collision occurs when two different keys produce the same hash-table index.

Common collision-resolution methods include:

### Separate Chaining

Each table position stores a collection of elements that share the same index.

### Open Addressing

When a position is occupied, the algorithm searches for another available position.

Common techniques include:
- Linear probing.
- Quadratic probing.
- Double hashing.

## 12. Choosing a Searching Algorithm

- Use linear search for small or unsorted collections.
- Use binary search when data is sorted and efficient searching is required.
- Use hash tables for frequent key-based retrieval.
- Consider preprocessing costs when sorting data before searching.

## Common Exam Traps

- Linear search does not require sorted data.
- Binary search requires sorted data.
- Binary search has O(log n) worst-case time complexity.
- Linear search has O(n) worst-case time complexity.
- Hash tables offer average-case O(1) searching, not guaranteed O(1) in every case.
- Recursive binary search uses additional call-stack memory.
- Hash collisions occur when different keys map to the same location.

## Quiz

1. Which searching algorithm requires sorted data?
   - [ ] Linear search
   - [x] Binary search
   - [ ] Sequential search
   - [ ] Unordered traversal

   > Binary search depends on sorted data to eliminate half of the search interval at each step.

2. What is the worst-case time complexity of linear search?
   - [ ] O(1)
   - [ ] O(log n)
   - [x] O(n)
   - [ ] O(n log n)

   > Linear search may need to examine every element.

3. What is a hash collision?
   - [ ] When a file cannot be opened
   - [ ] When an array becomes full
   - [x] When different keys map to the same hash-table location
   - [ ] When an algorithm sorts data incorrectly

   > A collision occurs when multiple keys produce the same hash-table index.