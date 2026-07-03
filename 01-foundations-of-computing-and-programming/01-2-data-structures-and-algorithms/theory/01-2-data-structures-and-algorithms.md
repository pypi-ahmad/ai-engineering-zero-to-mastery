# Overview

Data structures and algorithms are performance architecture. In AI systems, latency and cost often depend more on data movement and lookup patterns than on model inference itself.

Formal objective:
Given a computational problem, choose a representation and procedure that optimize time, space, and operational reliability for expected workloads.

In applied AI pipelines, this shows up in places like feature joins, deduplication, retrieval, and streaming event handling. Two teams can use the same model but observe very different latency/cost profiles because one uses structure-aware algorithms and the other relies on accidental quadratic logic. A common example is ranking candidate items: full sorting millions of rows each request is usually unnecessary when only top-`k` results are needed.

Practical decision pattern:
1. Define workload shape (`n`, update frequency, query pattern).
2. Choose structure to match access pattern (e.g., hash map for lookup, heap for top-`k`).
3. Validate with benchmark traces, not intuition only.
4. Revisit complexity assumptions when data scale shifts.

# Core Data Structures

## Arrays & Lists

- Array (concept): contiguous memory, fixed-type semantics in many languages.
- Python `list`: dynamic array of object references.

Typical costs for Python list:
- Index access: $O(1)$ average
- Append: $O(1)$ amortized
- Insert/delete near front: $O(n)$

When to use:
- Ordered sequences with frequent append/index operations.

When to avoid:
- Queue behavior using `pop(0)` in high-throughput code.

## Tuples

Immutable ordered collections.

Use tuples when:
- Record structure is fixed.
- Values should be hashable (dictionary keys, set elements).

Immutability communicates intent and reduces accidental mutation bugs.

## Sets

Hash-table-backed collection of unique elements.

Average-case operations:
- Membership test: $O(1)$
- Insert/delete: $O(1)$

Use-cases in AI workflows:
- Deduplication of event IDs.
- Fast seen-check in streaming pipelines.

## Hash Maps (Dictionaries)

Dictionary maps keys to values via hashing.

Average-case operations:
- Lookup/insert/delete: $O(1)$

Use-cases:
- Frequency counts
- Aggregations by key
- Join-like operations in memory

Design caveat:
Worst-case behavior can degrade with adversarial collisions, but Python implementations are optimized for practical workloads.

## Stacks & Queues

- Stack: Last In First Out (LIFO)
- Queue: First In First Out (FIFO)

Implementations in Python:
- Stack: `list.append` + `list.pop`
- Queue: `collections.deque.append` + `deque.popleft`

Operational rule:
Never implement high-volume FIFO queues with `list.pop(0)`.

## Trees & Graphs (High-Level)

- Tree: connected acyclic hierarchical graph.
- Graph: vertices and edges with arbitrary connectivity.

Formal graph notation:
$$
G = (V, E)
$$
where $V$ is the vertex set and $E$ is the edge set.

AI-relevant examples:
- Workflow DAGs for feature pipelines.
- Knowledge graphs for retrieval.
- Service dependency graphs for incident analysis.

# Core Algorithms

## Search

### Linear Search
Checks elements sequentially.
- Time: $O(n)$
- Works on unsorted data.

### Binary Search
Halves search space on each step.
- Time: $O(\log n)$
- Requires sorted data.

Binary search intuition:
Imagine repeatedly cutting a phone book in half to locate a name.

## Sorting

### Insertion Sort
Simple and educational.
- Worst-case: $O(n^2)$
- Good for tiny or nearly sorted arrays.

### Timsort (`sorted`, `.sort()`)
Python built-in hybrid algorithm.
- Typical: $O(n \log n)$
- Exploits existing order runs efficiently.

## Graph Traversal

### Depth-First Search (DFS)
Explore one branch deeply before backtracking.
- Time: $O(|V| + |E|)$
- Memory usually lower than BFS for wide graphs.

### Breadth-First Search (BFS)
Explore level by level.
- Time: $O(|V| + |E|)$
- Finds shortest path in unweighted graphs.

Diagram in words:
Imagine a company org chart. DFS follows one management chain to the bottom first. BFS visits everyone level-by-level by job level.

# Big-O Complexity (Intuition)

Big-O captures asymptotic growth as input size $n$ increases.

Common classes:
- $O(1)$: constant
- $O(\log n)$: logarithmic
- $O(n)$: linear
- $O(n \log n)$: common for divide-and-conquer
- $O(n^2)$: pairwise comparisons

Space complexity matters equally. A faster algorithm with memory blow-up can still fail in production.

