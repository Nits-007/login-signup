import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic import conint


class UserResponse(BaseModel) :
    id : int
    firstName : str
    lastName : str  
    email : EmailStr
    phone: int

    class Config :
        from_attributes = True


class UserCreate(BaseModel) :
    firstName : str
    lastName : str
    phone : int
    email : EmailStr 
    password : str


class UserLogin(BaseModel) :
    email : EmailStr
    password : str