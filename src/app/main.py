from fastapi import FastAPI
from app.api import status

app = FastAPI()

app.include_router(status.router, prefix="/status", tags=["status"])





