from supabase import create_client, Client
from config import settings

_key = settings.supabase_service_key or settings.supabase_anon_key
supabase: Client = create_client(settings.supabase_url, _key)
