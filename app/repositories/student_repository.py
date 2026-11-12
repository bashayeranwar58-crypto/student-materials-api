from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Student
from app.schemas import StudentCreate, StudentUpdate


class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: StudentCreate, password_hash: str) -> Student:
        student = Student(
            email=data.email,
            password_hash=password_hash,
            name=data.name,
        )
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def get_all(self) -> List[Student]:
        return self.db.query(Student).all()

    def get_by_id(self, student_id: UUID) -> Optional[Student]:
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_by_email(self, email: str) -> Optional[Student]:
        return self.db.query(Student).filter(Student.email == email).first()

    def update(self, student_id: UUID, data: StudentUpdate) -> Optional[Student]:
        student = self.get_by_id(student_id)
        if not student:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(student, field, value)

        self.db.commit()
        self.db.refresh(student)
        return student

    def delete(self, student_id: UUID) -> bool:
        student = self.get_by_id(student_id)
        if not student:
            return False

        self.db.delete(student)
        self.db.commit()
        return True