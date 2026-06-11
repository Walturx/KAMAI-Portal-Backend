import httpx
from app.db.repositories import create_company
from app.models.onboarding import OnboardingPayload, OnboardingResponse
from config import settings

async def handle_nuevo_cliente(payload: OnboardingPayload) -> OnboardingResponse:
    company = create_company(payload)

    if settings.n8n_webhook_url:
        async with httpx.AsyncClient() as client:
            await client.post(settings.n8n_webhook_url, json={
                "empresa": payload.empresa,
                "programa": payload.programa
            }, timeout=10)

    return OnboardingResponse(status="success", company_id=company["id"], empresa=company["name"])