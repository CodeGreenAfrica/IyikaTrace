from pydantic import BaseModel, HttpUrl
from typing import Optional
from uuid import UUID
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None
    file_url: HttpUrl

class DocumentCreate(DocumentBase):
    pass

class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[HttpUrl] = None

class DocumentOut(DocumentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # instead of orm_mode = True

