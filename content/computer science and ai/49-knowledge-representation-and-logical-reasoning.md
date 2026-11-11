---
title: Knowledge Representation and Logical Reasoning
level: advanced
---

Knowledge Representation and Reasoning (KRR) is an important area of Artificial Intelligence concerned with storing information in structured forms and using that information to derive conclusions.

An intelligent system needs more than raw data. It requires representations that allow it to identify relationships, understand facts, apply rules, and reason about situations.

## 1. Meaning of Knowledge Representation

Knowledge representation is the process of organizing information in a form that a computer system can use for reasoning and problem-solving.

Knowledge may include:
- Facts.
- Relationships.
- Rules.
- Concepts.
- Constraints.
- Events.
- Procedures.

Example:

A system may store the following facts:

- All humans are mammals.
- Ravi is a human.

Using logical reasoning, the system can conclude:

- Ravi is a mammal.

This demonstrates how stored knowledge can be used to derive new information.

## 2. Data, Information, and Knowledge

These terms are related but have different meanings.

**Data:** Raw observations or values without necessarily having an interpreted meaning.

**Information:** Data that has been organized and interpreted.

**Knowledge:** Information combined with relationships, rules, or context that supports reasoning and decision-making.

Example:

- Data: 38.
- Information: The measured temperature is 38 degrees Celsius.
- Knowledge: A temperature of 38 degrees Celsius may indicate fever and should be interpreted with other symptoms.

## 3. Requirements of a Good Knowledge Representation

A useful knowledge representation should provide several capabilities.

**Representational Adequacy:** Ability to represent the required knowledge.

**Inferential Adequacy:** Ability to derive new knowledge from existing information.

**Inferential Efficiency:** Ability to perform reasoning efficiently.

**Acquisitional Efficiency:** Ability to add, update, and acquire knowledge conveniently.

These properties help evaluate knowledge representation systems.

## 4. Types of Knowledge

AI systems may use different types of knowledge.

**Declarative Knowledge:** Describes facts about the world.

Example: Earth revolves around the Sun.

**Procedural Knowledge:** Describes how to perform a task.

Example: Steps for sorting a list.

**Heuristic Knowledge:** Uses practical rules or experience-based strategies.

Example: In route planning, prefer roads that appear to move closer to the destination.

**Meta-Knowledge:** Knowledge about other knowledge.

Example: Information describing which source of knowledge should be trusted for a particular task.

**Structural Knowledge:** Describes relationships among concepts.

Example: A car contains an engine, wheels, and other components.

## 5. Logical Representation

Logic provides a formal method for representing facts and relationships.

Two important forms are:

- Propositional Logic.
- First-Order Logic.

## 6. Propositional Logic

Propositional Logic represents statements that are either true or false.

A proposition is a declarative statement with a truth value.

Examples:

P: It is raining.

Q: The road is wet.

Propositions can be combined using logical connectives.

**Negation (NOT):**

NOT P is true when P is false.

**Conjunction (AND):**

P AND Q is true only when both P and Q are true.

**Disjunction (OR):**

P OR Q is true when at least one proposition is true.

**Implication:**

P implies Q is false only when P is true and Q is false.

**Biconditional:**

P if and only if Q is true when both propositions have the same truth value.

## 7. Truth Table

A truth table shows the output of logical operations for every possible combination of input truth values.

| P | Q | P AND Q | P OR Q | P implies Q |
|---|---|---|---|---|
| True | True | True | True | True |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

Truth tables are useful for evaluating logical expressions and checking logical equivalence.

## 8. First-Order Logic

First-Order Logic (FOL) extends propositional logic by representing objects, properties, relationships, and quantified statements.

It uses:

- Constants.
- Variables.
- Predicates.
- Functions.
- Quantifiers.

**Constants:** Refer to specific objects.

Example: Ravi.

**Variables:** Represent objects that may vary.

Example: x.

**Predicates:** Represent properties or relationships.

Example: Human(Ravi).

**Functions:** Map objects to other objects.

Example: FatherOf(Ravi).

### Quantifiers

First-Order Logic uses two major quantifiers.

**Universal Quantifier (FOR ALL):**

