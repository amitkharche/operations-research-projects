from fastapi import FastAPI, UploadFile
import pandas as pd
import io
from src.queue_simulator import simulate_queue

app = FastAPI()

@app.post("/simulate/")
async def simulate(file: UploadFile):
    df = pd.read_csv(io.BytesIO(await file.read()))
    result = simulate_queue(df)
    return result.to_dict(orient="records")
