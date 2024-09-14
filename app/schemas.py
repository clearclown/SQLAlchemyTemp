# app/schemas.py

from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        # Pydantic v2.xでの変更に対応
        from_attributes = True
