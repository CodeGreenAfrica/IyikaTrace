from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from apps.backend.db.database import get_db
from apps.backend.schemas.trace_log import TraceLogCreate, TraceLogOut, TraceLogUpdate
from apps.backend.services.trace_log_services import (
    create_trace_log,
    get_all_trace_logs,
    get_trace_log_by_id,
    update_trace_log
)

router_trace_logs = APIRouter(prefix="/api/v1/trace-logs", tags=["Trace Logs"])

@router_trace_logs.post("/", response_model=TraceLogOut)
def create_log(log_data: TraceLogCreate, db: Session = Depends(get_db)):
    return create_trace_log(db, log_data)

@router_trace_logs.get("/", response_model=list[TraceLogOut])
def list_logs(db: Session = Depends(get_db)):
    return get_all_trace_logs(db)

@router_trace_logs.get("/{log_id}", response_model=TraceLogOut)
def get_log(log_id: UUID, db: Session = Depends(get_db)):
    log = get_trace_log_by_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Trace log not found")
    return log

@router_trace_logs.put("/{log_id}", response_model=TraceLogOut)
def update_log(log_id: UUID, log_data: TraceLogUpdate, db: Session = Depends(get_db)):
    updated = update_trace_log(db, log_id, log_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Trace log not found")
    return updated
