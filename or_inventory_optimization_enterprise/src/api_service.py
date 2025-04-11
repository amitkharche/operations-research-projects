from fastapi import FastAPI, UploadFile
import pandas as pd
import io
from src.eoq_solver import optimize_inventory

app = FastAPI()

@app.post("/optimize/")
async def optimize(file: UploadFile):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    result = optimize_inventory(df)
    return result.to_dict(orient="records")
