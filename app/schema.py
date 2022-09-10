from typing import Optional
from datetime import datetime
import uuid

from pydantic import BaseModel, EmailStr, constr

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