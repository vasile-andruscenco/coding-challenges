# Sliding Window

## Description

The **sliding window** pattern maintains a contiguous range `[left, right]` over a
sequence and slides it forward, expanding on the right and contracting on the left,
to answer questions about the *best* (longest, shortest, or constrained) subarray or
substring. It turns the `O(n²)` "check every subarray" approach into a single `O(n)`
pass, because each element enters and leaves the window at most once.

---

## When to recognize this pattern

- The question is about a **contiguous** subarray or substring (not subsequences).
- You want the **longest / shortest / maximum / minimum** range satisfying a
  constraint ("at most K distinct," "no repeating characters," "sum ≥ target").
- A constraint can be **incrementally maintained** as elements enter and leave: a
  running count, sum, or frequency map.
- The brute force is "try every start and every end."

There are two common shapes:

- **Fixed-size window** — the window length is given; slide it one step at a time.
- **Variable-size window** — grow the right edge greedily; shrink the left edge only
  when the constraint is violated.

---

## Core idea

Keep some aggregate over the current window (a sum, a `set`, or a frequency `dict`).
Advance `right` to include a new element and update the aggregate in `O(1)`. If the
window now violates the constraint, advance `left`, undoing the aggregate for each
removed element, until the window is valid again. Record the best window whenever it
is valid.

The reason this is linear: `left` and `right` each move forward only, never
backward, so together they take at most `2n` steps regardless of how the window
breathes in between.

---

## Generic template

### Variable-size window (longest valid window)

```text
left = 0
state = <empty aggregate>          # set / dict / running sum
best = 0
for right in range(n):
    add a[right] to state
    while constraint is violated:
        remove a[left] from state
        left += 1
    best = max(best, right - left + 1)
return best
```

### Fixed-size window (length k)

```text
window = aggregate of a[0:k]
best = value(window)
for right in range(k, n):
    add a[right] to window
    remove a[right - k] from window
    best = better(best, value(window))
return best
```

---

## Complexity

| | Time | Space |
|---|------|-------|
| Variable / fixed window | `O(n)` | `O(k)` for the window's aggregate (`k` = distinct elements or window size) |

---

## Common mistakes

- Confusing **subarray/substring** (contiguous — window applies) with
  **subsequence** (non-contiguous — window does *not* apply).
- Forgetting to **undo** the aggregate when shrinking from the left; the window state
  must always describe exactly `[left, right]`.
- Using `if` instead of `while` to shrink — one removal may not be enough to restore
  the constraint.
- Recording the answer at the wrong time (before re-validating the window).
- Off-by-one in the window length: it is `right - left + 1`.

---

## Related LeetCode Problems

- [003 — Longest Substring Without Repeating Characters](../leetcode/medium/003_longest_substring_without_repeating_characters.py)
  — variable-size window with a `set` of characters: grow `right`, and shrink `left`
  while the incoming character is already inside the window.

*More sliding-window problems will be linked here as they are solved.*

---

## References

- [LeetCode Explore — Sliding Window](https://leetcode.com/explore/)
- [Sean Prashad — LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)
