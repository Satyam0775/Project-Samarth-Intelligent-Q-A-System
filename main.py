from data_layer.fetch_agriculture_api import fetch_agriculture_data   # 🌾 fetches Agriculture data from API
from data_layer.fetch_imd_api import fetch_rainfall_data               # 🌧️ fetches IMD rainfall data from API
from data_layer.integrate_data import integrate_data                   # 🔗 merges both datasets

if __name__ == "__main__":
    print("🌾 Fetching Agriculture Data ...")
    agri_df = fetch_agriculture_data()

    print("🌧️ Fetching IMD Rainfall Data ...")
    rain_df = fetch_rainfall_data()

    print("🔗 Integrating Datasets ...")
    integrate_data(agri_df, rain_df)

    print("\n✅ Phase 1 Completed Successfully!")
    print("Now run: streamlit run ui/app_streamlit.py")
