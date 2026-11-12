from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import MaterialCreate, MaterialUpdate, MaterialResponse
from app.services import MaterialService

router = APIRouter(prefix="/materials", tags=["Materials"])


@router.post(
    "",
    response_model=MaterialResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload a new material",
)
def create_material(data: MaterialCreate, db: Session = Depends(get_db)):
    service = MaterialService(db)
    return service.create(data)


@router.get(
    "",
    response_model=List[MaterialResponse],
    summary="Get all materials",
)
def get_all_materials(db: Session = Depends(get_db)):
    service = MaterialService(db)
    return service.get_all()


@router.get(
    "/{material_id}",
    response_model=MaterialResponse,
    summary="Get a material by ID",
)
def get_material(material_id: UUID, db: Session = Depends(get_db)):
    service = MaterialService(db)
    material = service.get_by_id(material_id)
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Material not found"
        )
    return material


@router.get(
    "/by-subject/{subject_id}",
    response_model=List[MaterialResponse],
    summary="Get materials by subject",
)
def get_materials_by_subject(subject_id: UUID, db: Session = Depends(get_db)):
    service = MaterialService(db)
    return service.get_by_subject(subject_id)


@router.get(
    "/by-student/{student_id}",
    response_model=List[MaterialResponse],
    summary="Get materials by student",
)
def get_materials_by_student(student_id: UUID, db: Session = Depends(get_db)):
    service = MaterialService(db)
    return service.get_by_student(student_id)


@router.put(
    "/{material_id}",
    response_model=MaterialResponse,
    summary="Update an existing material",
)
def update_material(
    material_id: UUID, data: MaterialUpdate, db: Session = Depends(get_db)
):
    service = MaterialService(db)
    material = service.update(material_id, data)
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Material not found"
        )
    return material


@router.delete(
    "/{material_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a material",
)
def delete_material(material_id: UUID, db: Session = Depends(get_db)):
    service = MaterialService(db)
    deleted = service.delete(material_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Material not found"
        )
    return None