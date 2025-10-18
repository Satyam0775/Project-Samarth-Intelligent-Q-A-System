# -----------------------------------------------------------
# 🌾 Project Samarth — Logic Engine (Final Polished Version)
# -----------------------------------------------------------

import pandas as pd
import numpy as np

DATA_PATH = "hybrid_dataset/merged_agri_rainfall.csv"

try:
    df = pd.read_csv(DATA_PATH)
    df.columns = df.columns.str.lower().str.strip()
    df["crop_year"] = pd.to_numeric(df.get("crop_year", pd.Series()), errors="coerce")
    df["state_name"] = df["state_name"].fillna("").astype(str)
    df["crop"] = df["crop"].fillna("").astype(str)
    print(f"✅ Dataset loaded successfully → {DATA_PATH} ({len(df)} rows)")
except Exception as e:
    print(f"⚠️ Error loading dataset: {e}")
    df = pd.DataFrame()


def run_query(parsed_query: dict):
    """Executes logic for a given parsed query using integrated dataset."""

    if df.empty:
        return {"error": "Dataset not found or empty."}

    if not parsed_query or not isinstance(parsed_query, dict):
        return {"error": "Invalid query format."}

    states = [s.lower().strip() for s in parsed_query.get("states", [])]
    crop = parsed_query.get("crop", "").lower().strip()
    years = parsed_query.get("years", 5)
    metrics = parsed_query.get("metrics", [])
    result = {"states": states, "crop": crop, "years": years}

    filtered = df.copy()

    # ✅ Safely filter by state
    if "state_name" in filtered.columns and states:
        filtered = filtered[filtered["state_name"].str.lower().isin(states)]

    # ✅ Safely filter by crop
    if "crop" in filtered.columns and crop:
        filtered = filtered[filtered["crop"].str.lower() == crop]

    # ✅ Filter by year range
    if "crop_year" in filtered.columns and not filtered["crop_year"].isna().all():
        latest_year = int(filtered["crop_year"].max())
        start_year = latest_year - years + 1
        filtered = filtered[
            (filtered["crop_year"] >= start_year)
            & (filtered["crop_year"] <= latest_year)
        ]

    if filtered.empty:
        return {"message": "No matching records found for your query."}

    # 🌧️ Compute Average Rainfall
    if "rainfall" in metrics:
        rain_cols = [c for c in ["annual", "jjas", "jf", "mam", "ond"] if c in filtered.columns]
        if rain_cols:
            filtered["avg_rainfall"] = filtered[rain_cols].apply(
                pd.to_numeric, errors="coerce"
            ).mean(axis=1)
            rainfall_summary = (
                filtered.groupby("state_name")["avg_rainfall"]
                .mean()
                .round(2)
                .to_dict()
            )
            result["rainfall_summary"] = rainfall_summary

    # 🌾 Compute Total Crop Production
    if "production" in metrics and "production_" in filtered.columns:
        prod_summary = (
            filtered.groupby("state_name")["production_"]
            .sum()
            .round(2)
            .to_dict()
        )
        result["production_summary"] = prod_summary

    # 📊 If no data found
    if "rainfall_summary" not in result and "production_summary" not in result:
        result["message"] = "No metrics found in dataset for the given query."

    # ✅ Format clean output
    result["states"] = sorted([s.title() for s in result.get("states", [])])

    return result


# 🧪 Quick test
if __name__ == "__main__":
    test_query = {
        "states": ["andaman and nicobar islands", "andhra pradesh"],
        "crop": "rice",
        "years": 5,
        "metrics": ["rainfall", "production"],
    }
    print("\n🧠 Running test query...\n")
    print(run_query(test_query))
