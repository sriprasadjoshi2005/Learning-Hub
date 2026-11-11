---
title: Adversarial Search and Game Playing
level: advanced
---

Adversarial search is a problem-solving technique used in competitive environments where multiple agents have conflicting objectives.

It is particularly important in game-playing AI, where an agent must select actions while considering the possible responses of an opponent.

Unlike ordinary search, adversarial search accounts for the decisions of competing agents.

## 1. Meaning of Adversarial Search

Adversarial search is used when an intelligent agent operates in an environment where another agent attempts to achieve a competing objective.

Examples include:
- Chess.
- Checkers.
- Tic-tac-toe.
- Competitive strategy games.
- Certain security and resource-allocation problems.

The agent must consider not only its own actions but also the possible actions of its opponent.

## 2. Game Representation

A game can be represented using several components.

**Initial State:** The starting configuration of the game.

**Players:** The agents participating in the game.

**Actions:** Legal moves available to the current player.

**Transition Model:** Determines the next state after a move.

**Terminal Test:** Determines whether the game has ended.

**Utility Function:** Assigns a value to a terminal state according to its outcome.

For a two-player zero-sum game, one player's gain corresponds to the other player's loss.

## 3. Game Trees

A game tree represents possible sequences of moves.

Each node represents a game state, and each edge represents a legal move.

The tree generally alternates between:
- MAX nodes, where the AI attempts to maximize utility.
- MIN nodes, where the opponent attempts to minimize the AI's utility.

Example:

Suppose MAX has two possible moves:

- Move A leads to terminal values 3 and 5.
- Move B leads to terminal values 2 and 9.

If MIN selects the outcome least favourable to MAX:

- Move A receives a value of min(3, 5) = 3.
- Move B receives a value of min(2, 9) = 2.

MAX therefore selects Move A because 3 is greater than 2.

## 4. Minimax Algorithm

Minimax is a decision-making algorithm used in two-player, zero-sum, deterministic games with alternating turns and suitable game-tree representations.

It assumes:
- MAX attempts to maximize utility.
- MIN attempts to minimize utility.
- Both players make optimal decisions.

The minimax value is calculated recursively.

At a MAX node:

Value(node) = maximum value of its children.

At a MIN node:

Value(node) = minimum value of its children.

**Working Procedure:**

1. Generate the game tree to terminal states or a selected depth.
2. Assign utility values to terminal states.
3. Propagate values upward.
4. At MAX nodes, select the maximum child value.
5. At MIN nodes, select the minimum child value.
6. Select the action with the highest resulting minimax value at the root.

## 5. Minimax Example

Consider the following game tree:

Root: MAX

Two children: A and B.

Terminal values:

- A → 4, 7.
- B → 2, 9.

At A, MIN selects:

min(4, 7) = 4.

At B, MIN selects:

min(2, 9) = 2.

At the root, MAX selects:

max(4, 2) = 4.

Therefore, the optimal action is A.

The algorithm assumes that the opponent will choose the move most harmful to MAX.

## 6. Minimax Complexity

Let:
- b be the branching factor.
- m be the maximum depth of the game tree.

The time complexity of basic minimax is:

O(b^m)

The space complexity for a depth-first implementation is generally:

O(bm)

The large time complexity makes full game-tree exploration impractical for many complex games.

## 7. Alpha-Beta Pruning

Alpha-Beta Pruning improves minimax by avoiding the exploration of branches that cannot influence the final decision.

It maintains two values:

**Alpha (α):** The best value MAX can guarantee so far.

**Beta (β):** The best value MIN can guarantee so far.

A branch can be pruned when:

α >= β

Pruning does not change the final minimax result. It only reduces unnecessary exploration.

**Example:**

Suppose MAX already has an alternative move with a guaranteed value of 5.

During the evaluation of another branch, MIN discovers an option that can force a value of 3.

MAX will never choose this branch because it is worse than the existing alternative.

Further exploration of that branch may therefore be unnecessary.

## 8. Advantages of Alpha-Beta Pruning

- Produces the same result as minimax.
- Reduces the number of nodes explored.
- Allows deeper search within the same computational budget.
- Becomes more effective with good move ordering.

In the best case, with ideal move ordering, the effective time complexity can improve to approximately:

O(b^(m/2))

The worst-case time complexity remains O(b^m).

## 9. Evaluation Functions

For complex games, exploring the complete game tree may be impossible.

A depth-limited search evaluates non-terminal states using a heuristic evaluation function.

For chess, an evaluation function may consider:
- Material advantage.
- King safety.
- Piece mobility.
- Pawn structure.
- Board control.
- Positional advantages.

The evaluation function estimates how favourable a position is for a player.

Its quality strongly influences the strength of the game-playing system.

## 10. Depth-Limited Search and Horizon Effect

Depth-limited search stops exploring after a predefined depth.

At that point, an evaluation function estimates the value of the current position.

However, this can produce the horizon effect.

The horizon effect occurs when an important consequence lies just beyond the search depth, causing the algorithm to evaluate a position incorrectly.

A common approach for reducing this problem is quiescence search, which extends evaluation in unstable positions until a more suitable stopping condition is reached.

## 11. Applications of Adversarial Search

Adversarial search is used in:
- Chess engines.
- Checkers programs.
- Strategy game AI.
- Competitive planning.
- Automated negotiation research.
- Security decision-making.

More advanced game-playing systems may also use Monte Carlo Tree Search, learned evaluation functions, and reinforcement learning.

## Common Exam Traps

- MAX tries to maximize utility.
- MIN tries to minimize utility.
- Minimax assumes rational opposing players.
- Alpha-Beta Pruning produces the same minimax decision as the original algorithm.
- Alpha represents MAX's current lower bound.
- Beta represents MIN's current upper bound.
- Pruning occurs when alpha is greater than or equal to beta.
- Good move ordering improves alpha-beta efficiency.
- Evaluation functions estimate non-terminal positions in depth-limited search.

## Quiz

1. What is the objective of the MAX player in minimax?

- [ ] Minimize the opponent's branching factor.
- [x] Maximize the utility value.
- [ ] Minimize its own utility.
- [ ] Explore every possible game state regardless of depth.

> MAX selects actions that maximize the utility value under the minimax decision process.

2. What is the purpose of Alpha-Beta Pruning?

- [ ] To change the minimax result.
- [ ] To increase the number of explored branches.
- [x] To avoid exploring branches that cannot affect the final decision.
- [ ] To eliminate the need for an evaluation function.

> Alpha-Beta Pruning reduces unnecessary exploration while preserving the minimax result.

3. Under what condition can Alpha-Beta Pruning occur?

- [ ] Alpha is always equal to zero.
- [ ] Beta is always greater than the branching factor.
- [x] Alpha is greater than or equal to Beta.
- [ ] Alpha is smaller than the search depth.

> When alpha is greater than or equal to beta, the remaining branch cannot improve the decision for the relevant player.