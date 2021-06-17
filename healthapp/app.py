from fastapi.encoders import jsonable_encoder
import uvicorn

from .features import models, schemas, crud

from .features.database import engine, SessionLocal

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer
from pydantic import BaseModel
from fastapi import APIRouter

models.Base.metadata.create_all(bind=engine)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Test
# Dependency

app = FastAPI()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/user", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/reservation")
async def reserve_visit(user: schemas.VisitUpdate, db: Session = Depends(get_db)):
    reserveVisit=crud.reserveVisit(db=db,user=user)
    return reserveVisit



@app.post("/authenticate", response_model=schemas.Token)
def authenticate_user(user: schemas.UserAuthenticate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, email=user.email)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username doesnt exist")
    else:
        is_password_correct = crud.check_username_password(db, user)
        if is_password_correct is False:
            raise HTTPException(status_code=400, detail="Password is not correct")
        else:
            from datetime import timedelta
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            from .features.app_utils import create_access_token
            access_token = create_access_token(
                data={"sub": user.email}, expires_delta=access_token_expires)
            return {"access_token": access_token,"token_type":"bearer","role":db_user.role}


@app.get("/getID/{username}")
async def get_ID(username:str,db: Session = Depends(get_db)):
    db_user = crud.get_user_ID(db, username)
    return db_user


@app.get("/professions")
async def get_Professions(db: Session = Depends(get_db)):
    profession = crud.get_professions(db)
    return profession


# @app.get("/visits/{profession}")
# async def get_visits_profession(profession:str,db:Session=Depends(get_db)):
#     visits_profession=crud.get_visits_profesion(db,profession)
#     return visits_profession


    
# @app.get("/AllFreeVisits")
# async def get_AllFreeVisits(db:Session=Depends(get_db)):
#     AllFreeVisits=crud.get_AllFreeVisits(db)
#     return AllFreeVisits


@app.get("/AllDoctorVisits/{id}")
async def get_AllVisits(id:int,db:Session=Depends(get_db)):
    AllVisits=crud.get_AllVisits(db,id)
    return AllVisits


@app.get("/AllUserVisits/{id}")
async def get_AllUserVisits(id:int,db:Session=Depends(get_db)):
    AllVisits=crud.get_AllUserVisits(db,id)
    return AllVisits

# @app.get("/Name")
# async def nameAll(db:Session=Depends(get_db)):
#     AllVisits=crud.nameAll(db)
#     return AllVisits

@app.get("/doctors")
async def doctors(db:Session=Depends(get_db)):
    doctors=crud.doctors(db)
    return doctors

#WOLNE WIZYTY BY PROFESJA
@app.get("/AllVisitsName/{name}")
async def get_byName(name:str,db:Session=Depends(get_db)):
    get_byname=crud.get_byName(db,name)
    return get_byname


@app.get("/AllVisitsProfession/{profession}")
async def get_byProfession(profession:str,db:Session=Depends(get_db)):
    get_byprofession=crud.get_byProfession(db,profession)
    return get_byprofession



Base = declarative_base()
Base.metadata.create_all(bind=engine)




persons = SQLAlchemyCRUDRouter(
    schema=schemas.Person,
    create_schema=schemas.PersonCreate,
    db_model=models.PersonModel,
    db=get_db,
    prefix='Person'
)


Tests = SQLAlchemyCRUDRouter(
    schema=schemas.Test,
    create_schema=schemas.Test,
    db_model=models.TestModel,
    db=get_db,
    prefix='Test'
)


Visits = SQLAlchemyCRUDRouter(
    schema=schemas.VisitAll,
    create_schema=schemas.VisitCreate,
    db_model=models.VisitModel,
    db=get_db,
    prefix='Visit'
)




app.include_router(persons)
# app.include_router(Tests)
app.include_router(Visits)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
