# Simulation

## Description

A **simulation** solves the problem by directly reproducing the process it describes,
step by step, rather than deriving a shortcut. The skill is faithful modeling: track
the right state, advance it by the stated rules, and read the answer off the final
state. These problems test careful implementation more than algorithmic cleverness.

## When to recognize this pattern

- The statement describes a *procedure*, *movement*, or *transformation* and asks for
  its end result ("write the characters in a zigzag, then read them off row by row").
- There is no obvious formula, but the rules are concrete and bounded.
- The input size is small enough that mimicking the process directly is fast enough.
- Words like *traverse*, *rotate*, *iterate*, *until*, or step-by-step examples
  dominate the prompt.

## Core idea

Model exactly the state the process needs — and nothing more — then apply the rules in
a loop. The two recurring decisions are **what to store** (the minimal state: a set of
buckets, a position plus a direction, a grid) and **how to advance it** (the update
rule per step). Choosing compact state and a clean update keeps an otherwise fiddly
problem manageable.

## Generic template

```text
state = initial_state()        # buckets / position / direction / grid
for step in process:
    state = apply_rule(state, step)
    if at a boundary:
        adjust direction / wrap / reset
return read_result(state)
```

## Complexity

| | Time | Space |
|---|------|-------|
| One pass over the process | `O(n)` | `O(n)` for the modeled state (often `O(1)`–`O(rows)`) |

## Common mistakes

- Modeling more state than necessary (e.g. a full 2-D grid when a list of rows
  suffices), making the code harder and slower.
- Mishandling **boundary transitions** — reversing direction one step too early or
  late, or failing to wrap.
- Missing trivial fast-paths that the rules degenerate to (e.g. a single row, or a
  width that exceeds the input length).
- Reading the result in the wrong order relative to how it was written.

## Related LeetCode Problems

- [006 — Zigzag Conversion](../leetcode/medium/006_zigzag_conversion.py) — keep one
  string buffer per row and a `going_down` direction flag; append each character to the
  current row, flip direction at the top and bottom rows, and finally concatenate the
  rows. The early-out for `numRows == 1` (or wider than the string) avoids the boundary
  logic entirely.

## References

- [Simulation — competitive-programming overview](https://cp-algorithms.com/)
