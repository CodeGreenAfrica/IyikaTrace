from sqlalchemy.orm import Session
from apps.backend.models.batch import Batch
from apps.backend.schemas.batch import BatchCreate, BatchUpdate
from uuid import uuid4
from datetime import datetime


def create_batch(db: Session, batch_data: BatchCreate):
    new_batch = Batch(
        id=uuid4(),
        produce_type=batch_data.produce_type,
        produce_name=batch_data.produce_name,
        quantity=batch_data.quantity,
        unit=batch_data.unit,
        harvest_date=batch_data.harvest_date,
        location=batch_data.location,
        input_method=batch_data.input_method,
        fertilizers_used=batch_data.fertilizers_used,
        drugs_administered=batch_data.drugs_administered,
        created_by=batch_data.created_by
    )
    db.add(new_batch)
    db.commit()
    db.refresh(new_batch)
    return new_batch


def get_all_batches(db: Session):
    return db.query(Batch).all()


def get_batch_by_id(db: Session, batch_id):
    return db.query(Batch).filter(Batch.id == batch_id).first()


def update_batch(db: Session, batch_id, update_data: BatchUpdate):
    batch = db.query(Batch).filter(Batch.id == batch_id).first()
    if not batch:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(batch, key, value)
    batch.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(batch)
    return batch
