from pydantic import BaseModel, EmailStr, HttpUrl
from uuid import UUID
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    role: str
    kyc_docs: Optional[HttpUrl] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    kyc_docs: Optional[HttpUrl] = None

class UserOut(UserBase):
    id: UUID
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
