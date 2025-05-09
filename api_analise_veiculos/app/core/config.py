import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI = os.getenv("MONGODB_URI")
    DATABASE_NAME = "data-engineer"

settings = Settings()