#  Graph-Based Order-to-Cash Intelligence System

> AI-powered analytics system combining **Graph Intelligence + SQL Generation + LLM Reasoning** to explore ERP (SAP O2C) data in a modern, interactive way.

---

#  Overview

This project is a **next-generation data intelligence platform** that allows users to:

*  Ask natural language questions
*  Automatically generate SQL queries
*  Visualize results instantly
*  Explore relationships via graph visualization
*  Get AI-powered business insights

It transforms traditional ERP datasets into an **interactive AI-driven analytics experience**.

---

#  Key Features

##  AI-Powered Query System

* Natural Language → SQL (Auto-generated)
* LLM-based reasoning using Groq API
* Zero manual query writing required

##  Graph Intelligence

* Visualize Order-to-Cash relationships:

  * Orders → Customers → Products
* Interactive graph with node highlighting
* Detect relationships instantly

##  Smart Query Routing (Agent System)

* Automatically decides:

  * SQL query
  * Graph reasoning
  * LLM explanation

##  Data Visualization

* Auto-generated charts from query results
* Real-time insights
* Clean and interactive UI

##  Intelligent Chat Assistant

* Ask questions like:

  * "Which product appears most frequently?"
  * "How many orders per customer?"
* Streaming AI responses (ChatGPT-like feel)

##  Guardrails

* Restricts irrelevant queries
* Ensures dataset-only answers
* Prevents hallucination

---

#  System Architecture

```
User Query
   ↓
Guardrails 
   ↓
Query Router 
   ↓
 ┌───────────────┬──────────────┬──────────────┐
 │ SQL Engine    │ Graph Engine │ LLM Engine   │
 └───────────────┴──────────────┴──────────────┘
   ↓
Results + Insights
   ↓
Streamlit UI (Graph + Chat + Charts)
```

---

#  Project Structure

```
graph-llm-system/
│
├── app.py                  # Main Streamlit app
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── dataset.csv
│
├── db/
│   └── database.db
│
├── graph/
│   ├── build_graph.py
│   ├── graph_utils.py
│
├── llm/
│   ├── llm_engine.py
│   ├── sql_generator.py
│   ├── agent.py
│   ├── explainer.py
│   ├── prompt.py
│
├── services/
│   ├── query_router.py
│   ├── query_engine.py
│   ├── guardrails.py
│
├── utils/
│   ├── loader.py
│   ├── sql.py
│
└── ui/
    ├── graph_view.py
    ├── chat_ui.py
```

---

#  Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/manojpm181/graph-llm-system.git
cd graph-llm-system
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Setup Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

App will run on:

```
http://localhost:8501
```
https://manojpm181-graph-llm-system-app-m8qwem.streamlit.app/

---

#  Dataset

This system uses **Order-to-Cash ERP dataset**, including:

* Orders (`salesorder`)
* Customers (`soldtoparty`)
* Products (`material`)

---

#  Sample Questions

Try these in the app:

*  Which product appears most frequently?
*  How many orders per customer?
*  Top 5 products by frequency
*  Show relationship between orders and customers
*  Show broken orders

---

# AI Components

##  SQL Generator

* Converts natural language → SQL
* Uses LLM via Groq API
* Ensures schema-safe queries

## Agent System

* Central brain of system
* Executes:

  * SQL generation
  * Query execution
  * Result formatting

## LLM Explainer

* Converts raw data → business insights
* No hallucination (strict prompt rules)

---

#  Graph Design

Graph nodes:

* Order
* Customer
* Product

Edges:

* Order → Customer
* Order → Product

Features:

* Highlight nodes from query results
* Interactive visualization (PyVis)

---

#  UI Highlights

* Dark-themed professional dashboard
* Split layout:

  * Left → Graph Visualization
  * Right → AI Chat Assistant
* Streaming AI responses
* Auto charts from results
* Node highlighting

---

#  Guardrails & Safety

* Blocks unrelated queries
* Restricts to dataset scope
* Prevents incorrect AI outputs

---

#  Performance Optimizations

* Streamlit caching (`@st.cache_data`)
* Lightweight graph rendering
* Efficient SQL execution (SQLite)
* Minimal LLM calls

---

#  Deployment

### Option 1: Streamlit Cloud

* Push repo to GitHub
* Deploy directly

### Option 2: Render

* Add build + start commands

---

#  Trade-offs

| Area            | Trade-off                         |
| --------------- | --------------------------------- |
| LLM Accuracy    | Controlled via schema prompts     |
| Graph Scale     | Limited for very large datasets   |
| SQL Flexibility | Restricted to avoid hallucination |

---

#  Future Improvements

*  Vector search (semantic queries)
*  Multi-step reasoning agent
*  Advanced dashboards (Plotly)
*  Authentication system
*  Cloud database integration

---
## Results
<img width="1202" height="629" alt="Screenshot 2026-03-23 144135" src="https://github.com/user-attachments/assets/f445d1bb-a492-4d5d-9a0b-2a536690e5cf" />
<img width="1767" height="886" alt="Screenshot 2026-03-23 151050" src="https://github.com/user-attachments/assets/fd282866-ffd6-4365-b98d-2c3aea81e168" />
<img width="336" height="779" alt="Screenshot 2026-03-23 151238" src="https://github.com/user-attachments/assets/2620930c-1d86-47fd-a5d2-2fc89767d9e4" />
<img width="1919" height="556" alt="Screenshot 2026-03-23 151250" src="https://github.com/user-attachments/assets/fb1a2d86-fad5-4973-bbf7-8a06346d201a" />
<img width="978" height="797" alt="Screenshot 2026-03-23 151410" src="https://github.com/user-attachments/assets/e9038a89-08ec-42ff-8697-f90b4bd7183f" />
<img width="570" height="732" alt="Screenshot 2026-03-23 151420" src="https://github.com/user-attachments/assets/3643965f-f045-4879-a125-f3876c0f2ec8" />
<img width="576" height="477" alt="Screenshot 2026-03-23 151431" src="https://github.com/user-attachments/assets/cd7e5d12-697c-4883-9d59-932fbeba7003" />
<img width="590" height="666" alt="Screenshot 2026-03-23 151440" src="https://github.com/user-attachments/assets/39d25a23-24c8-4e1d-a836-297734444aa8" />
<img width="556" height="200" alt="Screenshot 2026-03-23 151451" src="https://github.com/user-attachments/assets/f7233047-9591-47e2-974d-1491eb74fb77" />
<img width="525" height="638" alt="Screenshot 2026-03-23 151509" src="https://github.com/user-attachments/assets/a09b291b-ec0f-49c4-84b4-3ff9acc67d3b" />

---
# 👨 Author

**Manoj PM**

---

#  Final Note

This project demonstrates how **AI can transform enterprise data systems** into interactive, intelligent platforms.

> Not just a dashboard — this is an **AI-powered data assistant**.

---


