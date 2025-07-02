from sqlalchemy.orm import Session
from models.document import Document
from schemas.document import DocumentCreate, DocumentUpdate
from uuid import uuid4
from datetime import datetime


def create_document(db: Session, doc_data: DocumentCreate):
    document = Document(id=uuid4(), **doc_data.dict())
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def get_all_documents(db: Session):
    return db.query(Document).all()


def get_document_by_id(db: Session, document_id):
    return db.query(Document).filter(Document.id == document_id).first()


def update_document(db: Session, document_id, update_data: DocumentUpdate):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(document, key, value)
    document.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(document)
    return document
