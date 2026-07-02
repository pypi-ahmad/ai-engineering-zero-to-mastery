# Capstone Design & Scoping

## Overview

In AI engineering programs, the capstone is the integration point where learners prove they can deliver a full project under realistic constraints, not just train isolated models. Strong capstones combine technical depth with planning discipline, communication, and practical trade-off decisions.

What a capstone should demonstrate:

- end-to-end ownership from problem framing to delivery,
- evidence-based technical decisions,
- reproducibility and professional documentation,
- communication of impact, limitations, and risks.

How this curriculum maps into the capstone:

- Lessons 1-3: core programming, math, ML reasoning.
- Lessons 5-10: deep learning, GenAI, agentic systems, domain and edge contexts.
- Lessons 12-14: MLOps/LLMOps, safety, and frontier awareness.
- Lesson 11: product and research framing.

A capstone should not maximize complexity; it should maximize signal of competence.

## Capstone Objectives & Competencies

Typical capstone objectives across AI engineering and university capstone programs:

1. define a real and bounded problem,
2. convert goals into measurable criteria,
3. execute a full AI lifecycle,
4. communicate decisions and outcomes professionally.

Core competencies expected in capstone syllabi and project-based programs:

- technical execution (data, modeling, evaluation),
- engineering rigor (versioning, testing, packaging, deployment),
- collaboration and team practices,
- oral/written communication,
- ethical and societal reflection.

Practical competency matrix:

| Competency | Evidence in Capstone |
|---|---|
| Problem framing | Problem statement + stakeholder needs |
| Technical depth | Baselines, improved models, analysis |
| Engineering quality | Reproducible scripts, configs, deployable artifact |
| Professional practice | Status updates, decisions, presentation |
| Responsible AI | Risk/ethics section and mitigation notes |

## Project Selection & Scoping

### Selecting a Capstone Topic

Evaluate candidate ideas on five dimensions:

- `impact`: meaningful business/research outcome,
- `feasibility`: can finish with available time/resources,
- `data readiness`: access and quality are realistic,
- `technical signal`: demonstrates relevant capabilities,
- `career alignment`: supports target role trajectory.

### Statement of Work (SoW) Essentials

A strong SoW includes:

- project objective and non-objectives,
- concrete deliverables,
- assumptions and constraints,
- timeline and milestones,
- risk register with mitigation triggers,
- acceptance criteria.

Minimal SoW template:

1. Background and problem context.
2. Scope in/out boundaries.
3. Deliverables and quality bar.
4. Milestones and deadlines.
5. Risks, dependencies, and fallback plan.
6. Stakeholder review schedule.

### Scope Control Pattern

Use a three-tier scope model:

- `Must-have`: minimum viable capstone.
- `Should-have`: high-value additions if schedule permits.
- `Could-have`: stretch goals only after core completion.

This prevents capstone failure from uncontrolled ambition.

## Linking to Earlier Lessons

### Choosing the Right Stack

Decide with role and problem fit, not hype:

- `Classical ML` when tabular prediction and interpretability dominate.
- `Deep learning` when unstructured data tasks require representation learning.
- `GenAI/RAG/Agents` when language reasoning, knowledge grounding, or workflow automation is central.
- `Edge/robotics` when latency/power/physical interaction constraints matter.
- `Research orientation` when novelty and hypothesis testing are primary outcomes.

### Minimal Architecture Decision Questions

- What is the smallest system that proves value?
- Which lesson techniques are necessary vs optional?
- What can be simulated if production infra is unavailable?

## Capstone Case Studies & Exceptions

### Case 1: Enterprise-Style Product Capstone

A team built a document assistant with retrieval, API serving, and monitoring dashboard. They limited scope to one document domain and one primary workflow. Result: polished end-to-end demo and credible production discussion.

### Case 2: Research-Style Capstone

A student compared causal vs correlational methods on a synthetic + real dataset and delivered strong ablation analysis, even without a production API. Result: high research signal with clear limitations.

