# Linked List

## Description

A **linked list** stores elements as nodes, each holding a value and a reference to the
next node. Without random access, the toolkit is pointer manipulation: walking node by
node, rewiring `next` references, and using a **dummy head** to simplify edge cases.
Many list problems are traversals that build a new list while carrying some state along
the way.

## When to recognize this pattern

- The input or output is a chain of `ListNode`s rather than an array.
- The operation is sequential — merge, reverse, add, partition — and you only ever
  need the *current* and *next* nodes.
- You must build a result list whose length is not known in advance.
- Index-based array tricks do not apply because there is no `O(1)` random access.

## Core idea

Use a **dummy head** node that sits before the real first node, and a moving `tail`
pointer that always points at the last node built so far. Appending is then uniform —
no special case for the first element — and the answer is simply `dummy.next`. When the
traversal carries state (a running carry, a comparison, a toggle), update that state
once per node as you advance.

## Generic template

```text
dummy = ListNode()        # sentinel before the head
tail  = dummy
state = <initial>         # e.g. carry = 0

while nodes remain or state is non-trivial:
    value, state = combine(current nodes, state)
    tail.next = ListNode(value)
    tail = tail.next
    advance the input pointers

return dummy.next         # skip the sentinel
```

## Complexity

| | Time | Space |
|---|------|-------|
| Single traversal building a result list | `O(n)` | `O(1)` extra (plus the `O(n)` output list) |

## Common mistakes

- Not using a dummy head, then writing fragile special-case code for the first node.
- Losing the rest of the list by overwriting a `next` pointer before saving it.
- Forgetting to flush trailing state — e.g. a final `carry` of 1 needs one more node.
- Returning `dummy` instead of `dummy.next`, leaking the sentinel into the result.
- Creating a cycle by pointing a node back at an earlier one.

## Related LeetCode Problems

- [002 — Add Two Numbers](../leetcode/medium/002_add_two_numbers.py) — digits are
  stored in reverse order, so a single forward walk adds corresponding digits with a
  running **carry** (elementary-school addition), appending each result digit behind a
  dummy head and emitting a final node when a carry remains.

## References

- [Linked list — Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
