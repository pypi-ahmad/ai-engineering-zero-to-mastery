# Exercises: 4.4 Sequence Models, Attention & Transformers

Prerequisite (recommended):

```bash
uv sync --frozen --extra dl
```

These exercises focus on *mechanics* (shapes, masks, correctness), not on training a big model.

## Exercise 1: Scaled Dot-Product Attention (Shapes)

Implement scaled dot-product attention:

$$
\\text{Attention}(Q,K,V) = \\text{softmax}(QK^T / \\sqrt{d_k})V
$$

Verify shapes for:
- `Q, K, V` of shape `(B, T, D)`.

Expected outcome:
- output has shape `(B, T, D)`.

## Exercise 2: Causal Mask (No Looking Ahead)

Add a causal mask so position `t` cannot attend to positions `> t`.

Expected outcome:
- attention weights above the diagonal are ~0.

## Exercise 3: Positional Encoding (Sinusoidal)

Implement sinusoidal positional encodings and verify:
- shape `(T, D)`,
- different positions produce different vectors,
- values are bounded in `[-1, 1]`.

Expected outcome:
- you can explain why we need position information in transformers.

## Exercise 4: Multi-Head Attention (Minimal)

Implement a minimal multi-head attention module:
- split `D` into `H` heads,
- apply attention per head,
- concat and project back to `D`.

Expected outcome:
- output shape matches input shape.

## Exercise 5: Parameter Count Spot Check

For a transformer block with:
- model dim `D`,
- heads `H`,
- MLP hidden `4D`,

Compute approximate parameter count for:
- QKV projections + output projection,
- MLP layers.

Expected outcome:
- you can estimate “how big” a block is without looking it up.

