from fastapi import FastAPI, UploadFile, Form
import pandas as pd
from app.extractor import extract_financials

app = FastAPI()

@app.post("/upload")
async def upload(
    file: UploadFile,
    company: str = Form(...),
    period: str = Form(...)
):
    contents = await file.read()

    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)

    df = pd.read_excel(file_path)
    text = df.to_string()

    result = extract_financials(text)

    return {"result": result}
