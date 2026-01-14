# PhysarumAI

PhysarumAI is a research project studying how the slime mould *Physarum polycephalum* forms transport networks and whether this process follows **probabilistic rules** rather than strict determinism or pure randomness.

The repository contains example experimental data, Wolfram Mathematica notebooks, and sample images used to analyse repeated experiments and construct **General (Probability) Matrices** of network connections.

Network structures are analysed using graph-theoretical methods and compared with classical geometric graphs (MST, RNG, GG).  
The long-term goal is to train an AI model that learns network formation principles directly from biological data.

**Author:** Timur Sakiev


## Repository contents

- `example_data_set.xlsx` — example dataset (experiment IDs, attractant positions, adjacency matrices, General matrices, distance matrices, etc.).
- `PROBABILITY.nb` — Wolfram Mathematica notebook for constructing and analysing **General / Probability Matrices**, edge frequencies, thresholds, and distributions.
- `MVP-7.nb` — Wolfram Mathematica notebook with the main visualisation / analysis pipeline (graphs, overlays, metrics, threshold filtering).
- `703_1 copy.jpg`, `703_1 copy.png` — example images from an experiment (photo / processed image).
- `организация_экспериментов.pdf` — protocol and organisation notes for experiments (Russian).

---

## Project idea (short)

*Physarum polycephalum* is a living system without a nervous system that still forms efficient networks.  
**Hypothesis:** network formation is **not strictly deterministic** and **not purely random**, but follows stable **probabilistic patterns** that can be measured across repeated experiments.

To test this, repeated runs with identical attractant configurations are aggregated into a **General (Probability) Matrix**, where edge weights represent how often each connection appears.

---

## Workflow (high-level)

1. Define a spatial configuration of attractant points (axial symmetry / radial symmetry / random).
2. Run repeated experiments under standardised conditions.
3. Photograph the final network and preprocess images (thresholding → binary).
4. Extract network connections and store them as adjacency matrices (Matrix 1–Matrix 10).
5. Sum repeated matrices into a **General Matrix** (edge weight = frequency).
6. Analyse:
   - edge-frequency histogram (rare / unstable / stable edges)
   - node-degree frequency (how often each node connects)
   - thresholded networks (edges with weight ≥ T)
   - comparison with reference graphs (MST / RNG / GG)

---

## How to use

### Option A — Using the example dataset
1. Download `example_data_set.xlsx`.
2. Open `PROBABILITY.nb` or `MVP-7.nb` in Wolfram Mathematica.
3. Update the data import section in the notebook (Excel path or your Google Sheets CSV link).
4. Run all cells.

### Option B — Using Google Sheets
If your notebook is configured for Google Sheets:
1. Publish the sheet as CSV or use the direct CSV link.
2. Paste the `sheetID` and `gid` into the notebook variables.
3. Evaluate the notebook.

> Note: some parts may require adjusting column names depending on your sheet structure.

---

## Data structure (typical)

For each experiment / configuration the dataset may include:
- `ru_ID` (experiment ID)
- attractant coordinates (grid cells)
- `Matrix 1–Matrix 10` (binary adjacency matrices from repeated runs)
- `General Matrix` (sum of repeated matrices; edge weights = frequency)
- distance matrix (pairwise distances between nodes)

---

## Requirements

- Wolfram Mathematica / Wolfram Language (tested on v14.2)
- (Optional) ImageJ/Fiji for preprocessing and binarisation

---

## Author and supervision

- **Author:** Timur Sakiev  
- **Supervisor / Advisor:** Korneyeva Darya

---

## Contact
+77052902292
dari30ko@gmail.com
Nazarbaev Intellectual School
