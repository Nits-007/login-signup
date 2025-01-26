from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text, BigInteger
from sqlalchemy.sql.expression import null
from .database import Base 
from sqlalchemy.orm import relationship


class User(Base) :
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    phone = Column(BigInteger, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)