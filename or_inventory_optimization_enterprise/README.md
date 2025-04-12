
# 📦 Inventory Optimization with EOQ

Optimize inventory levels by minimizing total cost using the classic EOQ formula.

## Features
- Upload inventory CSV (demand, ordering cost, holding cost)
- Get EOQ, reorder frequency, total cost
- Download optimized results
- Docker + Streamlit support

---

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app/app.py
```

---

## Docker
```bash
docker build -t eoq-optimizer .
docker run -p 8501:8501 eoq-optimizer
```

---

## 🚀 How to Use the Complete System

This project includes 4 key components:
- ✅ Streamlit frontend (`app/app.py`)
- ✅ FastAPI backend (`src/api_service.py`)
- ✅ Auto-launch script (`start_server.py`)
- ✅ Notification system (`src/notifier.py`)

---

### 🖥️ 1. Run the Streamlit App (Interactive UI)

Launch the visual app:
```bash
streamlit run app/app.py
```

- Upload a CSV with inventory data
- View EOQ calculations: optimal quantity, reorder frequency, total cost
- Download results as a new CSV

---

### 🌐 2. Run the EOQ API Server

Start FastAPI backend:
```bash
uvicorn src.api_service:app --reload
```

Then open Swagger UI in your browser:
```
http://127.0.0.1:8000/docs
```

- Use the `POST /optimize/` endpoint
- Upload inventory CSV
- Get EOQ-optimized output in JSON format

---

### 🧠 3. Run `start_server.py` (Auto-launch API + Docs)

This script auto-starts the API and opens Swagger UI:

```bash
python start_server.py
```

Use it for quick startup during development.

---

### 📩 4. Use `notifier.py` (Email/Slack Alerts)

You can configure `src/notifier.py` to:
- Send alerts when stock is below reorder point
- Integrate with Slack or email (SMTP setup required)

Example usage:

```python
from src.notifier import send_email_notification

send_email_notification(
    subject="Low Inventory Alert",
    body="Item ABC123 is below reorder level. Reorder immediately.",
    to_email="ops-team@example.com"
)
```

You can trigger this after EOQ optimization or during monitoring scripts.

---

## 📘 Business Use Case

Inventory optimization using EOQ is essential for:
- **Minimizing total inventory cost** (ordering + holding)
- **Avoiding stockouts** while preventing overstocking
- **Streamlining procurement cycles** for better planning

This system allows:
- Strategic planners to simulate reorder plans
- Developers to integrate optimization via API
- Operations teams to be alerted on critical stock levels

---

## 🧪 Sample CSV Format

```csv
Item,AnnualDemand,OrderingCost,HoldingCost
A,1000,50,2
B,500,40,1.5
C,800,30,2.2
```

---

## 🛠 Tech Stack

- Python
- Streamlit
- FastAPI
- Pandas
- Uvicorn
- Docker (optional)
