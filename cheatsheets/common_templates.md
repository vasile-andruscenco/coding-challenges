# Common Patterns Cheatsheet

Short pseudocode snippets for the algorithmic patterns that come up most often. These
are memory joggers, not drop-in code — the point is to recall the *shape* of a
pattern, then write it out yourself. Each section links to the fuller write-up under
[`../patterns/`](../patterns/), where you will find recognition signals, complexity,
common mistakes, and the solved problems that use it.

---

## Binary search (exact match)

```text
left, right = 0, n - 1
while left <= right:
    mid = left + (right - left) // 2
    if a[mid] == target:        return mid
    elif a[mid] < target:       left  = mid + 1
    else:                       right = mid - 1
return -1
```

Boundary variants (first/last occurrence, first ≥, last ≤) and *search on the answer*:
[`patterns/binary_search.md`](../patterns/binary_search.md)

---

## Two pointers — opposite ends

```text
left, right = 0, n - 1
while left < right:
    if condition_met(a[left], a[right]):  record / move both
    elif need_larger:                     left  += 1
    else:                                 right -= 1
```

---

## Two pointers — fast & slow (in-place filter)

```text
slow = 0                        # next write position
for fast in range(n):           # fast reads every element
    if keep(a[fast]):
        a[slow] = a[fast]
        slow += 1
return slow                     # length of the kept prefix
```

In-place merge (write from the back) and the full variant list:
[`patterns/two_pointers.md`](../patterns/two_pointers.md)

---

## Sliding window (variable size)

```text
left = 0
state = <empty aggregate>       # set / dict / running sum
best = 0
for right in range(n):
    add a[right] to state
    while constraint_violated:
        remove a[left] from state
        left += 1
    best = max(best, right - left + 1)
return best
```

[`patterns/sliding_window.md`](../patterns/sliding_window.md)

---

## BFS (shortest path, unweighted)

```text
visited = {start}
queue   = deque([start])
distance = 0
while queue:
    distance += 1
    for _ in range(len(queue)):     # drain exactly one level
        node = queue.popleft()
        for nxt in neighbors(node):
            if nxt == target:       return distance
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
return None
```

Level-by-level traversal with a FIFO queue gives the fewest-edges path.

---

## DFS (recursive)

```text
def dfs(node):
    visited.add(node)
    for nxt in neighbors(node):
        if nxt not in visited:
            dfs(nxt)
```

Explore deep first with a stack (or recursion); use an explicit stack to avoid hitting
the recursion limit on deep graphs.

---

## Hash map — complement lookup

```text
seen = {}                       # value -> index
for i, num in enumerate(nums):
    if target - num in seen:    return [seen[target - num], i]
    seen[num] = i
```

[`patterns/hash_map.md`](../patterns/hash_map.md)

---

## Frequency counting

```text
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1
# or: freq = Counter(items)
```
