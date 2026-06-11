from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers.onboarding_router import router as onboarding_router

app = FastAPI(title="KAMAI Portal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://kamai-portal.vercel.app", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(onboarding_router)


@app.exception_handler(Exception)
async def global_exception_handler(_request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
        headers={"Access-Control-Allow-Origin": "https://kamai-portal.vercel.app"},
    )


@app.get("/health")
def health():
    return {"status": "ok"}
