# Boyer-Moore Voting

## Description

The **Boyer-Moore Voting** algorithm finds the element that occupies *more than half*
of an array in a single linear pass using only two variables — a `candidate` and a
`count`. It is the constant-space refinement of the naive "count every element"
approach: instead of a frequency table (see [Hash Map](hash_map.md)), it lets occurrences
of the same value reinforce a running candidate while different values cancel it out.
It is a specialised member of the [Array](array.md) single-pass family.

## When to recognize this pattern

- The problem guarantees (or asks you to assume) a **strict majority** element — one
  that appears more than `n // 2` times.
- You are asked for `O(n)` time **and** `O(1)` space, ruling out a hash-map count or a
  sort. This is the classic "follow-up" framing.
- The answer depends only on *which* value dominates, not on its positions or counts.
- A generalisation appears: "find all elements appearing more than `n // k` times"
  (the same cancellation idea, tracked with `k - 1` candidates).

## Core idea

Pair up and discard. Whenever two **different** values meet, cancel them against each
other — neither can be the strict majority on its own, and removing a matched pair
leaves the majority element still in the majority among the rest. After all
cancellations, only the majority value can survive.

Operationally this is tracked without actually removing anything:

- `count == 0` means everything so far has cancelled out, so adopt the current value as
  the new `candidate`.
- A value equal to `candidate` reinforces it (`count += 1`); any other value cancels
  one occurrence (`count -= 1`).

Because the majority element appears more than `n // 2` times, the cancellations can
never zero it out permanently — it is left standing as the final `candidate`.

> Note: the algorithm only *guarantees* a correct answer when a strict majority is
> known to exist. Without that guarantee, the survivor is merely a candidate and needs
> a second pass to verify its count actually exceeds `n // 2`.

## Generic template

```text
candidate = None
count = 0
for value in values:
    if count == 0:
        candidate = value          # adopt a fresh candidate
    count += 1 if value == candidate else -1
return candidate                   # verify with a second pass if majority is not guaranteed
```

## Complexity

| | Time | Space |
|---|------|-------|
| Single pass, two scalars | `O(n)` | `O(1)` |

## Common mistakes

- Applying it when no strict majority is guaranteed and skipping the verification pass —
  the survivor can then be a non-majority value.
- Updating `count` before (re)adopting the candidate, so the `count == 0` reset misfires.
- Confusing "majority" (`> n // 2`) with "most frequent" (plurality) — Boyer-Moore
  solves the former, not the latter.
- Reaching for a hash-map frequency count out of habit and losing the `O(1)` space that
  is the whole point of the pattern.

## Related LeetCode Problems

- [169 — Majority Element](../leetcode/easy/169_majority_element.py) — adopt a new
  candidate whenever the running count hits zero, then increment on a match and
  decrement otherwise. The guaranteed strict majority means the final candidate is the
  answer with no verification pass needed.

## References

- [Boyer-Moore majority vote algorithm — Wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
