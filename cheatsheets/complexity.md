# Complexity Cheatsheet

A quick reference for time and space complexity. The goal in interviews and contests
is usually to pick the data structure / algorithm whose complexity comfortably fits
the input constraints.

## Big-O growth, from best to worst

| Notation | Name | Example |
|----------|------|---------|
| `O(1)` | Constant | Hash-map lookup, array index, math formula |
| `O(log n)` | Logarithmic | Binary search, balanced-tree operations |
| `O(n)` | Linear | Single pass over the input, two pointers |
| `O(n log n)` | Linearithmic | Efficient sorting, divide & conquer |
| `O(n²)` | Quadratic | Nested loops over the input, naive pair search |
| `O(n³)` | Cubic | Triple nested loops (e.g. naive matrix multiply) |
| `O(2ⁿ)` | Exponential | Subsets / power set, naive recursion |
| `O(n!)` | Factorial | Permutations, brute-force travelling salesman |

## What input size suggests which complexity

A rough guide assuming ~10⁸ simple operations per second:

| Max `n` | Target complexity |
|---------|-------------------|
| `n ≤ 10` | `O(n!)` / `O(2ⁿ)` is fine |
| `n ≤ 20` | `O(2ⁿ)`, bitmask DP |
| `n ≤ 500` | `O(n³)` |
| `n ≤ 5 000` | `O(n²)` |
| `n ≤ 10⁶` | `O(n log n)` or `O(n)` |
| `n ≤ 10⁸` | `O(n)` / `O(log n)` / `O(1)` |

## Common data-structure operations (Python, average case)

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| `list` (dynamic array) | `O(1)` | `O(n)` | `O(1)` amortized append / `O(n)` middle | `O(n)` |
| `dict` / `set` (hash) | — | `O(1)` | `O(1)` | `O(1)` |
| `collections.deque` | `O(n)` | `O(n)` | `O(1)` both ends | `O(1)` both ends |
| `heapq` (binary heap) | `O(1)` peek | `O(n)` | `O(log n)` push | `O(log n)` pop-min |
| Balanced BST (e.g. `sortedcontainers`) | `O(log n)` | `O(log n)` | `O(log n)` | `O(log n)` |

## Sorting

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Python `sort` / `sorted` (Timsort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes |
| Quicksort | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(log n)` | No |
| Mergesort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes |
| Heapsort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | No |

## Amortized vs worst case

Some operations are cheap *on average* but occasionally expensive: appending to a
Python `list` is `O(1)` amortized (a resize is `O(n)` but happens rarely), and
hash-map operations are `O(1)` average but `O(n)` under adversarial collisions. Quote
the amortized bound, but know the worst case exists.

## Space complexity reminders

- Recursion uses `O(depth)` stack space — a recursive DFS on a degenerate (chain)
  graph is `O(n)` stack.
- An in-place algorithm uses `O(1)` *extra* space beyond the input.
- Memoization trades `O(states)` space for time.
