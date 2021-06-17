from datetime import datetime
from typing import List
from pydantic import BaseModel


class UserInfoBase(BaseModel):
    email: str


class UserCreate(UserInfoBase):
    password: str
    role:str
    profession:str


class UserAuthenticate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True


class Profession(BaseModel):
    name:str

class Token(BaseModel):
    access_token: str
    token_type: str
    role:str


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

class Test(BaseModel):
    profession_id:int
    class Config:
        orm_mode=True


# class VisitUpdate(BaseModel):
#     id:int
#     patient_id:int
class VisitUpdate(BaseModel):
    id:int
    patient_id:int
class VisitCreate(BaseModel):
    date_start:datetime
    date_end:datetime
    doctor_id:int
class Visit(VisitCreate):
    id:int
    date_start:datetime
    date_end:datetime
    doctor_id:int
    
    class Config:
        orm_mode=True

class VisitAll(BaseModel):
    date_start:datetime
    date_end:datetime
    doctor_id:int
    patient_id:int
    note:str
    
    class Config:
        orm_mode=True



