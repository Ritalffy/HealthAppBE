from typing import List
from pydantic import BaseModel


class UserInfoBase(BaseModel):
    email: str


class UserCreate(UserInfoBase):
    password: str


class UserAuthenticate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None



class PersonCreate(BaseModel):
    FirstName: str
    LastName: str
    Street:str
    City:str
    Zip:str
    Phone:str

class Person(PersonCreate):
    id: int

    class Config:
        orm_mode = True




