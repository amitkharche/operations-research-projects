from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
from scipy.optimize import linear_sum_assignment
import io

app = FastAPI()

@app.post("/assign/")
async def solve_assignment(file: UploadFile):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents), index_col=0)
    row_ind, col_ind = linear_sum_assignment(df.values)
    assignments = [{"worker": df.index[r], "task": df.columns[c], "cost": df.values[r, c]}
                   for r, c in zip(row_ind, col_ind)]
    total_cost = df.values[row_ind, col_ind].sum()
    return JSONResponse(content={"assignments": assignments, "total_cost": total_cost})
