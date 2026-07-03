# Convolutional Neural Networks & Computer Vision

## Overview

Computer vision became practical at scale because CNNs encode spatial inductive bias: nearby pixels interact strongly, patterns repeat across positions, and hierarchical features emerge from simple edges to complex objects.

This chapter covers CNN mechanics and production-minded CV pipeline choices.

## CNN Building Blocks

### Convolution

Convolution applies learnable filters across local receptive fields. Weight sharing reduces parameters and improves translation tolerance.

### Pooling and Strides

Pooling/downsampling reduces spatial resolution and compute while increasing receptive field.

### Feature Hierarchies

Early layers learn edges/textures; deeper layers learn shapes, parts, and semantic patterns.

## Canonical Architecture Progression

- `LeNet`: early proof of learned convolution features.
- `AlexNet`: deep CNNs + ReLU + GPU acceleration.
- `VGG`: simple repeated blocks with depth.
- `ResNet`: residual connections enabling very deep networks.
- `EfficientNet/MobileNet`: efficiency-oriented scaling for resource constraints.

Why this matters:

- architecture families reflect different accuracy/latency/compute trade-offs.

## Transfer Learning for Practical Teams

Training from scratch is often unnecessary for capstones and real products with limited data.

Practical transfer strategy:

1. start from pretrained backbone,
2. replace classification head,
3. freeze backbone initially,
4. unfreeze selectively for fine-tuning.

Benefits:

- faster convergence,
- better performance with limited labeled data,
- lower compute budget.

## Evaluation and Error Analysis

Beyond top-line accuracy, track:

- per-class precision/recall,
- confusion matrix,
- calibration where needed,
- error slices (lighting, blur, background, viewpoint).

Operationally relevant checks:

- robustness to simple perturbations,
- data distribution mismatch between train and deployment context,
- fairness across user/environment segments when applicable.

## Deployment Considerations

Vision model deployment decisions:

- cloud API vs edge device,
- latency budget,
- model size and quantization,
- batching strategy,
- monitoring pipeline for data drift.

Capstone-appropriate deployment pattern:

- start with single-image API + logging,
- add batching and optimization only when justified by metrics.

## Business Cases and Practical Translation

Common CV applications:

- manufacturing defect detection,
- medical image triage support,
- retail shelf analytics,
- document and visual content moderation.

Key product principle:

- optimize for risk-adjusted reliability, not only benchmark score.

## Case Studies & Exceptions

### Case 1: Manufacturing Defect Detector with False Confidence

Scenario:
A production line vision model achieved high validation accuracy but missed rare defect types after deployment.

What happened:

- training set underrepresented edge-case defects,
- confidence scores were not calibrated,
- monitoring tracked only average accuracy.

Fix:

- add targeted data collection for rare defect modes,
- evaluate per-defect recall and confidence calibration,
- create human-review fallback for low-confidence predictions.

### Case 2: Retail Shelf Analytics in Uncontrolled Lighting

Scenario:
Shelf detection worked in lab images but degraded in stores.

Root causes:

- domain shift in illumination and camera angle,
- insufficient augmentation for deployment conditions.

Fix:

- enrich augmentation with realistic lighting transforms,
- use periodic re-labeling and incremental fine-tuning,
- add store-level drift alerts.

Exception:
If camera setup is fixed and environment controlled, simpler deterministic image-processing plus lightweight ML can outperform large CNN pipelines on maintenance cost.

### Case 3: Edge Deployment Trade-off

Scenario:
A mobile app needed <80 ms inference latency.

Decision:

- switched from heavier ResNet to MobileNet variant with quantization.

Outcome:

- small accuracy drop,
- large latency and battery gains,
- better user retention.

Lesson:
Model selection must optimize end-to-end utility, not leaderboard rank.

## CV Deployment Checklist

- Dataset includes deployment-specific variability (lighting, blur, viewpoint).
- Metrics reported by class and risk segment.
- Latency and memory budgets validated on target hardware.
- Confidence thresholds and fallback actions defined.
- Drift monitoring pipeline ready before rollout.

## Project Prompts & Practice Exercises

1. Build a transfer-learning classifier on CIFAR-10 or a domain-specific image set.
2. Compare frozen-backbone vs fine-tuned-backbone performance and training time.
3. Create an error taxonomy and propose targeted data augmentation.
4. Prototype a FastAPI image prediction endpoint with response-time logging.

## Interview Questions & Answers

1. **Q:** Why are CNNs effective for images?  
   **A:** They exploit local spatial structure and shared patterns via convolution.
2. **Q:** What is parameter sharing?  
   **A:** Using the same filter weights across spatial positions.
3. **Q:** Why use pooling?  
   **A:** Reduce spatial resolution and improve robustness while lowering compute.
4. **Q:** What problem do residual connections solve?  
   **A:** They improve gradient flow and enable deeper training.
5. **Q:** Why use transfer learning?  
   **A:** Better performance and faster convergence with limited labeled data.
6. **Q:** Freeze then fine-tune—why?  
   **A:** Stabilizes early training and prevents destructive updates to pretrained features.
7. **Q:** How do you debug poor CV performance?  
   **A:** Use confusion matrices, class-wise metrics, and visual error inspection.
8. **Q:** What is domain shift in vision?  
   **A:** Difference between training image distribution and real deployment images.
9. **Q:** Why is latency a first-class metric in CV deployment?  
   **A:** Many CV applications are real-time or near-real-time.
10. **Q:** What is quantization used for?  
    **A:** Reducing model size and inference cost, especially for edge/mobile.
11. **Q:** What is a receptive field?  
    **A:** Input region influencing a unit's activation.
12. **Q:** Why might accuracy be misleading in multi-class vision tasks?  
    **A:** Class imbalance can hide poor minority-class performance.
13. **Q:** How do you choose augmentation strategy?  
    **A:** Based on realistic deployment variability, not arbitrary transformations.
14. **Q:** What deployment artefacts should you provide in a capstone?  
    **A:** Model card summary, API spec, inference script, and monitoring notes.
15. **Q:** What is the first production risk to check in CV?  
    **A:** Input distribution mismatch and failure behavior under poor image quality.

## Bridge to Lesson 4.4

Vision introduced inductive bias and scalable deep architectures. The next chapter shifts to sequence modeling and attention, culminating in transformers that underpin modern LLM and GenAI systems.
