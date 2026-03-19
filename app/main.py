from fastapi import FastAPI, UploadFile
from app.worker import process_document

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/upload")
async def upload(file: UploadFile, company: str, period: str):
    contents = await file.read()

    from app.extractor import extract_financials

    text = contents.decode("utf-8", errors="ignore")

    result = extract_financials(text)

    return {"result": result}
