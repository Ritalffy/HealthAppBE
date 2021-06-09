from os import name
from re import S
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from pydantic import BaseModel

class UserInfo(Base):
    __tablename__ = "Login"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="patient")
    profession = Column(String,default="")

class PersonModel(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Street = Column(String)
    City = Column(String)
    Zip = Column(String)
    Phone = Column(String)


class ProfessionModel(Base):
    __tablename__ = 'Profession'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # profession = relationship("Profession", back_populates="Profession")


    # profession = relationship("Person", back_populates="Profession")






