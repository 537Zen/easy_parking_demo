from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    surname: str
    phone: str
    email: EmailStr
    password:str
    user_type:str

class User(BaseModel):
    id:int
    name:str
    surname:str
    phone:str
    email:EmailStr
    user_type:str

class Config:
    orm_mode = True