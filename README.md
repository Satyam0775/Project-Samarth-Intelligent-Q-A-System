# 🌾 Project Samarth — Intelligent Q&A System
**Bridging Agriculture & Climate Insights using Live Government Data**

---

### 🧠 Overview

**Project Samarth** is an intelligent **Q&A system** built to analyze and answer complex, data-driven questions about **India’s agricultural economy** and its relationship with **climate patterns** — powered entirely by **live datasets from [data.gov.in](https://data.gov.in/)**.

This system fetches real-time data from the:
- 🏛️ **Ministry of Agriculture & Farmers Welfare**
- 🌦️ **India Meteorological Department (IMD)**

It integrates both datasets and allows users to query them in **natural language** through a clean **Streamlit-based interface**.

---

### 🎯 Problem Statement

Government portals like **data.gov.in** contain thousands of valuable datasets — but they exist in diverse formats across ministries, making it difficult to extract cross-domain insights.

**Your Mission:**  
To design and build a **functional end-to-end prototype** that:
1. Fetches live government data using APIs.
2. Integrates multiple datasets (Agriculture + IMD Rainfall).
3. Enables users to ask **natural language questions**.
4. Returns accurate, traceable, and data-backed insights with proper citations.

---

### 🚀 Features

✅ **Real-Time API Integration**
- Fetches data directly from `data.gov.in` via official API keys and resource IDs.  
- Agriculture: Crop production data (1997–2014)  
- IMD: Sub-divisional rainfall data (1901–2017)

✅ **Data Integration Layer**
- Automatically merges climate and crop production datasets using cleaned and normalized state names.

✅ **Intelligent Q&A Engine**
- Understands queries like:
  - “Compare rainfall and rice production in Bihar and Jharkhand for the last 5 years.”
  - “Analyze crop trends in Andhra Pradesh.”

✅ **Streamlit Chat Interface**
- Simple user input box.
- Clean, markdown-based formatted answers.
- Auto-citation of data sources.

✅ **Accuracy & Traceability**
- Every answer is directly backed by the live dataset and cited source.

---

### 🧩 System Architecture

User (Streamlit UI)
│
▼
Natural Language Parser (LLM / Keyword Extractor)
│
▼
Query Engine (Pandas Logic)
│
▼
Data Layer (APIs + Local CSV Integration)
│
▼
Answer Generator (Formatter + Citation)


---

### 🧰 Tech Stack

| Layer | Tools / Libraries |
|-------|--------------------|
| Data Fetching | `requests`, `pandas`, `json` |
| Data Integration | `pandas`, `numpy` |
| NLP Parsing | Custom keyword parser / rule-based |
| Visualization | `matplotlib`, `seaborn`, `plotly` |
| Frontend | `streamlit`, `style.css` |
| Backend Logic | Python 3.10+ |
| Source | [data.gov.in](https://data.gov.in) APIs |

---

### ⚙️ Setup Instructions

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/<your-username>/Project_Samarth.git
cd Project_Samarth

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Fetch & Integrate Data

python main.py


5️⃣ Run the Streamlit Q&A Interface

streamlit run ui/app_streamlit.py

🧠 Example Query

Input:

Compare rainfall and rice production in Andaman and Nicobar Islands for the last 5 years


Output:

📊 Analysis for Andaman and Nicobar Islands — Crop: Rice

🌧️ Average Rainfall (mm):
 • Andaman and Nicobar Islands: 1142.46

🌾 Total Production (tonnes):
 • Andaman and Nicobar Islands: 45,451

📚 Data Source: Ministry of Agriculture & Farmers Welfare and India Meteorological Department (IMD), data.gov.in

🧩 Key Dataset References
Dataset	Ministry	API Resource ID
District-wise Crop Production Statistics (1997–2014)	Ministry of Agriculture & Farmers Welfare	xxxxx
Sub-divisional Rainfall Data (1901–2017)	India Meteorological Department (IMD)	xxxxxx

👨‍💻 Developed By
Satyam Kumar