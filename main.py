import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("DATABASE_URL")
key: str = os.environ.get("DB_PASSWORD")
supabase: Client = create_client(url, key)

print('Supabase', supabase)
