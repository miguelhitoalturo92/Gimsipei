from pydantic import BaseModel, EmailStr, constr, ValidationError
from typing import Optional


class RegisterSchema(BaseModel):
    email: EmailStr
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6)
    full_name: Optional[constr(max_length=100)] = None
    role: constr(min_length=1, max_length=20)


class LoginSchema(BaseModel):
    username: str
    password: str
