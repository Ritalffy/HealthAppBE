from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel

class UserInfo(Base):
    __tablename__ = "Login"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

class PersonModel(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Street = Column(String)
    City = Column(String)
    Zip = Column(String)
    Phone = Column(String)








