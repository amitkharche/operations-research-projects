"""
Streamlit App for EOQ Optimization
"""
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
