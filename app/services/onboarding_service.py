from app.db.repositories import create_company
from app.models.onboarding import OnboardingPayload, OnboardingResponse

async def handle_nuevo_cliente(payload: OnboardingPayload) -> OnboardingResponse:
    company = create_company(payload)
    return OnboardingResponse(status="success", company_id=company["id"], empresa=company["name"])