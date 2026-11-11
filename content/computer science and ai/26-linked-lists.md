---
title: Linked Lists
level: intermediate
---

A linked list is a dynamic linear data structure consisting of nodes connected through references or pointers. Unlike arrays, linked-list elements do not need to occupy consecutive memory locations.

## 1. Understanding Linked Lists

A linked list is made up of individual nodes.

Each node commonly contains:
- Data: The information stored in the node.
- Link: A reference to another node.

The first node is called the head.

The final node generally contains a link indicating that there is no next node.

Example:

```text
Head
 |
 v
[10 | Next] -> [20 | Next] -> [30 | None]
```

Each node stores a value and a reference to the next node.

## 2. Node Structure

A node contains data and one or more links.

In a singly linked list, a node contains:
- Data.
- A reference to the next node.

Example using Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

A linked list can be constructed by connecting nodes together.

## 3. Types of Linked Lists

### Singly Linked List

Each node points to the next node.

Traversal normally occurs in one direction.

```text
10 -> 20 -> 30 -> None
```

### Doubly Linked List

Each node contains references to both the previous and next nodes.

```text
None <- 10 <-> 20 <-> 30 -> None
```

This allows traversal in both directions.

### Circular Singly Linked List

The final node points back to the first node.

```text
10 -> 20 -> 30
^           |
|___________|
```

There is no ordinary null link at the end of the circular structure.

### Circular Doubly Linked List

Each node has previous and next references, and the first and final nodes are connected in both directions.

## 4. Traversal

Traversal means visiting nodes sequentially to process their data.

Example:

```python
current = head

while current is not None:
    print(current.data)
    current = current.next
```

The traversal begins at the head and continues until the end of the list.

## 5. Insertion

Insertion adds a new node to a linked list.

Common insertion positions include:

- At the beginning.
- At the end.
- At a specified position.
- After a selected node.

Insertion at the beginning generally requires updating the head reference.

For insertion after a node, the new node's link must be connected to the appropriate next node.

## 6. Deletion

Deletion removes a node from the linked list.

Common deletion operations include:

- Removing the first node.
- Removing the final node.
- Removing a node containing a specific value.
- Removing a node at a particular position.

Deleting a node requires updating the relevant links so that the remaining nodes stay connected.

## 7. Searching

Searching checks whether a particular value exists in the linked list.

A typical search begins at the head and examines each node.

In a general unsorted singly linked list, searching requires O(n) time in the worst case.

## 8. Time Complexity

Typical complexities for a singly linked list are:

| Operation | Time Complexity |
| --- | --- |
| Access by position | O(n) |
| Search | O(n) |
| Insert at beginning | O(1) |
| Delete at beginning | O(1) |
| Insert at end | O(n) without a tail reference |
| Insert after a known node | O(1) |

A tail reference can improve insertion at the end to O(1), provided the list maintains it correctly.

## 9. Linked Lists vs Arrays

| Feature | Array | Linked List |
| --- | --- | --- |
| Memory Arrangement | Typically contiguous | Nodes may be scattered |
| Indexed Access | O(1) | O(n) |
| Insertion at Beginning | Usually O(n) | O(1) |
| Deletion at Beginning | Usually O(n) | O(1) |
| Extra Memory | Usually lower | Required for links |
| Resizing | May require allocation | Nodes can be added dynamically |

## 10. Advantages and Limitations

### Advantages

- Dynamic size.
- Efficient insertion and deletion at known positions.
- Does not require contiguous memory.
- Useful for implementing other data structures.

### Limitations

- No direct indexed access.
- Extra memory is required for links.
- Searching can be slow.
- Pointer or reference management can be complicated.
- Traversal generally requires sequential movement.

## 11. Applications

Linked lists are useful in:

- Implementing stacks and queues.
- Managing playlists.
- Representing sequences of changing length.
- Maintaining certain memory-management structures.
- Implementing adjacency lists in graphs.
- Navigating between connected records.

## Common Exam Traps

- The first node is called the head.
- A singly linked list normally supports traversal in one direction.
- A doubly linked list stores previous and next references.
- A circular linked list connects its final node back to the beginning.
- Indexed access in a linked list is generally O(n).
- Insertion at the beginning of a singly linked list is O(1).

## Quiz

1. What is the first node of a linked list called?
   - [ ] Tail
   - [ ] Root
   - [x] Head
   - [ ] Parent

   > The head stores the reference to the first node.

2. Which linked list supports traversal in both directions?
   - [ ] Singly linked list
   - [ ] Simple array
   - [x] Doubly linked list
   - [ ] Linear queue

   > A doubly linked list stores references to both previous and next nodes.

3. What is the typical time complexity of searching an unsorted singly linked list?
   - [ ] O(1)
   - [ ] O(log n)
   - [x] O(n)
   - [ ] O(n squared)

   > In the worst case, every node must be examined.