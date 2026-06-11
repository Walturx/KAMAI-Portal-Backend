from app.db.supabase import get_client
from app.models.onboarding import OnboardingPayload

def create_company(payload: OnboardingPayload) -> dict:
    result = get_client().table("companies").insert({
        "name": payload.empresa,
        "status": "active",
        "program": payload.programa,
    }).execute()
    return result.data[0]
