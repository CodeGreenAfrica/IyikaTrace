# apps/backend/models/user.py
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship # <-- Import relationship here
from uuid import uuid4
from datetime import datetime # Keep this for Python-side defaults if not using server_default

# Import the centralized Base
from apps.backend.db.database import Base # <-- IMPORTANT: Import Base from your central database.py

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    kyc_docs = Column(String, nullable=True)
    # Using datetime.utcnow for default and onupdate
    # Note: For production, consider using server_default=func.now()
    # and onupdate=func.now() for database-managed timestamps.
    # If you use datetime.utcnow, it sets the timestamp when the Python object is created/updated.
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define the back_populates for the relationship with Batch
    # 'batches' is the attribute on the User model that will hold a list of Batch objects
    # 'user' refers to the relationship name defined in the Batch model
    batches = relationship("Batch", back_populates="user")