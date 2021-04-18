from fastapi import FastAPI
from app.api import status, predictions

app = FastAPI()

app.include_router(status.router, prefix="/status", tags=["status"])
app.include_router(predictions.router, prefix="/predict", tags=["predictions"])





