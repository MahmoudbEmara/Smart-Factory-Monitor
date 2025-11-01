from datetime import timezone
import psycopg2
import os

EGYPT_TZ = timezone.utc  # replace with TIMEZONE !!! after testing

RESET_KEY = os.getenv("RESET_KEY", "default-reset-key")

def get_db_conn():
    return psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
