from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str
    address : str
    status : str

    class Config:
        orm_mode = True