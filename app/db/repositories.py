import re
import time
import random
from app.db.supabase import get_client
from app.models.onboarding import OnboardingPayload

TINTS = ['#7C5CDB', '#1F8A5B', '#C2603A', '#0E8FAE', '#378ADD', '#B9820F']

def create_company(payload: OnboardingPayload) -> dict:
    words = payload.empresa.strip().split()
    initials = ''.join(w[0] for w in words[:2]).upper()
    slug = re.sub(r'[^a-z0-9-]', '', payload.empresa.lower().replace(' ', '-'))
    company_id = f"{slug}-{int(time.time() * 1000)}"
    tint = random.choice(TINTS)

    result = get_client().table("companies").insert({
        "id":       company_id,
        "name":     payload.empresa,
        "initials": initials,
        "tint":     tint,
        "sector":   "Nuevo cliente",
        "plan":     "Starter",
        "program":  payload.programa,
        "status":   "active",
    }).execute()
    return result.data[0]
