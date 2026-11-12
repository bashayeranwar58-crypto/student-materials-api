from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Material
from app.schemas import MaterialCreate, MaterialUpdate
from app.repositories import MaterialRepository


class MaterialService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = MaterialRepository(db)

    def create(self, data: MaterialCreate) -> Material:
        return self.repo.create(data)

    def get_all(self) -> List[Material]:
        return self.repo.get_all()

    def get_by_id(self, material_id: UUID) -> Optional[Material]:
        return self.repo.get_by_id(material_id)

    def get_by_subject(self, subject_id: UUID) -> List[Material]:
        return self.repo.get_by_subject(subject_id)

    def get_by_student(self, student_id: UUID) -> List[Material]:
        return self.repo.get_by_student(student_id)

    def update(self, material_id: UUID, data: MaterialUpdate) -> Optional[Material]:
        return self.repo.update(material_id, data)

    def delete(self, material_id: UUID) -> bool:
        return self.repo.delete(material_id)