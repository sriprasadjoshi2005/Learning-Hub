---
title: Informed Search and Heuristic Algorithms
level: advanced
---

Informed search algorithms use additional knowledge about a problem to guide exploration toward promising states.

Unlike uninformed search, which explores without estimating closeness to the goal, informed search uses heuristic information to prioritize nodes.

Heuristics can significantly reduce unnecessary exploration when they provide useful estimates.

## 1. Meaning of Informed Search

Informed search uses problem-specific knowledge to decide which states should be explored first.

The additional knowledge is commonly represented by a heuristic function.

A heuristic function estimates the remaining cost or distance from a current state to a goal.

It is generally represented as:

h(n)

Where:
- n represents a search node.
- h(n) represents the estimated cost from node n to the goal.

A heuristic does not necessarily provide the exact remaining cost.

## 2. Heuristic Functions

A heuristic function provides an estimate that guides search.

Example: Route Finding

Suppose a navigation agent must travel from City A to City D.

The straight-line distance between a current city and City D can be used as a heuristic estimate.

The actual road distance may be greater because roads do not always follow straight paths.

Therefore, straight-line distance can provide a useful estimate of the remaining journey.

A good heuristic generally:
- Is computationally inexpensive.
- Provides useful estimates.
- Helps identify promising search directions.
- Does not unnecessarily mislead the search process.

## 3. Greedy Best-First Search

Greedy Best-First Search selects the node that appears closest to the goal according to the heuristic function.

Its evaluation function is:

f(n) = h(n)

The algorithm chooses the node with the smallest estimated remaining cost.

**Working Procedure:**

1. Insert the initial node into a priority queue.
2. Calculate its heuristic value.
3. Select the node with the lowest heuristic value.
4. Check whether it is the goal.
5. Generate successors if necessary.
6. Calculate their heuristic values.
7. Repeat until the goal is found.

**Example:**

Suppose three available nodes have the following heuristic estimates:

- Node A: h(A) = 8.
- Node B: h(B) = 3.
- Node C: h(C) = 5.

Greedy Best-First Search selects Node B because it has the smallest estimated distance to the goal.

**Advantages:**
- Can find solutions quickly with useful heuristics.
- Often explores fewer nodes than uninformed search.

**Limitations:**
- Does not consider the cost already incurred.
- May follow misleading heuristic estimates.
- Is not generally optimal.
- May be incomplete in some search spaces.

## 4. A* Search Algorithm

A* Search combines the cost already incurred with an estimate of the remaining cost.

Its evaluation function is:

f(n) = g(n) + h(n)

Where:

- g(n): Actual path cost from the initial state to node n.
- h(n): Estimated remaining cost from node n to the goal.
- f(n): Estimated total solution cost through node n.

A* expands the node with the smallest f(n).

**Example:**

Consider two nodes:

Node A:
- g(A) = 5.
- h(A) = 8.
- f(A) = 13.

Node B:
- g(B) = 7.
- h(B) = 3.
- f(B) = 10.

A* selects Node B because its estimated total cost is lower.

This demonstrates why A* differs from Greedy Best-First Search.

Greedy Search considers only h(n), whereas A* considers both g(n) and h(n).

## 5. Admissible Heuristics

A heuristic is admissible if it never overestimates the actual minimum remaining cost to reach the goal.

Mathematically:

h(n) <= h*(n)

Where:
- h(n) is the heuristic estimate.
- h*(n) is the true minimum remaining cost.

For example:

If the actual minimum remaining cost is 12, a heuristic estimate of 8 is admissible.

An estimate of 15 is not admissible because it overestimates the true cost.

Admissibility is an important condition for the optimality of A* under the appropriate search assumptions.

## 6. Consistent Heuristics

A heuristic is consistent if it satisfies the following condition for every transition from n to a successor n':

h(n) <= c(n,n') + h(n')

Where c(n,n') is the cost of moving from n to n'.

Consistency ensures that estimated costs behave in a suitable way along paths.

A consistent heuristic is also admissible when the goal heuristic is zero.

Consistency is particularly useful in graph-search implementations of A* because it supports efficient node expansion without repeatedly reopening previously expanded nodes under standard assumptions.

## 7. Comparison of Greedy Search and A*

| Feature | Greedy Best-First Search | A* Search |
|---|---|---|
| Evaluation function | f(n) = h(n) | f(n) = g(n) + h(n) |
| Considers path cost | No | Yes |
| Uses heuristic | Yes | Yes |
| Generally optimal | No | Yes, with suitable heuristic and assumptions |
| Main objective | Reach an apparently close goal | Minimize estimated total solution cost |

## 8. Heuristic Quality

The quality of a heuristic affects search performance.

**Weak Heuristic:** Provides little information about the remaining cost.

**Informative Heuristic:** Helps distinguish promising states from less promising ones.

**Perfect Heuristic:** Gives the exact remaining optimal cost.

A perfect heuristic is generally difficult or expensive to obtain because calculating it may require solving the original problem.

For minimization problems, if two admissible heuristics satisfy:

h1(n) <= h2(n) <= h*(n)

Then h2 is generally more informed because it provides estimates closer to the true remaining cost without overestimating.

## 9. Heuristics in Common Problems

**Route Finding:** Straight-line distance to the destination.

**Eight-Puzzle:** Number of misplaced tiles.

**Eight-Puzzle:** Sum of Manhattan distances of tiles from their goal positions.

**Game Playing:** Estimated desirability of a board position.

**Scheduling:** Estimated remaining processing time or delay.

Different problems require different heuristic designs.

## 10. Limitations of Informed Search

Informed search can still face several difficulties.

- A poor heuristic may guide the algorithm toward unproductive states.
- A* can consume large amounts of memory.
- Computing a sophisticated heuristic may be expensive.
- An inadmissible heuristic may prevent optimality guarantees.
- Large state spaces may remain computationally difficult.

Heuristic design is therefore an important part of practical AI problem-solving.

## Common Exam Traps

- Informed search uses heuristic information.
- Greedy Best-First Search uses f(n) = h(n).
- A* uses f(n) = g(n) + h(n).
- g(n) represents the cost already incurred.
- h(n) estimates the remaining cost.
- An admissible heuristic never overestimates the true minimum remaining cost.
- A consistent heuristic satisfies the triangle-like inequality for transitions.
- Greedy Best-First Search is not generally optimal.
- A* has optimality guarantees under appropriate assumptions.

## Quiz

1. Which evaluation function is used by A* Search?

- [ ] f(n) = h(n) - g(n).
- [ ] f(n) = g(n) - h(n).
- [x] f(n) = g(n) + h(n).
- [ ] f(n) = g(n) × h(n).

> A* combines the actual path cost with the estimated remaining cost.

2. What condition must an admissible heuristic satisfy?

- [ ] It must always overestimate the remaining cost.
- [x] It must never overestimate the actual minimum remaining cost.
- [ ] It must always return zero.
- [ ] It must ignore the goal state.

> Admissibility ensures that heuristic estimates do not exceed the true minimum remaining cost.

3. Which algorithm uses only the heuristic estimate when selecting the next node?

- [ ] Uniform-Cost Search.
- [ ] A* Search.
- [x] Greedy Best-First Search.
- [ ] Breadth-First Search.

> Greedy Best-First Search selects nodes using h(n) without considering the path cost already incurred.