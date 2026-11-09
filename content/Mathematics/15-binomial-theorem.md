---
title: Binomial Theorem
level: intermediate
---

## Learning objective

Expand powers of binomials efficiently and identify general terms, coefficients and middle terms.

## Core concepts

- For a non-negative integer n, (x+y)^n=Σ from r=0 to n of C(n,r)x^(n−r)y^r.
- The binomial coefficient C(n,r)=n!/[r!(n−r)!]. It counts selections of r objects from n distinct objects.
- The general term is T_(r+1)=C(n,r)x^(n−r)y^r. Be careful: the index r starts at zero, so it is the (r+1)th term.
- Coefficients are symmetric: C(n,r)=C(n,n−r). Their sum is 2^n.
- For odd n there is one middle term; for even n there are two middle terms.

## Essential formulae and results

(x+y)^n=Σ C(n,r)x^(n−r)y^r.

## Worked examples

**Example 1.** The coefficient of x²y³ in (x+y)^5 is C(5,3)=10.
**Example 2.** The 4th term in (2x+y)^5 is C(5,3)(2x)^2y^3=10×4x²y³=40x²y³.

## Common mistakes to avoid

- The 4th term corresponds to r=3, not r=4.
- Include powers of both terms when finding a coefficient.
- The theorem in this form is for non-negative integer n.

## Exam approach

1. Identify the topic and write down the relevant definition or formula.
2. Check the conditions: domain, non-zero denominators, interval, sign and units where applicable.
3. Show the essential algebraic steps instead of jumping to an answer.
4. Substitute the result into the original condition whenever extraneous solutions are possible.
5. Keep exact values (fractions, radicals and π) until a decimal approximation is requested.

## Quiz

1. The coefficient of x² in (x+2)^4 is:
- [ ] 4
- [ ] 8
- [ ] 16
- [x] 24
> Choose r=2 for x²: C(4,2)×2²=6×4=24. Correct option: 24.

2. The number of terms in (a+b)^7 after expansion is:
- [ ] 7
- [x] 8
- [ ] 14
- [ ] 49
> There are n+1=8 terms before any like terms combine.

3. C(6,2) equals:
- [ ] 12
- [x] 15
- [ ] 20
- [ ] 30
> 6!/(2!4!)=15.
