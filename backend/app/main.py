from fastapi import FastAPI

app = FastAPI(
    title="Prep AI Backend",
    description="Edge-Assisted Micro-Learning & Assessment API for Loksewa Preparation",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": "Prep AI Engine",
        "target_exam": "Loksewa Aayog",
        "message": "FastAPI service is running smoothly."
    }