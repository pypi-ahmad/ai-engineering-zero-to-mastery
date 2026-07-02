# Overview

AI ethics is not an optional add-on to technical work. It is the discipline of analyzing and governing how AI systems affect people, institutions, and society at scale. University syllabi in AI ethics and governance (Georgia Tech PHIL 3101, UChicago Harris PPHA 38850, Luiss Ethics for AI) consistently frame ethics as a core competency because modern AI systems influence employment, policing, finance, health, education, and political discourse.

From an engineering perspective, ethics matters because:

- AI systems are sociotechnical systems, not only mathematical models.
- Harm can emerge even when offline metrics look strong.
- Trust, adoption, and regulatory compliance depend on ethical design.

Connection to earlier technical lessons:

- Lessons 1-3 showed how models are built and evaluated.
- Lessons 5-7 showed LLMs, agents, and deployment architecture.
- This chapter asks: "Should this system be built, deployed, and scaled this way?"

A useful framing equation is:

$$
\text{AI Impact} = f(\text{Model Behavior}, \text{Data Quality}, \text{Deployment Context}, \text{Power Relations})
$$

# Core Ethical Theories & Concepts

## Consequentialism (Outcome-Based Ethics)

Consequentialism evaluates actions by their outcomes. In AI, this often appears as cost-benefit analyses:

- Does an AI triage system reduce harm overall?
- Do efficiency gains outweigh false-positive harms?

Strength:

- Pragmatic for policy decisions at scale.

Limitation:

- Can justify harms to minorities if aggregate outcomes appear positive.

## Deontology (Duty- and Rights-Based Ethics)

Deontology focuses on duties, rights, and principles independent of outcomes.

AI implications:

- Respect privacy rights even if surveillance improves prediction.
- Do not use manipulative dark patterns even if engagement increases.

Strength:

- Protects individuals and constraints that should not be traded away.

Limitation:

- May not resolve conflicts between competing duties.

## Virtue Ethics (Character and Practice)

Virtue ethics asks what kind of people and institutions we become through technology choices.

AI implications:

- Are teams cultivating prudence, humility, and responsibility?
- Do organizations reward transparency or only growth metrics?

Strength:

- Highlights long-term institutional culture.

Limitation:

- Harder to operationalize into crisp pass/fail checks.

## AI-Relevant Ethical Concepts

1. Welfare
   - Impact on well-being (safety, dignity, opportunity).
2. Autonomy
   - Ability to make informed choices without coercion.
3. Liberty
   - Freedom from unjustified surveillance and control.
4. Equality
   - Fair treatment across social groups.
5. Privacy
   - Control over personal information and inference.
6. Fairness
   - Procedural and distributive justice in decisions.
7. Accountability
   - Clear ownership for decisions and harms.

# Ethical Challenges in AI

## Bias and Discrimination

Algorithmic bias arises when systems produce systematically unequal outcomes across groups due to data imbalance, label bias, historical injustice, or design choices.

Common mechanisms:

- Representation bias (some groups underrepresented).
- Measurement bias (labels encode historical prejudice).
- Deployment mismatch (model used outside intended context).

## Privacy and Surveillance

AI increases inference power: systems can infer sensitive traits from seemingly benign data. Even legal collection may still be ethically problematic if consent is weak or power asymmetry is high.

## Manipulation, Disinformation, and Dark Patterns

Recommendation engines and generative tools can optimize engagement at the expense of truth and autonomy. Risks include polarization, compulsive use, and targeted persuasion.

## Labor Impacts and Power Concentration

AI can augment workers, but can also deskill jobs, intensify monitoring, and concentrate control in a few organizations with compute and data advantages.

# Case Studies

## Case Study 1: Algorithmic Hiring

Scenario:

- A company deploys an automated resume screening model to reduce recruiter workload.

Stakeholders:

- applicants, recruiters, HR leadership, regulators, society.

Ethical risks:

- biased rejection patterns by gender/race proxies.
- opacity: candidates cannot contest outcomes.
- false objectivity: "algorithm says no" becomes unchallengeable.

Framework analysis:

- Consequentialist: efficiency and time-to-hire gains.
- Deontological: right to fair consideration and non-discrimination.
- Virtue ethics: whether hiring culture values justice over convenience.

## Case Study 2: Predictive Policing / Risk Assessment

Scenario:

- A municipality uses historical arrest data to forecast crime hotspots.

Ethical risks:

- feedback loop: over-policed communities generate more arrests, reinforcing the model.
- group harm despite local accuracy metrics.
- democratic legitimacy concerns if public oversight is weak.

Key lesson:

- "Predictive" systems can reproduce structural inequality when trained on biased institutional history.

## Case Study 3: Social Media Recommenders

Scenario:

- A platform optimizes feed ranking for watch time and retention.

Ethical risks:

- manipulation of attention and autonomy.
- amplification of harmful or extreme content.
- youth mental-health and civic discourse impacts.

Trade-off tension:

- business KPI optimization vs long-term social welfare.

