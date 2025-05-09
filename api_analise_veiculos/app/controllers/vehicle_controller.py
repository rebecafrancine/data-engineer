from fastapi import APIRouter, Depends
from app.services.vehicle_service import VehicleService
from app.repository.vehicle_repository import VehicleRepository
from app.models.vehicle import VehicleCreate, VehicleOut
from app.db.mongodb import get_db

router = APIRouter()

@router.post("/vehicles", response_model=VehicleOut)
async def create_vehicle(vehicle: VehicleCreate, db=Depends(get_db)):
    vehicle_service = VehicleService(VehicleRepository())
    vehicle_service.add_vehicle(vehicle)
    return vehicle
