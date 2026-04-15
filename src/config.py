import os 
from dotenv import load_dotenv

load_dotenv()

RLM_PROVIDER = os.getenv("RLM_PROVIDER")
AI_MODEL = os.getenv("AI_MODEL")