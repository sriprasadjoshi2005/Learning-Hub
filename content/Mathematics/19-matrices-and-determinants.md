---
title: Matrices and Determinants
level: intermediate
lesson: 19
subject: Mathematics
---

# Lesson 19: Matrices and Determinants

## Learning objective

Learn matrix notation, operations, determinants and inverse matrices, with applications to simultaneous linear equations.

## Core concepts

- A matrix is a rectangular array. Its order is rows × columns. Addition requires equal orders; multiplication AB requires columns of A to equal rows of B.
- Matrix multiplication is generally not commutative: AB may differ from BA. The identity matrix I satisfies AI=IA=A when defined.
- For A=[[a,b],[c,d]], det(A)=ad−bc. A 2×2 matrix is invertible exactly when its determinant is non-zero.
- For a 2×2 matrix, A⁻¹=(1/det A)[[d,−b],[−c,a]].
- A system of linear equations can be written AX=B. If A is square and invertible, X=A⁻¹B.

## Essential formulae and results

For [[a,b],[c,d]], det=ad−bc; inverse exists iff det≠0.

## Worked examples

**Example 1.** For A=[[1,2],[3,4]], det A=1×4−2×3=−2, so A is invertible.
**Example 2.** If A=[[2,1],[1,1]], then det A=1 and A⁻¹=[[1,−1],[−1,2]].

## Common mistakes to avoid

- Do not multiply matrices entry by entry; use row-by-column products.
- A zero determinant means no inverse, not that every related equation has no solution.
- Check matrix dimensions before attempting a product.

## Exam approach

1. Identify the topic and write down the relevant definition or formula.
2. Check the conditions: domain, non-zero denominators, interval, sign and units where applicable.
3. Show the essential algebraic steps instead of jumping to an answer.
4. Substitute the result into the original condition whenever extraneous solutions are possible.
5. Keep exact values (fractions, radicals and π) until a decimal approximation is requested.

## Quick quiz

**1. The determinant of [[2,3],[1,4]] is:**
- [x] 5
- [ ] 8
- [ ] 11
- [ ] −5
> **Explanation:** 2×4−3×1=5.

**2. If A is 2×3 and B is 3×4, AB has order:**
- [ ] 3×3
- [x] 2×4
- [ ] 4×2
- [ ] 2×3
> **Explanation:** The inner dimensions match and the result uses the outer dimensions.

**3. A square matrix is invertible if its determinant is:**
- [ ] Zero
- [x] Non-zero
- [ ] One row
- [ ] Negative only
> **Explanation:** A square matrix has an inverse exactly when its determinant is non-zero.


## Revision checklist

- [ ] I can explain the main definitions without looking at the notes.
- [ ] I can reproduce the essential formulae and state their conditions.
- [ ] I can solve the worked examples independently.
- [ ] I can explain why each incorrect quiz option is wrong.
- [ ] I can solve a fresh board-level question and an entrance-style question on this topic.
