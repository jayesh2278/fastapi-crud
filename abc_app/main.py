from fastapi import FastAPI,Depends
from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/createuser",response_model=schemas.User)
def cruser(user:schemas.User,db:Session= Depends(get_db)):
    
    return crud.create_user(db=db,user=user)

@app.get("/getuser",response_model=list[schemas.User])
def alluser(db:Session= Depends(get_db)):
    return crud.all_user(db=db)

@app.delete('/edituser/{id}')
def edituser(id,db:Session= Depends(get_db)):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return {"ok"}

@app.put('/updateuser/{id:int}')
def updateuser(id,request:schemas.User,db:Session= Depends(get_db)):
    db.query(models.User).filter(models.User.id == id).update(request.dict(),synchronize_session=False)
    db.commit()
    return {"updated"}   

