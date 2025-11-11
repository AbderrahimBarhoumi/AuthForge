# import necessary modules and dependencies for CRUD operations 
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_passwords

# Functions to create a new user and get a user by username
def create_user(db: Session, user: schemas.user_create):
    hashed_pw = hash_passwords(user.password)
    db_user = models.User(username=user.username, hashed_passwords=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Function to get a user by username 
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first() 
