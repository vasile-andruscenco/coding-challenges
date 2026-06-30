# Stack

## Description

A **stack** is a last-in, first-out (LIFO) container: the most recently added item is
the first one removed. As a pattern it shines whenever the *most recent* unfinished
thing is exactly what the next input must resolve — matching brackets, undo history,
backtracking a path, or evaluating nested expressions. In Python a plain `list` is the
stack: `append` to push, `pop` to remove the top.

## When to recognize this pattern

- The input is **nested or recursively structured** — brackets, tags, function calls,
  directory paths — and correctness depends on closing the *innermost* item first.
- You must match each element against the **most recent** unmatched element, not an
  arbitrary one.
- A problem mentions "balanced", "valid nesting", "innermost", "previous", or "undo".
- You are simulating recursion or a traversal iteratively and need to remember where to
  return to.

## Core idea

Push work that is *not yet resolved*; pop the moment the current input resolves the top
of the stack. Because the stack always exposes the most recent pending item, each new
element only ever needs to consult the top — an `O(1)` check — instead of scanning
everything seen so far. When the input is fully consumed, an **empty stack** usually
means everything was matched/resolved; a non-empty stack means something was left open.

## Generic template

```text
stack = []
for item in input:
    if item opens / defers work:
        push(item)
    elif item closes / resolves work:
        if stack is empty or top doesn't match item:
            return invalid
        pop()
    # else: handle items that need no stack
return stack is empty        # nothing left unresolved
```

## Complexity

| | Time | Space |
|---|------|-------|
| Single pass, each item pushed/popped at most once | `O(n)` | `O(n)` worst case |

## Common mistakes

- Popping from an empty stack — always check `if not stack` before `pop()`.
- Forgetting the final emptiness check, so unmatched *open* items (e.g. `"((("`) are
  wrongly accepted.
- Matching against the wrong end — using the bottom or scanning the whole stack instead
  of only the top.
- Pushing the closing token instead of mapping it back to the expected opener, which
  complicates the comparison.

## Related LeetCode Problems

- [20 — Valid Parentheses](../leetcode/easy/020_valid_parentheses.py) — push every
  opening bracket; on a closing bracket, fail fast if the stack is empty or its top is
  not the matching opener. A string is valid only if the stack is empty at the end.

## References

- [Stack (abstract data type) — Wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
