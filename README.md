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
git clone <your-repo-url>
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

# 👨 Author

**Manoj PM**

---

#  Final Note

This project demonstrates how **AI can transform enterprise data systems** into interactive, intelligent platforms.

> Not just a dashboard — this is an **AI-powered data assistant**.

---


