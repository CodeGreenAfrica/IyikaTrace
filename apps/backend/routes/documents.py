from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from apps.backend.db.database import get_db
from apps.backend.schemas.document import DocumentCreate, DocumentUpdate, DocumentOut
from apps.backend.services.document_services import (
    create_document,
    get_all_documents,
    get_document_by_id,
    update_document
)

router_documents = APIRouter(prefix="/api/v1/documents", tags=["Documents"])

@router_documents.post("/", response_model=DocumentOut)
def create_new_document(document: DocumentCreate, db: Session = Depends(get_db)):
    return create_document(db, document)

@router_documents.get("/", response_model=list[DocumentOut])
def list_documents(db: Session = Depends(get_db)):
    return get_all_documents(db)

@router_documents.get("/{document_id}", response_model=DocumentOut)
def get_document(document_id: UUID, db: Session = Depends(get_db)):
    document = get_document_by_id(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router_documents.put("/{document_id}", response_model=DocumentOut)
def update_existing_document(document_id: UUID, update: DocumentUpdate, db: Session = Depends(get_db)):
    updated = update_document(db, document_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="Document not found")
    return updated
