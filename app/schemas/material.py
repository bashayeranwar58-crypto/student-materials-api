from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class MaterialBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    file_path: str = Field(..., min_length=1, max_length=500)
    file_size: int | None = None
    subject_id: UUID
    student_id: UUID

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None
    file_path: str | None = None
    file_size: int | None = None
    subject_id: UUID | None = None
    student_id: UUID | None = None

class MaterialResponse(MaterialBase):
    id: UUID
    uploaded_at: datetime
    
    class Config:
        from_attributes = True