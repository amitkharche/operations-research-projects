import os
import webbrowser
import time
import subprocess

def run():
    time.sleep(2)  # Small delay so server can start
    webbrowser.open("http://127.0.0.1:8000/docs")

# Start the FastAPI server
subprocess.Popen(["uvicorn", "src.api_service:app", "--reload"])

# Open browser tab
run()
