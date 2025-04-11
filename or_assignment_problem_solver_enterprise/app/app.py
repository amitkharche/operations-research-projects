"""
Streamlit app to solve the assignment problem (Hungarian Algorithm).
"""

import streamlit as st
import pandas as pd
from scipy.optimize import linear_sum_assignment

st.set_page_config(page_title="🧮 Assignment Problem Solver")
st.title("🧮 Assignment Problem Solver using Hungarian Method")

uploaded_file = st.file_uploader("Upload Cost Matrix CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.subheader("📊 Cost Matrix")
    st.dataframe(df)

    try:
        row_ind, col_ind = linear_sum_assignment(df.values)
        assignments = list(zip(df.index[row_ind], df.columns[col_ind]))
        total_cost = df.values[row_ind, col_ind].sum()

        st.subheader("✅ Optimal Assignments")
        for i, (worker, task) in enumerate(assignments):
            st.markdown(f"**{worker}** → **{task}**")

        st.success(f"💰 Total Assignment Cost: {total_cost}")
        
        result_df = pd.DataFrame(assignments, columns=["Worker", "Task"])
        result_df["Cost"] = [df.loc[w, t] for w, t in assignments]
        st.download_button("Download Assignments", result_df.to_csv(index=False), "assignment_results.csv", "text/csv")

    except Exception as e:
        st.error(f"Failed to solve the assignment problem: {e}")
