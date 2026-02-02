## Detailed Architecture (MVP)

PhysarumAI MVP is structured as a reproducible pipeline with clear separation between:
(1) experimental data, (2) model training artifacts, (3) inference and visualization tools.

### 1) Data Layer (Experimental Dataset)
**Goal:** provide standardized inputs for training and validation.

**Inputs produced by the data pipeline:**
- **Node layout:** coordinates of resource points for each configuration.
- **Binary network images (ImageJ):** standardized masks used for extracting network structure.
- **Per-repeat adjacency matrices:** one adjacency matrix per repeat (edge present / absent).
- **General matrix (frequency matrix):** aggregation of adjacency matrices across repeats for the same configuration (edge counts).
- **Probability matrix:** normalized general matrix representing edge probability `p ∈ [0, 1]` for each node pair.
- **Distance matrix:** pairwise distances between nodes for each configuration.

**Key idea:** identical spatial configurations are repeated (10–18 times), so the dataset captures a **distribution of networks**, not a single “optimal” graph.

---

### 2) Model Layer (Training + Trained Artifacts)
**Goal:** learn probabilistic rules of network formation from experimental repetitions.

**Training objective (high level):**
- The model learns a mapping from **pairwise features (for node i–j)** → **probability of an edge** `P(edge_ij)`.

**Training target:**
- `P(edge_ij)` comes from the **probability matrix** (derived from repeated experiments for the same configuration).

**Training samples:**
- Each experiment configuration with `k` nodes generates `k×k` (or upper-triangular) **node-pair samples**.
- Each sample corresponds to a potential edge `(i, j)` with:
  - feature vector `X(i, j)` (4 inputs),
  - target value `y(i, j) = P(edge_ij)`.

**Why this works:**
- Repeats convert biological variability into a measurable signal:
  - stable edges → high probability,
  - optional edges → medium probability,
  - rare edges → low probability.

**Training artifact:**
- The trained model is saved as `trainedNet4_flow_groupSplit.wlnet` and reused for inference without retraining.

---

### 3) Application Layer (MVP Tools)
**Goal:** demonstrate the product value through two tools that use the same probability logic.

#### A) AI Prediction / Network Generation (Inference)
File: `PhysarumAI_PredictionV1.nb`

**What it does:**
- Loads the trained model (`.wlnet`).
- Accepts a new node configuration (coordinates).
- Computes predicted edge probabilities for all node pairs.
- Builds a network by applying a **user-defined probability threshold** `thr`:
  - keep edges where `P(edge_ij) ≥ thr`.

**Why threshold matters:**
- High `thr` → only the most stable “backbone” connections.
- Lower `thr` → adds redundancy and alternative routes.
- This acts as a practical “resilience dial” for network design.

#### B) Experimental Data Viewer (Real Networks from Dataset)
File: `experimental_data_viewer.nb`

**What it does:**
- Loads the dataset tables (CSV).
- Lets users select an experiment/configuration ID.
- Visualizes edges from the **experimental probability matrix** using the same threshold logic `thr`.
- Enables direct comparison between:
  - real experimental probability networks,
  - AI-predicted probability networks (same node layout).

---

## Model Training Details (MVP Level)

### Feature set (4-input model)
The MVP model uses four numeric inputs describing the relationship between nodes `(i, j)` and the configuration context.  
(Exact feature definitions are documented in the training notebook and can be extended in future versions.)

### Preventing data leakage
To avoid overly optimistic results, training and testing are separated by **configuration groups** (group split).  
This ensures that node-pair samples from the same experimental configuration do not appear in both train and test sets.

### Output and usage
The model outputs a probability `p ∈ [0, 1]` for each potential edge `(i, j)`.  
Downstream tools interpret these probabilities using a threshold to generate and analyze networks.
