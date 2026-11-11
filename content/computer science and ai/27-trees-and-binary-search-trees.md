---
title: Trees and Binary Search Trees
level: intermediate
---

Trees are non-linear data structures used to represent hierarchical relationships. They are widely used in databases, file systems, compilers, artificial intelligence, and searching algorithms.

## 1. Understanding Trees

A tree consists of nodes connected through edges.

A tree begins with a special node called the root.

Example:

```text
             A
           /   \
          B     C
         / \     \
        D   E     F
```

This structure represents a hierarchy.

## 2. Tree Terminology

Important tree terminology includes:

| Term | Meaning |
| --- | --- |
| Root | The topmost node |
| Parent | A node with one or more children |
| Child | A node connected below another node |
| Sibling | Nodes sharing the same parent |
| Leaf | A node without children |
| Edge | A connection between two nodes |
| Ancestor | A node above another node in the hierarchy |
| Descendant | A node below another node |
| Subtree | A tree formed from a node and its descendants |
| Depth | Number of edges from the root to a node |
| Height | Maximum number of edges from a node to a leaf |

## 3. Properties of Trees

A tree with n nodes has exactly n - 1 edges, provided it is a connected, non-empty tree.

Other important properties:

- Every node except the root has exactly one parent in a rooted tree.
- A tree contains no cycles.
- There is exactly one simple path between any two nodes.
- A leaf has no children.

## 4. Binary Trees

A binary tree is a tree in which each node has at most two children.

The two children are commonly called:
- Left child.
- Right child.

Example:

```text
        10
       /  \
      5    15
     / \
    2   8
```

## 5. Types of Binary Trees

### Full Binary Tree

Every node has either zero or two children.

### Complete Binary Tree

All levels are completely filled except possibly the last level, which is filled from left to right.

### Perfect Binary Tree

Every internal node has exactly two children, and all leaves occur at the same depth.

### Balanced Binary Tree

A balanced tree maintains controlled height so that important operations remain efficient.

### Skewed Binary Tree

A skewed tree has nodes arranged primarily along one side, resembling a linked list.

## 6. Binary Search Trees

A Binary Search Tree, or BST, is a binary tree that maintains an ordering property.

For a BST using distinct keys:

- Values in the left subtree are smaller than the node's value.
- Values in the right subtree are greater than the node's value.
- Both subtrees must also satisfy the BST property.

Example:

```text
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

## 7. Searching in a Binary Search Tree

Searching begins at the root.

1. Compare the target with the current node.
2. If equal, the value is found.
3. If smaller, move to the left child.
4. If greater, move to the right child.
5. Continue until the value is found or a null reference is reached.

A balanced BST can support searching in O(log n) time.

An unbalanced BST can require O(n) time in the worst case.

## 8. Insertion in a BST

Insertion places a new value in a position that preserves the BST ordering property.

Example: Insert 45 into the tree containing 50, 30, and 70.

- 45 is smaller than 50, so move left.
- 45 is greater than 30, so move right.
- Insert 45 at the available position.

The resulting structure preserves the BST property.

## 9. Deletion in a BST

Deleting a node involves three main cases.

### Case 1: Leaf Node

A node with no children can be removed directly.

### Case 2: One Child

The node is replaced by its only child.

### Case 3: Two Children

The node is replaced using an appropriate value, commonly its inorder successor or inorder predecessor.

The remaining links are adjusted to preserve the BST property.

## 10. Tree Traversal

Traversal means visiting every node according to a particular order.

### Preorder Traversal

Order:

1. Root.
2. Left subtree.
3. Right subtree.

### Inorder Traversal

Order:

1. Left subtree.
2. Root.
3. Right subtree.

For a BST, inorder traversal produces values in sorted order when the tree uses distinct keys and the standard ordering property.

### Postorder Traversal

Order:

1. Left subtree.
2. Right subtree.
3. Root.

### Level-Order Traversal

Visits nodes level by level, generally using a queue.

## 11. Traversal Example

Consider:

```text
        10
       /  \
      5    15
     / \
    2   8
```

The traversal results are:

| Traversal | Result |
| --- | --- |
| Preorder | 10, 5, 2, 8, 15 |
| Inorder | 2, 5, 8, 10, 15 |
| Postorder | 2, 8, 5, 15, 10 |
| Level Order | 10, 5, 15, 2, 8 |

## 12. Applications of Trees

Trees are used in:

- File-system organization.
- Database indexing.
- Expression parsing.
- Decision-making systems.
- Search applications.
- Hierarchical data representation.
- Artificial intelligence search.
- Syntax trees in compilers.

## Common Exam Traps

- A tree with n nodes has n - 1 edges.
- A leaf has no children.
- A binary tree allows at most two children per node.
- A BST maintains an ordering relationship between left and right subtrees.
- Inorder traversal of a standard BST produces sorted values.
- A balanced BST has better worst-case search performance than an ordinary unbalanced BST.
- A skewed BST can have O(n) search time.

## Quiz

1. How many edges does a tree with 10 nodes contain?
   - [ ] 10
   - [x] 9
   - [ ] 11
   - [ ] 20

   > A connected tree with n nodes contains n - 1 edges.

2. Which traversal of a standard Binary Search Tree produces sorted values?
   - [ ] Preorder
   - [ ] Postorder
   - [x] Inorder
   - [ ] Level order

   > Inorder traversal visits the left subtree, root, and right subtree.

3. What is the worst-case search complexity of an unbalanced BST?
   - [ ] O(1)
   - [ ] O(log n)
   - [x] O(n)
   - [ ] O(n log n)

   > A highly skewed BST may require examining every node.