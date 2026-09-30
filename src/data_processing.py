from pathlib import Path
import pandas as pd
from src.config import RAW_DATA_DIR


def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path, low_memory=False)

def load_raw_datasets(culture_path, demographics_path):
    """
    Load the raw culture and demographics datasets.
    """
    cultures = load_csv(culture_path)
    demographics = load_csv(demographics_path)

    return cultures, demographics

def clean_null_values(df):
    """
    Convert literal 'Null' values to pandas missing values.
    """
    cleaned_df = df.copy()

    cleaned_df = cleaned_df.replace(r"^\s*Null\s*$", pd.NA, regex=True)

    return cleaned_df