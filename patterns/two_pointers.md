# Two Pointers

## Description

The **two pointers** pattern uses two indices that walk through a sequence
together, instead of nesting two loops. By moving the pointers based on a simple
rule, many problems that look quadratic (`O(n²)`) collapse to a single linear
(`O(n)`) pass, usually with `O(1)` extra space.

It comes in a few distinct flavors. This document covers five:

- **Opposite Pointers** — one pointer starts at each end and they move toward the
  middle.
- **Fast & Slow Pointers** — two pointers move at different speeds (one writes,
  one reads), used for in-place filtering and cycle detection.
- **Backward Two Pointers (In-place Merge)** — pointers move from the end toward the
  start, used to merge into spare capacity without overwriting unread data.
- **Expand Around Center** — two pointers start together at a center and move
  *outward* in opposite directions, used to grow symmetric structures like
  palindromes.
- **Parallel Pointers (Interleaving)** — one pointer per sequence, both advancing
  left to right, used to scan two inputs at once and build a combined result.

---

## When to recognize this pattern

Reach for two pointers when you see:

- A **sorted** array and a question about a pair/triple summing to a target.
- "Do it **in-place** with `O(1)` extra memory."
- "Remove / keep / dedupe elements and return the new length."
- A symmetric question (palindrome check, reverse, container between two walls).
- "Merge two sorted sequences," especially when one has trailing free space.
- Linked-list questions about cycles, the middle node, or the *k*-th from the end.

---

## Core idea

Maintain an **invariant** about the region the pointers have already processed, and
move whichever pointer keeps that invariant true:

- **Opposite pointers** exploit ordering: if the current pair is too small/large,
  only one direction can possibly improve it, so move that pointer inward and the
  rest of the search space is discarded for free.
- **Fast & slow** separates *reading* from *writing*: the fast (read) pointer scans
  every element; the slow (write) pointer only advances when an element should be
  kept. Everything left of the slow pointer is the finished answer.
- **Backward merge** writes the largest remaining element into the highest empty
  slot. Filling from the back guarantees you never overwrite a value you still need
  to read.
- **Expand around center** is the mirror of opposite pointers: instead of converging,
  the two pointers start adjacent (or on the same index) and step outward while a
  symmetry condition holds. Trying every center gives every palindrome in `O(n²)`
  without the `O(n³)` cost of re-checking each substring from scratch.
- **Parallel pointers** keep one index per input sequence, each advancing
  independently from the left. At every step you pick from one (or both) sequences,
  emit it, and advance only the pointer(s) you consumed — then drain whatever remains.
  It interleaves or merges two sequences in a single linear pass.

---

## Generic template

### 1. Opposite pointers

```text
left  = 0
right = n - 1
while left < right:
    evaluate pair (a[left], a[right])
    if need a larger value:  left  += 1
    elif need a smaller one: right -= 1
    else:                    record / move both
```

### 2. Fast & slow (in-place filter)

```text
slow = 0                      # next position to write a kept element
for fast in range(n):         # fast reads every element
    if keep(a[fast]):
        a[slow] = a[fast]
        slow += 1
return slow                   # length of the kept prefix
```

### 3. Backward two pointers (in-place merge)

```text
i = m - 1                     # last valid element of A
j = n - 1                     # last element of B
k = m + n - 1                 # last slot of A's full capacity
while j >= 0:                 # B must be fully drained
    if i >= 0 and A[i] > B[j]:
        A[k] = A[i]; i -= 1
    else:
        A[k] = B[j]; j -= 1
    k -= 1
```

### 4. Expand around center

```text
def expand(left, right):      # widest symmetric span around this center
    while left >= 0 and right < n and a[left] == a[right]:
        left  -= 1
        right += 1
    return a[left + 1:right]   # pointers overshoot by one on exit

best = ""
for center in range(n):
    best = longer(best, expand(center, center))      # odd-length center
    best = longer(best, expand(center, center + 1))  # even-length center
```

### 5. Parallel pointers (interleaving)

```text
i = j = 0                     # one pointer per input
result = []
while i < len(A) and j < len(B):
    result.append(A[i]); i += 1   # take from A...
    result.append(B[j]); j += 1   # ...then from B (or pick by a rule)
result.extend(A[i:])          # drain whatever remains
result.extend(B[j:])
return combine(result)
```

---

## Complexity

| Variant | Time | Space |
|---------|------|-------|
| Opposite pointers | `O(n)` (plus `O(n log n)` if you must sort first) | `O(1)` |
| Fast & slow filter | `O(n)` | `O(1)` |
| Backward merge | `O(m + n)` | `O(1)` |
| Expand around center | `O(n²)` (n centers × `O(n)` expansion) | `O(1)` |
| Parallel pointers (interleaving) | `O(m + n)` | `O(m + n)` for the combined output |

---

## Common mistakes

- Using `left <= right` when the two pointers must not meet (e.g. pairing distinct
  positions), or `left < right` when the meeting point itself must be visited.
- Moving **both** pointers when the logic only justifies moving one — this skips
  candidate pairs.
- In the in-place filter, comparing against `a[fast - 1]` instead of the last
  *written* element `a[slow - 1]`; the input and the compacted output diverge as you
  go.
- In the backward merge, looping on `i >= 0 and j >= 0` and forgetting that any
  remaining `B` elements still need to be copied. Looping while `j >= 0` (B is the
  only array that lives outside A's original region) avoids the extra cleanup loop.
- Off-by-one on the write index `k` — it must start at `m + n - 1`, the last slot of
  the *full* capacity, not `m + n`.
- In expand-around-center, checking only odd-length centers and missing even-length
  palindromes (you must also expand from `center, center + 1`), or mishandling the
  one-step overshoot when slicing the result (`a[left + 1:right]`).
- In parallel pointers, forgetting to **drain the leftover tail** once the shorter
  sequence is exhausted, or advancing both pointers when only one element was
  consumed — both drop or duplicate characters.

---

## Related LeetCode Problems

### Backward Two Pointers (In-place Merge)

- [088 — Merge Sorted Array](../leetcode/easy/088_merge_sorted_array.py) — the
  canonical example: merge `nums2` into `nums1`'s trailing free space by writing the
  larger element into the highest empty slot.

### Opposite Pointers

- [011 — Container With Most Water](../leetcode/medium/011_container_with_most_water.py)
  — start at both ends; always move the shorter wall inward, since the shorter wall
  is what caps the area.

### Fast & Slow Pointers (in-place filter)

- [026 — Remove Duplicates from Sorted Array](../leetcode/easy/026_remove_duplicates_from_sorted_array.py)
  — write a value only when it differs from the last kept one.
- [027 — Remove Element](../leetcode/easy/027_remove_element.py) — write a value
  only when it is not equal to the target.
- [080 — Remove Duplicates from Sorted Array II](../leetcode/medium/080_remove_duplicates_from_sorted_array_ii.py)
  — same idea, but allow each value at most twice by comparing against `nums[i - 2]`.

### Expand Around Center

- [005 — Longest Palindromic Substring](../leetcode/medium/005_longest_palindromic_substring.py)
  — treat every index (and every gap between indices) as a center, expand outward
  while the characters match, and keep the longest span.

### Parallel Pointers (Interleaving)

- [1768 — Merge Strings Alternately](../leetcode/easy/1768_merge_strings_alternately.py)
  — walk both strings with one pointer each, appending one character from each in turn,
  then append the tail of whichever string is longer.

---

## References

- [LeetCode Explore — Two Pointer Technique](https://leetcode.com/explore/)
- [Sean Prashad — LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)
