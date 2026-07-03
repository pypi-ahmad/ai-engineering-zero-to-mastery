# Overview

AI engineers who can run experiments are useful; AI engineers who can design valid experiments are rare.

Research literacy matters in production and science settings because it helps you:

- interpret claims from papers and benchmarks,
- avoid false improvements from leakage or weak baselines,
- design experiments that transfer to real-world environments,
- communicate uncertainty and limitations responsibly.

Modern AI-for-science teaching increasingly combines probabilistic methods, domain-informed architectures, simulation-based inference, and reproducibility discipline. Recent course structures from research-methods and AI-for-science syllabi reinforce this integrated approach.

# Research Paradigms in AI

## Formal, probabilistic, and empirical traditions

AI research historically combines three paradigms:

1. Formal-symbolic methods (search, logic, planning).
2. Probabilistic reasoning and uncertainty modeling.
3. Empirical machine learning with benchmark-driven evaluation.

In practice, strong research work often blends all three.

## Qualitative vs quantitative research in AI contexts

- Quantitative: model performance, effect sizes, uncertainty intervals.
- Qualitative: user studies, annotation quality analysis, failure-mode characterization.

Both can coexist in one study. Example: quantitative benchmark gains plus qualitative error taxonomy.

## Empirical vs theoretical contributions

- Empirical: new results on datasets/tasks.
- Theoretical: proofs, guarantees, or complexity insights.
- Systems: infrastructure that enables reliable evaluation or scale.

# Methodology & Experiment Design

## Hypothesis formulation

A useful AI hypothesis should be falsifiable and measurable.

Weak: "Model B is better."

Strong: "On dataset D under fixed split S, adding retrieval reranking increases grounded answer F1 by at least 3 points with no more than 15% latency increase."

## Baselines, controls, and ablations

Minimum rigorous protocol:

- strong baseline (not a strawman),
- controlled comparison with fixed preprocessing and split,
- ablations isolating each component,
- significance-aware reporting (mean, variance, confidence intervals).

## Reproducibility checklist

- fixed random seeds,
- versioned data and code,
- explicit train/val/test separation,
- hyperparameter disclosure,
- compute budget and hardware context,
- failure cases and limitations.

## Leakage and robustness

Data leakage occurs when training process accesses information unavailable at inference time. It creates inflated metrics and weak real-world transfer.

Robustness checks should include:

- distribution-shift stress tests,
- subgroup performance slices,
- calibration analysis,
- adversarial or perturbation-based sanity tests where appropriate.

# Reading & Critiquing AI Papers

## A practical 8-pass reading workflow

1. Title/abstract: contribution claim.
2. Problem framing and assumptions.
3. Data sources and split policy.
4. Baselines and fairness of comparison.
5. Metrics and error decomposition.
6. Ablations and sensitivity.
7. Reproducibility artifacts (code/data/checkpoints).
8. External validity and limitations.

## Red flags

- weak baselines hidden in appendix,
- cherry-picked metrics or datasets,
- no variance bars across runs,
- unclear data preprocessing,
- claims that exceed demonstrated scope.

# AI-for-Science

## What makes AI-for-science distinct

AI-for-science is not only "apply model to scientific data." It often requires:

- embedding physical constraints or symmetries,
- coupling statistical learning with mechanistic models,
- linking simulation outputs with observations,
- designing experiment loops where AI suggests next measurements.

## Domain-informed modeling patterns

Common patterns:

- symmetry-aware neural architectures,
- physics-informed losses/constraints,
- probabilistic inference for uncertainty-aware decision-making,
- simulation-based inference to infer latent parameters from simulated-to-observed comparisons.

## Human-AI scientific collaboration

LLMs and agentic workflows can accelerate literature triage and hypothesis generation, but scientific validation remains empirical and domain-led.

# Ethics & Responsibility in AI Research

## Core responsibilities

- report uncertainty honestly,
- avoid overclaiming beyond evidence,
- document data provenance and consent constraints,
- assess dual-use and misuse pathways,
- publish enough detail for scrutiny and replication.

## Why this matters

Reproducibility concerns in AI and computational science directly affect trust, especially in health, climate, and policy-informing domains.

# Research Case Studies & Exceptions

## Case 1: Retrieval-augmented scientific assistant

Goal:

- support literature synthesis for a biomedical team.

Strong design:

- compare RAG against no-retrieval baseline,
- include groundedness and citation-validity metrics,
- require human review of high-impact outputs.

Exception:

- if corpus coverage is poor, fluent answers can still be unsupported.

## Case 2: AI-for-materials discovery workflow

