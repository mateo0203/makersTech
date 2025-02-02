from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for reading user data
class UserSchema(BaseModel):
    user_id: int
    name: str
    age: int
    email: EmailStr
    gender: Optional[str] = None  # Gender is optional

    class Config:
        orm_mode = True

# Schema for creating a new user
class UserCreateSchema(BaseModel):
    name: str
    age: int
    email: EmailStr
    gender: Optional[str] = None