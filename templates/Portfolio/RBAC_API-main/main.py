# Define the main FastAPI application including routes and static files 
from fastapi import FastAPI
from app.routes import users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="RBAC API")

static_path = os.path.abspath("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

#Include user routes with prefix and tags for better organization 
app.include_router(users.router, prefix="/users", tags=["Users"])

# Root endpoint to verify that the API is running  
@app.get("/")
def read_root():
    return {"message": "RBAC API is running"}

# Endpoint to serve favicon
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    path = os.path.join("assests", "favicon.ico")
    return FileResponse(path)

