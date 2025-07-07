from sqlalchemy.orm import Session
from models.document import Document
from schemas.document import DocumentCreate, DocumentUpdate
from uuid import uuid4
from datetime import datetime
from pydantic import HttpUrl

def create_document(db: Session, doc_data: DocumentCreate):
    file_url_str = str(doc_data.file_url) if doc_data.file_url else None
    # Ensure file_url is a string
    document = Document(id=uuid4(), title=doc_data.title,
                        description=doc_data.description,
                        file_url=file_url_str,)
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
        if key == "file_url" and isinstance(value, HttpUrl):
            setattr(document, key, str(value))
        else:
            setattr(document, key, value)
    document.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(document)
    return document