Represents a statement that applies to every object in a specified domain.

Example:

For all x, if x is human, then x is mortal.

**Existential Quantifier (THERE EXISTS):**

Represents a statement that applies to at least one object.

Example:

There exists an x such that x is a student.

## 9. Inference and Logical Reasoning

Inference is the process of deriving new conclusions from existing knowledge.

Two important inference methods are:

**Modus Ponens:**

If P is true and P implies Q is true, then Q is true.

Example:

- If it rains, the ground becomes wet.
- It is raining.
- Therefore, the ground becomes wet.

**Modus Tollens:**

If P implies Q is true and Q is false, then P must be false.

Example:

- If a device is connected to power, its indicator light turns on.
- The indicator light is not on.
- Therefore, under the stated rule, the device is not connected to power.

## 10. Knowledge-Based Systems

A knowledge-based system stores domain knowledge and uses reasoning mechanisms to solve problems.

Its main components include:

**Knowledge Base:** Stores facts, rules, and relationships.

**Inference Engine:** Applies reasoning rules to derive conclusions.

**User Interface:** Allows users to interact with the system.

**Explanation Facility:** Provides explanations for conclusions when supported by the system design.

Example:

A troubleshooting system may contain rules about computer hardware failures and use user-provided symptoms to identify possible causes.

## 11. Semantic Networks

A semantic network represents knowledge using a graph structure.

It contains:
- Nodes representing concepts or objects.
- Edges representing relationships.

Example:

Animal → is-a → Living Thing

Dog → is-a → Animal

Dog → has → Four Legs

Semantic networks make relationships among concepts easier to visualize.

They can also support inheritance of properties through hierarchical relationships.

## 12. Frames

A frame is a structured representation used to describe an object, concept, or situation through attributes called slots.

Example:

Frame: Car

| Slot | Value |
|---|---|
| Type | Vehicle |
| Wheels | 4 |
| Fuel | Petrol or electricity |
| Purpose | Transportation |
| Engine | Present in many designs |

Frames organize related information into a structured representation.

## 13. Production Rules

Production systems represent knowledge using condition-action rules.

A general rule is:

IF condition THEN action.

Example:

IF temperature is high AND cooling system is inactive THEN generate an overheating warning.

Production rules are commonly used in expert systems and rule-based reasoning.

## 14. Knowledge Representation Challenges

AI systems may face several difficulties when representing knowledge.

**Incomplete Knowledge:** Some required facts may be unavailable.

**Uncertainty:** Available information may be unreliable.

**Inconsistency:** Different facts may contradict one another.

**Knowledge Acquisition:** Collecting expert knowledge can be difficult.

**Scalability:** Large knowledge bases can become difficult to maintain.

**Context Dependence:** The meaning of information may depend on its surrounding circumstances.

## Common Exam Traps

- Propositional Logic represents complete statements as true or false.
- First-Order Logic supports objects, predicates, variables, and quantifiers.
- Universal quantification applies to every object in a domain.
- Existential quantification requires at least one object.
- Modus Ponens uses P and P implies Q to derive Q.
- A semantic network represents knowledge through nodes and relationships.
- Frames organize information through slots and values.
- A knowledge base stores information, while an inference engine applies reasoning.

## Quiz

1. Which logical system can represent objects, properties, relationships, and quantifiers?

- [ ] Propositional Logic only.
- [x] First-Order Logic.
- [ ] Binary arithmetic.
- [ ] Boolean algebra without predicates.

> First-Order Logic extends propositional logic using variables, predicates, functions, and quantifiers.

2. What does the universal quantifier represent?

- [ ] At least one object satisfies a condition.
- [ ] No objects satisfy a condition.
- [x] Every object in the specified domain satisfies a condition.
- [ ] Exactly two objects satisfy a condition.

> The universal quantifier expresses statements that apply to all objects in the specified domain.

3. Which inference rule derives Q from P and P implies Q?

- [ ] Modus Tollens.
- [ ] Disjunction Elimination.
- [x] Modus Ponens.
- [ ] Negation Introduction.

> Modus Ponens concludes Q when P is true and the implication from P to Q is established.