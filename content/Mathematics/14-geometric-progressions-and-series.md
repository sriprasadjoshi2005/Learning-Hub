---
title: Geometric Progressions and Series
level: intermediate
---

## Learning objective

Study sequences with a constant ratio, finite geometric sums and the condition for an infinite sum.

## Core concepts

- A geometric progression (GP) has a constant ratio r between consecutive terms, provided the preceding term is non-zero.
- The nth term is a_n=ar^(n−1). The finite sum for r≠1 is S_n=a(r^n−1)/(r−1), equivalently a(1−r^n)/(1−r).
- If r=1, S_n=na. The infinite GP sum exists for real r only when |r|<1, and then S_∞=a/(1−r).
- A negative common ratio produces alternating signs. A ratio with magnitude greater than one produces terms whose magnitudes grow, unless a=0.
- Applications include repeated percentage growth/decay, bouncing objects under an idealised constant rebound ratio and recurring fractions.

## Essential formulae and results

GP: a_n=ar^(n−1); S_n=a(1−r^n)/(1−r); S∞=a/(1−r) if |r|<1.

## Worked examples

**Example 1.** For 3, 6, 12, 24, ..., a=3 and r=2. The 6th term is 3×2^5=96.
**Example 2.** For 8+4+2+1+..., r=1/2, so S_∞=8/(1−1/2)=16.

## Common mistakes to avoid

- Do not use the infinite-sum formula when |r|≥1.
- For r<0, retain the sign in powers and in the denominator.
- The finite formula is not valid as written at r=1; use S_n=na.

## Exam approach

1. Identify the topic and write down the relevant definition or formula.
2. Check the conditions: domain, non-zero denominators, interval, sign and units where applicable.
3. Show the essential algebraic steps instead of jumping to an answer.
4. Substitute the result into the original condition whenever extraneous solutions are possible.
5. Keep exact values (fractions, radicals and π) until a decimal approximation is requested.

## Quiz

1. The 5th term of 2, 6, 18, ... is:
- [ ] 54
- [ ] 108
- [x] 162
- [ ] 486
> a_5=2×3^4=162.

2. The infinite sum of 6+3+1.5+... is:
- [ ] 9
- [x] 12
- [ ] 15
- [ ] ∞
> a=6, r=1/2, so S∞=6/(1−1/2)=12.

3. An infinite real GP has a finite sum when:
- [ ] r>1
- [ ] r<−1
- [x] |r|<1
- [ ] r=1
> The terms must approach zero; this occurs for |r|<1.
