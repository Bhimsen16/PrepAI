from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Prep AI Backend",
    description="Edge-Assisted Micro-Learning & Assessment API for Loksewa Preparation",
    version="0.1.0",
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": "Prep AI Engine",
        "target_exam": "Loksewa Aayog"
    }