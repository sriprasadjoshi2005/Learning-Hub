---
title: Integration by Parts and Partial Fractions
level: advanced
lesson: 38
subject: Mathematics
---

# Lesson 38: Integration by Parts and Partial Fractions

## Learning objective

Handle products and rational functions using integration by parts and algebraic decomposition.

## Core concepts

- Integration by parts: ∫u dv=uv−∫v du. Choose u so its derivative becomes simpler and dv is readily integrable.
- A common heuristic for selecting u is LIATE: logarithmic, inverse trigonometric, algebraic, trigonometric, exponential; it is a guide, not a theorem.
- For a proper rational function, factor the denominator and decompose into simpler fractions. Distinct linear factors use constants over each factor; repeated factors require a sum of powers.
- For an irreducible quadratic factor, the numerator is linear in x.
- If the rational function is improper, perform polynomial division before partial fractions.

## Essential formulae and results

∫u dv=uv−∫v du.

## Worked examples

**Example 1.** ∫x e^x dx: take u=x, dv=e^x dx. Result = xe^x−∫e^x dx=e^x(x−1)+C.
**Example 2.** Decompose 1/[(x−1)(x+1)]=1/2[1/(x−1)−1/(x+1)]. Its integral is (1/2)ln|(x−1)/(x+1)|+C.

## Common mistakes to avoid

- Do not omit the minus sign in integration by parts.
- Check that a rational function is proper before decomposition.
- For repeated factors, include every power up to the multiplicity.

## Exam approach

1. Identify the topic and write down the relevant definition or formula.
2. Check the conditions: domain, non-zero denominators, interval, sign and units where applicable.
3. Show the essential algebraic steps instead of jumping to an answer.
4. Substitute the result into the original condition whenever extraneous solutions are possible.
5. Keep exact values (fractions, radicals and π) until a decimal approximation is requested.

## Quick quiz

**1. The integration-by-parts formula is:**
- [ ] uv+∫vdu
- [x] uv−∫vdu
- [ ] u/v
- [ ] u'v'
> **Explanation:** It follows from the product rule.

**2. ∫x e^x dx is:**
- [ ] xe^x+C
- [x] e^x(x−1)+C
- [ ] e^x(x+1)+C
- [ ] x²e^x/2+C
> **Explanation:** Apply integration by parts with u=x and dv=e^x dx.

**3. A rational function with numerator degree greater than denominator degree is:**
- [ ] Always proper
- [x] Improper
- [ ] A polynomial only
- [ ] Undefined
> **Explanation:** Polynomial division is needed before partial fractions.


## Revision checklist

- [ ] I can explain the main definitions without looking at the notes.
- [ ] I can reproduce the essential formulae and state their conditions.
- [ ] I can solve the worked examples independently.
- [ ] I can explain why each incorrect quiz option is wrong.
- [ ] I can solve a fresh board-level question and an entrance-style question on this topic.
