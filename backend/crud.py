from sqlalchemy.orm import Session
from backend import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

def get_user_by_email(db:Session, email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db:Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.user(
        name = user.name,
        surname = user.surname,
        phone = user.phone,
        email = user.email,
        password = hashed_password,
        user_type = user.user_type
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user