# import necessary modules and dependencies for implementing user routes and operations 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.auth import password_verification, access_control_creation, getting_current_user 

# Create a router for user_related endpoints
router = APIRouter()

# Dependency to get a database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to register a new user 
@router.post("/register", response_model=schemas.user_read)
def register_user(user: schemas.user_create, db: Session = Depends(get_db)):
    existing_user = crud.getting_current_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already used by another user! please choose a different one")
    new_user = crud.create_user(db, user)
    role_name = new_user.role.name if new_user.role else None
    return schemas.user_read(id=new_user.id, username=new_user.username, role_name=role_name)

# Endpoint for user Login and token generation
@router.post("/login", response_model=schemas.token)
def login(user: schemas.user_login, db: Session = Depends(get_db)):
    db_user = crud.getting_current_username(db, user.username)
    if not db_user or not password_verification(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token_data = {"sub": db_user.username, "role": db_user.role.name if db_user.role else "user"}
    access_token = access_control_creation(data=token_data)
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint to get current user information
@router.get("/me")
def read_current_user(current_user: dict = Depends(getting_current_user)):
    return {"user": current_user}
