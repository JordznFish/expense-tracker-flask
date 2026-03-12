import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = os.getenv("PORT", 5000)
    DATABASE_URL = os.getenv("DATABASE_URL")
    JWT_SECRET = os.getenv("JWT_SECRET")
    