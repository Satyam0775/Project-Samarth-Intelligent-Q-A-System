import requests
import pandas as pd
import os
import time
from data_layer.config import BASE_URL, API_KEY, IMD_RESOURCE_ID

def fetch_rainfall_data(limit=500, retries=3, max_records=2000):
    """
    Fetch IMD rainfall data from data.gov.in API in chunks and save as CSV.
    Automatically handles rate limits and saves into hybrid_dataset folder.
    """
    os.makedirs("hybrid_dataset", exist_ok=True)
    csv_path = "hybrid_dataset/imd_rainfall_data.csv"
    all_data = []

    print("🌦️  Starting IMD Rainfall data fetch...")

    offset = 0
    total_fetched = 0

    while total_fetched < max_records:
        url = f"{BASE_URL}{IMD_RESOURCE_ID}?api-key={API_KEY}&format=json&limit={limit}&offset={offset}"

        for attempt in range(retries):
            try:
                response = requests.get(url, timeout=20)
                response.raise_for_status()

                data = response.json().get("records", [])
                if not data:
                    print("✅ No more records found.")
                    break

                df_chunk = pd.DataFrame(data)
                all_data.append(df_chunk)

                total_fetched += len(df_chunk)
                offset += limit

                print(f"✅ Chunk fetched: {len(df_chunk)} rows (Total: {total_fetched})")

                time.sleep(2)  # avoid rate-limit
                break

            except requests.exceptions.HTTPError as e:
                if "429" in str(e):
                    print("⚠️ Too Many Requests — waiting 20 seconds...")
                    time.sleep(20)
                elif "403" in str(e):
                    print("🚫 Forbidden: check API key or IMD resource ID in config.py")
                    return pd.DataFrame()
                else:
                    print(f"⚠️ Attempt {attempt+1} failed: {e}")
                    time.sleep(3)
        else:
            print("❌ Max retries reached, skipping this chunk.")
            break

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_csv(csv_path, index=False)
        print(f"✅ Rainfall data fetched & saved → {csv_path} ({len(final_df)} rows total)")
        return final_df
    else:
        print("❌ No rainfall data fetched.")
        return pd.DataFrame()
