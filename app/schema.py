from typing import Optional
from datetime import datetime
import uuid
import enum

from pydantic import BaseModel, EmailStr, constr

class LanguageEnum(str, enum.Enum):
    english = 'English'
    german = 'German'

class UserBaseSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    photo: Optional[str]

    class Config:
        orm_mode=True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    password_confirm: str
    role: str = 'user'
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class CourseBaseSchema(BaseModel):
    name: str
    description: Optional[str]
    photo: Optional[str]

    class Config:
        orm_mode=True

class CreateCourseSchema(CourseBaseSchema):
    identifier: Optional[str]
    language: Optional[LanguageEnum]
    parent_id: Optional[str]
    user_id: str

class ComponentBaseSchema(BaseModel):
    element: str
    
    class Config:
        orm_mode=True

class CreateComponentSchema(ComponentBaseSchema):
    page_id: str
