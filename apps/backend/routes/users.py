# routes/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from db.database import get_db
from schemas.user import UserCreate, UserOut, UserUpdate, LoginRequest
from services.user_services import (
    create_user,
    get_all_users,
    update_user,
    verify_user,
    login_user
)

router_users = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router_users.post("/", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router_users.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router_users.put("/{user_id}", response_model=UserOut)
def update_user_profile(user_id: UUID, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated = update_user(db, user_id, user_update)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router_users.patch("/{user_id}/verify")
def verify_user_account(user_id: UUID, db: Session = Depends(get_db)):
    verified = verify_user(db, user_id)
    if not verified:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User verified successfully"}

@router_users.post("/login")
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, credentials)
