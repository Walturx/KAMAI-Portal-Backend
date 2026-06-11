from fastapi import APIRouter
from app.models.onboarding import OnboardingPayload, OnboardingResponse
from app.services.onboarding_service import handle_nuevo_cliente

router = APIRouter(prefix="/webhooks", tags=["webhooks"])

@router.post("/nuevo-cliente", response_model=OnboardingResponse)
async def nuevo_cliente(payload: OnboardingPayload):
    return await handle_nuevo_cliente(payload)