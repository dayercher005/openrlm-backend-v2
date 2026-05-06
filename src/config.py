import os 
from dotenv import load_dotenv

load_dotenv()

RLM_PROVIDER = os.getenv("RLM_PROVIDER")
AI_MODEL = os.getenv("AI_MODEL")

FRONTEND_URL = os.getenv("FRONTEND_URL")

PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DATABASE = os.getenv("PG_DATABASE")