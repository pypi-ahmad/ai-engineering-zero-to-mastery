# Overview

By Lesson 11, the objective is no longer "learn one more model." The objective is evidence of end-to-end capability.

A compelling AI portfolio should demonstrate four dimensions:

1. Engineering execution.
2. Product/business reasoning.
3. Responsible AI and governance awareness.
4. Communication and iteration maturity.

Capstones are the highest-signal artifact because they force trade-off decisions across model quality, UX, reliability, and impact.

# Portfolio Strategy

## Build a portfolio architecture, not a random project list

Use a portfolio matrix:

- Axis 1: technical depth (data, modeling, systems).
- Axis 2: impact depth (user/business outcomes).

Target a balanced mix:

- one systems-heavy project,
- one product-outcome project,
- one domain-specialized project,
- one research-style project with rigorous evaluation.

## Storytelling framework

For each project, capture:

1. Problem and stakeholders.
2. Why this solution path was chosen.
3. What was built and measured.
4. Trade-offs and failures.
5. What you would do next.

Recruiters and investors evaluate decision quality as much as technical stack choice.

# Capstone Design Patterns

## Pattern A: End-to-end AI product

Includes:

- ingestion/feature pipeline,
- model or LLM workflow,
- API/service layer,
- monitoring and feedback loop,
- dashboard or user-facing interface.

Strong evidence:

- measurable impact on a workflow metric,
- clear launch and rollback strategy.

## Pattern B: Research-style capstone

Includes:

- hypothesis and baseline definitions,
- controlled experiments and ablations,
- reproducibility package,
- limitations and external validity analysis.

Strong evidence:

- clear methodological rigor and honest uncertainty reporting.

## Pattern C: Domain-focused solution

Includes:

- domain constraints (regulatory, latency, safety),
- domain-specific KPIs,
- governance controls relevant to the sector.

Strong evidence:

- adaptation of generic AI methods to real domain requirements.

# Documentation & Publication

## Artifact stack

Every serious project should have:

- concise README (problem, architecture, runbook, results),
- reproducible notebook(s) for key experiments,
- architecture diagram (even text-based),
- model/system card covering limitations,
- demo walkthrough and evaluation summary.

## Publication channels

- GitHub project with issue tracker and roadmap,
- technical blog post with methods and outcomes,
- short demo video,
- preprint or report for research-heavy projects,
- launch post with measurable pilot outcomes.

# Launch & Feedback Loops

## MVP to iteration path

A useful launch sequence:

1. Internal alpha with synthetic and historical cases.
2. External pilot with narrow user segment.
3. Metric review and failure analysis.
4. Iterative hardening before broader rollout.

## Feedback loop design

Collect three classes of feedback:

- quantitative usage/performance telemetry,
- qualitative user friction and trust signals,
- operator/developer incident logs.

Then map findings into prioritized next experiments.

# Business / Research Case Studies & Exceptions

## Case 1: Candidate targeting ML engineering roles

Portfolio shape:

- one production pipeline project,
- one LLM application with evaluation harness,
- one error-analysis and monitoring artifact.

Why this worked:

- demonstrated reliability, not just modeling.

Exception:

- if documentation is weak, strong technical code still underperforms in interviews.

## Case 2: Candidate targeting AI PM or founder roles

Portfolio shape:

- one product PRD + metrics tree artifact,
- one MVP pilot report with business outcomes,
- one responsible AI risk/governance document.

Why this worked:

- showed decision quality, prioritization, and measurable impact.

Exception:

- purely strategic artifacts without runnable prototypes can weaken credibility.

## Case 3: Candidate targeting research/applied scientist roles

Portfolio shape:

- one reproducible experimentation project (baselines + ablations),
- one domain AI-for-science case with uncertainty analysis,
- one concise technical report/preprint-style write-up.

Why this worked:

- showcased methodological rigor and scientific communication.

Exception:

- strong benchmark scores without robustness checks are increasingly viewed as incomplete evidence.

# Interview Questions & Answers

1. **How would you describe your strongest AI project?**  
Using problem, constraints, architecture, metrics, outcomes, and next-step improvements.

2. **How do you choose capstone scope?**  
Constrain by one core user/job and one measurable success metric.

3. **What makes a portfolio project high-signal?**  
Clear decisions, reproducible evidence, and realistic trade-off handling.

4. **How do you balance breadth vs depth in portfolio design?**  
Maintain one deep flagship project and supporting projects that show range.

5. **What should be in a project README for AI roles?**  
Problem, approach, architecture, evaluation, limitations, run instructions, and future work.

6. **How do you prove impact if data is limited?**  
Use pilot proxies, baseline comparisons, and explicit assumptions.

7. **How do you discuss project failures in interviews?**  
Explain hypothesis, what failed, diagnostic process, and design changes made.

8. **What is a strong capstone launch plan?**  
Narrow pilot, predefined success criteria, safety checks, and rollback protocol.

9. **How do you show product thinking as an engineer?**  
Link technical choices to user outcomes and business constraints.

10. **How do you show research rigor in a portfolio?**  
Publish baseline parity, ablations, variance, and reproducibility details.

11. **How do you make capstone results credible?**  
Document methodology, control confounders, and include limitations.

12. **What are common portfolio mistakes?**  
Too many shallow demos, no metric evidence, and missing operational considerations.

13. **How do you prioritize next iterations post-launch?**  
Rank by user impact, risk reduction, and learning value.

14. **How do you adapt one project for PM vs engineering interviews?**  
PM version emphasizes outcomes/roadmap; engineering version emphasizes architecture/reliability.

15. **How do you choose publication format?**  
Match audience: practitioners need deployment clarity; researchers need methodological rigor.

16. **How do you include responsible AI in portfolio narratives?**  
Show risk controls, fairness checks, governance decisions, and incident handling.

17. **What metrics should you show for GenAI projects?**  
Task success, groundedness, latency, cost per task, and escalation rate.

18. **How do you justify model choices in interviews?**  
Compare alternatives by performance, cost, reliability, and maintainability.

19. **What if your project had no real users?**  
Use realistic simulation, expert review, and explicit validation limits.

20. **What would you do next with a finished capstone?**  
Harden data/monitoring, run a controlled pilot, and expand scope only after evidence.

# References

- Udacity AI Product Manager Nanodegree (project and PM framing): https://www.udacity.com/course/ai-product-manager-nanodegree--nd088
- InstitutePM AI Product Management Masterclass context: https://www.institutepm.com/
- HelloPM AI PM course (PRD/analytics/interview structure): https://hellopm.co/free/
- UCSB Applied AI and Innovation (portfolio/team studio framing): https://www.professional.ucsb.edu/certificate-applied-ai-and-innovation
- JHU AI for Entrepreneurs (startup-oriented AI course context): https://ep.jhu.edu/courses/635674-ai-for-entrepreneurs/
- DeepMind Science overview for AI-for-science positioning: https://deepmind.google/science/
