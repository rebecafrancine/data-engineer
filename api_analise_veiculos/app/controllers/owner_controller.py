from fastapi import APIRouter, Depends
from app.services.owner_service import OwnerService
from app.repository.owner_repository import OwnerRepository
from app.models.owner import OwnerCreate, OwnerOut
from app.db.mongodb import get_db

router = APIRouter()

@router.post("/owners", response_model=OwnerOut)
async def create_owner(owner: OwnerCreate, db=Depends(get_db)):
    owner_service = OwnerService(OwnerRepository())
    owner_service.add_owner(owner)
    return owner