# AI Engineering - Zero to Mastery

Practical, production-minded curriculum for applied AI engineers. Each lesson combines theory chapters and executable notebooks.

## Purpose
Build end-to-end AI engineering skill from programming foundations to robust ML systems, with strong mathematics, model evaluation, and software practice.

## Curriculum
1. Foundations of Computing and Programming
   - 1.1 Programming Basics
   - 1.2 Data Structures & Algorithms
   - 1.3 Software Engineering Practices
2. Mathematics for AI
   - 2.1 Linear Algebra
   - 2.2 Calculus & Optimization
   - 2.3 Probability & Statistics
   - 2.4 Applied Stats for ML
3. Classical Machine Learning
   - 3.1 Supervised Learning
   - 3.2 Unsupervised Learning
   - 3.3 Model Evaluation & Selection
4. Deep Learning Fundamentals (planned)
5. LLM Engineering (planned)
6. RAG Systems (planned)
7. Agents (planned)
8. MLOps (planned)

## Repository Structure
- `01-foundations-of-computing-and-programming/`
- `02-mathematics-for-ai/`
- `03-classical-machine-learning/`

Each sub-lesson uses:
- `theory/` markdown chapter + PDF export
- `notebooks/` executable Jupyter notebook
- `README.md` lesson map

## Environment Setup (uv)
```bash
uv venv --python 3.12.10
source .venv/bin/activate
uv pip install -r requirements.txt
jupyter lab
```

## PDF Export
```bash
python3 scripts/export_theory_pdf.py
```
This exports all lesson theory markdown files to matching PDFs.
