# import modules for SQLAlchmey ORM models and relationships 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Define Role and User modles with relationships between them
class Role(Base):
    __tablename__ = "Roles"
    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

# Establish one to many relationship between Role and User
    users = relationship("User", back_populates="Role")

# Define User model with foreign key to Role 
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role_id = Column(Integer, ForeignKey("Roles.role_id"))

    role = relationship("Role", back_populates="Users")
