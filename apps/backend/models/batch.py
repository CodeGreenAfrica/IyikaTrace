from sqlalchemy import Column, String, Float, Date, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from db.database import Base
import enum

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
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    user = relationship("User")
