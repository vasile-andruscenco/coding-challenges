# Binary Search

## Description

**Binary search** finds a target in a sorted range by repeatedly halving the search
space. Each comparison discards half of the remaining candidates, so a range of size
`n` is resolved in `O(log n)` steps.

The pattern generalizes well beyond "find this number in this array." Any time you
can frame a problem as *"find the boundary where a monotonic condition flips from
False to True,"* binary search applies — including **searching on the answer** itself.

---

## When to recognize this pattern

- The data is **sorted**, or can be sorted cheaply, and you need a value or its
  position.
- The problem asks for a **boundary**: first/last element satisfying a condition,
  insertion point, lower/upper bound.
- The answer is a number in a known range, and there is a **monotonic predicate**
  `feasible(x)` such that once it becomes True it stays True (or vice versa). This is
  *binary search on the answer*.
- The naive solution is `O(n)` per query and you need `O(log n)`.

---

## Core idea

Keep a window `[left, right]` that is guaranteed to contain the answer. Probe the
middle, decide which half can still contain the answer, and shrink the window to
that half. The whole technique is really about choosing the **comparison** and the
**pointer updates** so that:

1. the window always still contains the answer (the invariant), and
2. the window strictly shrinks every iteration (so it terminates).

The classic search returns as soon as it lands on the target. The *boundary*
variants never return early — they record the best candidate seen so far and keep
shrinking toward the edge, because a better candidate may still lie to one side.

Always compute the midpoint as `mid = left + (right - left) // 2` to avoid integer
overflow in languages with fixed-width ints, and as a consistent habit.

---

## Generic template

### Classic binary search (exact match)

```text
left, right = 0, n - 1
while left <= right:
    mid = left + (right - left) // 2
    if a[mid] == target: return mid
    elif a[mid] < target: left  = mid + 1
    else:                 right = mid - 1
return -1
```

### Search on the answer (monotonic predicate)

```text
left, right = lo, hi          # range of possible answers
best = <sentinel>
while left <= right:
    mid = left + (right - left) // 2
    if feasible(mid):
        best = mid            # mid works; try to push further
        left = mid + 1        # (or right = mid - 1, depending on direction)
    else:
        right = mid - 1
return best
```

### Boundary variants

All four record a `result` on a match and then *keep going* toward the wanted edge:

```text
# first occurrence            on a[mid] == target: result = mid; right = mid - 1
# last occurrence             on a[mid] == target: result = mid; left  = mid + 1
# first element >= target     on a[mid] >= target: result = mid; right = mid - 1
# last element  <= target     on a[mid] <= target: result = mid; left  = mid + 1
```

Each of these is implemented and documented in
[`leetcode/algo_practice.py`](../leetcode/algo_practice.py).

---

## Complexity

| | Time | Space |
|---|------|-------|
| All variants (iterative) | `O(log n)` | `O(1)` |
| Recursive form | `O(log n)` | `O(log n)` call stack |
| Search on the answer | `O(log(range) × cost(feasible))` | depends on `feasible` |

---

## Common mistakes

- **Wrong loop condition.** `while left <= right` (inclusive `right`) pairs with
  `right = mid - 1`. `while left < right` (exclusive `right`) pairs with
  `right = mid`. Mixing the two causes infinite loops or off-by-one bugs.
- **Returning early in boundary searches.** For first/last occurrence you must
  *record and continue*, not return on the first match.
- **Forgetting the overflow-safe midpoint** `left + (right - left) // 2`.
- **Non-monotonic predicate** in "search on the answer": if `feasible` is not
  monotonic, binary search is simply not applicable.
- **Empty-range handling**: make sure `left`/`right` are initialized so an empty
  input returns the right sentinel (`-1`, or the insertion index).

---

## Related LeetCode Problems

- [035 — Search Insert Position](../leetcode/easy/035_search_insert_position.py) —
  classic search that returns `left` when the target is absent, i.e. the insertion
  point (a *first element ≥ target* boundary in disguise).
- [069 — Sqrt(x)](../leetcode/easy/069_sqrt_x.py) — *search on the answer*: the
  predicate `mid * mid <= x` is monotonic, so binary-search the largest `mid` that
  satisfies it.

Supporting practice (binary-search variants implemented directly):

- [`leetcode/algo_practice.py`](../leetcode/algo_practice.py) — first/last occurrence,
  first ≥ target, last ≤ target, existence check, and integer square root.

---

## References

- [LeetCode Explore — Binary Search](https://leetcode.com/explore/learn/card/binary-search/)
- [Python `bisect` module](https://docs.python.org/3/library/bisect.html)
