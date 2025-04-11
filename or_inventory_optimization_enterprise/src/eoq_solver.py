"""
EOQ Optimizer using classical EOQ formula.
"""

import pandas as pd
import numpy as np

def calculate_eoq(demand, ordering_cost, holding_cost):
    return np.sqrt((2 * demand * ordering_cost) / holding_cost)

def optimize_inventory(df):
    df["EOQ"] = df.apply(lambda row: calculate_eoq(
        row["Annual_Demand"], row["Ordering_Cost"], row["Holding_Cost_Per_Unit"]), axis=1)
    df["Reorder_Frequency"] = df["Annual_Demand"] / df["EOQ"]
    df["Total_Cost"] = (df["EOQ"] * df["Holding_Cost_Per_Unit"] / 2) + (df["Annual_Demand"] / df["EOQ"] * df["Ordering_Cost"])
    return df
