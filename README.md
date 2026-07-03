# AI Engineering Zero to Mastery

![Build](https://img.shields.io/badge/build-curriculum--ci-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

Beginner-first, production-oriented curriculum for **AI engineering**: building AI systems end-to-end (data, modeling, evaluation, serving, and operations), not just training models in isolation.

## Start Here
- Curriculum entrypoint: [Lesson 1](./01-foundations-of-computing-and-programming/README.md)
- Consolidated study guide: [HANDBOOK.md](./HANDBOOK.md) / [HANDBOOK.pdf](./HANDBOOK.pdf)
- Capstone culmination: [Lesson 15](./15-ai-engineering-capstone-and-professional-practice/README.md)
- Runnable capstone scaffold: [projects/capstone-template](./projects/capstone-template/README.md)
- Learning tracks: [docs/learning-tracks.md](./docs/learning-tracks.md)
- Setup + troubleshooting: [docs/setup-and-troubleshooting.md](./docs/setup-and-troubleshooting.md)
- Documentation architecture: [docs/documentation-map.md](./docs/documentation-map.md)

## What This Solves
Most learning paths teach isolated slices (ML only, LLM only, or deployment only). This repository teaches the full engineering lifecycle:
- foundations and math,
- ML/DL and GenAI,
- agents and operations,
- safety/governance,
- capstone delivery and professional practice.

## Who This Is For
- **Absolute beginners** who want a structured, step-by-step path (start at Lesson 1).
- **Intermediate learners** who know basic Python/ML and want end-to-end system skills (use the tracks).
- **Practitioners** who want checklists, templates, and production tradeoffs (use the handbook + Lesson 6/12/13/15).

## Learning Outcomes
By the end, you can:
- build and evaluate ML/DL/LLM systems,
- implement RAG/agent workflows and fine-tuning patterns,
- operate production AI with MLOps/LLMOps patterns,
- apply safety, governance, and reliability controls,
- present a portfolio-ready end-to-end capstone.

## Learning Tracks (Recommended)
See full details in [docs/learning-tracks.md](./docs/learning-tracks.md).

- **Beginner Track (first wins):** Lessons 1–3, then the runnable [capstone template](./projects/capstone-template/README.md), then Lesson 6.
- **Full Track (zero-to-mastery):** follow Lessons 1 → 15 sequentially.

## How to Use This Repo
1. Study sequentially for best results.
2. Run each sub-lesson notebook after reading theory.
3. Use the handbook for fast review and interview prep.

Parallel-friendly paths (after Lesson 5):
- Lesson 6 and Lesson 12 both cover MLOps/LLMOps with different depth and framing.
- Lesson 9 and Lesson 10 can be explored in parallel based on specialization goals.

## Setup

Install `uv` (recommended). Official instructions:
https://docs.astral.sh/uv/getting-started/installation/

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
git clone https://github.com/pypi-ahmad/ai-engineering-zero-to-mastery.git
cd ai-engineering-zero-to-mastery
uv venv --python 3.12
source .venv/bin/activate
uv sync --frozen --group dev
jupyter lab
```

Optional extras (install only when you reach those lessons):

```bash
# Deep learning (torch/vision)
uv sync --frozen --extra dl

# GenAI / LLM lessons (HF stack + PEFT/TRL)
uv sync --frozen --extra genai

# RL demos
uv sync --frozen --extra rl

# Serving demos + capstone API
uv sync --frozen --extra serving

# Ops / experiment tracking
uv sync --frozen --extra ops
```

## Curriculum Index
### Full Curriculum Index

1. [Lesson 1: Foundations of Computing and Programming](./01-foundations-of-computing-and-programming/README.md)
   - [1.1 Programming Basics](./01-foundations-of-computing-and-programming/01-1-programming-basics/README.md)
   - [1.2 Data Structures & Algorithms](./01-foundations-of-computing-and-programming/01-2-data-structures-and-algorithms/README.md)
   - [1.3 Software Engineering Practices](./01-foundations-of-computing-and-programming/01-3-software-engineering-practices/README.md)
2. [Lesson 2: Mathematics for AI](./02-mathematics-for-ai/README.md)
   - [2.1 Linear Algebra](./02-mathematics-for-ai/02-1-linear-algebra/README.md)
   - [2.2 Calculus & Optimization](./02-mathematics-for-ai/02-2-calculus-and-optimization/README.md)
   - [2.3 Probability & Statistics](./02-mathematics-for-ai/02-3-probability-and-statistics/README.md)
   - [2.4 Applied Stats for ML](./02-mathematics-for-ai/02-4-applied-stats-for-ml/README.md)
3. [Lesson 3: Classical Machine Learning](./03-classical-machine-learning/README.md)
   - [3.1 Supervised Learning](./03-classical-machine-learning/03-1-supervised-learning/README.md)
   - [3.2 Unsupervised Learning](./03-classical-machine-learning/03-2-unsupervised-learning/README.md)
   - [3.3 Model Evaluation & Selection](./03-classical-machine-learning/03-3-model-evaluation-and-selection/README.md)
4. [Lesson 4: Deep Learning Fundamentals](./04-deep-learning-fundamentals/README.md)
   - [4.1 Neural Networks & Backpropagation](./04-deep-learning-fundamentals/04-1-neural-networks-and-backpropagation/README.md)
   - [4.2 Training Deep Neural Networks](./04-deep-learning-fundamentals/04-2-training-deep-neural-networks/README.md)
   - [4.3 Convolutional Neural Networks & Computer Vision](./04-deep-learning-fundamentals/04-3-convolutional-neural-networks-and-computer-vision/README.md)
   - [4.4 Sequence Models, Attention & Transformers](./04-deep-learning-fundamentals/04-4-sequence-models-attention-and-transformers/README.md)
5. [Lesson 5: Generative Models & LLMs](./05-generative-models-and-llms/README.md)
   - [5.1 Classical Deep Generative Models](./05-generative-models-and-llms/05-1-classical-deep-generative-models/README.md)
   - [5.2 Autoregressive & Diffusion Models](./05-generative-models-and-llms/05-2-autoregressive-and-diffusion-models/README.md)
   - [5.3 LLM Foundations & Prompt Engineering](./05-generative-models-and-llms/05-3-llm-foundations-and-prompt-engineering/README.md)
   - [5.4 RAG, Tools, and AI Agents](./05-generative-models-and-llms/05-4-rag-tools-and-ai-agents/README.md)
   - [5.5 LLM Post-Training & Fine-Tuning](./05-generative-models-and-llms/05-5-llm-post-training-and-fine-tuning/README.md)
6. [Lesson 6: MLOps & LLMOps: Production AI Systems](./06-mlops-and-llmops-production-ai-systems/README.md)
   - [6.1 MLOps Fundamentals & Lifecycle](./06-mlops-and-llmops-production-ai-systems/06-1-mlops-fundamentals-and-lifecycle/README.md)
   - [6.2 Data & Feature Pipelines](./06-mlops-and-llmops-production-ai-systems/06-2-data-and-feature-pipelines/README.md)
   - [6.3 Model Deployment & Serving](./06-mlops-and-llmops-production-ai-systems/06-3-model-deployment-and-serving/README.md)
   - [6.4 Monitoring, Drift & Governance](./06-mlops-and-llmops-production-ai-systems/06-4-monitoring-drift-and-governance/README.md)
   - [6.5 LLMOps: Operationalizing LLMs, RAG & Agents](./06-mlops-and-llmops-production-ai-systems/06-5-llmops-operationalizing-llms-rag-and-agents/README.md)
7. [Lesson 7: Agentic AI & Applied AI Systems Design](./07-agentic-ai-and-applied-ai-systems-design/README.md)
   - [7.1 Agentic AI Foundations & Architectures](./07-agentic-ai-and-applied-ai-systems-design/07-1-agentic-ai-foundations-and-architectures/README.md)
   - [7.2 Multi-Agent Workflows & Orchestration](./07-agentic-ai-and-applied-ai-systems-design/07-2-multi-agent-workflows-and-orchestration/README.md)
   - [7.3 Context Engineering, Memory & Planning](./07-agentic-ai-and-applied-ai-systems-design/07-3-context-engineering-memory-and-planning/README.md)
   - [7.4 AI Product & System Design](./07-agentic-ai-and-applied-ai-systems-design/07-4-ai-product-and-system-design/README.md)
   - [7.5 Capstone: End-to-End Agentic AI System](./07-agentic-ai-and-applied-ai-systems-design/07-5-capstone-end-to-end-agentic-ai-system/README.md)
   - [7.6 MCP and Agent2Agent Interoperability](./07-agentic-ai-and-applied-ai-systems-design/07-6-mcp-and-agent2agent-interoperability/README.md)
8. [Lesson 8: Responsible AI, Ethics, Policy & Career Readiness](./08-responsible-ai-ethics-policy-and-career-readiness/README.md)
   - [8.1 Foundations of AI Ethics](./08-responsible-ai-ethics-policy-and-career-readiness/08-1-foundations-of-ai-ethics/README.md)
   - [8.2 Responsible AI in Practice](./08-responsible-ai-ethics-policy-and-career-readiness/08-2-responsible-ai-in-practice/README.md)
   - [8.3 AI Law, Policy & Governance](./08-responsible-ai-ethics-policy-and-career-readiness/08-3-ai-law-policy-and-governance/README.md)
   - [8.4 AI Career Roadmap, Portfolio & Interviews](./08-responsible-ai-ethics-policy-and-career-readiness/08-4-ai-career-roadmap-portfolio-and-interviews/README.md)
9. [Lesson 9: Advanced AI Specializations (RL, CV, NLP, Domain AI)](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/README.md)
   - [9.1 Deep Reinforcement Learning (RL)](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-1-deep-reinforcement-learning/README.md)
   - [9.2 Advanced Computer Vision](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-2-advanced-computer-vision/README.md)
   - [9.3 Advanced NLP & LLM Applications](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-3-advanced-nlp-and-llm-applications/README.md)
   - [9.4 Domain AI: Applied AI in Key Industries](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-4-domain-ai-applied-ai-in-key-industries/README.md)
   - [9.5 Graph AI and GraphRAG Knowledge-Graph Pipelines](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines/README.md)
   - [9.6 Speech/Audio AI and Voice Agents](./09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-6-speech-audio-ai-and-voice-agents/README.md)
10. [Lesson 10: Robotics, Edge AI & TinyML](./10-robotics-edge-ai-and-tinyml/README.md)
   - [10.1 Robotics & Control Foundations](./10-robotics-edge-ai-and-tinyml/10-1-robotics-and-control-foundations/README.md)
   - [10.2 Perception, Planning & Navigation](./10-robotics-edge-ai-and-tinyml/10-2-perception-planning-and-navigation/README.md)
   - [10.3 Edge AI & TinyML](./10-robotics-edge-ai-and-tinyml/10-3-edge-ai-and-tinyml/README.md)
   - [10.4 Integrated Robotics/IoT Project (Capstone)](./10-robotics-edge-ai-and-tinyml/10-4-integrated-robotics-iot-project-capstone/README.md)
11. [Lesson 11: AI Product Management, Entrepreneurship & Research Methods](./11-ai-product-entrepreneurship-and-research-methods/README.md)
   - [11.1 AI Product Management Foundations](./11-ai-product-entrepreneurship-and-research-methods/11-1-ai-product-management-foundations/README.md)
   - [11.2 AI Entrepreneurship & Startup Design](./11-ai-product-entrepreneurship-and-research-methods/11-2-ai-entrepreneurship-and-startup-design/README.md)
   - [11.3 AI Research Methods & AI-for-Science](./11-ai-product-entrepreneurship-and-research-methods/11-3-ai-research-methods-and-ai-for-science/README.md)
   - [11.4 Portfolio, Capstone & Publication / Launch](./11-ai-product-entrepreneurship-and-research-methods/11-4-portfolio-capstone-and-publication-or-launch/README.md)
12. [Lesson 12: MLOps & LLMOps: Production AI & Operations](./12-mlops-and-llmops-production-ai-and-operations/README.md)
   - [12.1 MLOps Foundations & ML Lifecycle in Production](./12-mlops-and-llmops-production-ai-and-operations/12-1-mlops-foundations-and-ml-lifecycle/README.md)
   - [12.2 ML Pipelines, Deployment & Monitoring](./12-mlops-and-llmops-production-ai-and-operations/12-2-ml-pipelines-deployment-and-monitoring/README.md)
   - [12.3 LLMOps Foundations & LLM Lifecycle](./12-mlops-and-llmops-production-ai-and-operations/12-3-llmops-foundations-and-llm-lifecycle/README.md)
   - [12.4 LLM Application Deployment, Observability & Governance](./12-mlops-and-llmops-production-ai-and-operations/12-4-llm-application-deployment-observability-and-governance/README.md)
   - [12.5 LLM Inference Systems Engineering](./12-mlops-and-llmops-production-ai-and-operations/12-5-llm-inference-systems-engineering/README.md)
   - [12.6 LLM Evaluation, Data Flywheel & Continuous Post-Training Ops](./12-mlops-and-llmops-production-ai-and-operations/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops/README.md)
   - [12.7 Distributed LLM Training Systems](./12-mlops-and-llmops-production-ai-and-operations/12-7-distributed-llm-training-systems/README.md)
   - [12.8 Privacy-Preserving ML and LLM Ops](./12-mlops-and-llmops-production-ai-and-operations/12-8-privacy-preserving-ml-and-llm-ops/README.md)
   - [12.9 Data-Centric Labeling Ops](./12-mlops-and-llmops-production-ai-and-operations/12-9-data-centric-labeling-ops/README.md)
13. [Lesson 13: AI Safety, Security & Trustworthy AI](./13-ai-safety-security-and-trustworthy-ai/README.md)
   - [13.1 AI Safety & Alignment Fundamentals](./13-ai-safety-security-and-trustworthy-ai/13-1-ai-safety-and-alignment-fundamentals/README.md)
   - [13.2 Robustness, Adversarial ML & AI Security](./13-ai-safety-security-and-trustworthy-ai/13-2-robustness-adversarial-ml-and-ai-security/README.md)
   - [13.3 Trustworthy AI: Robust, Fair, Explainable & Governed Systems](./13-ai-safety-security-and-trustworthy-ai/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems/README.md)
   - [13.4 Practical Guardrails, Evaluations & Safe Agent Design](./13-ai-safety-security-and-trustworthy-ai/13-4-practical-guardrails-evaluations-and-safe-agent-design/README.md)
14. [Lesson 14: Frontier & Emerging Directions in AI](./14-frontier-and-emerging-directions-in-ai/README.md)
   - [14.1 Neurosymbolic AI & Causal Reasoning](./14-frontier-and-emerging-directions-in-ai/14-1-neurosymbolic-ai-and-causal-reasoning/README.md)
   - [14.2 Multi-Agent Systems & Complex Environments](./14-frontier-and-emerging-directions-in-ai/14-2-multi-agent-systems-and-complex-environments/README.md)
   - [14.3 Quantum & Neuromorphic AI (Conceptual Overview)](./14-frontier-and-emerging-directions-in-ai/14-3-quantum-and-neuromorphic-ai/README.md)
   - [14.4 Lifelong Learning, Reading Groups & Contributing to the Field](./14-frontier-and-emerging-directions-in-ai/14-4-lifelong-learning-reading-groups-and-contributing/README.md)
   - [14.5 GenAI Observability and Evaluation Standards](./14-frontier-and-emerging-directions-in-ai/14-5-genai-observability-and-evaluation-standards/README.md)
15. [Lesson 15: AI Engineering Capstone & Professional Practice](./15-ai-engineering-capstone-and-professional-practice/README.md)
   - [15.1 Capstone Design & Scoping](./15-ai-engineering-capstone-and-professional-practice/15-1-capstone-design-and-scoping/README.md)
   - [15.2 Execution: Data, Modeling, Deployment & Documentation](./15-ai-engineering-capstone-and-professional-practice/15-2-execution-data-modeling-deployment-and-documentation/README.md)
   - [15.3 Teamwork, Communication & Stakeholder Management](./15-ai-engineering-capstone-and-professional-practice/15-3-teamwork-communication-and-stakeholder-management/README.md)
   - [15.4 Final Presentation, Reflection & Next Steps](./15-ai-engineering-capstone-and-professional-practice/15-4-final-presentation-reflection-and-next-steps/README.md)


## Tech Stack (Observed in Notebooks)
- Python 3.10+, Jupyter, `uv`
- ML: `scikit-learn`, `xgboost`
- DL/LLM: `torch`, `torchvision`, `transformers`, `diffusers`, `datasets`, `peft`, `trl`
- Systems: `fastapi`, `networkx` (Airflow appears as optional pseudo-code in one lesson)

## Sources and References
- Full registry: [docs/sources-and-references.md](./docs/sources-and-references.md)

Curated “start here” references (authoritative + beginner-friendly):
- Python docs: https://docs.python.org/3/
- uv docs: https://docs.astral.sh/uv/
- NumPy: https://numpy.org/doc/stable/
- pandas: https://pandas.pydata.org/docs/
- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
- PyTorch: https://pytorch.org/docs/stable/index.html
- Hugging Face Transformers: https://huggingface.co/docs/transformers/
- FastAPI: https://fastapi.tiangolo.com/
- MLflow: https://mlflow.org/docs/latest/index.html
- W&B: https://docs.wandb.ai/

- Documentation benchmark sources used for doc quality:
  - GitHub README guidance: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
  - GitHub contributor guidelines: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
  - Open Source Guides maintainer practices: https://opensource.guide/best-practices/
  - Diátaxis framework: https://diataxis.fr/
  - Google developer style guide: https://developers.google.com/style
  - Read the Docs style guide: https://docs.readthedocs.com/dev/stable/style-guide.html
  - The Good Docs Project templates: https://www.thegooddocsproject.dev/

## Contributing and Governance
- Contribution process: open issue or pull request with lesson path + rationale + references.
- Governance files may be added later as the repo evolves (for wider open-source contribution and security processes).

## License
MIT License. See `LICENSE`.
