from fastapi import FastAPI

from app.routes.auth import router as auth_router

app = FastAPI(
    title="AI Productivity Dashboard API",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "API is running"
    }