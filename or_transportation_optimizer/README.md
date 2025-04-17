
# 🚛 Transportation Problem Solver

This project provides a Python-based solution for the **Transportation Problem** using **Linear Programming (LP)** via the **PuLP** library. The goal is to determine the most cost-efficient shipping plan from multiple warehouses to multiple stores, given supply and demand constraints.

---

## 📘 Business Use Case

In logistics and supply chain management, companies often face the challenge of minimizing the **total transportation cost** when distributing products from **warehouses (sources)** to **stores or customers (destinations)**.

This tool helps decision-makers:
- Allocate supplies optimally across distribution centers
- Minimize total logistics cost while meeting all demand
- Simulate and analyze different demand/supply scenarios interactively

---

## 🧮 Mathematical Model

**Objective**: Minimize total transportation cost  
**Decision Variables**: Quantity of goods shipped from warehouse `i` to store `j`  
**Constraints**:
- Supply from each warehouse cannot be exceeded
- Demand at each store must be satisfied

Formulated as a **Linear Program** and solved using `PuLP`.

---

## 🛠 How It Works

### 🔧 Function Signature

```python
solve_transportation_problem(cost_df, supply, demand)
```

### ✅ Parameters

- `cost_df`: `DataFrame` with shape `(m x n)` where rows are warehouses and columns are stores
- `supply`: `Series` with length `m` for each warehouse's available units
- `demand`: `Series` with length `n` for each store's required units

### 🔄 Steps

1. Build an LP problem using `pulp.LpProblem`
2. Define variables `x[i][j]` for each warehouse-store pair
3. Add objective function: `Minimize total cost = Σ (cost[i][j] * x[i][j])`
4. Add supply constraints: total shipments from each warehouse ≤ supply
5. Add demand constraints: total received by each store ≥ demand
6. Solve using the default LP solver in PuLP

---

## 📦 Output

- `result`: Pandas DataFrame showing optimal number of units shipped from each warehouse to each store
- `total_cost`: The minimized total cost based on the provided cost matrix

---

## 📊 Sample Input Format

### `cost_df`
|      | StoreA | StoreB | StoreC |
|------|--------|--------|--------|
| W1   |   4    |   6    |   8    |
| W2   |   5    |   4    |   3    |

### `supply`
```python
W1    100
W2    120
```

### `demand`
```python
StoreA    80
StoreB    70
StoreC    70
```

---

## 💡 Example Usage

```python
import pandas as pd

# Define cost matrix
cost_df = pd.DataFrame({
    "StoreA": [4, 5],
    "StoreB": [6, 4],
    "StoreC": [8, 3]
}, index=["W1", "W2"])

# Supply and Demand
supply = pd.Series([100, 120], index=["W1", "W2"])
demand = pd.Series([80, 70, 70], index=["StoreA", "StoreB", "StoreC"])

# Solve
from transport_solver import solve_transportation_problem
result, total_cost = solve_transportation_problem(cost_df, supply, demand)

print("Optimal Shipments:")
print(result)
print(f"Total Minimum Cost: ₹{total_cost}")
```

---

## 🧰 Requirements

- Python 3.7+
- pandas
- PuLP

Install via:

```bash
pip install pandas pulp
```

---

## 📁 File Structure

```
transportation_problem_optimizer/
├── transport_solver.py        # Core logic
├── app.py                     # Optional Streamlit UI
├── sample_data/               # Example CSV files for cost, supply, demand
├── requirements.txt
└── README.md
```

---

## 📬 Author

**Amit Kharche**  
🔗 [LinkedIn](https://www.linkedin.com/in/amitkharche)  

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Contributions

Feel free to fork this repo, use it for educational or business purposes, and suggest improvements!
