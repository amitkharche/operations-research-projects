"""
Streamlit App for EOQ Optimization
"""

import os
import sys

# ✅ Dynamically add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
import pandas as pd
from src.eoq_solver import optimize_inventory

st.set_page_config(page_title="📦 EOQ Inventory Optimizer")
st.title("📦 EOQ-based Inventory Optimization")

uploaded_file = st.file_uploader("Upload inventory CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    optimized = optimize_inventory(df)
    st.subheader("✅ Optimized Inventory Plan")
    st.dataframe(optimized)
    st.download_button("Download Results", optimized.to_csv(index=False), "optimized_inventory.csv", "text/csv")
