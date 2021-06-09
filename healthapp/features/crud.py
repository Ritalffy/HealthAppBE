from sqlalchemy.orm import Session
from . import models, schemas
import bcrypt


def get_user_by_username(db: Session, email: str):
    return db.query(models.UserInfo).filter(models.UserInfo.email == email).first()

def get_user_ID(db: Session, email: str):
    return db.query(models.UserInfo.id).filter(models.UserInfo.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.UserInfo(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    db_person = models.PersonModel(FirstName="",LastName="",Street="",City="",Zip="",Phone="")
    db.add(db_person)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(db: Session, user: schemas.UserAuthenticate):
    db_user_info: models.UserInfo = get_user_by_username(db, email=user.email)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))

