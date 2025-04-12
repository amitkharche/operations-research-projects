from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from src.eoq_solver import optimize_inventory

app = FastAPI()

@app.post("/optimize/")
async def optimize(file: UploadFile = File(...)):
    """
    Upload an inventory CSV file and get EOQ optimization results.
    """
    contents = await file.read()  # Read the file content as bytes
    df = pd.read_csv(io.BytesIO(contents))  # Convert bytes to DataFrame
    result = optimize_inventory(df)  # Apply EOQ optimization logic
    return result.to_dict(orient="records")  # Return as JSON

@app.get("/")
def read_root():
    return {
        "message": "✅ EOQ Optimization API is running. Visit /docs to upload a file."
    }
