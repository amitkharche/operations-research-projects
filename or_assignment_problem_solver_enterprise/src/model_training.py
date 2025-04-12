
import pandas as pd
import numpy as np
import os
from scipy.optimize import linear_sum_assignment

# Paths
DATA_PATH = os.path.join("data", "raw", "cost_matrix.csv")
OUTPUT_PATH = os.path.join("data", "processed", "assignment_result.csv")
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

def load_cost_matrix(path):
    print(f"Loading cost matrix from: {path}")
    return pd.read_csv(path, index_col=0)

def solve_assignment(cost_matrix):
    print("Solving assignment problem...")
    row_ind, col_ind = linear_sum_assignment(cost_matrix.values)
    assignment_result = pd.DataFrame({
        "Task": cost_matrix.index[row_ind],
        "AssignedTo": cost_matrix.columns[col_ind],
        "Cost": cost_matrix.values[row_ind, col_ind]
    })
    assignment_result["TotalCost"] = assignment_result["Cost"].sum()
    return assignment_result

def save_results(result_df, output_path):
    print(f"Saving results to: {output_path}")
    result_df.to_csv(output_path, index=False)

def main():
    cost_matrix = load_cost_matrix(DATA_PATH)
    result = solve_assignment(cost_matrix)
    save_results(result, OUTPUT_PATH)
    print("✅ Assignment optimization complete!")

if __name__ == "__main__":
    main()
