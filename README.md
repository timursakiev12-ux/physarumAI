# PhysarumAI  
Data-driven AI for adaptive network design

## Overview
PhysarumAI is an AI-based system for designing and analyzing adaptive transport and infrastructure networks.  
The project combines large-scale experimental data with machine learning to model how efficient and resilient networks emerge under uncertainty.

Unlike classical optimization approaches that produce a single deterministic solution, PhysarumAI operates with probabilistic network structures, allowing the analysis of stability, redundancy, and alternative pathways.

---

## Problem
Many real-world infrastructure and transport networks must operate under changing conditions, limited resources, and partial failures.  
Classical engineering and mathematical optimization methods are typically designed for fixed assumptions and often produce fragile solutions that degrade when conditions change.

At the same time, adaptive network formation in real physical systems is difficult to capture using purely theoretical models. This creates a need for data-driven approaches that learn network formation rules directly from real processes rather than predefined optimization criteria.

---

## Solution
PhysarumAI proposes a non-traditional, data-driven approach inspired by experimentally observed network formation in physical systems.

Instead of using abstract simulations or hand-crafted rules, the project is based on a large experimental dataset collected through repeated controlled experiments. These experiments capture how networks form, adapt, and reorganize under identical spatial conditions, producing distributions of possible network structures rather than a single optimal result.

Using this dataset, PhysarumAI trains a machine learning model that learns probabilistic rules of network formation and applies them to the generation and analysis of adaptive network topologies.

---

## Experimental Dataset
At the core of PhysarumAI lies a proprietary experimental dataset collected under controlled laboratory conditions.

### Data collection pipeline:
1. **Physical experiments**  
   Network formation experiments are conducted in Petri dishes with an agar medium.  
   Each spatial configuration of nodes is repeated 10–18 times to capture variability in network formation.

2. **Image processing**  
   Network images are processed using ImageJ and converted into standardized binary representations.

3. **Graph construction**  
   Binary images are transformed into graph representations consisting of nodes and connections.

4. **Adjacency matrices**  
   For each experimental repeat, an adjacency matrix is generated to represent the presence or absence of connections.

5. **General matrix**  
   Adjacency matrices from repeated experiments are aggregated into a general matrix representing connection frequencies.

6. **Probability matrix**  
   The general matrix is normalized to produce a probability matrix indicating how often each connection appears across repetitions.

### Stored dataset information:
- experiment ID;
- repeat ID;
- node coordinates;
- probability matrices;
- distance matrices.

This structure allows the model to learn from distributions of network structures rather than single outcomes.

---

## AI Model
The core AI component is a supervised neural network trained on experimental probability matrices.

### Model characteristics:
- **Input:** four numerical features describing relationships between node pairs;
- **Output:** probability of connection between nodes;
- **Training target:** experimentally derived connection probabilities;
- **Purpose:** learning probabilistic rules of adaptive network formation.

The model prioritizes robustness and adaptability over minimal path length or cost.

---

## MVP
The current MVP is implemented in **Wolfram Mathematica** and runs locally.

It includes two main tools:

### 1. AI-based network generation
- accepts user-defined node configurations;
- predicts connection probabilities using the trained model;
- generates adaptive networks based on a selectable probability threshold.

### 2. Experimental data exploration
- allows navigation through the experimental dataset;
- visualizes real networks using probability thresholds;
- enables comparison between observed and AI-generated structures.

The MVP focuses on demonstrating core principles and does not require deployment or a graphical interface.

---

## Data Access
The experimental dataset is hosted externally on **Zenodo**.

- Data type: graphs, adjacency matrices, probability matrices, distance matrices  
- Access: external download (not stored in this repository)

Instructions for dataset usage are provided in `scripts/download_data.py`.

---

## How to Run (Local)
1. Install **Wolfram Mathematica**.
2. Download the dataset from Zenodo and place CSV files into the `data/` directory.
3. Open the provided Wolfram Notebook files.
4. Execute the notebook cells to load the model and visualize networks.

All computations are performed locally.

---

## Project Status
PhysarumAI is an experimental AI project focused on adaptive network modeling.  
Future development directions include model scaling, extended feature sets, and interactive visualization tools.


---

## Author and supervision

- **Author:** Timur Sakiev  
- **Supervisor / Advisor:** Korneyeva Darya

---

## Contact
+77052902292
dari30ko@gmail.com
Nazarbaev Intellectual School
