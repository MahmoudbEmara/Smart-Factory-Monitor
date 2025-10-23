import os

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "fallback-key")
    DATABASE_URL = os.getenv("DATABASE_URL")
    LOGIN_USER = os.getenv("LOGIN_USER")
    LOGIN_PASS = os.getenv("LOGIN_PASS")
    DASHBOARD_API_KEY = os.getenv("DASHBOARD_API_KEY")
    RESET_KEY = os.getenv("RESET_KEY")
