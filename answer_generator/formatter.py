def format_response(result: dict, source: str):
    """Format the Q&A result for Streamlit display."""

    if not result or "error" in result:
        return f"❌ {result.get('error', 'No valid data found.')}"

    states = [s.title() for s in result.get("states", [])]
    crop = result.get("crop", "N/A").title()
    text = f"📊 Analysis for {', '.join(states)} — Crop: {crop}\n\n"

    # 🌧️ Rainfall Summary
    rainfall = result.get("rainfall_summary", {})
    if rainfall:
        text += "🌧️ Average Rainfall (mm):\n"
        for state, value in rainfall.items():
            text += f" • {state.title()}: {round(value, 2)}\n"
        text += "\n"

    # 🌾 Production Summary
    production = result.get("production_summary", {})
    if production:
        text += "🌾 Total Production (tonnes):\n"
        for state, value in production.items():
            text += f" • {state.title()}: {int(value):,}\n"
        text += "\n"

    # 📚 Citation
    text += f"📚 Data Source: {source}"
    return text
