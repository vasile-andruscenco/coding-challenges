# Math

## Description

Some problems are solved less by data-structure manipulation and more by a **number-
theoretic or algebraic insight**. Recognizing the underlying mathematical property —
a divisibility rule, a closed-form formula, modular arithmetic, the greatest common
divisor — collapses what looks like a search into a handful of arithmetic operations.

This document focuses on the recurring tool that shows up most often in this
repository: the **Euclidean algorithm** for the greatest common divisor (GCD).

## When to recognize this pattern

- The answer is a count, length, or period that must *divide* some quantity.
- The problem involves repetition or tiling: "X is a concatenation/multiple of Y."
- Brute force iterates over divisors, factors, or multiples — a formula may replace
  the loop.
- Words like *greatest common divisor*, *least common multiple*, *modulo*, *prime*,
  or *digits* appear.

## Core idea

The **Euclidean algorithm** computes `gcd(a, b)` from the fact that any common divisor
of `a` and `b` also divides `a mod b`. Repeatedly replacing `(a, b)` with
`(b, a mod b)` shrinks the pair until the remainder is zero; the last non-zero value is
the GCD. It runs in `O(log(min(a, b)))` — far faster than trial division.

The GCD frequently answers "what is the largest repeating unit?" questions: the size
of the largest block that tiles two lengths is exactly `gcd` of those lengths.

## Generic template

```text
# Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

```text
# LCM in terms of GCD
def lcm(a, b):
    return a // gcd(a, b) * b      # divide first to avoid overflow
```

## Complexity

| | Time | Space |
|---|------|-------|
| Euclidean GCD | `O(log(min(a, b)))` | `O(1)` iterative |
| Most closed-form / modular tricks | `O(1)`–`O(log n)` | `O(1)` |

## Common mistakes

- Reinventing GCD with slow trial division instead of the Euclidean recurrence.
- Integer-overflow in LCM: compute `a // gcd * b`, not `a * b // gcd` (less relevant
  in Python's big integers, but a good habit).
- Forgetting the base/edge cases: `gcd(x, 0) == x`; guard against division by zero.
- Skipping the necessary *precondition* check before applying a formula (e.g.
  confirming a common structure exists at all).

## Related LeetCode Problems

- [1071 — Greatest Common Divisor of Strings](../leetcode/easy/1071_greatest_common_divisor_of_strings.py)
  — a common divisor string exists only if `str1 + str2 == str2 + str1`; when it does,
  the answer's length is `gcd(len(str1), len(str2))`, so the string GCD reduces
  directly to the numeric GCD.

## References

- [Euclidean algorithm — Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Python `math.gcd`](https://docs.python.org/3/library/math.html#math.gcd)
