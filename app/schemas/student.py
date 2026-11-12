from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime

class StudentBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)

class StudentCreate(StudentBase):
    password: str = Field(..., min_length=6)

class StudentUpdate(BaseModel):
    email: EmailStr | None = None
    name: str | None = Field(None, min_length=1, max_length=100)

class StudentResponse(StudentBase):
    id: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True