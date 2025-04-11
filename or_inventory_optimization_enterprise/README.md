# 📦 Inventory Optimization with EOQ

Optimize inventory levels by minimizing total cost using the classic EOQ formula.

## Features
- Upload inventory CSV (demand, ordering cost, holding cost)
- Get EOQ, reorder frequency, total cost
- Download optimized results
- Docker + Streamlit support

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

## Docker
```bash
docker build -t eoq-optimizer .
docker run -p 8501:8501 eoq-optimizer
```
