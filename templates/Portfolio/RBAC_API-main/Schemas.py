# import modules and classes for data validation and serialzation 
from pydantic import BaseModel
from typing import Optional

# Define Pydantic models for user creation, login, reading user data, and token representation
class user_create(BaseModel):
    username: str
    password: str

# Define Pydantic model for user Login
class user_login(BaseModel):
    username: str
    password: str

# Define Pydantic model for reading user data, including role name 
class user_read(BaseModel):
    id: int
    username: str
    role_name: Optional[str]

# Configuration to enable ORM mode for compatibility with SQLAlchemy models
class Config:
    from_attributes = True

# Define Pydantic model for token representation 
class token(BaseModel):
    access_token: str
    token_type: str = "bearer"
