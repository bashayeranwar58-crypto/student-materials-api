from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SubjectCreate, SubjectUpdate, SubjectResponse
from app.services import SubjectService

router = APIRouter(prefix="/subjects", tags=["Subjects"])


@router.post(
    "",
    response_model=SubjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new subject",
)
def create_subject(data: SubjectCreate, db: Session = Depends(get_db)):
    service = SubjectService(db)
    return service.create(data)


@router.get(
    "",
    response_model=List[SubjectResponse],
    summary="Get all subjects",
)
def get_all_subjects(db: Session = Depends(get_db)):
    service = SubjectService(db)
    return service.get_all()


@router.get(
    "/{subject_id}",
    response_model=SubjectResponse,
    summary="Get a subject by ID",
)
def get_subject(subject_id: UUID, db: Session = Depends(get_db)):
    service = SubjectService(db)
    subject = service.get_by_id(subject_id)
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found"
        )
    return subject


@router.put(
    "/{subject_id}",
    response_model=SubjectResponse,
    summary="Update an existing subject",
)
def update_subject(
    subject_id: UUID, data: SubjectUpdate, db: Session = Depends(get_db)
):
    service = SubjectService(db)
    subject = service.update(subject_id, data)
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found"
        )
    return subject


@router.delete(
    "/{subject_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a subject",
)
def delete_subject(subject_id: UUID, db: Session = Depends(get_db)):
    service = SubjectService(db)
    deleted = service.delete(subject_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found"
        )
    return None