from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.tasks import router as tasks_router
from .api.auth import router as auth_router
from .core.config import settings
import os

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# Add CORS middleware - for production, restrict origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You should restrict this in production
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
    from .models.task import Task  # Import models to register them
    from .models.user import User  # Import user model to register it

    # Create tables - this is idempotent, meaning it won't fail if tables already exist
    SQLModel.metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown if needed"""
    pass

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo Backend API"}

# For Hugging Face Spaces, make sure the app object is accessible
# The Hugging Face runner will look for this app object