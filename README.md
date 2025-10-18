# 🌾 Project Samarth — Intelligent Q&A System  
**Bridging Agriculture & Climate Insights using Live Government Data**

---

### 🌐 Live Demo & Video Showcase

- 🚀 **Live App:** [Hugging Face Space — Project Samarth](https://huggingface.co/spaces/Satyam0077/Project-Samarth-Intelligent-QA-System)  
- 🎥 **2-Minute Demo Video (Loom):** [Watch on Loom](https://www.loom.com/share/8c9d6943e90d4345973541624adc6666?t=146)

---

### 🧠 Overview

**Project Samarth** is an intelligent **Q&A system** that answers complex, data-driven questions about **India’s agricultural economy** and its relationship with **climate patterns** — powered entirely by **live datasets from [data.gov.in](https://data.gov.in/)**.

The system fetches real-time data from:
- 🏛️ **Ministry of Agriculture & Farmers Welfare**
- 🌦️ **India Meteorological Department (IMD)**

It integrates both datasets and enables users to query them using **natural language**, providing accurate, traceable, and policy-relevant insights.

---

### 🎯 Problem Statement

Government portals like **data.gov.in** host thousands of open datasets — but they are inconsistent in structure and stored across different ministries, making cross-domain analysis challenging.

**Mission Objective:**  
To design and build a **functional end-to-end prototype** that:
1. Fetches live data via official government APIs.  
2. Integrates multiple datasets (Agriculture + IMD Rainfall).  
3. Processes natural language queries.  
4. Generates accurate, traceable, data-backed insights.

---

### 🚀 Features

✅ **Real-Time API Integration**
- Fetches live data from `data.gov.in` APIs using unique `resource_id` and API key.  
- Agriculture data: 1997–2014  
- IMD Rainfall data: 1901–2017  

✅ **Data Integration Layer**
- Normalizes and merges datasets by `state_name` and `crop_year`.

✅ **Q&A Engine**
- Understands and executes queries like:
  - “Compare rainfall and rice production in Bihar and Jharkhand for the last 5 years.”
  - “Analyze rice yield trends in Andhra Pradesh.”

✅ **Streamlit Chat Interface**
- User-friendly input box and formatted markdown output.

✅ **Source Traceability**
- Each response cites its data source: **IMD** and **Ministry of Agriculture**.

---

### 🧩 System Architecture

User (Streamlit UI)
│
▼
Natural Language Parser (Rule-Based / LLM)
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
| NLP Parsing | Custom keyword parser |
| Visualization | `matplotlib`, `seaborn`, `plotly` |
| Frontend | `streamlit`, `style.css` |
| Backend Logic | Python 3.10+ |
| Data Source | [data.gov.in](https://data.gov.in) APIs |

---

### ⚙️ Setup Instructions

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Satyam0077/Project_Samarth.git
cd Project_Samarth
2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Fetch and Integrate Data

python main.py


5️⃣ Run the Streamlit Interface

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

🧩 Dataset References
Dataset	Ministry	API Resource ID
District-wise Crop Production Statistics (1997–2014)	Ministry of Agriculture & Farmers Welfare	35be999b-0208-4354-b557-f6ca9a5355de
Sub-divisional Rainfall Data (1901–2017)	India Meteorological Department (IMD)	8e0bd482-4aba-4d99-9cb9-ff124f6f1c2f
🎥 Demo Links

🌐 Live App (Hugging Face): Project Samarth Q&A System

🎬 Loom Demo Video: Watch Here
