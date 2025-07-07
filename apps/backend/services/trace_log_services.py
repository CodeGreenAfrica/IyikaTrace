from sqlalchemy.orm import Session
from apps.backend.models.trace_log import TraceLog
from apps.backend.schemas.trace_log import TraceLogCreate, TraceLogUpdate
from uuid import uuid4
from datetime import datetime


def create_trace_log(db: Session, log_data: TraceLogCreate):
    log = TraceLog(
        id=uuid4(),
        batch_id=log_data.batch_id,
        user_id=log_data.user_id,
        event_type=log_data.event_type,
        location=log_data.location,
        temperature=log_data.temperature,
        humidity=log_data.humidity,
        notes=log_data.notes
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_all_trace_logs(db: Session):
    return db.query(TraceLog).all()


def get_trace_log_by_id(db: Session, log_id):
    return db.query(TraceLog).filter(TraceLog.id == log_id).first()


def update_trace_log(db: Session, log_id, update_data: TraceLogUpdate):
    log = db.query(TraceLog).filter(TraceLog.id == log_id).first()
    if not log:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(log, key, value)
    log.timestamp = datetime.utcnow()
    db.commit()
    db.refresh(log)
    return log
