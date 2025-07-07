from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from apps.backend.db.database import get_db
from apps.backend.schemas.location import LocationCreate, LocationUpdate, LocationOut
from apps.backend.services.location_services import (
    create_location,
    get_all_locations,
    get_location_by_id,
    update_location
)

router_locations = APIRouter(prefix="/api/v1/locations", tags=["Locations"])

@router_locations.post("/", response_model=LocationOut)
def create_new_location(location: LocationCreate, db: Session = Depends(get_db)):
    return create_location(db, location)

@router_locations.get("/", response_model=list[LocationOut])
def list_locations(db: Session = Depends(get_db)):
    return get_all_locations(db)

@router_locations.get("/{location_id}", response_model=LocationOut)
def get_location(location_id: UUID, db: Session = Depends(get_db)):
    location = get_location_by_id(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router_locations.put("/{location_id}", response_model=LocationOut)
def update_existing_location(location_id: UUID, update: LocationUpdate, db: Session = Depends(get_db)):
    updated = update_location(db, location_id, update)
    if not updated:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated
