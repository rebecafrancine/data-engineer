from pydantic import BaseModel
from typing import List

class OwnerBase(BaseModel):
    cpf: str
    name: str
    vehicles: List[str] = []

class OwnerCreate(OwnerBase):
    pass

class OwnerOut(OwnerBase):
    pass
