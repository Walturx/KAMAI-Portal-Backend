from pydantic import BaseModel

class OnboardingPayload(BaseModel):
    empresa: str
    programa: str



class OnboardingResponse(BaseModel):
    status: str
    company_id: str
    empresa: str 