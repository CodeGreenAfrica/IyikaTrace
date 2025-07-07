# apps/backend/models/batch.py
from sqlalchemy import Column, String, Float, Date, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime # Keep this for Python-side defaults if not using server_default
import enum

# Import the centralized Base
from apps.backend.db.database import Base # <-- IMPORTANT: Import Base from your central database.py

class ProduceType(str, enum.Enum):
    crop = "crop"
    livestock = "livestock"

class Batch(Base):
    __tablename__ = "batches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    produce_type = Column(Enum(ProduceType), nullable=False)
    produce_name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    harvest_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    qr_code_url = Column(String, nullable=True)
    input_method = Column(String, nullable=True)
    fertilizers_used = Column(String, nullable=True)
    drugs_administered = Column(String, nullable=True)
    status = Column(String, default="Pending")
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False) # Refers to "users" table

    # Define the relationship to User
    # 'user' is the attribute on the Batch model that will hold the User object
    # 'batches' refers to the relationship name defined in the User model
    user = relationship("User", back_populates="batches")