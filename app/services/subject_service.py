from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Subject
from app.schemas import SubjectCreate, SubjectUpdate
from app.repositories import SubjectRepository


class SubjectService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = SubjectRepository(db)

    def create(self, data: SubjectCreate) -> Subject:
        return self.repo.create(data)

    def get_all(self) -> List[Subject]:
        return self.repo.get_all()

    def get_by_id(self, subject_id: UUID) -> Optional[Subject]:
        return self.repo.get_by_id(subject_id)

    def update(self, subject_id: UUID, data: SubjectUpdate) -> Optional[Subject]:
        return self.repo.update(subject_id, data)

    def delete(self, subject_id: UUID) -> bool:
        return self.repo.delete(subject_id)