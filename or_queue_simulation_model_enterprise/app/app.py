"""
Streamlit app to simulate queue performance.
"""
import sys
import os

# Add the src folder to the Python path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# ✅ Add the project root folder to the Python path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Dynamically add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
import pandas as pd
from src.queue_simulator import simulate_queue

st.set_page_config(page_title="🔁 Queue Simulation")
st.title("🔁 Queue Simulation - Wait Time Optimization")

uploaded_file = st.file_uploader("Upload queue data CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    result = simulate_queue(df)

    st.subheader("📈 Simulation Results")
    st.dataframe(result)
    st.line_chart(result[["ArrivalTime", "StartTime", "EndTime"]])
    st.download_button("Download Simulation CSV", result.to_csv(index=False), "simulation_output.csv", "text/csv")
