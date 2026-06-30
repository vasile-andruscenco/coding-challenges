# Algorithmic Patterns

This folder is the conceptual core of the repository. Each document explains **one**
algorithmic pattern: how to recognize it, the intuition behind it, a generic
template, its complexity, the mistakes people make, and the problems in this
repository that use it.

The rule that keeps everything maintainable:

> **Explain each pattern in exactly one place.** Problems link to patterns;
> patterns link to problems. Never copy an explanation into two documents.

---

## Index

| Pattern | What it solves |
|---------|----------------|
| [Two Pointers](two_pointers.md) | Linear scans with two indices: pair search in sorted data, in-place rewriting, in-place merging, expanding around a center, interleaving two sequences. |
| [Binary Search](binary_search.md) | Logarithmic search over a sorted range *or* over a monotonic answer space. |
| [Hash Map](hash_map.md) | O(1) lookup, frequency counting, complement search, and duplicate detection. |
| [Sliding Window](sliding_window.md) | Optimal contiguous subarray / substring under a constraint. |
| [Array](array.md) | Foundational linear scans with a precomputed global aggregate. |
| [Boyer-Moore Voting](boyer_moore_voting.md) | Strict-majority element in `O(n)` time and `O(1)` space via candidate/count cancellation. |
| [Greedy](greedy.md) | Locally optimal choices that build a global optimum in one pass. |
| [Math](math.md) | Number-theoretic insight: GCD / Euclidean algorithm, formulas, modular arithmetic. |
| [Linked List](linked_list.md) | Pointer rewiring and dummy-head traversal over node chains. |
| [Simulation](simulation.md) | Directly reproducing a described process step by step. |
| [Matrix Traversal](matrix_traversal.md) | Visiting 2-D grid cells in order, with row/column/sub-region index arithmetic. |
| [Stack](stack.md) | LIFO matching of nested structure: the next input resolves the most recent unfinished item. |

---

## Pattern document template

Every pattern document follows this structure so they stay consistent and easy to
scan:

```markdown
# Pattern name

## Description
## When to recognize this pattern
## Core idea
## Generic template
## Complexity
## Common mistakes
## Related LeetCode Problems
## References
```

---

## Maintenance contract

Whenever a **new LeetCode solution** is added to the repository:

1. **Identify the algorithmic pattern(s)** the solution uses.
2. **Update the corresponding pattern document** under `patterns/`.
3. **Add the problem** to that document's *Related LeetCode Problems* section,
   linking to the solution file.
4. If a **new pattern** is discovered, create a new markdown file using the template
   above.
5. **Keep the documentation synchronized** with the codebase (paths, problem
   numbers, links).
6. **Never duplicate explanations** across multiple pattern documents — if two
   patterns share an idea, explain it once and cross-link.

This contract is what lets the repository scale to 300+ problems without turning
into a pile of disconnected files.

---

## Workflow for Adding a New Solution

The maintenance contract above states the rules. This section is the procedure that
enforces them — run it end to end for every newly solved problem. It is a learning
process first and a bookkeeping process second: the goal is a durable understanding
of patterns, not just a larger archive of solutions.

### 1. Solve and place the problem

- Place the file in the correct platform folder: `leetcode/{easy,medium,hard}/`,
  `codewars/`, `codingame/`, or `project_euler/`.
- Follow the naming convention. LeetCode files use the zero-padded official problem
  number followed by the slugified title, e.g. `001_two_sum.py`,
  `088_merge_sorted_array.py`.

### 2. Follow the solution conventions

Every solution file is structured the same way:

- A standard module docstring containing, in order:
  - the official problem URL,
  - a short description,
  - `Args` / `Returns`,
  - worked examples,
  - the constraints.
- A `Solution` class matching the judge's expected signature.
- Type hints on the public method(s).
- A small runnable demo block (`if __name__ == "__main__":` or an equivalent guard)
  that exercises the solution.

### 3. Identify the algorithmic pattern

Ask the defining question:

> **What algorithmic pattern does this problem use?**

Typical answers: Hash Map, Binary Search, Two Pointers, Sliding Window, DFS, BFS,
Dynamic Programming, Greedy, Heap, Backtracking, and so on. A problem may use more
than one.

### 4. Understand the pattern

Solving the problem is not the goal — understanding *why* the solution works is.
This is the step the repository exists for: the pattern matters more than the
individual problem. Before touching any documentation, answer:

- Why does this algorithm work?
- What is the key insight?
- What transforms the brute-force solution into the optimal one?
- What recognition signals would help identify this pattern in another problem?
- Could I implement this solution again from memory, without looking at the code?

If these questions cannot be answered confidently, the learning process is not yet
complete.

### 5. Update the pattern documentation

- If the pattern **already exists**, add the problem to that document's *Related
  LeetCode Problems* section, linking to the solution file with a one-line note on
  how the pattern applies.
- If the pattern **does not exist**, create a new document under `patterns/` using
  the [pattern document template](#pattern-document-template), and add it to the
  [Index](#index).
- Never duplicate explanations across pattern documents — explain once, cross-link
  everywhere else.

### 6. Update the cheatsheets (only if something new was learned)

Add to `cheatsheets/` only when the problem taught something reusable:

- a Python language trick,
- a useful standard-library module,
- a new complexity insight,
- an improvement to a generic pseudocode snippet.

Skip this step when nothing new was learned.

### 7. Verify consistency

- All links resolve.
- File names follow the naming convention.
- Pattern references (problem → pattern and pattern → problem) are correct and
  mutual.
- Documentation is synchronized with the code (paths, problem numbers, signatures).

### 8. Commit

Use a commit message that names both the problem and the algorithmic pattern, so the
history reads as a learning log. Follow this convention consistently:

```
Solve LeetCode 088 using Backward Two Pointers pattern
Add LeetCode 167 solution (Two Pointers)
```

---

## Solution Checklist

Copy this checklist into the pull request or commit notes for each new solution:

- [ ] Problem solved
- [ ] Solution follows repository conventions
- [ ] Pattern identified
- [ ] Pattern fully understood
- [ ] Able to explain the key insight
- [ ] Pattern documentation updated
- [ ] Cheatsheets updated (if needed)
- [ ] Links verified
- [ ] Documentation synchronized
- [ ] Ready to commit
