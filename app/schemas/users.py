from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    user_name: str

class UserCreate(BaseModel):
    user_name: str
    password: str
    email: EmailStr
    role: Optional[str] = "user"

class UserInDb(BaseModel):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_name: str
