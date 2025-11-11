from fastapi import APIRouter, Depends, HTTPException
from app.schemas import UserCreate, UserLogin
from app.models import User
from app.utils import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    # Simulate user creation
    hashed_pw = HashPassword(user.password)
    return {"email": user.email, "hashed_password": hashed_pw}

@router.post("/login")
def login(user: UserLogin):
    # Simulate login
    if not verify_password(user.password, "stored_hashed_pw"):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(user.email)
    return {"access_token": token}
