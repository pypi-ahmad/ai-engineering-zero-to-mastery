# AI Engineering - Zero to Mastery

A practical, end-to-end learning repository for becoming an AI Engineer from fundamentals to production systems.

## Purpose
This repo is a structured tutorial path to build strong foundations, mathematical intuition, and production-ready AI engineering skills through theory + hands-on notebooks.

## High-Level Roadmap
1. Foundations of Computing and Programming
2. Mathematics for AI
3. Machine Learning Fundamentals
4. Deep Learning
5. LLM Engineering
6. Retrieval-Augmented Generation (RAG)
7. AI Agents and Multi-Agent Systems
8. MLOps and Production AI Systems
9. Capstone Projects and Interview Prep

## Repository Structure
- `01-foundations-of-computing-and-programming/`
- `02-mathematics-for-ai/`

Each heading follows a reusable pattern:
- `notebooks/` for hands-on Jupyter lessons
- `data/` for local dataset copies/cache
- `theory/` for deep-dive markdown and PDF lessons
- `README.md` for lesson coverage overview

## How to Run Notebooks

### Option A: `venv`
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

### Option B: Conda
```bash
conda create -n ai-z2m python=3.10 -y
conda activate ai-z2m
pip install -r requirements.txt
jupyter notebook
```

## Current Progress
- Implemented: Foundations Lesson 01 (Python & Jupyter Basics)
- Deferred intentionally: Mathematics Lesson 01+ (pending review)

## Curriculum So Far
- Lesson 01 - Python & Jupyter Basics (Foundations of Computing and Programming)
- Lesson 02 - Linear Algebra for ML & AI (Mathematics for AI)
- Lesson 1.2 - Data Structures & Algorithms in Python (Foundations of Computing and Programming)
