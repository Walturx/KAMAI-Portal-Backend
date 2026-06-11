from fastapi import FastAPI
from app.routers.onboarding_router import router as onboarding_router

app = FastAPI(title="KAMAI Portal API")

app.include_router(onboarding_router)


@app.get("/health")
def health():
    return {"status": "ok"}
