"""
data_loader.py
Automatically download MOT15 dataset from KaggleHub into ./data/
Usage:
    python data_loader.py
"""

import os
import kagglehub

# Download dataset from KaggleHub
dataset_path = kagglehub.dataset_download("mdraselsarker/mot15-challenge-dataset", extract=True)

# Ensure ./data folder exists
os.makedirs("data", exist_ok=True)

print("Path to dataset files:", dataset_path)
