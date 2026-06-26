# Hash Map

## Description

A **hash map** (Python `dict`, or `set` when you only need keys) trades memory for
speed: it turns an `O(n)` linear scan for "have I seen this?" into an average `O(1)`
lookup. A great many problems that look quadratic become linear simply by
remembering what you have already encountered.

This document covers four closely related uses:

- **Lookup** — record values you have seen so you can test membership instantly.
- **Frequency counting** — map each value to how often it appears.
- **Complement lookup** — for pair problems, store values and look for the *missing
  partner* in one pass.
- **Duplicate Detection with Sets** — track seen values within a constrained context
  (a row, column, box, window, or group) to catch a repeat the moment it occurs.

---

## When to recognize this pattern

- "Have I seen X before?" / "Are there duplicates?" / "Is this an anagram?"
- "Find two items that combine to a target" (sum, product, difference).
- "Count occurrences" / "most frequent" / "group by some key."
- You are tempted to write a nested loop just to find a matching earlier element.
- You need to compare two collections by *contents* rather than order.

---

## Core idea

A hash map answers membership and association questions in (amortized) constant
time. The three uses are variations on what you store as the **value**:

- **Lookup:** store nothing meaningful (use a `set`) — presence is the answer.
- **Frequency counting:** store a running count. `dict.get(k, 0) + 1` or
  `collections.Counter` does this idiomatically.
- **Complement lookup:** while scanning, for each element compute the partner you
  *would need* (`target - num`) and check whether you have already stored it. If yes,
  you found the pair in a single pass; if no, store the current element and move on.
- **Duplicate detection with sets:** keep a `set` of values already seen within each
  constrained context and report a violation the instant an insert would collide. When
  several constraints apply at once (a grid cell belongs to a row, a column, *and* a
  box), encode the context in a composite key — e.g. `(value, "row", r)` — so one set
  covers them all.

The complement trick is the key insight: instead of searching the *rest* of the array
for a match (the `O(n²)` instinct), you ask the map whether the match has *already
gone by*.

---

## Generic template

### Complement lookup (pair-sum)

```text
seen = {}                       # value -> index
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Frequency counting

```text
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1
# or: freq = collections.Counter(items)
```

### Membership / duplicate detection

```text
seen = set()
for x in items:
    if x in seen:
        return True            # duplicate found
    seen.add(x)
return False
```

### Duplicate detection with sets (constrained context)

```text
seen = set()                    # composite keys keep contexts separate
for r, c, value in filled_cells:
    keys = ((value, "row", r),
            (value, "col", c),
            (value, "box", r // 3, c // 3))
    if any(k in seen for k in keys):
        return False            # value repeats within some context
    seen.update(keys)
return True
```

---

## Complexity

| Operation | Average | Worst case |
|-----------|---------|------------|
| Insert / lookup / delete | `O(1)` | `O(n)` (pathological hashing) |
| One pass over `n` items | `O(n)` | `O(n²)` worst case, effectively `O(n)` |

Space is `O(k)` where `k` is the number of distinct keys stored.

---

## Common mistakes

- **Storing before checking** in complement lookup. Check for the complement *first*,
  then insert the current value — otherwise an element can match itself (e.g. target
  `= 2 * num`).
- Using a value (rather than index) as the map value when the problem asks for
  **positions**.
- Comparing frequency *dictionaries* directly when the question is about the
  *multiset of counts*; compare `sorted(freq.values())` instead (see Close Strings).
- Forgetting that `dict`/`set` membership is `O(1)` **average**, not guaranteed — fine
  for interviews, worth noting for adversarial inputs.
- Mutating a dict while iterating over it.

---

## Related LeetCode Problems

- [001 — Two Sum](../leetcode/easy/001_two_sum.py) — the canonical complement lookup:
  store `value → index`, and for each number check whether `target - num` is already
  in the map.
- [1657 — Determine if Two Strings Are Close](../leetcode/medium/1657_determine_if_two_strings_are_close.py)
  — frequency counting plus set comparison: the strings are "close" iff they share the
  same character set and the same multiset of frequencies.
- [036 — Valid Sudoku](../leetcode/medium/036_valid_sudoku.py) — duplicate detection
  with sets across three constrained contexts at once: a digit is invalid if it
  repeats within its row, its column, or its 3 x 3 box, tracked via composite keys.

---

## References

- [Python `collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Python `dict` documentation](https://docs.python.org/3/library/stdtypes.html#dict)
