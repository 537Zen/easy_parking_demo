from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:123456@127.0.0.1:3306/easy_parking_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
metadata = MetaData()
metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=True)
Base = declarative_base(name='Base')