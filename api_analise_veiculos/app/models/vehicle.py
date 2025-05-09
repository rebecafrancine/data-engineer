from pydantic import BaseModel
from typing import Optional
from datetime import date

class VehicleBase(BaseModel):
    brand: str
    model: str
    manufacture_year: int
    mileage: float
    fuel_type: str
    price: float
    has_fines: bool
    has_insurance: bool
    color: str
    transmission: str
    doors: int
    airbag: bool
    abs: bool
    last_service_date: date

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    vehicle_id: str

    class Config:
        orm_mode = True
