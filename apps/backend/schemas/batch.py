from pydantic import BaseModel, HttpUrl
from typing import Optional
from uuid import UUID
from datetime import date, datetime
import enum

class ProduceType(str, enum.Enum):
    crop = "crop"
    livestock = "livestock"

class BatchBase(BaseModel):
    produce_type: ProduceType
    produce_name: str
    quantity: float
    unit: str
    harvest_date: date
    location: str
    input_method: Optional[str] = None
    fertilizers_used: Optional[str] = None
    drugs_administered: Optional[str] = None

class BatchCreate(BatchBase):
    created_by: UUID

class BatchUpdate(BaseModel):
    produce_name: Optional[str]
    quantity: Optional[float]
    unit: Optional[str]
    harvest_date: Optional[date]
    location: Optional[str]
    input_method: Optional[str]
    fertilizers_used: Optional[str]
    drugs_administered: Optional[str]
    status: Optional[str]

class BatchOut(BatchBase):
    id: UUID
    status: str
    qr_code_url: Optional[HttpUrl]
    created_at: datetime
    updated_at: datetime
    created_by: UUID

    class Config:
        orm_mode = True
