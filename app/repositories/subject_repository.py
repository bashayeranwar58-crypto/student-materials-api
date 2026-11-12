from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Subject
from app.schemas import SubjectCreate, SubjectUpdate


class SubjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: SubjectCreate) -> Subject:
        subject = Subject(
            name=data.name,
            description=data.description,
        )
        self.db.add(subject)
        self.db.commit()
        self.db.refresh(subject)
        return subject

    def get_all(self) -> List[Subject]:
        return self.db.query(Subject).all()

    def get_by_id(self, subject_id: UUID) -> Optional[Subject]:
        return self.db.query(Subject).filter(Subject.id == subject_id).first()

    def update(self, subject_id: UUID, data: SubjectUpdate) -> Optional[Subject]:
        subject = self.get_by_id(subject_id)
        if not subject:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(subject, field, value)

        self.db.commit()
        self.db.refresh(subject)
        return subject

    def delete(self, subject_id: UUID) -> bool:
        subject = self.get_by_id(subject_id)
        if not subject:
            return False

        self.db.delete(subject)
        self.db.commit()
        return True