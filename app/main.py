from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="EvoForge AI",
    version="0.1.0",
    description="AI-powered software enhancement automation and future-version impact simulation",
)

app.include_router(router)
