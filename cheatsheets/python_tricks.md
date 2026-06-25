# Python Tricks for Coding Interviews

Idiomatic Python that keeps solutions short, readable, and fast. Everything here is
standard library — no third-party imports.

## Collections

```python
from collections import Counter, defaultdict, deque

Counter("aabbbc")              # {'b': 3, 'a': 2, 'c': 1}
Counter(nums).most_common(2)   # the two most frequent (value, count) pairs

d = defaultdict(list)          # missing keys auto-create an empty list
d[key].append(x)               # no "if key not in d" needed

q = deque()                    # O(1) append/pop at BOTH ends -> queue or stack
q.append(x); q.popleft()       # FIFO (BFS)
q.append(x); q.pop()           # LIFO (DFS)
```

## Heaps (priority queues)

```python
import heapq

heap = []
heapq.heappush(heap, val)      # min-heap by default
smallest = heapq.heappop(heap)
heapq.heapify(some_list)       # O(n) build in place
heapq.nlargest(k, iterable)    # top-k without a full sort
# Max-heap trick: push negated values, negate on pop.
```

## Binary search without writing it

```python
import bisect

bisect.bisect_left(a, x)       # first index where x could go (lower bound)
bisect.bisect_right(a, x)      # last index where x could go (upper bound)
bisect.insort(a, x)            # insert x keeping a sorted
```

## Iteration helpers

```python
for i, val in enumerate(seq):          # index + value
for a, b in zip(xs, ys):               # parallel iteration
for combo in itertools.product(xs, repeat=2):
sorted(items, key=lambda p: (p[1], -p[0]))   # multi-key sort, mixed direction
reversed(seq)                          # lazy reverse iterator
```

## Comprehensions and generators

```python
squares = [x * x for x in nums]
evens   = {x for x in nums if x % 2 == 0}      # set comprehension
index   = {val: i for i, val in enumerate(nums)}  # dict comprehension
total   = sum(x * x for x in nums)             # generator -> no temp list
any(x < 0 for x in nums)                        # short-circuits on first True
all(x > 0 for x in nums)
```

## Strings

```python
"".join(parts)                 # O(n) build; never += in a loop (that is O(n²))
s[::-1]                        # reverse a string
s.isalnum(); s.lower()
ord("a"); chr(97)              # char <-> codepoint
count = [0] * 26               # fixed lowercase-letter frequency array
count[ord(c) - ord("a")] += 1
```

## Numbers

```python
divmod(17, 5)                  # (3, 2): quotient and remainder together
float("inf"); float("-inf")    # sentinels for min/max accumulation
math.gcd(a, b); math.isqrt(x)  # integer gcd and floor sqrt (no float error)
x // y                         # floor division; careful: -7 // 2 == -4
```

## Unpacking and swapping

```python
a, b = b, a                    # swap without a temp
first, *rest = items           # head/tail
left, right = 0, len(a) - 1    # parallel assignment
```

## Useful defaults and guards

```python
value = mapping.get(key, default)      # no KeyError
seen = set(); seen.add(x); x in seen   # O(1) membership
nums.sort()                            # sorts in place, returns None
result = sorted(nums)                  # returns a new sorted list
```

## Recursion limit (for deep DFS)

```python
import sys
sys.setrecursionlimit(10**6)   # raise the cap when recursing deeply
```
