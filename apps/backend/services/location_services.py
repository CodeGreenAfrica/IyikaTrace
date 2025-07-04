from sqlalchemy.orm import Session
from apps.backend.models.location import Location
from apps.backend.schemas.location import LocationCreate, LocationUpdate
from uuid import uuid4
from datetime import datetime


def create_location(db: Session, location_data: LocationCreate):
    location = Location(id=uuid4(), **location_data.dict())
    db.add(location)
    db.commit()
    db.refresh(location)
    return location


def get_all_locations(db: Session):
    return db.query(Location).all()


def get_location_by_id(db: Session, location_id):
    return db.query(Location).filter(Location.id == location_id).first()


def update_location(db: Session, location_id, update_data: LocationUpdate):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(location, key, value)
    location.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(location)
    return location
