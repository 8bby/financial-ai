from fastapi import FastAPI, UploadFile
from app.worker import process_document

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/upload")
async def upload(file: UploadFile, company: str, period: str):
    contents = await file.read()

    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)

    process_document.delay(file_path, company, period)

    return {"status": "processing"}
