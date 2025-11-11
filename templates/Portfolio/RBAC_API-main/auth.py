#import necessary libraries and modules for authentication and security 
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Define constraints and configurations for JWT and password hashing 
SECRET_KEY = "your secret key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 25

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# Functions for hasshing passwords, verifying passwords, creating JWT tokens and getting current user from token 
def hash_passwords(password: str) -> str:
    return pwd_context.hash(password)

def password_verification(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def access_control_creation(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def getting_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Credentails could not be validated",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Decode the JWT token and extract user information 
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception
