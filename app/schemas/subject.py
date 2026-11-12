from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class SubjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None

class SubjectResponse(SubjectBase):
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True