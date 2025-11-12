from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

#Sign tokens and encryption definition
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

#bcrypt hashing C configuration 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Plain text conversion into a secure hash
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

#Receive user data and add expiration time to return signed JWT string 
def create_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": email, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
