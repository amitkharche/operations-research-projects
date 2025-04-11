# 🧮 Assignment Problem Solver

## 🚀 Overview
This tool solves the classic **assignment problem** using the **Hungarian Algorithm** to find the optimal assignment of tasks to agents (e.g., workers to jobs) with minimum total cost.

## 🧾 How to Use
1. Upload a CSV file containing a cost matrix where:
   - Rows = workers/agents
   - Columns = tasks/jobs
   - Values = cost/time of assignment

2. View the optimal assignment, total cost, and download the results.

## 🖥️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## 🐳 Run via Docker
```bash
docker build -t assignment-solver .
docker run -p 8501:8501 assignment-solver
```

## 📁 Project Structure
```
assignment_problem_solver/
├── data/raw/cost_matrix.csv
├── app/app.py
├── src/ (optional for future extension)
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── model_training_and_evaluation.ipynb
├── requirements.txt
├── Dockerfile
└── README.md
```

## 📦 Output
- 🗂️ Optimized assignment matrix
- 💰 Total minimum cost
- 📥 Downloadable CSV results

---

*Made for operations research & supply chain efficiency!* 🚚📦
