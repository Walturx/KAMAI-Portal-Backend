from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.onboarding_router import router as onboarding_router

app = FastAPI(title="KAMAI Portal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://kamai-portal.vercel.app", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(onboarding_router)


@app.get("/health")
def health():
    return {"status": "ok"}
