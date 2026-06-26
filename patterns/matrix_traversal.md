# Matrix Traversal

## Description

**Matrix traversal** is the access pattern for visiting the cells of a 2-D grid in a
controlled order — row by row, column by column, or region by region. It is rarely the
whole solution; instead it is the *scaffold* that carries another pattern (hash-map
duplicate detection, dynamic programming, flood fill) across two dimensions. The skill
is the index arithmetic: mapping a cell `(r, c)` to the row, column, and sub-region it
belongs to.

## When to recognize this pattern

- The input is a 2-D grid / board / image and every cell must be examined.
- Cells are grouped into **sub-regions** addressed by arithmetic (3 x 3 boxes, tiles,
  quadrants) rather than by a separate data structure.
- The task references rows, columns, diagonals, neighbours, or boundaries.
- You need a stable visiting order to combine with another pattern applied per cell.

## Core idea

Iterate the grid with a double loop and derive every coordinate you need from `(r, c)`
by arithmetic — no auxiliary bookkeeping:

- **Row / column index:** `r` and `c` themselves.
- **Sub-box index:** `(r // k, c // k)` for `k x k` blocks (e.g. `k = 3` for Sudoku).
- **Neighbours:** `(r ± 1, c)` and `(r, c ± 1)`, guarded against the borders.

The traversal only *delivers* each cell in order; the actual decision per cell belongs
to whatever pattern you layer on top. To avoid duplicating that logic here, see the
patterns it most often composes with — e.g. duplicate detection across rows, columns,
and boxes is documented under [Hash Map → Duplicate Detection with Sets](hash_map.md).

## Generic template

```text
rows, cols = len(grid), len(grid[0])
for r in range(rows):
    for c in range(cols):
        value = grid[r][c]
        box = (r // 3, c // 3)        # sub-region key, when needed
        process(value, r, c, box)     # delegate to the layered pattern
```

## Complexity

| | Time | Space |
|---|------|-------|
| Visiting every cell of an `m x n` grid | `O(m · n)` | `O(1)` for the traversal itself |

(For a fixed board such as 9 x 9 Sudoku, `m · n` is constant, so the traversal is
effectively `O(1)`.)

## Common mistakes

- Confusing row and column indices, or assuming the grid is square when it is `m x n`.
- Off-by-one or out-of-bounds errors at the borders when reading neighbours — guard
  every neighbour access.
- Wrong sub-region arithmetic (`r // 3` vs `r % 3`): integer **division** selects the
  block, the remainder selects the position within it.
- Letting the traversal carry heavy per-cell logic inline instead of delegating to a
  clearly named helper / pattern.

## Related LeetCode Problems

- [036 — Valid Sudoku](../leetcode/medium/036_valid_sudoku.py) — a single row-major
  pass over the 9 x 9 board, mapping each cell to its row, column, and `(r // 3, c // 3)`
  box; the per-cell check is duplicate detection with sets
  ([Hash Map](hash_map.md)).

## References

- [Row- and column-major order — Wikipedia](https://en.wikipedia.org/wiki/Row-_and_column-major_order)
