from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.api.routes import students_router, subjects_router, materials_router

# Import models so SQLAlchemy registers them
from app import models  # noqa: F401

# Create tables (if not exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Materials Management Service",
    description=(
        "A service-oriented system for managing students' educational materials, "
        "including uploading, storing, categorizing, and searching learning materials."
    ),
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(students_router, prefix="/api/v1")
app.include_router(subjects_router, prefix="/api/v1")
app.include_router(materials_router, prefix="/api/v1")


@app.get("/", tags=["Health"])
def root():
    return {
        "service": "Student Materials Management Service",
        "version": "1.0.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}