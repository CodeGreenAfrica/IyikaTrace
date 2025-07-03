from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class LocationBase(BaseModel):
    name: str
    type: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = None

class LocationCreate(LocationBase):
    pass

class LocationUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = None

class LocationOut(LocationBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # instead of orm_mode = True