### Case 3: Domain-Focused Capstone

A healthcare-oriented project used conservative model choices and heavy documentation on ethics and risk handling. Result: less model novelty but stronger real-world viability.

### When Smaller is Better

A focused, complete project often outperforms an over-scoped unfinished system. If time is limited, prioritize:

- one high-quality workflow,
- one robust evaluation story,
- one clear deployment or simulation artifact.

## Interview Questions & Answers

1. **Q:** How would you scope an AI capstone project?
   **A:** Define problem, stakeholders, constraints, and success metrics; then reduce scope to a must-have MVP with milestone gates.
2. **Q:** What makes a capstone realistic?
   **A:** Feasible timeline, accessible data, measurable objective, and clear fallback options.
3. **Q:** How do you choose between ML and LLM approaches?
   **A:** By task fit, data type, explainability needs, cost, and delivery timeline.
4. **Q:** What is a statement of work in capstone context?
   **A:** A formal scope contract describing objectives, deliverables, milestones, risks, and acceptance criteria.
5. **Q:** What is a common capstone failure mode?
   **A:** Overly broad scope without milestone-based de-risking.
6. **Q:** How do you define capstone success?
   **A:** Technical metrics + delivery quality + reproducibility + stakeholder clarity.
7. **Q:** How should learners handle uncertain data availability?
   **A:** Add contingency datasets and synthetic prototypes early.
8. **Q:** Why include non-objectives?
   **A:** To prevent scope creep and expectation mismatch.
9. **Q:** What if the best model is not deployable in time?
   **A:** Deploy simpler robust baseline and document upgrade path.
10. **Q:** Why are communication competencies part of capstone grading?
    **A:** Real AI projects succeed through cross-functional alignment, not modeling alone.
11. **Q:** How do you pick an impressive but feasible capstone?
    **A:** Select a narrow real problem and deliver complete lifecycle evidence.
12. **Q:** Should capstones prioritize novelty?
    **A:** Only if baseline execution is still solid; novelty without delivery is weak.
13. **Q:** What is the role of risk register?
    **A:** Early identification of blockers and explicit mitigation planning.
14. **Q:** How do you align capstone with career goals?
    **A:** Match project artifacts to target role expectations (MLOps, GenAI, product, research).
15. **Q:** What is an acceptable minimum capstone artifact set?
    **A:** Reproducible code, evaluation report, architecture notes, and clear demo.
16. **Q:** Why should capstones include ethics/safety reflection?
    **A:** Responsible AI is expected in modern production and leadership contexts.
17. **Q:** How often should scope be revisited?
    **A:** Weekly, with explicit must/should/could re-prioritization.
18. **Q:** What is a capstone milestone gate?
    **A:** A checkpoint where continuation depends on objective completion criteria.
19. **Q:** What if team members have different priorities?
    **A:** Use decision logs and role clarity to resolve trade-offs transparently.
20. **Q:** What would you do in week 1 of a capstone?
    **A:** Finalize problem framing, SoW, success metrics, dataset plan, and risk assumptions.

## Source-Informed References

- IBM AI Engineering Professional Certificate: https://www.coursera.org/professional-certificates/ai-engineer
- AI Capstone Project with Deep Learning (IBM/Coursera): https://www.coursera.org/learn/ai-deep-learning-capstone
- Monash FIT3193 AI Project (capstone learning outcomes): https://handbook.monash.edu/2026/units/fit3193
- Miami Dade College AI Capstone competencies: https://www.mdc.edu/asa/documents/competencies/pdf/CAI4950C%20Artificial%20Intelligence%20Capstone.pdf
- South Dakota AIE 465 AI Engineering Capstone II: https://www.sdstate.edu/sites/default/files/file-archive/2026-04/AIE%20465%20Aritficial%20Intelligence%20Engineering%20Capstone%20II%20%28NCR%29.pdf
