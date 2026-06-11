# pyrefly: ignore [missing-import]
import httpx
from app.db.repositories import create_company
from app.models.onboarding import OnboardingPayload, OnboardingResponse
from config import settings

PROGRAM_MAP = {
    "Champions":      "Champions",
    "Implementation": "Implementacion",
    "Workshop":       "Executive Workshop",
    "Consulting":     "Implementacion",
}

async def handle_nuevo_cliente(payload: OnboardingPayload) -> OnboardingResponse:
    company = create_company(payload)

    if settings.n8n_webhook_url:
        programa_n8n = PROGRAM_MAP.get(payload.programa, payload.programa)
        async with httpx.AsyncClient() as client:
            await client.post(settings.n8n_webhook_url, json={
                "empresa": payload.empresa,
                "programa": programa_n8n
            }, timeout=10)

    return OnboardingResponse(status="success", company_id=company["id"], empresa=company["name"])