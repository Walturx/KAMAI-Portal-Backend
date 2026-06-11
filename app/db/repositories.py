from app.db.supabase import supabase
from app.models.onboarding import OnboardingPayload

def create_company(payload: OnboardingPayload) -> dict:
    result = supabase.table("companies").insert({
        "name": payload.empresa,
        "status": "active",
        "program": payload.programa,
    }).execute()
    return result.data[0]
