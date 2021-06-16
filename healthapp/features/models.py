from healthapp.features.schemas import Person
from os import name
from re import S
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import column, null, true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime, VARCHAR
from sqlalchemy.sql.type_api import NULLTYPE
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
    id = Column(Integer,primary_key=True, index=True)
    login_id=Column(Integer,ForeignKey(UserInfo.id))
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

class TestModel(Base):
    __tablename__='Test'
    id=Column(Integer,primary_key=True,index=True)
    profession_id=Column(Integer,ForeignKey(ProfessionModel.id))
    # profession = relationship("Person", back_populates="Profession")

class VisitModel(Base):
    __tablename__="Visit"
    id=Column(Integer,primary_key=True,index=True)
    date_start=Column(DateTime)
    date_end=Column(DateTime)
    doctor_id=Column(Integer,ForeignKey(PersonModel.id))
    patient_id=Column(Integer,ForeignKey(PersonModel.login_id),default=1)
    note=Column(String,default="")

  #  patient = relationship('PersonModel', foreign_keys='VisitModel.doctor_id')
   # doctor = relationship('PersonModel', foreign_keys='VisitModel.patient_id')

#Tabela rezerwacji
#ID
#Start wizyty
#Koniec wizyty
#id_lekarza
#profesja?
#id_pacjenta
#notka





