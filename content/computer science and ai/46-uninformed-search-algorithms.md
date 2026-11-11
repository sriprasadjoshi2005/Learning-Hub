---
title: Uninformed Search Algorithms
level: intermediate
---

Uninformed search algorithms explore a state space without using additional information about how close a state is to the goal.

They rely on the problem definition, available actions, transition model, and goal test.

Uninformed search is also known as blind search because the algorithms do not use heuristic estimates to guide exploration.

## 1. Meaning of Uninformed Search

Uninformed search explores possible states using a predefined strategy without estimating their distance or desirability relative to the goal.

Examples include:
- Breadth-First Search.
- Depth-First Search.
- Uniform-Cost Search.
- Depth-Limited Search.
- Iterative Deepening Depth-First Search.
- Bidirectional Search.

Different algorithms explore the state space in different orders and have different completeness, optimality, time, and space properties.

## 2. Breadth-First Search (BFS)

Breadth-First Search explores nodes level by level.

It first explores the root node, then all nodes at depth 1, followed by all nodes at depth 2, and so on.

BFS uses a FIFO queue.

FIFO means First In, First Out.

**Working Procedure:**

1. Insert the initial node into a queue.
2. Remove the first node from the queue.
3. Check whether it is the goal.
4. If it is not the goal, generate its unvisited successors.
5. Add the successors to the end of the queue.
6. Repeat until a goal is found or the queue becomes empty.

**Example:**

Consider the following tree:

A → B, C

B → D, E

C → F, G

The BFS traversal order is:

A, B, C, D, E, F, G

**Properties:**
- Complete when the branching factor is finite.
- Optimal when all actions have equal cost.
- Time complexity: O(b^(d+1)).
- Space complexity: O(b^(d+1)).

Where:
- b is the branching factor.
- d is the depth of the shallowest goal.

BFS is useful when the goal is expected to be near the initial state and all actions have equal cost.

## 3. Depth-First Search (DFS)

Depth-First Search explores one branch as deeply as possible before returning to explore alternative branches.

It uses a LIFO stack or recursive function calls.

LIFO means Last In, First Out.

**Working Procedure:**

1. Insert the initial node into a stack.
2. Remove the top node.
3. Check whether it is the goal.
4. If it is not the goal, add its unvisited successors.
5. Continue exploring the deepest available branch.
6. Backtrack when a branch cannot be expanded.

**Example:**

For the tree:

A → B, C

B → D, E

C → F, G

One possible DFS traversal is:

A, B, D, E, C, F, G

The exact order depends on the order in which successors are inserted.

**Properties:**
- Not complete in infinite-depth spaces without additional safeguards.
- Not generally optimal.
- Time complexity: O(b^m).
- Space complexity: O(bm).

Where m is the maximum search depth.

DFS generally uses less memory than BFS but may explore an unnecessarily deep branch.

## 4. Uniform-Cost Search (UCS)

Uniform-Cost Search expands the node with the lowest cumulative path cost.

Unlike BFS, it considers the cost of actions rather than merely the number of steps.

UCS uses a priority queue.

**Working Procedure:**

1. Insert the initial node with path cost 0.
2. Remove the node with the lowest cumulative cost.
3. Check whether it is the goal.
4. If it is not the goal, generate successors.
5. Calculate their cumulative path costs.
6. Insert or update the successors in the priority queue.
7. Continue until the least-cost goal is selected.

**Example:**

Suppose the following routes exist:

- A → B costs 2.
- A → C costs 5.
- B → D costs 4.
- C → D costs 1.

The possible route costs are:

- A → B → D = 6.
- A → C → D = 6.

Both routes have the same minimum cost.

UCS selects nodes according to accumulated path cost.

**Properties:**
- Complete under suitable assumptions, such as a finite branching factor and a positive minimum action cost.
- Optimal when action costs are non-negative and the algorithm is implemented correctly.
- Can require substantial memory and computation.

## 5. Depth-Limited Search (DLS)

Depth-Limited Search is a modified DFS that restricts exploration to a predefined depth limit.

