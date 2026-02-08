# app/main.py
from fastapi import FastAPI
# from app.api.routes import weather

app = FastAPI()
# app.include_router(weather.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