# Frameworks & Principles for Ethical AI

## FAT and Beyond

FAT (Fairness, Accountability, Transparency) is a foundational lens:

- Fairness: avoid unjust disparate outcomes.
- Accountability: assign responsibility and remedy paths.
- Transparency: make system purpose, limits, and reasoning understandable.

Most modern Responsible AI frameworks expand FAT with:

- safety/security
- privacy/data governance
- human oversight
- reliability/robustness

## Example Principle Sets

- Microsoft Responsible AI principles and standardized requirements.
- Google Responsible AI guidance (fairness, accountability, safety, privacy).
- OECD AI Principles for trustworthy and human-centered AI.
- UNESCO Recommendation emphasizing human rights and dignity.
- EU trustworthy AI guidance and later risk-based legal frameworks.

No single checklist is enough; high-stakes systems require contextual, iterative governance.

# Business Case Studies & Exceptions

## Case Study A: Recommender System Fairness vs Privacy

A streaming platform wants to improve recommendations using richer personal data.

Benefits:

- better relevance and retention.

Risks:

- privacy intrusion from sensitive behavior inferences.
- minority creators under-exposed due to popularity feedback loops.

Practical response:

1. limit sensitive feature usage by policy.
2. monitor creator exposure parity and user well-being signals.
3. offer user controls for recommendation transparency.

## Case Study B: Startup and Sensitive Attributes

A health-tech startup debates whether to include protected attributes to improve calibration.

Tension:

- excluding attributes may hide bias.
- including them can introduce legal/ethical risk if misused.

Pragmatic pattern:

- use sensitive attributes in controlled fairness evaluation, not unrestricted optimization.
- involve legal/compliance and domain experts before deployment.

## Exceptions

- In safety-critical settings, conservative human review may be mandatory even if automation seems accurate.
- In low-risk internal tools, lightweight governance may be sufficient; apply proportionality.

# Interview Questions & Answers

1. **What are the main ethical concerns around AI-based hiring?**  
Bias, opacity, contestability, and potential discrimination through proxy features.

2. **Explain algorithmic bias.**  
Systematic unfair outcomes caused by data, modeling, or deployment factors, often reflecting historical inequities.

3. **How would you explain fairness vs accuracy trade-offs to non-technical stakeholders?**  
A model can be globally accurate while repeatedly failing specific groups; fairness ensures benefits and errors are distributed justly.

4. **What is the difference between ethics and compliance?**  
Compliance is legal minimum requirements; ethics asks what is right and responsible even when law is silent.

5. **When can a model be ethically problematic but technically strong?**  
When it achieves high metrics but harms autonomy, dignity, or equal opportunity.

6. **Why is transparency important in AI systems?**  
It enables trust, auditing, contestability, and informed oversight.

7. **Give an example of autonomy harm in AI products.**  
A recommendation engine nudging users into compulsive behavior using manipulative design.

8. **How do consequentialism and deontology differ in AI decisions?**  
Consequentialism prioritizes aggregate outcomes; deontology enforces rights and duties regardless of aggregate gain.

9. **What is accountability in AI practice?**  
Clear ownership, traceability, and mechanisms to investigate and remediate harms.

10. **Why can predictive policing systems be controversial?**  
They can reinforce historical over-policing and create self-reinforcing bias loops.

11. **Can removing protected attributes solve fairness?**  
Not always; proxies can preserve bias and hide disparate impact.

12. **How should teams prioritize ethical risks?**  
By severity, affected populations, reversibility, and scale of potential harm.

13. **What is ethical debt?**  
Accumulated unresolved ethical risk from shortcuts, similar to technical debt.

14. **How do you respond when business pressure conflicts with ethics?**  
Escalate risk with evidence, propose safer alternatives, and document decisions and ownership.

15. **What does human oversight mean in ethics terms?**  
Humans retain meaningful control over high-impact decisions and can intervene effectively.

# References

- Georgia Tech PHIL 3101 course page (AI Ethics and Policy): https://syllabus.gatech.edu/syllabi/3101/rm
- Georgia Tech AI Ethics and Policy launch note: https://iac.gatech.edu/news/item/668558/ethics-policy-course-launched-georgia-tech
- UChicago Harris syllabus (PPHA 38850): https://harris.uchicago.edu/sites/default/files/2024-03/PPHA%2038850_Ethics%20and%20Governance%20of%20AI_2024_Uhl.pdf
- Luiss Ethics for AI syllabus: https://www.luiss.it/sites/default/files/2026-02/EthicsForAI.pdf
- UNESCO Recommendation on the Ethics of AI: https://www.unesco.org/en/articles/recommendation-ethics-artificial-intelligence
- OECD AI policy overview: https://www.oecd.org/en/topics/policy-issues/artificial-intelligence.html
- Google Responsible AI intro: https://developers.google.com/machine-learning/guides/intro-responsible-ai
- Microsoft Responsible AI principles and approach: https://www.microsoft.com/en-us/ai/principles-and-approach
