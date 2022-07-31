from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db:Session,user:schemas.User):
    db_user = models.User(name=user.name,address=user.address,status=user.status)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def all_user(db:Session,limit=10):
    return   db.query(models.User).all() 

def changeuser_data(db:Session,user:schemas.User):
    db.query(models.User)
