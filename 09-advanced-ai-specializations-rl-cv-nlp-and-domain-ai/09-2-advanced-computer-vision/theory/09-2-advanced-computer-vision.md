# Overview

Modern computer vision has moved far beyond image classification. Production systems now require object detection, semantic/instance segmentation, multimodal understanding, and deployment-aware design for real-time and edge constraints.

Why this matters:

- classification answers "what is in this image?"
- detection answers "what and where?"
- segmentation answers "which pixel belongs to which class/object?"

From a systems perspective, advanced CV is a trade-off among:

$$
\text{Quality} \leftrightarrow \text{Latency} \leftrightarrow \text{Cost} \leftrightarrow \text{Robustness}
$$

# Key Architectures & Tasks

## Object Detection

Goal: localize and classify objects with bounding boxes.

### Faster R-CNN (Two-Stage)

Pipeline:

1. backbone extracts feature maps,
2. region proposal network (RPN) proposes candidate boxes,
3. ROI head classifies/refines proposals.

Strength:

- high accuracy for many settings.

Weakness:

- often slower than single-stage detectors.

### YOLO Family (Single-Stage, High-Level)

Predicts boxes/classes directly from dense feature maps.

Strength:

- strong real-time performance.

Weakness:

- historical precision trade-offs on small/occluded objects (varies by version).

## Semantic Segmentation

Goal: assign class label to every pixel.

### U-Net

Encoder-decoder with skip connections, widely used in biomedical imaging.

### DeepLab (High-Level)

Uses atrous/dilated convolutions and multi-scale context modeling.

## Instance Segmentation

Goal: detect each object instance and segment its pixels.

### Mask R-CNN

Extends Faster R-CNN by adding a mask prediction branch.

## Vision Transformers (ViT)

Treat image as sequence of patches and use transformer attention over patch embeddings.

Pros:

- strong scaling behavior and global context modeling.

Cons:

- can require substantial data/compute without strong pretraining.

# Multimodal Vision

## CLIP-Style Models

Contrastive training aligns image and text embeddings into shared space.

Use cases:

- zero-shot image classification,
- image-text retrieval,
- multimodal search.

## Vision-Language Tasks

1. Image captioning
2. Visual question answering (VQA)
3. Grounded retrieval and assistant-style perception

Design implication:

- multimodal systems shift evaluation from raw accuracy to semantic alignment and hallucination control.

# Edge & Real-Time Vision

## Deployment Constraints

- low latency budgets,
- limited compute/memory,
- battery and thermal limits,
- intermittent connectivity.

## Optimization Techniques

1. Quantization (INT8/FP16)
2. Pruning and distillation
3. Efficient backbones (MobileNet-like)
4. Runtime optimization (ONNX/TensorRT/TFLite style workflows)

## Monitoring in Vision Systems

Track:

- confidence distribution drift,
- class imbalance in live traffic,
- false positive/negative hot spots,
- end-to-end latency percentiles.

# Business Case Studies & Exceptions

## Case Study 1: Manufacturing Defect Detection

Scenario:

- Vision model flags defects on production lines.

Architecture pattern:

- detection model for defect localization,
- anomaly fallback for unseen defect types,
- edge inference near cameras for low latency.

Trade-offs:

- threshold tuning impacts false rejects vs escaped defects.

## Case Study 2: Retail Analytics

Scenario:

- Stores use cameras for shelf analysis and footfall heatmaps.

Challenges:

- privacy governance,
- occlusions and lighting shifts,
- real-time throughput during peak hours.

Practical constraints:

- strict anonymization and retention policy,
- domain adaptation for each store layout.

## Exceptions

- If precise localization is unnecessary, classification can be cheaper and sufficient.
- In highly privacy-sensitive zones, non-visual sensors may be preferred.

# Interview Questions & Answers

1. **Detection vs segmentation: what is the difference?**  
Detection outputs boxes + labels; segmentation outputs pixel-level class or instance masks.

2. **When would you choose Faster R-CNN?**  
When accuracy is prioritized over raw inference speed.

3. **When would you choose YOLO-like models?**  
When near-real-time inference is required.

4. **What is instance segmentation?**  
Separating each individual object mask, not just class-wise pixel labeling.

5. **What makes U-Net strong in medical imaging?**  
Skip connections preserve spatial detail critical for fine boundaries.

6. **What is a Vision Transformer?**  
A transformer-based vision model operating on patch tokens with self-attention.

7. **What is CLIP useful for?**  
Learning joint image-text representations enabling zero-shot and retrieval tasks.

8. **How do you optimize CV models for edge?**  
Quantization, pruning/distillation, efficient backbones, and optimized runtimes.

9. **What is a common failure mode in production CV?**  
Domain shift from training data (lighting, camera angle, weather, clutter).

10. **How do you evaluate detection models?**  
Typically mAP and per-class precision/recall with IoU thresholds.

11. **How do you monitor a deployed vision model?**  
Track latency, confidence drift, class distributions, and sampled human audits.

12. **What is the trade-off between precision and recall in defect detection?**  
Higher recall can increase false alarms; higher precision can miss true defects.

13. **Why is dataset curation critical for segmentation?**  
Label quality and boundary consistency strongly impact pixel-level performance.

14. **How do multimodal vision systems fail?**  
Text-image misalignment, hallucinated associations, and biased retrieval.

15. **How do you decide if edge deployment is needed?**  
Based on latency, privacy, connectivity, and operational cost constraints.

# References

- Stanford CS231n site: https://cs231n.stanford.edu/ and schedule archive: https://cs231n.stanford.edu/2021/schedule.html
- CS231n notes (ConvNets): https://cs231n.github.io/convolutional-networks/
- Torchvision Faster R-CNN docs: https://docs.pytorch.org/vision/stable/models/faster_rcnn.html
- Stanford course ecosystem (AI specialization reference): https://web.stanford.edu/class/cs224n/ (for neighboring transformer content)
