import os

DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

print("PhysarumAI dataset is hosted on Zenodo.") 
https://doi.org/10.5281/zenodo.18411398

print("Please download the CSV files from Zenodo and place them into the 'data/' directory.")
print("Expected data format: CSV files containing adjacency matrices, probability matrices,")
print("node coordinates, and distance matrices.")
