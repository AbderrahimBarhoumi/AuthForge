from pydantic import BaseModel, EmailStr

#Set up models for User Register and Login
class UserCreate(BaseModel):
    FisrtName:str
    LastName:str
    Age:int
    email: EmailStr
    password: str
    role: Annotated[str|None]=None
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
