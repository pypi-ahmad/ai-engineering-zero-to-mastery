# Exercises: 1.2 Data Structures & Algorithms

## How to Use

- Do these after running the notebook.
- Focus on picking the right structure first, then writing code.
- When you finish, write a 3-sentence “tradeoff note” for each exercise (time, space, failure modes).

## Exercise 1: Membership Test Benchmark (List vs Set)

Write code that compares `x in list_of_ids` vs `x in set_of_ids` for:

- `n = 1_000`, `10_000`, `100_000`,
- a mix of hits and misses.

Expected outcome:
- you can explain why `set` membership is typically faster for large `n`.

## Exercise 2: Queue Discipline (BFS)

Implement `bfs_levels(graph: dict[str, list[str]], start: str) -> dict[str, int]` that returns the shortest distance (in edges) from `start` to every reachable node.

Constraints:
- use `collections.deque`,
- do not revisit nodes.

Expected outcome:
- on a small graph, results match what you can compute by hand.

## Exercise 3: Top-K With a Heap

Implement `top_k(nums: list[int], k: int) -> list[int]` that returns the `k` largest numbers in descending order.

Constraints:
- use `heapq`,
- validate `k` (0 <= k <= len(nums)).

Expected outcome:
- better than sorting the entire list when `k` is small relative to `n`.

## Exercise 4: LRU Cache (Correctness First)

Implement a minimal `LRUCache` with:

- `get(key) -> value | None` that marks the key as “recent”,
- `put(key, value)` that evicts the least-recently-used key when full.

Constraint:
- use `collections.OrderedDict` (keep it simple).

Expected outcome:
- a short test sequence shows correct eviction behavior.

## Exercise 5: Complexity “Spot Check”

For each operation, write the typical Big-O time:

1. append to Python list
2. insert at the beginning of a Python list
3. membership test in a set
4. dictionary lookup by key
5. push/pop from a heap

Expected outcome:
- you can justify each in one sentence.

