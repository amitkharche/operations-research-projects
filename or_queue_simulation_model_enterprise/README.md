
# 🔁 Queue Simulation Model with LangChain Agent

## 📘 Business Use Case
In service environments (banks, call centers, hospitals, etc.), long queues can lead to poor customer experience, revenue loss, and operational inefficiencies.

This project simulates queue behavior using **Poisson-distributed arrival times** and **Exponential service durations**, then uses **LangChain + OpenAI** to recommend autonomous queue management strategies.

---

## ✅ Features

### 🎯 Core Components
- 📂 Simulated dataset with `ArrivalTime` and `ServiceTime`
- 🔁 Queue simulation logic (`src/queue_simulator.py`)
- 📊 Streamlit app to run simulations and download results
- 🧠 FastAPI microservice for programmatic queue evaluation

### 🧠 LangChain Agent (Autonomous Reasoning)
- Ask questions like _"How to reduce wait time?"_
- Autonomously recommends:
  - More counters
  - Shift adjustments
  - Priority queueing
- Uses LangChain tools + memory

### 🔐 API Key Integration
- Secure OpenAI API key input via Streamlit sidebar

### 📚 Memory
- FAISS-based vector store memory to retain context across sessions

### 📈 Prompt Templating
- Standardized decision prompts with dynamic input (queue data)

### 🗃️ Decision Logging
- Logs each agent interaction as JSON
- Stored in `logs/agent_decisions.json`

---

## 📓 Notebooks
- `notebooks/exploratory_analysis.ipynb`: EDA of queue simulation
- `notebooks/model_training_and_evaluation.ipynb`: Queue logic walkthrough

## 🐳 Docker Support
```bash
docker build -t queue-sim .
docker run -p 8501:8501 queue-sim
```

## 🚀 Streamlit App
```bash
streamlit run app/app.py
```

## 🤖 LangChain Agent
```bash
streamlit run app/langchain_agent.py
```

## 🛠 Requirements
See `requirements.txt` for Python libraries including:
- pandas, streamlit, langchain, faiss-cpu, openai

## 📁 Folder Structure
```
queue_simulation_model/
├── app/                 # Streamlit apps (simulation + agent)
├── data/                # Raw and processed queue data
├── logs/                # Agent decision logs
├── notebooks/           # EDA and training walkthroughs
├── src/                 # Simulation logic, API, notifications
├── tests/               # Test stubs
├── .github/             # CI workflows
├── Dockerfile
├── requirements.txt
├── README.md
├── LICENSE
```

---

## 🏁 Final Output
- 📦 Zip file for local or cloud execution
- 💬 Agent explanations with prompt context
- 🔁 Replayable simulation and analysis
