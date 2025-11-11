# app/main.py

from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.database import session_local, Engine, base
from app.models import User

# Create database tables
base.metadata.create_all(bind=Engine)

# Initialize FastAPI app
app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency to get DB session
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# GET: Login form
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# POST: Login handler
@app.post("/login", response_class=HTMLResponse)
def login_user(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.Email == email).first()
    if user and pwd_context.verify(password, user.HashedPassword):
        return templates.TemplateResponse("login.html", {"request": request, "message": "Login successful!"})
    return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid credentials."})

# GET: Register form
@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# POST: Register handler
@app.post("/register", response_class=HTMLResponse)
def register_user(request: Request, 
                  FirstName:str = Form(...),
                  LastName:str = Form(...),
                  Age:int = Form(...),
                  Email: str = Form(...),
                  password: str = Form(...),
                  Role: str = Form("user"),
                  db: Session = Depends(get_db)
): 

 existing_user = db.query(User).filter(User.email == email).first()
 if existing_user:
    return templates.TemplateResponse("register.html", {"request": request, "message": "Email already registered."})

    hashed_pw = pwd_context.hash(password[:72])
    user = User(FirstName=FirstName, LastName=LastName, Age=Age, Email=Email, HashedPassword=HashedPassword, Role=Role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return templates.TemplateResponse("register.html", {"request": request, "message": "User registered successfully!"})
