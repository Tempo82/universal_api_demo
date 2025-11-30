from fastapi import FastAPI, Form
import os
import json
from datetime import datetime

app = FastAPI(title="Demo Universal API Skeleton")

STORAGE_DIR = "./demo_storage"
os.makedirs(STORAGE_DIR, exist_ok=True)

@app.post("/data/submit")
def submit_data_demo(app_name: str = Form(...), payload: str = Form(...)):
    file_name = f"{app_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    file_path = os.path.join(STORAGE_DIR, file_name)
    with open(file_path, "w") as f:
        json.dump(payload, f)
    return {
        "saved_path": file_path,
        "is_sensitive": False,
        "next_actions": ["auto_save"]
    }