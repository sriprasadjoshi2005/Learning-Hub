---
title: Mathematical Reasoning and Problem Solving
level: foundation
---

Mathematical reasoning forms the logical foundation of mathematical proofs and deductive problem-solving. Understanding propositional logic, truth tables, conditional statements, and proof techniques allows mathematicians to rigorously establish truth.

## Logic Statements and Truth Tables

A **proposition (statement)** is a declarative sentence that is strictly either True ($\text{T}$) or False ($\text{F}$), but not both.

- **Negation ($\neg P$ or $\sim P$):** Reverses the truth value of proposition $P$.
- **Conjunction ($P \land Q$):** True only when **both** $P$ and $Q$ are True.
- **Disjunction ($P \lor Q$):** True when **at least one** of $P$ or $Q$ is True.
- **Conditional Statement ($P \implies Q$):** "If $P$, then $Q$". False only when $P$ is True and $Q$ is False.
- **Biconditional Statement ($P \iff Q$):** "P if and only if Q". True when $P$ and $Q$ have the exact same truth value.

### Truth Table for Logical Connectives

| $P$ | $Q$ | $\neg P$ | $P \land Q$ | $P \lor Q$ | $P \implies Q$ | $P \iff Q$ |
|---|---|---|---|---|---|---|
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ |

## Implication Variations and Proof Techniques

### Related Conditional Statements

Given the primary implication $P \implies Q$:

- **Converse:** $Q \implies P$ (Not logically equivalent to $P \implies Q$).
- **Inverse:** $\neg P \implies \neg Q$ (Not logically equivalent to $P \implies Q$).
- **Contrapositive:** $\neg Q \implies \neg P$ (**Logically equivalent** to $P \implies Q$).

### Core Mathematical Proof Strategies

1. **Direct Proof:** Assume $P$ is true and apply axioms/theorems algebraically to derive $Q$.
2. **Proof by Contrapositive:** Prove the logically equivalent statement $\neg Q \implies \neg P$.
3. **Proof by Contradiction (Reductio ad Absurdum):** Assume $P$ is true and $Q$ is false ($\neg Q$), then derive a logical absurdity (e.g., $1 = 0$).
4. **Proof by Counterexample:** To disprove a universal claim ("For all $x$..."), find a single specific case where the claim fails.

## Logical Equivalence and De Morgan's Laws

| Logical Equivalent | Formal Symbolic Statement | Verbal Description |
|---|---|---|
| Contrapositive Identity | $(P \implies Q) \equiv (\neg Q \implies \neg P)$ | An implication equals its contrapositive |
| Implication Disjunction | $(P \implies Q) \equiv (\neg P \lor Q)$ | Conditional expressed with disjunction |
| De Morgan's Law 1 | $\neg (P \land Q) \equiv \neg P \lor \neg Q$ | Negation flips AND to OR |
| De Morgan's Law 2 | $\neg (P \lor Q) \equiv \neg P \land \neg Q$ | Negation flips OR to AND |
| Double Negation | $\neg(\neg P) \equiv P$ | Negating twice yields original statement |

## Important Formulas and Logical Axioms

Tautology and Contradiction Definitions:

$$\text{Tautology}: \text{A statement that is ALWAYS True (e.g., } P \lor \neg P \text{)}$$

$$\text{Contradiction}: \text{A statement that is ALWAYS False (e.g., } P \land \neg P \text{)}$$

Quantifier Negation Rules:

$$\neg (\forall x, P(x)) \equiv \exists x, \neg P(x) \quad (\text{Negating "For all" yields "There exists"})$$

$$\neg (\exists x, P(x)) \equiv \forall x, \neg P(x) \quad (\text{Negating "There exists" yields "For all"})$$

## Common Exam Traps

- **Confusing Converse with Contrapositive:** Assuming if $P \implies Q$ is true, then $Q \implies P$ must be true. (e.g., "If $x = 2$, then $x^2 = 4$" is true, but "If $x^2 = 4$, then $x = 2$" is false because $x$ could be $-2$).
- **Misinterpreting $P \implies Q$ when $P$ is False:** Forgetting that if premise $P$ is false, the implication $P \implies Q$ is **vacuously true** regardless of $Q$.
- **Incomplete Negation of Quantifiers:** Negating $\forall x (x > 0)$ as $\forall x (x \le 0)$ instead of correctly changing the quantifier: $\exists x (x \le 0)$.

## Quiz

1. What is the contrapositive of the statement: "If an integer is divisible by $6$, then it is divisible by $3$"?
  - [ ] If an integer is divisible by $3$, then it is divisible by $6$.
  - [ ] If an integer is not divisible by $6$, then it is not divisible by $3$.
  - [x] If an integer is not divisible by $3$, then it is not divisible by $6$.
  - [ ] An integer is divisible by $6$ if and only if it is divisible by $3$.
   > The contrapositive of $P \implies Q$ is $\neg Q \implies \neg P$. Here, $P = \text{"divisible by } 6\text{"}$ and $Q = \text{"divisible by } 3\text{"}$. Thus, $\neg Q \implies \neg P$ is "If it is not divisible by $3$, then it is not divisible by $6$."

2. Which of the following symbolic expressions is logically equivalent to $\neg (P \implies Q)$?
  - [ ] $\neg P \implies \neg Q$
  - [ ] $\neg P \lor Q$
  - [x] $P \land \neg Q$
  - [ ] $\neg P \land Q$
   > Since $(P \implies Q) \equiv (\neg P \lor Q)$, taking the negation yields $\neg (\neg P \lor Q) \equiv \neg(\neg P) \land \neg Q \equiv P \land \neg Q$ by De Morgan's Law.

3. Which strategy disproves the universal claim: "For all real numbers $x$, $x^2 > x$"?
  - [ ] Prove that $x^2 > x$ holds for $x = 5$.
  - [x] Provide the single counterexample $x = 0.5$, where $(0.5)^2 = 0.25 < 0.5$.
  - [ ] Show that $x^2 - x = 0$ has two real roots.
  - [ ] Demonstrate that the claim holds for negative numbers.
   > To disprove a universal claim ("For all..."), presenting a single counterexample where the statement fails ($x = 0.5$) is sufficient.