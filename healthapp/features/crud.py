# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from . import models, schemas
import bcrypt


def get_user_by_username(db: Session, email: str):
    return db.query(models.UserInfo).filter(models.UserInfo.email == email).first()

def get_user_ID(db: Session, email: str):
    return db.query(models.UserInfo.id).filter(models.UserInfo.email == email).first()

def get_professions(db: Session):
    return db.query(models.ProfessionModel.name).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.UserInfo(email=user.email, password=hashed_password,role=user.role,profession=user.profession)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    myLoginID=get_user_ID(db,user.email)

    db_person = models.PersonModel(login_id=myLoginID,FirstName="",LastName="",Street="",City="",Zip="",Phone="")
    db.add(db_person)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(db: Session, user: schemas.UserAuthenticate):
    db_user_info: models.UserInfo = get_user_by_username(db, email=user.email)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))

#get_visits_profesion

def get_visits_profesion(db: Session,profession:str):
    return db.query(models.VisitModel).filter(models.UserInfo.profession == profession).all()


    
def get_AllFreeVisits(db: Session):
    allFree=db.query("select * from visit").all()#.filter(models.VisitModel.patient_id == 1).all()

    return allFree


def get_DoctorName(db:Session,id:str):
    name=db.query(models.PersonModel.FirstName).filter(models.PersonModel.id == id).first()
    return str(name)


#def get_AllVisits(db: Session,id:str):
 #   return db.query(models.VisitModel.date_start,models.VisitModel.date_end,models.VisitModel.doctor_id,models.VisitModel.patient_id,models.VisitModel.note).filter(models.VisitModel.doctor_id == id).all()
def get_AllVisits(db: Session,id:str):
    # return db.query(models.VisitModel).filter(models.VisitModel.doctor_id == id).all()
    return db.query(models.VisitModel.date_start,models.VisitModel.date_end,models.PersonModel.FirstName +" "+models.PersonModel.LastName,models.VisitModel.note).filter(models.VisitModel.doctor_id == id).filter(models.VisitModel.patient_id == models.PersonModel.login_id).all()
    #return db.query(models.PersonModel.FirstName).filter(models.PersonModel.id == id).first()

def nameAll(db: Session):
    # return db.query(models.VisitModel).filter(models.VisitModel.doctor_id == id).all()
    return db.query(models.VisitModel).all()

def doctors(db: Session):
    return db.query(models.PersonModel.FirstName +" "+models.PersonModel.LastName,models.UserInfo.profession).join(models.PersonModel).filter(models.UserInfo.role == "doctor").all()

def get_byName(db: Session,name:str):
    # return db.query(models.VisitModel).filter(models.VisitModel.doctor_id == id).all()
    return db.query(models.VisitModel.id,models.VisitModel.date_start,models.VisitModel.date_end).filter(models.VisitModel.doctor_id ==models.PersonModel.id).filter(models.PersonModel.FirstName+" "+models.PersonModel.LastName == name).filter(models.VisitModel.patient_id==1).all()
    #return db.query(models.PersonModel.FirstName).filter(models.PersonModel.id == id).first()


def get_byProfession(db: Session,profession:str):
    return db.query(models.VisitModel.id,models.VisitModel.date_start,models.VisitModel.date_end,models.PersonModel.FirstName+" "+models.PersonModel.LastName).filter(models.VisitModel.doctor_id ==models.PersonModel.id).filter(models.PersonModel.id==models.UserInfo.id).filter(models.UserInfo.profession==profession).filter(models.VisitModel.patient_id==1).all()

# def tescior(db: Session):
#     return db.query(models.TestModel,models.ProfessionModel).join(models.ProfessionModel).all()

# def tescior(db: Session):
#     test=[]
#     for a,b in db.query(models.TestModel,models.ProfessionModel).join(models.ProfessionModel).all():
#         test.append("ID:{} Profession:{}".format(a.id,b.name))
#     return jsonable_encoder(test)
