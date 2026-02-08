# app/main.py
from fastapi import FastAPI
from app.api.routes import health

app = FastAPI()
# app.include_router(weather.router)

app.include_router(health.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
