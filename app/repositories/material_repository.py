from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models import Material
from app.schemas import MaterialCreate, MaterialUpdate


class MaterialRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: MaterialCreate) -> Material:
        material = Material(
            title=data.title,
            description=data.description,
            file_path=data.file_path,
            file_size=data.file_size,
            subject_id=data.subject_id,
            student_id=data.student_id,
        )
        self.db.add(material)
        self.db.commit()
        self.db.refresh(material)
        return material

    def get_all(self) -> List[Material]:
        return self.db.query(Material).all()

    def get_by_id(self, material_id: UUID) -> Optional[Material]:
        return self.db.query(Material).filter(Material.id == material_id).first()

    def get_by_subject(self, subject_id: UUID) -> List[Material]:
        return self.db.query(Material).filter(Material.subject_id == subject_id).all()

    def get_by_student(self, student_id: UUID) -> List[Material]:
        return self.db.query(Material).filter(Material.student_id == student_id).all()

    def update(self, material_id: UUID, data: MaterialUpdate) -> Optional[Material]:
        material = self.get_by_id(material_id)
        if not material:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(material, field, value)

        self.db.commit()
        self.db.refresh(material)
        return material

    def delete(self, material_id: UUID) -> bool:
        material = self.get_by_id(material_id)
        if not material:
            return False

        self.db.delete(material)
        self.db.commit()
        return True