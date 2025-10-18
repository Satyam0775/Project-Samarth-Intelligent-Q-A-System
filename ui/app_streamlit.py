# ---------------------------------------------------
# 🌾 Project Samarth — Intelligent Q&A System
# ---------------------------------------------------

import sys, os
import streamlit as st

# ✅ Ensure Python finds your project modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from query_engine.parser import parse_query
from query_engine.logic_engine import run_query
from answer_generator.citation_manager import get_source

# ---------------------------------------------------
# ⚙️ Streamlit Page Setup
# ---------------------------------------------------
st.set_page_config(page_title="🌾 Project Samarth — Intelligent Q&A", layout="centered")

# ✅ Load custom CSS
try:
    st.markdown("<style>" + open("ui/style.css").read() + "</style>", unsafe_allow_html=True)
except Exception as e:
    st.warning("⚠️ Could not load CSS file. Using default Streamlit styling.")

# ---------------------------------------------------
# 🧠 Title and Info
# ---------------------------------------------------
st.title("🌾 Project Samarth — Intelligent Q&A System")
st.caption("Ask intelligent, data-driven questions about agriculture and climate using live datasets from data.gov.in.")

# ---------------------------------------------------
# ✍️ Input Section
# ---------------------------------------------------
query = st.text_area(
    "🧠 Ask your question:",
    height=100,
    placeholder="Example: Compare rainfall and rice production in Andaman and Nicobar Islands and Andhra Pradesh for the last 5 years"
)

# ---------------------------------------------------
# 🔍 Analyze Button Logic
# ---------------------------------------------------
if st.button("🔍 Analyze"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Analyzing your question..."):
            try:
                # 1️⃣ Parse user query
                parsed_query = parse_query(query)

                # 2️⃣ Run analysis logic
                result = run_query(parsed_query)

                # 3️⃣ Get citation source
                source = get_source(parsed_query.get("query_type"))

                # 4️⃣ Display structured results
                st.markdown("---")
                st.markdown("### 📊 Result Summary")

                if "error" in result:
                    st.error(result["error"])

                elif "message" in result:
                    st.info(result["message"])

                else:
                    states = parsed_query.get("states", [])
                    crop = parsed_query.get("crop", "")
                    st.markdown(f"### 📊 Analysis for {', '.join(states)} — Crop: {crop.title()}")

                    # 🌧️ Rainfall Summary
                    if "rainfall_summary" in result:
                        st.markdown("#### 🌧️ Average Rainfall (mm):")
                        for state, value in result["rainfall_summary"].items():
                            st.markdown(f"- **{state.title()}**: `{value}` mm")

                    # 🌾 Production Summary
                    if "production_summary" in result:
                        st.markdown("#### 🌾 Total Production (tonnes):")
                        for state, value in result["production_summary"].items():
                            st.markdown(f"- **{state.title()}**: `{int(value)}` tonnes")

                    st.markdown("---")
                    st.markdown(f"📚 **Data Source:** {source}")
                    st.caption("Developed for Project Samarth — Integrating Agriculture & Climate Data 🌦️🌾")

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
