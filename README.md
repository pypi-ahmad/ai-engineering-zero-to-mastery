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
5. Generative Models & LLMs
   - 5.1 Classical Deep Generative Models (VAEs, GANs, Flows)
   - 5.2 Autoregressive & Diffusion Models
   - 5.3 LLM Foundations & Prompt Engineering
   - 5.4 RAG, Tools, and AI Agents
6. MLOps & LLMOps: Production AI Systems
   - 6.1 MLOps Fundamentals & Lifecycle
   - 6.2 Data & Feature Pipelines
   - 6.3 Model Deployment & Serving
   - 6.4 Monitoring, Drift & Governance
   - 6.5 LLMOps: Operationalizing LLMs, RAG & Agents
7. Agentic AI & Applied AI Systems Design
   - 7.1 Agentic AI Foundations & Architectures
   - 7.2 Multi-Agent Workflows & Orchestration
   - 7.3 Context Engineering, Memory & Planning
   - 7.4 AI Product & System Design
   - 7.5 Capstone: End-to-End Agentic AI System
8. Responsible AI, Ethics, Policy & Career Readiness
   - 8.1 Foundations of AI Ethics
   - 8.2 Responsible AI in Practice
   - 8.3 AI Law, Policy & Governance
   - 8.4 AI Career Roadmap, Portfolio & Interviews
9. Advanced AI Specializations: RL, CV, NLP & Domain AI
   - 9.1 Deep Reinforcement Learning (RL)
   - 9.2 Advanced Computer Vision
   - 9.3 Advanced NLP & LLM Applications
   - 9.4 Domain AI: Applied AI in Key Industries
10. Robotics, Edge AI & TinyML
   - 10.1 Robotics & Control Foundations
   - 10.2 Perception, Planning & Navigation
   - 10.3 Edge AI & TinyML
   - 10.4 Integrated Robotics/IoT Project (Capstone)
11. AI Product Management, Entrepreneurship & Research Methods
   - 11.1 AI Product Management Foundations
   - 11.2 AI Entrepreneurship & Startup Design
   - 11.3 AI Research Methods & AI-for-Science
   - 11.4 Portfolio, Capstone & Publication / Launch

## Repository Structure
- `01-foundations-of-computing-and-programming/`
- `02-mathematics-for-ai/`
- `03-classical-machine-learning/`
- `05-generative-models-and-llms/`
- `06-mlops-and-llmops-production-ai-systems/`
- `07-agentic-ai-and-applied-ai-systems-design/`
- `08-responsible-ai-ethics-policy-and-career-readiness/`
- `09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/`
- `10-robotics-edge-ai-and-tinyml/`
- `11-ai-product-entrepreneurship-and-research-methods/`

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
