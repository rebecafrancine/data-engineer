from app.db.mongodb import get_db
from app.models.vehicle import VehicleCreate

class VehicleRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.get_collection("vehicles")

    def insert_vehicle(self, vehicle_data: VehicleCreate):
        return self.collection.insert_one(vehicle_data.dict())

    def find_all_vehicles(self):
        return self.collection.find()
