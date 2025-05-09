from app.repository.vehicle_repository import VehicleRepository
from app.models.vehicle import VehicleCreate

class VehicleService:
    def __init__(self, vehicle_repo: VehicleRepository):
        self.vehicle_repo = vehicle_repo

    def add_vehicle(self, vehicle_data: VehicleCreate):
        return self.vehicle_repo.insert_vehicle(vehicle_data)