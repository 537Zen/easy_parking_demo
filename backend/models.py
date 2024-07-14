from sqlalchemy import Column, Integer, String, Datetime, func
from backend.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment='Name')
    surname = Column(String(50), nullable=False, comment='Surname')
    phone = Column(String(20), unique=True, comment='Phone')
    email = Column(String(100), unique=True, comment='Email')
    password = Column(String(100), comment='Password')
    user_type = Column(String(100), comment='User Type: admin/normal')
    created_at = Column(Datetime, server_default=func.now(), comment='Created time')
    updated_at = Column(Datetime, server_default=func.now(),onupdate=func.now(), comment='Update time')

    __table_args__ = {'extend_existing': True}