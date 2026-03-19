import os
from celery import Celery

celery = Celery(
    "worker",
    broker=os.environ.get("REDIS_URL"),
    backend=os.environ.get("REDIS_URL")
)

@celery.task
def process_document(file_path, company, period):
    print(f"Processing {file_path} for {company} ({period})")
