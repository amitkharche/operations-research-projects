
# 🧮 Operations Research Projects

A comprehensive collection of interactive, modular, and deployment-ready Operations Research (OR) tools built using Python, Streamlit, FastAPI, and optimization libraries. Each project solves a practical problem in logistics, supply chain, inventory, scheduling, or service systems.

---

## 🚀 Projects Included

### 🔁 Assignment Problem Solver
Assign tasks to agents (e.g., workers to jobs) using the Hungarian Algorithm to minimize total cost.

- Upload CSV cost matrix
- View optimized assignment and total cost
- Download results
- Streamlit app + Docker-ready

**Run Locally**
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

**Run with Docker**
```bash
docker build -t assignment-solver .
docker run -p 8501:8501 assignment-solver
```

---

### 📦 Inventory Optimization with EOQ
Optimize inventory levels using the classic EOQ formula to minimize holding and ordering costs.

**Features**
- Upload CSV with demand, ordering cost, and holding cost
- Get EOQ, reorder frequency, and total cost
- Download optimized results
- Docker + Streamlit + FastAPI

**EOQ System Includes**
- ✅ Streamlit App
- ✅ FastAPI Backend (`src/api_service.py`)
- ✅ Auto-launch script (`start_server.py`)
- ✅ Notification Alerts (Email/Slack via `src/notifier.py`)

**Run Locally**
```bash
streamlit run app/app.py
```

**Run API Server**
```bash
uvicorn src.api_service:app --reload
```

**Start Full System**
```bash
python start_server.py
```

---

### ⏳ Queue Simulation Model with LangChain Agent
Simulate queue behavior and recommend improvements using LangChain + OpenAI.

**Features**
- Simulate queue with Poisson arrivals & exponential service
- Streamlit dashboard for analysis
- LangChain agent to recommend optimizations (more counters, shift changes, etc.)
- Decision logging using JSON
- FAISS memory + OpenAI API integration

**Run Simulation App**
```bash
streamlit run app/app.py
```

**Run LangChain Agent**
```bash
streamlit run app/langchain_agent.py
```

**Docker**
```bash
docker build -t queue-sim .
docker run -p 8501:8501 queue-sim
```

---

### 🚛 Transportation Problem Optimizer
Minimize transportation cost from warehouses to stores using Linear Programming.

**Features**
- Input cost matrix, supply, and demand
- Output optimized route matrix and total cost
- Interactive Streamlit app

**Run Locally**
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

**Docker**
```bash
docker build -t transport-optimizer .
docker run -p 8501:8501 transport-optimizer
```

---

## 📁 Folder Structure

```
operations-research-projects/
├── assignment_problem_solver/
├── inventory_optimization_model/
├── queue_simulation_model/
├── transportation_problem_optimizer/
├── shared_components/
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

- Python, Pandas, NumPy
- PuLP, SciPy, SimPy
- Streamlit, FastAPI, LangChain
- OpenAI API, FAISS, Plotly
- Docker & Uvicorn

---

## 📬 Author

**Amit Kharche**  
🔗 [LinkedIn](https://www.linkedin.com/in/amitkharche)

---

## 📄 License

MIT License – free to use, modify, and distribute.

---

## ⭐ Feedback & Contributions

Found this helpful? Give the repo a ⭐!  
Open an issue or submit a PR to improve or extend any module.
