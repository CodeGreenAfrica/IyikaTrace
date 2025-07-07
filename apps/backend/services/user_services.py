from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
from passlib.context import CryptContext
from fastapi import HTTPException

from apps.backend.models.user import User
from apps.backend.schemas.user import UserCreate, UserUpdate, LoginRequest

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    #converting HttpUrl to string for kyc_docs
    kyc_docs_str = str(user.kyc_docs) if user.kyc_docs else None
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if not user.role:
        raise HTTPException(status_code=400, detail="Role is required")
    db_user = User(
        id=uuid4(),
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        password=hashed_password,
        role=user.role,
        is_verified=False,
        kyc_docs=kyc_docs_str, # Ensure kyc_docs is a string
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: str, user_data: UserUpdate):
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
     # Update fields only if they are provided in user_data
    if user_data.name is not None: # Use 'is not None' for optional fields
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email
    if user_data.phone_number is not None:
        user.phone_number = user_data.phone_number
    if user_data.password is not None:
        user.password = get_password_hash(user_data.password)
    if user_data.role is not None:
        user.role = user_data.role

    if user_data.kyc_docs is not None:
        # Convert HttpUrl to string before assigning to the SQLAlchemy model
        user.kyc_docs = str(user_data.kyc_docs)
   
    # Update the updated_at timestamp to current UTC time
    user.updated_at = datetime.utcnow() # Use datetime.datetime.utcnow()

    db.commit()
    db.refresh(user)
    return user

def verify_user(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.is_verified = True
    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, credentials: LoginRequest):
    user = get_user_by_email(db, credentials.email)
    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "is_verified": user.is_verified
    }
