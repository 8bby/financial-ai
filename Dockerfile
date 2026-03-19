FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Default command (API)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
