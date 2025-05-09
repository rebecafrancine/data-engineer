from app.repository.owner_repository import OwnerRepository
from app.models.owner import OwnerCreate

class OwnerService:
    def __init__(self, owner_repo: OwnerRepository):
        self.owner_repo = owner_repo

    def add_owner(self, owner_data: OwnerCreate):
        return self.owner_repo.insert_owner(owner_data)
