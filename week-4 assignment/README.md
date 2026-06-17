
# Graph Representation Learning Assignment

## 2️⃣ Knowledge Graphs (KGs)
A Knowledge Graph is a structured representation of entities (nodes) and relationships (edges) where:
- Nodes = entities (people, objects, concepts)
- Edges = relationships (works_at, located_in, etc.)

Formally, KG = (E, R, T)
- E: entity set
- R: relation set
- T: triples (h, r, t)

KGs enable reasoning over structured knowledge and are widely used in search engines, recommendation systems, and LLM augmentation.

---

## 3️⃣ Over-smoothing vs Over-squashing

### Over-smoothing
When stacking many GNN layers, node embeddings become indistinguishable.

Why?
- Repeated averaging over neighbors
- Convergence to similar representations

Effect:
- Node embeddings lose uniqueness

Fixes:
- Residual connections
- Jumping Knowledge networks
- Normalization tricks

---

### Over-squashing
Too much information from large neighborhoods is compressed into fixed-size embeddings.

Why?
- Exponential growth of receptive field
- Bottleneck in message aggregation

Effect:
- Long-range dependencies get lost

Fixes:
- Graph rewiring
- Attention mechanisms
- Positional encodings

---

### Key Tension
More layers = larger receptive field BUT more over-smoothing.
Fewer layers = preserve identity BUT miss global structure.

---

## 5️⃣ Graph Thinking Shift
Example dataset: Tabular Iris dataset

We can convert:
- Each sample = node
- Similarity (kNN) = edges

Why graph?
- Captures local similarity structure
- Enables relational reasoning between samples

---

## Reflection Task (example idea)
Train GNN vs MLP on same dataset and compare performance.
