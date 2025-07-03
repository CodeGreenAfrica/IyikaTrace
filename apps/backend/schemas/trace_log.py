from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class TraceLogBase(BaseModel):
    batch_id: UUID
    user_id: UUID
    event_type: str
    location: Optional[str] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    notes: Optional[str] = None

class TraceLogCreate(TraceLogBase):
    pass

class TraceLogUpdate(BaseModel):
    event_type: Optional[str]
    location: Optional[str]
    temperature: Optional[float]
    humidity: Optional[float]
    notes: Optional[str]

class TraceLogOut(TraceLogBase):
    id: UUID
    timestamp: datetime

    class Config:
        from_attributes = True  # instead of orm_mode = True

