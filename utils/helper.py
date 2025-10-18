# utils/helper.py
# Basic helper functions used across the project

import pandas as pd

def load_csv(path):
    """Safely loads a CSV file."""
    try:
        df = pd.read_csv(path)
        print(f"✅ Loaded file: {path} ({len(df)} rows)")
        return df
    except FileNotFoundError:
        print(f"⚠️ File not found: {path}")
        return pd.DataFrame()

def save_csv(df, path):
    """Saves a DataFrame as CSV."""
    df.to_csv(path, index=False)
    print(f"💾 Data saved to {path}")
