import re

def parse_query(user_input: str):
    """
    🌾 Project Samarth — Query Parser (Final Version)
    --------------------------------
    Converts user natural language question into structured query.
    """

    query = (user_input or "").lower().strip()
    result = {
        "states": [],
        "crop": None,
        "years": 5,  # Default
        "metrics": [],
        "query_type": "general"
    }

    # 1️⃣ Extract number of years
    match = re.search(r"last (\d+) years?", query)
    if match:
        result["years"] = int(match.group(1))

    # 2️⃣ Extract states — only ones that exist in your merged dataset
    state_list = [
        "andaman and nicobar islands", "andhra pradesh", "bihar", "jharkhand",
        "odisha", "tamil nadu", "rajasthan", "uttar pradesh", "west bengal",
        "kerala", "karnataka", "maharashtra"
    ]
    found_states = [s for s in state_list if s in query]
    if found_states:
        result["states"] = found_states

    # 3️⃣ Extract crop
    crop_list = [
        "rice", "maize", "wheat", "sugarcane", "turmeric", "banana", "groundnut",
        "arecanut", "sunflower", "moong", "urad", "black pepper", "cashewnut"
    ]
    for crop in crop_list:
        if crop in query:
            result["crop"] = crop
            break

    # 4️⃣ Extract metrics
    if "rainfall" in query:
        result["metrics"].append("rainfall")
    if "production" in query:
        result["metrics"].append("production")

    # Default metrics
    if not result["metrics"]:
        result["metrics"] = ["rainfall", "production"]

    # 5️⃣ Determine query type
    if "compare" in query:
        result["query_type"] = "compare_rainfall_production"
    elif "trend" in query:
        result["query_type"] = "crop_trend"
    elif "highest" in query:
        result["query_type"] = "highest_production"
    elif "policy" in query or "promote" in query:
        result["query_type"] = "policy_support"
    else:
        result["query_type"] = "general"

    return result


# 🧪 Quick test
if __name__ == "__main__":
    queries = [
        "Compare rainfall and rice production in Andaman and Nicobar Islands for the last 5 years",
        "Show rainfall trend for Rice in Andhra Pradesh for the last 10 years",
        "Which district had highest rice production in Andhra Pradesh?",
        "Suggest policy to promote drought-resistant crops in Odisha"
    ]
    for q in queries:
        print(f"\n🔍 Query: {q}")
        print("Parsed Output:", parse_query(q))
