def get_source(query_type: str):
    """
    Returns the accurate data source(s) based on query type.
    Ensures correct citation for all Q&A responses.
    """

    if query_type in ["compare_rainfall", "compare_rainfall_production"]:
        return "Ministry of Agriculture & Farmers Welfare and India Meteorological Department (IMD), data.gov.in"

    elif query_type in ["highest_production", "crop_trend"]:
        return "Ministry of Agriculture & Farmers Welfare, data.gov.in"

    elif query_type == "climate_correlation":
        return "India Meteorological Department (IMD), data.gov.in"

    # Default fallback
    return "Government Open Data Portal (data.gov.in)"


# 🧪 Test
if __name__ == "__main__":
    print(get_source("compare_rainfall_production"))
