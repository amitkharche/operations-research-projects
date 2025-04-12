"""
Streamlit App for Transportation Optimizer
"""
import os
import sys

# Dynamically add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import necessary libraries
import streamlit as st
import pandas as pd
from src.optimizer import solve_transportation_problem

st.set_page_config(page_title="🚛 Transportation Problem Optimizer")
st.title("🚛 OR-based Transportation Problem Solver")

uploaded_cost = st.file_uploader("Upload Cost Matrix (CSV)", type="csv")
uploaded_supply = st.file_uploader("Upload Supply (CSV)", type="csv")
uploaded_demand = st.file_uploader("Upload Demand (CSV)", type="csv")

if uploaded_cost and uploaded_supply and uploaded_demand:
    cost_df = pd.read_csv(uploaded_cost, index_col=0)
    supply = pd.read_csv(uploaded_supply, index_col=0).squeeze()
    demand = pd.read_csv(uploaded_demand, index_col=0).squeeze()

    st.subheader("🧮 Solving...")
    result_df, total_cost = solve_transportation_problem(cost_df, supply, demand)

    st.subheader("📦 Optimal Transportation Plan")
    st.dataframe(result_df)

    st.success(f"💰 Total Transportation Cost: {total_cost:.2f}")

    st.download_button("Download Plan", result_df.to_csv(), "transport_plan.csv", "text/csv")
