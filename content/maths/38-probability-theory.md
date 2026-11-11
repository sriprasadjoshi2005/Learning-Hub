---
title: Probability Theory
level: advanced
---

Probability theory quantifies uncertainty and randomness. Understanding classical definitions, conditional probability, Bayes' Theorem, and random variables enables rigorous modeling of uncertain events.

## Probability Definitions and Event Algebra

The **sample space ($S$)** is the set of all possible outcomes of a random experiment. An **event ($E$)** is a subset of $S$.

- **Classical Probability:** $P(E) = \frac{n(E)}{n(S)}$, where $0 \le P(E) \le 1$.
- **Complementary Event:** $P(E') = 1 - P(E)$.
- **Addition Rule (Mutually Exclusive vs. General):**
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
  If $A$ and $B$ are **mutually exclusive** ($A \cap B = \emptyset$), then $P(A \cup B) = P(A) + P(B)$.

## Conditional Probability, Independence, and Bayes' Theorem

### Conditional Probability

The probability of event $A$ occurring given that event $B$ has already occurred ($P(B) > 0$):

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Independent Events

Events $A$ and $B$ are **independent** if the occurrence of one does not affect the probability of the other:

$$P(A \cap B) = P(A) \cdot P(B) \iff P(A \mid B) = P(A)$$

### Total Probability and Bayes' Theorem

Let $E_1, E_2, \dots, E_k$ be a partition of sample space $S$.

- **Law of Total Probability:**
  $$P(A) = \sum_{i=1}^{k} P(E_i) \cdot P(A \mid E_i)$$

- **Bayes' Theorem (Updating Prior Probabilities):**
  $$P(E_j \mid A) = \frac{P(E_j) \cdot P(A \mid E_j)}{\sum_{i=1}^{k} P(E_i) \cdot P(A \mid E_i)}$$

## Probability Distribution Master Table

| Concept / Distribution | Probability Mass Function $P(X = x)$ | Expected Value $E[X]$ | Variance $\text{Var}(X)$ |
|---|---|---|---|
| General Discrete | Given distribution $p_i$ | $\mu = \sum x_i p_i$ | $\sigma^2 = \sum x_i^2 p_i - \mu^2$ |
| Binomial $B(n, p)$ | $\binom{n}{x} p^x (1-p)^{n-x}$ | $n p$ | $n p (1 - p)$ |
| Poisson $\text{Poi}(\lambda)$ | $\frac{e^{-\lambda} \lambda^x}{x!}$ | $\lambda$ | $\lambda$ |
| Uniform Discrete | $\frac{1}{n}$ | $\frac{n + 1}{2}$ | $\frac{n^2 - 1}{12}$ |

## Important Formulas and Probability Identities

Bayes' Theorem Formula:

$$P(E_j \mid A) = \frac{P(E_j) P(A \mid E_j)}{\sum_{i=1}^{k} P(E_i) P(A \mid E_i)}$$

Binomial Distribution Variance:

$$\text{Var}(X) = n p q \quad \text{where } q = 1 - p$$

Expectation Formula:

$$E[X] = \sum x_i P(X = x_i)$$

## Common Exam Traps

- **Confusing Mutually Exclusive with Independent:** Assuming mutually exclusive events are independent. If $A$ and $B$ are mutually exclusive ($P(A \cap B) = 0$), they are **dependent** if $P(A), P(B) > 0$.
- **Inverse Conditioning Error:** Treating $P(A \mid B)$ as equal to $P(B \mid A)$. This is the classic prosecutor's fallacy; Bayes' Theorem is required to invert conditioning.
- **Forgetting $P(A \cap B)$ in Addition Rule:** Writing $P(A \cup B) = P(A) + P(B)$ for non-mutually exclusive events, double-counting the intersection.

## Quiz

1. A fair coin is tossed $3$ times. What is the probability of obtaining at least two heads?
  - [ ] $\frac{1}{4}$
  - [ ] $\frac{3}{8}$
  - [x] $\frac{1}{2}$
  - [ ] $\frac{5}{8}$
   > Total outcomes $n(S) = 2^3 = 8$. Outcomes with at least 2 heads: $\{HHH, HHT, HTH, THH\} \implies 4$ outcomes. Probability $= \frac{4}{8} = \frac{1}{2}$.

2. Given $P(A) = 0.6$, $P(B) = 0.5$, and $P(A \cap B) = 0.3$, evaluate the conditional probability $P(A \mid B)$.
  - [ ] $0.5$
  - [x] $0.6$
  - [ ] $0.3$
  - [ ] $0.8$
   > $P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.3}{0.5} = 0.6$. (Note: Since $P(A \cap B) = P(A) P(B) = 0.6 \times 0.5 = 0.3$, $A$ and $B$ are independent).

3. Bag I contains $3$ red and $2$ black balls. Bag II contains $2$ red and $4$ black balls. A bag is chosen at random and a ball is drawn. If the drawn ball is red, what is the probability it came from Bag I?
  - [ ] $\frac{3}{5}$
  - [ ] $\frac{1}{3}$
  - [x] $\frac{9}{14}$
  - [ ] $\frac{5}{14}$
   > $P(\text{Bag I}) = P(\text{Bag II}) = \frac{1}{2}$. $P(R \mid \text{Bag I}) = \frac{3}{5}$, $P(R \mid \text{Bag II}) = \frac{2}{6} = \frac{1}{3}$. Total $P(R) = \frac{1}{2}\left(\frac{3}{5}\right) + \frac{1}{2}\left(\frac{1}{3}\right) = \frac{3}{10} + \frac{1}{6} = \frac{9 + 5}{30} = \frac{14}{30}$. By Bayes' Theorem: $P(\text{Bag I} \mid R) = \frac{3/10}{14/30} = \frac{3}{10} \times \frac{30}{14} = \frac{9}{14}$.