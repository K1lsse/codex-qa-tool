import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    TOKENESS_API_KEY = os.getenv("TOKENESS_API_KEY", "").strip()
    TOKENESS_BASE_URL = os.getenv("TOKENESS_BASE_URL", "").strip()

    MODEL = os.getenv("MODEL", "gpt-4o-mini")