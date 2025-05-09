from fastapi import FastAPI
from app.controllers import vehicle_controller, owner_controller, user_controller
from app.db.mongodb import get_db

app = FastAPI(title="Vehicle Management API", version="1.0.0")

app.include_router(vehicle_controller.router)
app.include_router(owner_controller.router)
app.include_router(user_controller.router)