Engineering note:
Asymptotics do not replace measurement. Constant factors, cache behavior, and language runtime details matter in practice. Good engineering combines Big-O intuition with profiling under realistic data distributions.

# Example Problems and Solutions

1. Frequency counting in event logs
- Use `dict` accumulation in one pass.
- Complexity: $O(n)$ time, $O(k)$ space.

2. Top-k frequent items
- Count with dict, then heap or partial sort.
- Better than full sort when `k << n`.

3. Shortest path in unweighted dependency graph
- Use BFS from source node.

4. Cycle detection in directed graph
- DFS with color states (`white/gray/black`) or recursion stack tracking.

5. Sliding-window deduplication
- Use set + queue/deque with TTL/expiry logic.

# Business Case Studies & Exceptions

## Case 1: Log Processing Pipeline Misses SLA

Scenario:
A team used nested loops to deduplicate and aggregate event logs.

Complexity profile:
- Old approach: near $O(n^2)$
- Improved approach: set/dict-based near $O(n)$

Result:
- Lower CPU time
- Predictable scaling under traffic spikes

Exception:
If dataset size is tiny and fixed, simpler $O(n^2)$ code may be acceptable when readability is critical.

## Case 2: Routing Queue CPU Spikes

Scenario:
FIFO queue implemented as list with `pop(0)`.

Impact:
Each pop triggers element shifting, creating avoidable CPU load.

Fix pattern:
- Replace with `deque`
- Add queue-length backpressure guardrails

## Case 3: Graph Traversal Fails in Production

Scenario:
Recursive DFS over deep graph exceeds recursion depth.

Fix pattern:
- Use iterative DFS with explicit stack
- Add max-depth controls and alerts

## Case 4: Candidate Retrieval Latency in Recommender System

Scenario:
Full sort used when only top 50 candidates needed.

Fix pattern:
- Use heap-based `nlargest` strategy
- Reduce time and memory overhead

## Case 5: Feature Store Point Lookup Bottleneck

Scenario:
An online scoring service performed repeated linear scans over a list of feature records by entity ID.

Impact:
- p95 latency regressed as entity count increased.
- CPU usage increased without model changes.

Fix pattern:
- Build dictionary index keyed by entity ID at load time.
- Use O(1) average lookups for request path.
- Add data freshness timestamp to avoid stale-cache issues.

# Interview Questions & Answers

1. **Q: List vs tuple in Python?**
   **A:** `list` is mutable and dynamic; `tuple` is immutable and safer for fixed records and hash-based usage.

2. **Q: Why use `dict` for counting instead of a list?**
   **A:** Dictionary lookup/update is average $O(1)$ by key; list search is $O(n)$.

3. **Q: What is the complexity of binary search?**
   **A:** $O(\log n)$ time, with a required sorted input.

4. **Q: BFS vs DFS when shortest path is needed?**
   **A:** BFS for unweighted shortest path because it explores by depth layers.

5. **Q: Why is `pop(0)` expensive?**
   **A:** It shifts all remaining elements left, making it $O(n)$.

6. **Q: Explain amortized complexity for list append.**
   **A:** Most appends are constant time; occasional resize operations are expensive but averaged cost remains $O(1)$.

7. **Q: What data structure for deduping a stream?**
   **A:** Set for membership, often combined with TTL/window tracking to control memory.

8. **Q: When is $O(n^2)$ acceptable?**
   **A:** Small bounded datasets, one-off offline tasks, or when clarity outweighs optimization.

9. **Q: How do algorithm choices affect cloud cost?**
   **A:** Poor complexity increases CPU time, memory usage, and autoscaling pressure.

10. **Q: Why track both time and space complexity?**
    **A:** Fast algorithms can still fail operationally if they exceed memory constraints.

11. **Q: Give one graph use-case in ML systems.**
    **A:** Traversing feature dependency DAGs to compute valid execution order.

12. **Q: How do you compare two algorithm implementations fairly?**
    **A:** Benchmark under same data distribution, multiple repeats, and report median/variance.

13. **Q: Why can a top-`k` heap outperform full sort?**
    **A:** When `k << n`, heap selection avoids sorting all elements, reducing time and memory overhead.

14. **Q: How do access patterns influence data-structure choice?**
    **A:** Frequent key lookups favor hash maps; FIFO operations favor deque; range queries may favor sorted structures.

15. **Q: Why revisit complexity decisions over time?**
    **A:** Input scale and workload shape evolve, turning previously acceptable choices into operational bottlenecks.

# References

- Python data structures tutorial: https://docs.python.org/3/tutorial/datastructures.html
- Python `collections` module: https://docs.python.org/3/library/collections.html
- Big-O cheat sheet (reference): https://www.bigocheatsheet.com/
