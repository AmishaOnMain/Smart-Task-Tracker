from fastapi import FastAPI

from app.routes.auth import router as auth_router

from app.routes.tasks import router as task_router

app = FastAPI(
    title="AI Productivity Dashboard API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {
        "message": "API is running"
    }