from calendar import c
from email.policy import strict
from enum import auto
from sqlalchemy import Column, String,Integer
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    status = Column(String)