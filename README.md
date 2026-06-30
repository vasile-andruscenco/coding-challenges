# Coding Challenges

A personal, pattern-driven handbook for learning algorithms and data structures in
Python — and a growing archive of solved competitive-programming problems.

The repository has two complementary goals:

1. **A solution archive** — clean, documented solutions to problems from multiple
   online judges.
2. **A knowledge base** — reusable explanations of the *patterns* behind those
   solutions, so the focus stays on understanding rather than memorizing.

> The guiding principle: **patterns reference problems, and problems reference
> patterns.** Every explanation lives in exactly one place and is linked from
> everywhere else.

---

## Supported platforms

| Platform | Folder | Notes |
|----------|--------|-------|
| [LeetCode](https://leetcode.com/) | [`leetcode/`](leetcode/) | Split by difficulty: `easy/`, `medium/`, `hard/`. |
| [CodeWars](https://www.codewars.com/) | [`codewars/`](codewars/) | Kata solutions. |
| [CodinGame](https://www.codingame.com/) | [`codingame/`](codingame/) | Puzzle and bot solutions. |
| [Project Euler](https://projecteuler.net/) | [`project_euler/`](project_euler/) | Math-heavy problems. |

---

## Repository structure

```
coding-challenges/
│
├── codewars/              # CodeWars kata
├── codingame/             # CodinGame puzzles
├── project_euler/         # Project Euler problems
│
├── leetcode/
│   ├── easy/
│   ├── medium/
│   └── hard/
│
├── patterns/              # The "why": one document per algorithmic pattern
│   ├── README.md
│   ├── hash_map.md
│   ├── binary_search.md
│   ├── two_pointers.md
│   └── sliding_window.md
│
├── cheatsheets/           # Quick references
│   ├── complexity.md
│   ├── python_tricks.md
│   └── common_templates.md
│
└── README.md
```

---

## How problems are organized

LeetCode solutions are named with the official problem number, zero-padded to
three digits, followed by the slugified title:

```
001_two_sum.py
026_remove_duplicates_from_sorted_array.py
069_sqrt_x.py
088_merge_sorted_array.py
```

This keeps the files sorted by problem number and makes any solution easy to find.
Each file follows the same layout:

1. A module docstring with the **problem URL**, a short description, `Args` /
   `Returns`, worked **examples**, and the **constraints**.
2. A `Solution` class matching the LeetCode signature, with type hints.
3. Inline comments only where they add value.
4. A small runnable demo block at the bottom.

---

## Learning methodology

The repository is built around recognizing and reusing patterns rather than
recalling individual solutions:

1. **Read the pattern first.** Before (or after) solving a problem, read the
   relevant document in [`patterns/`](patterns/). Each one explains the recognition
   signals, the core idea, a short pseudocode sketch, the complexity, and the common
   mistakes.
2. **Solve it yourself, then connect problem ↔ pattern.** Every solved problem is
   listed under its pattern's *Related LeetCode Problems* section, and each
   solution's docstring names the pattern it uses. The aim is to internalize the
   pattern, not to copy a ready-made skeleton.
3. **Review with cheatsheets.** [`cheatsheets/`](cheatsheets/) gives fast refreshers
   on complexity, Python idioms, and the most common pattern snippets.

---

## Algorithmic patterns included

| Pattern | Document | Example problems |
|---------|----------|------------------|
| Two Pointers | [`patterns/two_pointers.md`](patterns/two_pointers.md) | Merge Sorted Array, Container With Most Water, Remove Duplicates I/II |
| Binary Search | [`patterns/binary_search.md`](patterns/binary_search.md) | Search Insert Position, Sqrt(x) |
| Hash Map | [`patterns/hash_map.md`](patterns/hash_map.md) | Two Sum, Determine if Two Strings Are Close |
| Sliding Window | [`patterns/sliding_window.md`](patterns/sliding_window.md) | Longest Substring Without Repeating Characters |
| Boyer-Moore Voting | [`patterns/boyer_moore_voting.md`](patterns/boyer_moore_voting.md) | Majority Element, Majority Element II |
| Stack | [`patterns/stack.md`](patterns/stack.md) | Valid Parentheses, Simplify Path |

See [`patterns/README.md`](patterns/README.md) for the full index and the
maintenance contract that keeps patterns and solutions in sync.

---

## Contributing to your future self

When a new solution is added, follow the maintenance workflow described in
[`patterns/README.md`](patterns/README.md): identify the pattern, update the pattern
document, list the problem, and never duplicate an explanation.
