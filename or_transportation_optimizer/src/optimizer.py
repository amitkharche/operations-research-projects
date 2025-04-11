"""
Transportation Problem Solver using Linear Programming (PuLP).
"""

import pandas as pd
import pulp

def solve_transportation_problem(cost_df, supply, demand):
    warehouses = cost_df.index
    stores = cost_df.columns

    prob = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("route", (warehouses, stores), lowBound=0, cat="Continuous")

    # Objective function
    prob += pulp.lpSum(cost_df.loc[w][s] * x[w][s] for w in warehouses for s in stores)

    # Supply constraints
    for w in warehouses:
        prob += pulp.lpSum(x[w][s] for s in stores) <= supply[w], f"Supply_{w}"

    # Demand constraints
    for s in stores:
        prob += pulp.lpSum(x[w][s] for w in warehouses) >= demand[s], f"Demand_{s}"

    prob.solve()

    result = pd.DataFrame(index=warehouses, columns=stores)
    for w in warehouses:
        for s in stores:
            result.loc[w, s] = x[w][s].varValue

    total_cost = pulp.value(prob.objective)
    return result.fillna(0), total_cost
