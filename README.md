
# 📊 Operations Research Projects Portfolio

Welcome to my collection of **Operations Research (OR) projects**, designed to solve complex optimization problems across transportation, logistics, inventory, and service systems.  
These projects combine **mathematical modeling**, **Python implementation**, and **interactive dashboards** for real-world decision-making.

---

## 📁 Repository Structure

Each folder contains a standalone OR project with model logic, input data, optimization solver, and optional Streamlit/FastAPI deployment.

```
operations_research_projects/
├── transportation_problem_optimizer/
├── assignment_problem_solver/
├── inventory_optimization_model/
├── queue_simulation_engine/
└── network_analysis_cpm_pert/
```

---

## 🚀 Project Overviews

### 🚚 [Transportation Problem Optimizer](./transportation_problem_optimizer)
- Minimizes total transportation cost across suppliers and destinations
- Uses Linear Programming (LP) and `scipy.optimize.linprog`
- Visualizes optimal transport plan and total cost
- Includes Streamlit dashboard for scenario inputs

### 👔 [Assignment Problem Solver](./assignment_problem_solver)
- Solves task allocation or job scheduling using Hungarian Algorithm
- Uses `scipy.optimize.linear_sum_assignment` for optimization
- Supports cost matrix upload and returns optimal assignments
- FastAPI microservice version available for automation

### 🧮 [Inventory Optimization Model](./inventory_optimization_model)
- Calculates Economic Order Quantity (EOQ) and reorder points
- Minimizes holding and ordering costs
- Alerts when inventory drops below threshold
- Includes Slack/email notifications and FastAPI endpoint

### 🕒 [Queue Simulation Engine](./queue_simulation_engine)
- Simulates queueing systems (M/M/1, M/M/c)
- Uses Poisson/Exponential distributions to generate arrivals/services
- Computes average wait time, queue length, and server utilization
- Dashboard includes sliders for arrival/service rates

### 📅 [Network Analysis: CPM & PERT](./network_analysis_cpm_pert)
- Models project networks using activity nodes and durations
- Calculates critical paths and project slack
- Visualizes project flow and timeline
- Useful for engineering and construction scheduling

---

## 🛠 Tech Stack

- Python 3.8+
- NumPy, Pandas, SciPy, PuLP
- Streamlit, FastAPI for UI and microservices
- Matplotlib, Plotly for visualizations
- NetworkX for network modeling (CPM/PERT)

---

## 📦 How to Run

### 🔧 Clone the Repository

```bash
git clone https://github.com/amitkharche/operations-research-projects.git
cd operations-research-projects
```

### 📂 Navigate to a Project Folder

```bash
cd transportation_problem_optimizer
```

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 🧮 Run Optimization or Launch Dashboard

```bash
python solver.py
# or
streamlit run app.py
```

---

## 📬 Contact

**Amit Kharche**  
🔗 [LinkedIn](https://www.linkedin.com/in/amitkharche)

---

## 📄 License

This repository is licensed under the MIT License.  
You are welcome to fork, adapt, and contribute.

---

## ⭐ Feedback & Collaboration

If you find these models useful, feel free to ⭐ the repo.  
Pull requests and improvements are always appreciated!
