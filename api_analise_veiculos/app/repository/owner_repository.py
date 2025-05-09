from app.db.mongodb import get_db
from app.models.owner import OwnerCreate

class OwnerRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.get_collection("owners")

    def insert_owner(self, owner_data: OwnerCreate):
        return self.collection.insert_one(owner_data.dict())