It prevents the algorithm from exploring infinitely deep branches.

Example:

If the depth limit is 2, the algorithm does not expand nodes beyond depth 2.

**Properties:**
- Time complexity: O(b^l).
- Space complexity: O(bl).
- Not complete if the goal is deeper than the chosen limit.
- Not generally optimal.

Here, l represents the depth limit.

## 6. Iterative Deepening Depth-First Search (IDDFS)

Iterative Deepening combines the low memory requirements of DFS with the shallow-level exploration behaviour of BFS.

It repeatedly performs depth-limited searches with increasing limits.

The search proceeds as follows:

- First search with limit 0.
- Then search with limit 1.
- Then search with limit 2.
- Continue increasing the limit until the goal is found.

**Properties:**
- Complete when the branching factor is finite.
- Optimal when all actions have equal cost.
- Time complexity: O(b^d).
- Space complexity: O(bd).

IDDFS is useful when the solution depth is unknown and memory is limited.

## 7. Bidirectional Search

Bidirectional Search performs two searches:

- Forward search from the initial state.
- Backward search from the goal state.

The algorithm attempts to find a meeting point between the two searches.

Under suitable assumptions, its search complexity can be approximately:

O(b^(d/2))

This can be significantly smaller than searching through the entire depth d from one direction.

However, bidirectional search requires:
- A clearly defined goal state.
- The ability to generate predecessor states.
- An efficient method for detecting intersection between searches.

## 8. Comparison of Uninformed Search Algorithms

| Algorithm | Main data structure | Complete? | Optimal? |
|---|---|---|---|
| BFS | FIFO queue | Yes, under finite branching | Yes, for equal step costs |
| DFS | LIFO stack | Not generally | No |
| UCS | Priority queue | Under suitable cost assumptions | Yes, for non-negative costs |
| DLS | Stack or recursion | Only if limit is sufficient | No |
| IDDFS | Repeated depth-limited search | Yes, under finite branching | Yes, for equal step costs |
| Bidirectional | Two search frontiers | Under suitable assumptions | Under equal-cost conditions |

## 9. Choosing an Uninformed Search Algorithm

Use BFS when:
- The goal is likely to be shallow.
- All actions have equal cost.
- Memory is sufficient.

Use DFS when:
- Memory is limited.
- A deep solution may exist.
- Finding any solution is more important than finding the optimal one.

Use UCS when:
- Actions have different costs.
- The least-cost solution is required.

Use DLS when:
- A reasonable maximum depth is known.

Use IDDFS when:
- The solution depth is unknown.
- Memory efficiency is important.
- Actions have equal cost.

Use bidirectional search when:
- Both initial and goal states are known.
- Backward search is possible.

## Common Exam Traps

- BFS uses a FIFO queue.
- DFS uses a LIFO stack.
- UCS expands the lowest cumulative-cost node.
- BFS is optimal only under equal step-cost conditions.
- DFS is not generally optimal.
- DLS may fail if its depth limit is too small.
- IDDFS repeatedly increases the depth limit.
- Bidirectional search explores from both the initial and goal states.
- Uninformed search does not use heuristic estimates.

## Quiz

1. Which data structure is primarily used by Breadth-First Search?

- [ ] Stack.
- [x] FIFO queue.
- [ ] Priority queue.
- [ ] Hash table only.

> BFS explores nodes level by level using a First In, First Out queue.

2. Which algorithm expands the node with the lowest cumulative path cost?

- [ ] Depth-First Search.
- [ ] Breadth-First Search.
- [x] Uniform-Cost Search.
- [ ] Depth-Limited Search.

> Uniform-Cost Search selects the frontier node with the lowest accumulated path cost.

3. What is the main advantage of Iterative Deepening Depth-First Search?

- [ ] It always uses more memory than BFS.
- [ ] It requires a heuristic function.
- [x] It combines shallow-solution exploration with relatively low memory usage.
- [ ] It guarantees the lowest-cost solution when action costs differ.

> IDDFS repeatedly performs depth-limited searches while retaining the low memory requirements associated with DFS.