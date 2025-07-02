from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from db.database import get_db
from schemas.batch import BatchCreate, BatchOut, BatchUpdate
from services.batch_services import create_batch, get_all_batches, get_batch_by_id, update_batch

router_batches = APIRouter(prefix="/api/v1/batches", tags=["Batches"])

@router_batches.post("/", response_model=BatchOut)
def create_new_batch(batch: BatchCreate, db: Session = Depends(get_db)):
    return create_batch(db, batch)

@router_batches.get("/", response_model=list[BatchOut])
def list_all_batches(db: Session = Depends(get_db)):
    return get_all_batches(db)

@router_batches.get("/{batch_id}", response_model=BatchOut)
def retrieve_batch(batch_id: UUID, db: Session = Depends(get_db)):
    batch = get_batch_by_id(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch

@router_batches.put("/{batch_id}", response_model=BatchOut)
def update_existing_batch(batch_id: UUID, batch_data: BatchUpdate, db: Session = Depends(get_db)):
    batch = update_batch(db, batch_id, batch_data)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch
