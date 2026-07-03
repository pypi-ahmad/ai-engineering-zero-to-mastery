# 1.2 Data Structures & Algorithms

This lesson covers the core data structures and algorithmic thinking patterns needed for efficient AI/ML code.

## Why This Matters

AI systems often fail on performance and reliability long before they fail on “model quality”. Choosing the right data structure and understanding complexity prevents slow pipelines, memory blow-ups, and brittle retrieval logic.

## Learning Goals
- Choose appropriate structures (lists, dicts, sets, stacks, queues, graphs).
- Analyze time/space complexity for common operations.
- Implement and reason about search, sorting, BFS/DFS, and traversal trade-offs.

## How It Fits in the Curriculum
Efficient data handling and algorithmic reasoning are critical for feature engineering, retrieval systems, and scalable AI pipelines in later modules.

## Key Terms (Plain English)

- **Data structure**: a way to store data so certain operations are fast (lookup, insert, iterate).
- **Algorithm**: a step-by-step method for solving a problem (searching, sorting).
- **Time complexity**: how runtime grows as input size grows (big-O).
- **BFS/DFS**: graph traversal strategies used in routing, dependency graphs, and search.

## Start Here
1. Theory: `theory/01-2-data-structures-and-algorithms.md`
2. Notebook: `notebooks/01-2-data-structures-and-algorithms.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can choose list vs dict vs set for a task and justify it.
- You can estimate whether a loop will be “fine” or will explode at scale.
- You can implement and test BFS/DFS on a small graph.

## Verify Your Work

- Restart kernel -> Run all in the notebook without errors.
- Complete the exercises for complexity and traversal without copying solutions.
- Explain one real pipeline you’ve seen (or can imagine) where the wrong structure causes pain.

## Common Mistakes

- Using a list for membership checks (`x in list`) when a set is needed.
- Ignoring complexity because “it runs on small data”.
- Implementing algorithms without tests, then debugging by guesswork.
