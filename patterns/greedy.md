# Greedy

## Description

A **greedy** algorithm builds a solution one step at a time, always taking the choice
that looks best *right now* and never reconsidering it. When the problem has the right
structure, these locally optimal choices add up to a globally optimal answer — without
the bookkeeping of dynamic programming or the cost of exhaustive search.

## When to recognize this pattern

- The task asks for a maximum/minimum count, the longest/shortest arrangement, or a
  yes/no feasibility check, and a single left-to-right pass seems plausible.
- A natural ordering exists (by position, size, deadline, ratio) and processing in
  that order never forces you to undo an earlier decision.
- You can argue an **exchange / stays-ahead** property: swapping in the greedy choice
  never makes the solution worse.
- The problem says "as soon as possible," "at most once," or "without violating a
  local rule."

## Core idea

Define the greedy choice — the single rule applied at each step — and trust it. The
pattern only works when the greedy choice is *safe*: making it can never close off the
optimal solution. That safety usually rests on one of two arguments:

- **Greedy stays ahead:** after each step, the greedy partial solution is at least as
  good as any other partial solution of the same length.
- **Exchange argument:** any optimal solution can be transformed into the greedy one
  by swaps that never reduce its quality.

If neither holds, greedy is likely wrong and the problem needs DP or search instead.

## Generic template

```text
order items by the relevant key      # often the crux of the problem
result = <empty / 0 / True>
for item in items:
    if taking item is locally valid:
        commit to item               # never revisited
        update result
return result
```

## Complexity

| | Time | Space |
|---|------|-------|
| Single pass over pre-ordered input | `O(n)` | `O(1)` |
| When an explicit sort is required first | `O(n log n)` | `O(1)`–`O(n)` |

## Common mistakes

- Assuming greedy works without proving the greedy-choice property — many problems
  *look* greedy but require DP (e.g. 0/1 knapsack).
- Sorting by the wrong key, or forgetting to sort when the choice depends on order.
- Re-evaluating or undoing a committed choice — that is no longer greedy.
- Off-by-one or boundary errors when the "local rule" depends on neighbours (treat
  out-of-bounds neighbours as the permissive case).

## Related LeetCode Problems

- [605 — Can Place Flowers](../leetcode/easy/605_can_place_flowers.py) — scan
  left to right and plant a flower the moment a plot and both of its neighbours are
  empty. Planting as early as possible is the safe greedy choice; it never blocks a
  placement that a later strategy could have made.

## References

- [Greedy algorithm — Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)
