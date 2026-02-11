from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.tasks import router as tasks_router
from .api.auth import router as auth_router
from .core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# Add CORS middleware (FIXED)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://localhost:3001",
        "https://frontend-aohnsintx-tariq765s-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, tags=["authentication"])
app.include_router(tasks_router, prefix="/api/{user_id}", tags=["tasks"])


@app.on_event("startup")
async def startup_event():
    """Initialize database tables on startup"""
    from sqlmodel import SQLModel
    from .db.session import engine
    from .models.task import Task
    from .models.user import User

    SQLModel.metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown if needed"""
    pass


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo Backend API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)