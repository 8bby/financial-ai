from fastapi import FastAPI, UploadFile
from app.worker import process_document

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/upload")
from fastapi import FastAPI, UploadFile
import pandas as pd
from app.extractor import extract_financials

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/upload")
async def upload(file: UploadFile, company: str, period: str):
    contents = await file.read()

    # Save file temporarily
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)

    # Read Excel
    df = pd.read_excel(file_path)

    # Convert Excel to text
    text = df.to_string()

    # Extract financials
    result = extract_financials(text)

    return {"result": result}
