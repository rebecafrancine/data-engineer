from pymongo import MongoClient
from app.core.config import settings

def get_db():
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DATABASE_NAME]
    return db