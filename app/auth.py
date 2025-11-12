from fastapi import APIRouter, Depends, HTTPException
from app.schemas import UserCreate, UserLogin
from app.models import User
from app.utils import hash_password, verify_password, create_token

#Initialize the router 
router = APIRouter()

# Create POST router for register 
@router.post("/register")
def register(user: UserCreate):
    # User create Simulation
    hashed_pw = HashPassword(user.password)
    return {"email": user.email, "hashed_password": hashed_pw}


#POST route for Login
@router.post("/login")
def login(user: UserLogin):
    # Login Simulation
    if not verify_password(user.password, "stored_hashed_pw"):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(user.email)
    return {"access_token": token}
