from sqlalchemy import Column, Integer, String
from app.database import base

#create the base table for users
class User(base):
    __tablename__ = "users"

    ID= Column(Integer, primary_key=True, index=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Age = Column(Integer, nullable=False)
    Email = Column(String, unique=True, index=True, nullable=False)
    HashedPassword = Column(String, nullable=False)
    Role = Column(String, default="user")  # choose the user role by default
