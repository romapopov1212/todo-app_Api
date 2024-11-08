from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(Text)


class Note(Base):
    __tablename__ = "Notes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_start = Column(DateTime)
    date_end = Column(DateTime)

