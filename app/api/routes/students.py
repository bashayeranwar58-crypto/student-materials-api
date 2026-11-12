from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import StudentCreate, StudentUpdate, StudentResponse
from app.services import StudentService

router = APIRouter(prefix="/students", tags=["Students"])


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new student",
)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    service = StudentService(db)
    try:
        student = service.create(data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return student


@router.get(
    "",
    response_model=List[StudentResponse],
    summary="Get all students",
)
def get_all_students(db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.get_all()


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
    summary="Get a student by ID",
)
def get_student(student_id: UUID, db: Session = Depends(get_db)):
    service = StudentService(db)
    student = service.get_by_id(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return student


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
    summary="Update an existing student",
)
def update_student(
    student_id: UUID, data: StudentUpdate, db: Session = Depends(get_db)
):
    service = StudentService(db)
    try:
        student = service.update(student_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return student


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a student",
)
def delete_student(student_id: UUID, db: Session = Depends(get_db)):
    service = StudentService(db)
    deleted = service.delete(student_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return None