# Solutions: 1.2 Data Structures & Algorithms

## Exercise 1: Membership Test Benchmark (List vs Set)

```python
from __future__ import annotations

import random
import time


def bench(n: int, trials: int = 50_000) -> None:
    ids_list = list(range(n))
    ids_set = set(ids_list)

    rng = random.Random(42)
    queries = [rng.randrange(0, 2 * n) for _ in range(trials)]

    t0 = time.perf_counter()
    hits_list = sum(1 for q in queries if q in ids_list)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    hits_set = sum(1 for q in queries if q in ids_set)
    t3 = time.perf_counter()

    assert hits_list == hits_set
    print(f\"n={n:>7} list={t1 - t0:.4f}s set={t3 - t2:.4f}s\")\n\n\nfor n in [1_000, 10_000, 100_000]:\n    bench(n)\n```

## Exercise 2: Queue Discipline (BFS)

```python
from __future__ import annotations

from collections import deque


def bfs_levels(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    dist: dict[str, int] = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v in dist:
                continue
            dist[v] = dist[u] + 1
            q.append(v)
    return dist
```

## Exercise 3: Top-K With a Heap

```python
from __future__ import annotations

import heapq


def top_k(nums: list[int], k: int) -> list[int]:
    if k < 0 or k > len(nums):
        raise ValueError(\"k out of range\")\n    if k == 0:\n        return []\n\n    heap: list[int] = []\n    for x in nums:\n        if len(heap) < k:\n            heapq.heappush(heap, x)\n        else:\n            heapq.heappushpop(heap, x)\n\n    return sorted(heap, reverse=True)\n```

## Exercise 4: LRU Cache (Correctness First)

```python
from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar

K = TypeVar(\"K\")\nV = TypeVar(\"V\")\n\n\nclass LRUCache(Generic[K, V]):\n    def __init__(self, capacity: int) -> None:\n        if capacity < 1:\n            raise ValueError(\"capacity must be >= 1\")\n        self.capacity = capacity\n        self._d: OrderedDict[K, V] = OrderedDict()\n\n    def get(self, key: K) -> V | None:\n        if key not in self._d:\n            return None\n        self._d.move_to_end(key)\n        return self._d[key]\n\n    def put(self, key: K, value: V) -> None:\n        if key in self._d:\n            self._d[key] = value\n            self._d.move_to_end(key)\n            return\n        self._d[key] = value\n        if len(self._d) > self.capacity:\n            self._d.popitem(last=False)\n```

## Exercise 5: Complexity “Spot Check”

Typical answers:

1. append to list: amortized O(1)
2. insert at beginning of list: O(n) (shifts elements)
3. membership in set: average O(1)
4. dict lookup by key: average O(1)
5. heap push/pop: O(log n)