Goal:

- prioritize candidate compounds for expensive wet-lab tests.

Strong design:

- uncertainty-aware ranking,
- active-learning loop,
- cost-aware objective balancing exploration and exploitation.

Exception:

- if simulation fidelity is weak, model ranking may not transfer to lab reality.

## Case 3: Benchmark gain that fails deployment

Observation:

- model shows +2% benchmark accuracy.

Root cause:

- gains came from feature leakage and unrealistic split strategy.

Lesson:

- evaluation design can dominate apparent model improvement.

# Interview Questions & Answers

1. **Q: How do you design a fair comparison between two models?**
   **A:** Use the same data split, preprocessing, compute budget assumptions, and repeated runs with variance reporting.

2. **Q: What is an ablation study?**
   **A:** A controlled experiment that removes or alters components to isolate their contribution.

3. **Q: Why are strong baselines important?**
   **A:** Without them, improvements may reflect weak competition rather than true progress.

4. **Q: What is data leakage in ML experiments?**
   **A:** Any use of future or target-correlated information unavailable at inference time.

5. **Q: How do you read AI papers efficiently?**
   **A:** Start with claims, then verify data, baselines, metrics, ablations, and reproducibility artifacts.

6. **Q: What makes a hypothesis testable?**
   **A:** Clear measurable prediction, predefined protocol, and falsifiable outcome criteria.

7. **Q: What is simulation-based inference in simple terms?**
   **A:** Use simulations to generate synthetic observations and infer which hidden parameters best explain real observations.

8. **Q: How do you report uncertainty in experiments?**
   **A:** Provide confidence intervals, variance across seeds, and calibration or uncertainty estimates.

9. **Q: Why do benchmark gains fail in production?**
   **A:** Dataset mismatch, hidden leakage, and untested operational constraints.

10. **Q: What are signs of cherry-picking?**
   **A:** Selective tasks, selective metrics, and missing negative results.

11. **Q: How do you improve reproducibility?**
   **A:** Version data/code, disclose training recipe, publish environment details, and provide scripts.

12. **Q: What is external validity?**
   **A:** Whether results generalize beyond the specific benchmark setup.

13. **Q: How does AI-for-science differ from generic ML?**
   **A:** It must respect domain laws, experimental constraints, and scientific interpretation needs.

14. **Q: Why are domain-informed models useful?**
   **A:** They reduce sample complexity and improve physically plausible predictions.

15. **Q: How do you evaluate LLMs in research workflows?**
   **A:** Assess factual grounding, citation integrity, and effect on human research productivity.

16. **Q: What are ethical risks in AI-for-science?**
   **A:** Misleading claims, opaque methods, dual-use misuse, and inequitable access to tools.

17. **Q: What is a robust evaluation protocol?**
   **A:** Predefined metrics, fixed splits, baseline parity, ablations, and stress tests.

18. **Q: How do you avoid p-hacking in ML research?**
   **A:** Pre-register key decisions, limit exploratory post-hoc claims, and report full experiment logs.

19. **Q: What should a paper discussion section include?**
   **A:** Limitations, failure cases, assumptions, and transfer constraints.

20. **Q: Why should engineers learn research methods?**
   **A:** It improves decision quality in model selection, product experiments, and system reliability claims.
# References

- Jönköping University TRIS22 course context: https://ju.se/en/study-at-ju/courses/programme-course/research-methods-for-intelligent-systems-spring-2026-t1002.html
- TRIS22 syllabus page (course code and level): https://syllabus.ju.se/Syllabus/CourseOccasion/9f263824-897b-11f0-86ba-675da05741d8?lang=en
- Purdue CS 592 AI for Scientific Discovery: https://www.cs.purdue.edu/homes/yexiang/courses/21fall-cs592/index.html
- MIT Professional Education, AI for Scientific Discovery: https://professional.mit.edu/course-catalog/ai-scientific-discovery-live-online
- BU DS595 AI Methods for Science (course topics): https://smsharma.io/teaching/ds595-ai4science.html
- Cambridge/Science report, AI for science emerging agenda (PDF): https://science.ai.cam.ac.uk/assets/uploads/ai-for-science-an-emerging-agenda.pdf
- DeepMind Science overview: https://deepmind.google/science/
- DeepMind AI for Science policy essay: https://deepmind.google/public-policy/ai-for-science/
- Nature (2020), transparency and reproducibility in AI: https://www.nature.com/articles/s41586-020-2766-y
- Nature (2023), reproducibility concerns discussion: https://www.nature.com/articles/d41586-023-03817-6
