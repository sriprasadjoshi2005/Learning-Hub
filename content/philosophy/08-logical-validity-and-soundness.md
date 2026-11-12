---
title: Logical Validity and Soundness
level: foundation
---

# Lesson 8: Logical Validity and Soundness

A convincing argument is not necessarily a logically correct argument. People can present persuasive statements that contain false assumptions, irrelevant evidence or invalid reasoning.

Logic provides two important standards for evaluating deductive arguments: validity and soundness.

Understanding these concepts helps distinguish the logical structure of an argument from the truth of its individual claims.

## 1. Meaning of Logical Validity

A deductive argument is valid when it is impossible for all its premises to be true while its conclusion is false.

Validity concerns the relationship between premises and conclusion.

Example:

- All mammals are animals.
- All dogs are mammals.
- Therefore, all dogs are animals.

The conclusion necessarily follows from the premises.

### 1.1 Validity Is About Structure

Consider:

- All fish are mammals.
- All sharks are fish.
- Therefore, all sharks are mammals.

The first premise is false in reality.

However, the argument has a valid logical structure.

If the premises were true, the conclusion would have to be true.

Therefore, validity does not require that the premises actually be true.

## 2. Invalid Arguments

An argument is invalid when its conclusion does not logically follow from its premises.

Example:

- All dogs are mammals.
- All cats are mammals.
- Therefore, all cats are dogs.

The premises do not establish the conclusion.

Both categories may belong to the larger category of mammals without being identical.

## 3. Meaning of Soundness

A deductive argument is sound when:

1. It is logically valid.
2. All its premises are true.

Therefore:

\[
\text{Soundness} = \text{Validity} + \text{True Premises}
\]

Example:

- All humans are mortal.
- Socrates is human.
- Therefore, Socrates is mortal.

The argument is valid, and its premises are true. Therefore, it is sound.

## 4. Validity and Soundness Compared

| Feature | Validity | Soundness |
|---|---|---|
| Main concern | Logical structure | Structure and truth |
| Requires valid inference | Yes | Yes |
| Requires true premises | No | Yes |
| Can have false premises | Yes | No |
| Can have a false conclusion | Yes, if premises are false | No |

Every sound deductive argument is valid, but not every valid argument is sound.

## 5. Formal Structure and Logical Form

Logical form represents an argument independently of its particular subject matter.

Consider:

- All A are B.
- All B are C.
- Therefore, all A are C.

This structure is valid regardless of what A, B and C represent.

For example:

- All roses are flowers.
- All flowers are plants.
- Therefore, all roses are plants.

The same logical relationship can apply to many different subjects.

## 6. Truth Tables and Validity

Truth tables can be used to examine whether certain propositional arguments are valid.

An argument is valid if there is no possible truth-value assignment in which all premises are true and the conclusion is false.

Consider modus ponens:

\[
P \rightarrow Q
\]

\[
P
\]

\[
\therefore Q
\]

| P | Q | P → Q | Are both premises true? |
|---|---|---|---|
| T | T | T | Yes |
| T | F | F | No |
| F | T | T | No |
| F | F | T | No |

There is no row where both premises are true and Q is false.

Therefore, the argument is valid.

## 7. Necessary and Sufficient Conditions

Validity can be better understood through necessary and sufficient conditions.

A condition is **sufficient** when its presence guarantees another condition.

A condition is **necessary** when the other condition cannot exist without it.

For a sound deductive argument:

- Validity is necessary.
- True premises are also necessary.
- Together, validity and true premises are sufficient for soundness.

Example:

If a figure is a square, it is sufficient for it to have four sides.

Having four sides is necessary for being a square, but it is not sufficient because rectangles and other quadrilaterals also have four sides.

## 8. Counterexamples to Validity

To demonstrate that a deductive argument is invalid, it is sufficient to find a possible case in which:

- All premises are true.
- The conclusion is false.

Consider:

- All birds are animals.
- All dogs are animals.
- Therefore, all dogs are birds.

The premises can both be true while the conclusion is false.

This demonstrates invalidity.

## 9. Validity Does Not Guarantee Relevance to Reality

A valid argument may be based on unrealistic or false premises.

Example:

- All planets are made of glass.
- Earth is a planet.
- Therefore, Earth is made of glass.

The logical structure is valid, but the argument is unsound because its first premise is false.

This distinction is especially important when evaluating scientific, political and everyday arguments.

## 10. Evaluating a Deductive Argument

Use the following procedure:

**Step 1:** Identify the premises and conclusion.

**Step 2:** Determine the logical structure.

**Step 3:** Ask whether the conclusion could be false while all premises remain true.

**Step 4:** If this is possible, the argument is invalid.

**Step 5:** If the argument is valid, examine whether every premise is true.

**Step 6:** If the premises are all true, the argument is sound.

## 11. Common Exam Traps

- A true conclusion does not automatically make an argument valid.
- An argument can be valid even when its premises are false.
- An invalid argument can accidentally produce a true conclusion.
- Soundness requires both validity and true premises.
- Validity is primarily a property of deductive arguments, while inductive arguments are usually evaluated by strength.

## 12. Summary

- Validity concerns whether the conclusion follows logically from the premises.
- Soundness requires validity and true premises.
- Every sound argument is valid.
- A valid argument may contain false premises.
- Truth tables can be used to evaluate propositional validity.
- Counterexamples help demonstrate invalidity.
- Necessary and sufficient conditions clarify logical relationships.

## Quiz

1. What makes a deductive argument valid?
    - [ ] Its conclusion is popular.
    - [ ] All its premises are necessarily true.
    - [x] Its conclusion cannot be false when all its premises are true.
    - [ ] It contains at least three premises.
    > A deductive argument is valid when there is no possible situation in which all its premises are true and its conclusion is false.

2. Which combination is required for soundness?
    - [ ] True conclusion and false premises
    - [ ] Persuasive language and evidence
    - [x] Logical validity and true premises
    - [ ] A large number of premises
    > Soundness requires both a valid logical structure and premises that are all true.

3. Can a valid argument have false premises?
    - [x] Yes
    - [ ] No
    - [ ] Only when its conclusion is false
    - [ ] Only when it has one premise
    > Validity concerns the logical relationship between premises and conclusion, not whether the premises are actually true.