import hashlib
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Student
from app.schemas import StudentCreate, StudentUpdate
from app.repositories import StudentRepository


class StudentService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = StudentRepository(db)

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def create(self, data: StudentCreate) -> Student:
        # Check if email already exists
        existing = self.repo.get_by_email(data.email)
        if existing:
            raise ValueError("Email already registered")

        # Hash password
        password_hash = self._hash_password(data.password)

        # Create student
        return self.repo.create(data, password_hash)

    def get_all(self) -> List[Student]:
        return self.repo.get_all()

    def get_by_id(self, student_id: UUID) -> Optional[Student]:
        return self.repo.get_by_id(student_id)

    def update(self, student_id: UUID, data: StudentUpdate) -> Optional[Student]:
        # Check if student exists
        student = self.repo.get_by_id(student_id)
        if not student:
            return None

        # Check email uniqueness if changing
        if data.email and data.email != student.email:
            existing = self.repo.get_by_email(data.email)
            if existing:
                raise ValueError("Email already registered")

        return self.repo.update(student_id, data)

    def delete(self, student_id: UUID) -> bool:
        return self.repo.delete(student_id)