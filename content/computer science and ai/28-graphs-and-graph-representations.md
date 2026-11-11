---
title: Graphs and Graph Representations
level: intermediate
---

A graph is a non-linear data structure consisting of vertices and edges. Graphs represent relationships and connections between entities and are fundamental to networking, transportation, social media, artificial intelligence, and optimization.

## 1. Understanding Graphs

A graph is commonly represented as:

G = (V, E)

Where:

- V represents the set of vertices.
- E represents the set of edges.

Vertices represent entities, while edges represent relationships between them.

Example:

```text
A ----- B
|       |
|       |
C ----- D
```

Here, A, B, C, and D are vertices, while the connecting lines are edges.

## 2. Graph Terminology

| Term | Meaning |
| --- | --- |
| Vertex | A node in a graph |
| Edge | A connection between vertices |
| Adjacent Vertices | Vertices directly connected by an edge |
| Degree | Number of edges connected to a vertex in an undirected graph |
| Path | Sequence of connected vertices |
| Cycle | A path that begins and ends at the same vertex |
| Connected Graph | A graph in which every pair of vertices has a path between them |
| Subgraph | A graph formed from a subset of vertices and edges |

## 3. Directed and Undirected Graphs

### Undirected Graph

An undirected graph has edges without a specified direction.

If A is connected to B, the connection can be traversed in both directions.

Example:

```text
A ----- B
```

### Directed Graph

A directed graph contains edges with specific directions.

Example:

```text
A ----> B
```

The edge permits movement from A to B, but not necessarily from B to A.

Directed graphs are also called digraphs.

## 4. Weighted and Unweighted Graphs

### Weighted Graph

A weighted graph assigns a numerical value to each edge.

Weights may represent:
- Distance.
- Cost.
- Time.
- Network latency.
- Connection strength.

Example:

```text
A --5-- B
B --3-- C
A --8-- C
```

### Unweighted Graph

An unweighted graph treats edges as connections without numerical weights.

## 5. Graph Representations

Graphs can be represented using different data structures.

### Adjacency Matrix

An adjacency matrix is a two-dimensional array in which rows and columns represent vertices.

Example:

```text
    A B C
A   0 1 1
B   1 0 1
C   1 1 0
```

A value of 1 indicates an edge, while 0 indicates no edge in this unweighted example.

For an undirected graph, the adjacency matrix is symmetric.

Advantages:
- Checking whether an edge exists is O(1).
- Simple representation.
- Useful for dense graphs.

Limitations:
- Requires O(V squared) space.
- Can waste memory for sparse graphs.

### Adjacency List

An adjacency list stores the neighbours of each vertex.

Example:

```text
A: B, C
B: A, C
C: A, B
```

Advantages:
- Efficient memory usage for sparse graphs.
- Convenient for visiting neighbours.
- Commonly used in graph algorithms.

Its space requirement is generally O(V + E).

## 6. Graph Traversal

Graph traversal is the process of visiting vertices in a systematic manner.

Two important traversal algorithms are:

- Breadth-First Search.
- Depth-First Search.

## 7. Breadth-First Search

Breadth-First Search, or BFS, explores a graph level by level.

It generally uses a queue.

Basic procedure:

1. Start from a selected vertex.
2. Mark it as visited.
3. Insert it into a queue.
4. Remove a vertex from the queue.
5. Visit its unvisited neighbours.
6. Insert newly visited neighbours into the queue.
7. Repeat until the queue is empty.

BFS can find shortest paths in unweighted graphs when the graph is traversed appropriately.

Its time complexity using an adjacency list is O(V + E).

## 8. Depth-First Search

Depth-First Search, or DFS, explores as far as possible along one path before backtracking.

It can be implemented using:
- Recursion.
- An explicit stack.

Basic procedure:

1. Start from a selected vertex.
2. Mark it as visited.
3. Visit an unvisited neighbour.
4. Continue deeper into the graph.
5. Backtrack when no unvisited neighbour remains.
6. Continue until all reachable vertices have been processed.

Its time complexity using an adjacency list is O(V + E).

## 9. BFS vs DFS

| Feature | BFS | DFS |
| --- | --- | --- |
| Exploration | Level by level | Depth first |
| Main Structure | Queue | Stack or recursion |
| Shortest Path | Finds shortest paths in unweighted graphs | Does not generally guarantee shortest paths |
| Memory | May store a wide frontier | Depends on traversal depth and branching |
| Applications | Shortest paths, level exploration | Cycle detection, backtracking, connectivity |

## 10. Shortest Path Algorithms

Several algorithms solve shortest-path problems.

### Dijkstra's Algorithm

Finds shortest paths from a source vertex when edge weights are non-negative.

It is commonly implemented using a priority queue.

### Bellman-Ford Algorithm

Finds shortest paths even when some edge weights are negative, provided no reachable negative-weight cycle makes the shortest path undefined.

### Floyd-Warshall Algorithm

Computes shortest paths between all pairs of vertices.

It uses dynamic programming and has O(V cubed) time complexity in its standard form.

## 11. Minimum Spanning Trees

A spanning tree connects every vertex in a connected undirected graph without forming cycles.

A Minimum Spanning Tree, or MST, is a spanning tree with the minimum possible total edge weight.

Important algorithms include:

- Prim's Algorithm.
- Kruskal's Algorithm.

Minimum spanning trees are useful in network design and infrastructure planning.

## 12. Applications of Graphs

Graphs are used in:

- Social networks.
- Road and railway networks.
- Internet routing.
- Recommendation systems.
- Dependency management.
- Knowledge representation.
- Web page link analysis.
- Robotics and navigation.
- Artificial intelligence search.

## Common Exam Traps

- Vertices represent entities; edges represent connections.
- Directed edges have an orientation.
- Undirected graph edges do not have a specified direction.
- An adjacency matrix generally requires O(V squared) space.
- An adjacency list generally requires O(V + E) space.
- BFS uses a queue.
- DFS uses a stack or recursion.
- Dijkstra's algorithm requires non-negative edge weights.
- A minimum spanning tree contains no cycles and connects all vertices.

## Quiz

1. Which data structure is commonly used by Breadth-First Search?
   - [ ] Stack
   - [x] Queue
   - [ ] Hash table
   - [ ] Binary search tree

   > BFS explores vertices level by level using a queue.

2. Which graph representation generally uses O(V + E) space?
   - [ ] Adjacency matrix
   - [x] Adjacency list
   - [ ] Sorted array
   - [ ] Binary heap

   > An adjacency list stores vertices and their corresponding connections.

3. Which algorithm finds shortest paths with non-negative edge weights?
   - [ ] Kruskal's Algorithm
   - [ ] DFS
   - [x] Dijkstra's Algorithm
   - [ ] Prim's Algorithm

   > Dijkstra's algorithm computes shortest paths from a source when all edge weights are non-negative.