# 🚛 Transportation Problem Optimizer

## Problem
Minimize total cost for transporting goods from multiple warehouses to stores.

## Solution
- Uses **Linear Programming** via **PuLP**
- Input: cost matrix, supply, demand
- Output: optimized route matrix and cost
- Interactive Streamlit App

## Usage
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Docker
```bash
docker build -t transport-optimizer .
docker run -p 8501:8501 transport-optimizer
```

## Data Format
- cost_matrix.csv (index: warehouses, columns: stores)
- supply.csv (1-col series with index = warehouses)
- demand.csv (1-col series with index = stores)
