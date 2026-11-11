---
title: Algorithm Design Techniques
level: advanced
---

Algorithm design techniques are general strategies used to develop efficient solutions to computational problems. They provide systematic approaches for breaking down problems, exploring possibilities, and optimizing computations.

## 1. Understanding Algorithm Design

Algorithm design involves selecting an appropriate strategy for solving a problem.

A good algorithm should ideally be:

- Correct.
- Efficient.
- Understandable.
- Maintainable.
- Suitable for the problem constraints.

Different problems may require different design techniques.

## 2. Brute Force

Brute force solves a problem by systematically examining possible solutions without relying on advanced optimization.

Example: Finding the largest element in an array.

```python
def find_largest(values):
    largest = values[0]

    for value in values:
        if value > largest:
            largest = value

    return largest
```

Brute force is often simple and reliable, but it may become inefficient when the number of possibilities is very large.

## 3. Divide and Conquer

Divide and conquer solves a problem by dividing it into smaller subproblems, solving those subproblems, and combining their results.

Its three main stages are:

1. Divide: Break the problem into smaller parts.
2. Conquer: Solve the smaller problems.
3. Combine: Merge their solutions.

Examples include:

- Merge sort.
- Quick sort.
- Binary search.

Divide and conquer is useful when smaller versions of a problem can be solved independently.

## 4. Greedy Algorithms

A greedy algorithm makes the best-looking choice at each step according to a defined local rule.

It does not generally reconsider previous choices.

Examples include:

- Activity selection.
- Fractional knapsack.
- Certain minimum spanning tree algorithms.
- Huffman coding.

A greedy strategy is not automatically optimal for every problem.

Its correctness must be established for the particular problem.

## 5. Dynamic Programming

Dynamic programming solves problems by storing solutions to smaller subproblems and reusing them.

It is especially useful when a problem has:

- Overlapping subproblems.
- Optimal substructure.

### Overlapping Subproblems

The same smaller problems appear repeatedly during computation.

### Optimal Substructure

An optimal solution can be constructed from optimal solutions to relevant subproblems.

## 6. Memoization

Memoization is a top-down dynamic programming technique.

It stores the results of previously solved subproblems so they do not need to be recalculated.

Example:

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

This avoids repeatedly calculating the same Fibonacci values.

## 7. Tabulation

Tabulation is a bottom-up dynamic programming technique.

It begins with smaller known results and builds toward the required solution.

Example:

```python
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

The solution is constructed iteratively using previously computed values.

## 8. Backtracking

Backtracking explores possible solutions and abandons a path when it cannot lead to a valid solution.

It follows a general pattern:

1. Choose a possible option.
2. Check whether the choice is valid.
3. Continue exploring if valid.
4. Reverse the choice when necessary.
5. Explore another possibility.

Applications include:

- N-Queens problem.
- Sudoku solving.
- Maze solving.
- Generating permutations.
- Constraint satisfaction problems.

## 9. Branch and Bound

Branch and Bound is an optimization technique that explores possible solutions while using bounds to eliminate branches that cannot improve the current best solution.

Its main components are:

- Branching: Dividing the problem into smaller possibilities.
- Bounding: Calculating limits on the best achievable result.
- Pruning: Eliminating branches that cannot produce a better solution.

It is commonly applied to combinatorial optimization problems such as the travelling salesperson problem and certain scheduling problems.

## 10. Comparing Design Techniques

| Technique | Main Idea | Typical Applications |
| --- | --- | --- |
| Brute Force | Examine possibilities directly | Simple search and enumeration |
| Divide and Conquer | Divide, solve, combine | Merge sort and binary search |
| Greedy | Make locally optimal choices | Activity selection |
| Dynamic Programming | Store reusable subproblem results | Knapsack and sequence problems |
| Backtracking | Explore and reverse choices | Sudoku and N-Queens |
| Branch and Bound | Use bounds to prune optimization search | Travelling salesperson |

## 11. Choosing a Technique

The selection depends on the problem's structure.

- Use brute force when the search space is small or a straightforward reference solution is needed.
- Use divide and conquer when subproblems can be solved independently.
- Use greedy algorithms when local choices can be proven to lead to an optimal result.
- Use dynamic programming when subproblems overlap and optimal substructure exists.
- Use backtracking when valid solutions must be constructed under constraints.
- Use Branch and Bound when searching for an optimal solution and bounds can eliminate unpromising branches.

## Common Exam Traps

- Divide and conquer divides a problem and combines subproblem results.
- Greedy algorithms make local choices and do not automatically guarantee global optimality.
- Dynamic programming stores and reuses subproblem solutions.
- Memoization is generally top-down.
- Tabulation is generally bottom-up.
- Backtracking abandons choices that cannot lead to valid solutions.
- Branch and Bound uses bounds to eliminate unpromising search branches.
- Dynamic programming and greedy algorithms are different strategies.

## Quiz

1. Which technique stores previously calculated subproblem results?
   - [ ] Brute force
   - [ ] Backtracking
   - [x] Dynamic programming
   - [ ] Linear search

   > Dynamic programming avoids repeated calculations by storing reusable results.

2. Which dynamic programming approach generally solves smaller subproblems first using an iterative table?
   - [ ] Memoization
   - [x] Tabulation
   - [ ] Backtracking
   - [ ] Branching

   > Tabulation is a bottom-up technique that builds solutions from smaller known results.

3. Which technique eliminates unpromising branches using calculated bounds?
   - [ ] Greedy method
   - [ ] Linear search
   - [ ] Divide and conquer
   - [x] Branch and Bound

   > Branch and Bound uses bounds to avoid exploring branches that cannot improve the current solution.