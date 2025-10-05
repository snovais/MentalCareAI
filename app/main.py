from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MentalCareAI", version="2.0")
app.include_router(router)
