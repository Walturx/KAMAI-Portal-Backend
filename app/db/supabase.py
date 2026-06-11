from supabase import create_client, Client
from config import settings

_client: Client | None = None

def get_client() -> Client:
    global _client
    if _client is None:
        _key = settings.supabase_service_key or settings.supabase_anon_key
        _client = create_client(settings.supabase_url, _key)
    return _client
