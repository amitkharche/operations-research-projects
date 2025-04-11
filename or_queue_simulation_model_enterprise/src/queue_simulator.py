"""
Queue simulator based on Poisson arrivals and Exponential service times.
"""
import pandas as pd

def simulate_queue(df):
    df = df.copy()
    start_times = []
    end_times = []
    wait_times = []

    last_end = 0
    for i, row in df.iterrows():
        start = max(row["ArrivalTime"], last_end)
        end = start + row["ServiceTime"]
        wait = start - row["ArrivalTime"]

        start_times.append(start)
        end_times.append(end)
        wait_times.append(wait)
        last_end = end

    df["StartTime"] = start_times
    df["EndTime"] = end_times
    df["WaitTime"] = wait_times
    return df
