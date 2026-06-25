# Array

## Description

The **array** pattern covers the foundational linear-scan techniques: walking a
sequence once, optionally after precomputing an aggregate (a maximum, a sum, a count),
and producing a result in a single pass. Many "easy" problems are exactly this — no
auxiliary data structure, just disciplined iteration. More specialised array
techniques (two pointers, sliding window, binary search) have their own documents;
this one is the baseline they build on.

## When to recognize this pattern

- Every element must be examined, and the answer depends on each element's relation to
  a **global property** of the array (its max, min, total, average).
- The work per element is `O(1)` once that global property is known.
- A first pass computes something, and a second pass uses it — or both fuse into one.
- No ordering, pairing, or windowing is required; a plain loop suffices.

## Core idea

Separate **what you need to know about the whole array** from **the per-element
decision**. If the per-element test references a global aggregate (e.g. "is this the
largest?"), compute that aggregate first — usually in `O(n)` — then make every decision
in `O(1)`. The result is two linear passes, which is still `O(n)`, instead of an
`O(n²)` "compare each element with every other" loop.

## Generic template

```text
# Precompute the global property, then decide per element.
aggregate = reduce(values)        # e.g. max(values), sum(values)
result = [decide(x, aggregate) for x in values]
return result
```

## Complexity

| | Time | Space |
|---|------|-------|
| Precompute aggregate + per-element pass | `O(n)` | `O(1)` extra (plus `O(n)` output) |

## Common mistakes

- Recomputing the global aggregate inside the loop, turning an `O(n)` solution into
  `O(n²)`.
- Mutating the array while iterating in a way that invalidates the precomputed
  aggregate.
- Off-by-one errors at the first/last index when the decision looks at neighbours.
- Allocating an output list when an in-place update or a running counter would do.

## Related LeetCode Problems

- [1431 — Kids With the Greatest Number of Candies](../leetcode/easy/1431_kids_with_the_greatest_number_of_candies.py)
  — compute the current maximum once, then map each child to whether `candies[i] +
  extra >= max`. One reduction plus one linear pass.

## References

- [Python list documentation](https://docs.python.org/3/tutorial/datastructures.html)
