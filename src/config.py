from pathlib import Path


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directories
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Reproducibility
RANDOM_STATE = 42

# Model directory
MODEL_DIR = PROJECT_ROOT / "models"