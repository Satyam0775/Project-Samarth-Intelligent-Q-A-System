import pandas as pd
import os
import re

def clean_state_name(name: str):
    """Cleans and standardizes state/subdivision names."""
    if not isinstance(name, str):
        return ""
    name = name.lower().strip()
    name = re.sub(r"&", "and", name)
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r"[^a-z\s]", "", name)  # remove special chars
    return name

def integrate_data(agri_df: pd.DataFrame, rain_df: pd.DataFrame):
    """
    🔗 Final Integration Logic — Clean, Normalize, and Merge
    Works even if & or trailing spaces exist.
    """

    os.makedirs("hybrid_dataset", exist_ok=True)

    print(f"🧾 Agriculture unique states: {agri_df['state_name'].nunique()}")
    print(f"☁️ Rainfall unique subdivisions: {rain_df['subdivision'].nunique()}")

    # Clean columns
    agri_df.columns = agri_df.columns.str.lower().str.strip()
    rain_df.columns = rain_df.columns.str.lower().str.strip()

    # Clean text values
    agri_df["state_name"] = agri_df["state_name"].apply(clean_state_name)
    rain_df["subdivision"] = rain_df["subdivision"].apply(clean_state_name)

    # Create mapping
    mapping = {
        "andaman and nicobar islands": "andaman and nicobar islands",
        "orissa": "odisha",
        "sub himalayan west bengal and sikkim": "west bengal",
        "gangetic west bengal": "west bengal",
        "east uttar pradesh": "uttar pradesh",
        "west uttar pradesh": "uttar pradesh",
        "east rajasthan": "rajasthan",
        "west rajasthan": "rajasthan",
        "haryana delhi and chandigarh": "haryana",
        "assam and meghalaya": "assam",
        "naga mani mizo tripura": "tripura",
    }

    # Apply mapping to rainfall data
    rain_df["state_name"] = rain_df["subdivision"].replace(mapping)

    # Ensure year columns match type
    agri_df["crop_year"] = pd.to_numeric(agri_df["crop_year"], errors="coerce").astype("Int64")
    rain_df["year"] = pd.to_numeric(rain_df["year"], errors="coerce").astype("Int64")
    rain_df.rename(columns={"year": "crop_year"}, inplace=True)

    # Show what’s common after full cleaning
    common_states = sorted(set(agri_df["state_name"].unique()) & set(rain_df["state_name"].unique()))
    print(f"✅ Common states found: {common_states}")

    if not common_states:
        print("⚠️ No matching states even after cleaning — check character mismatches manually!")
        print("🔍 Example Agri states:", agri_df['state_name'].unique().tolist())
        print("🔍 Example Rainfall states:", rain_df['state_name'].unique().tolist())
        return pd.DataFrame()

    # Filter only matching states
    agri_df = agri_df[agri_df["state_name"].isin(common_states)]
    rain_df = rain_df[rain_df["state_name"].isin(common_states)]

    # Merge datasets
    merged = pd.merge(agri_df, rain_df, on=["state_name", "crop_year"], how="inner")

    # Save output
    output_path = "hybrid_dataset/merged_agri_rainfall.csv"
    merged.to_csv(output_path, index=False)

    print(f"✅ Data integrated and saved → {output_path} ({len(merged)} rows, {len(merged.columns)} columns)")
    print("🏛️ Unique merged states:", merged["state_name"].unique().tolist())

    return merged


# 🧪 Quick standalone test
if __name__ == "__main__":
    ag = pd.read_csv("hybrid_dataset/agriculture_data.csv")
    rd = pd.read_csv("hybrid_dataset/imd_rainfall_data.csv")
    integrate_data(ag, rd)
