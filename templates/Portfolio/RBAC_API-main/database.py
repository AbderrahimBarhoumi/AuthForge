# import modules for database connection and session management 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL and create the egine and session maker 
DATABASE_URL = "postgresql://postgres:rdm5skL5@Localhost:5432/RBAC_API"  

# Create the database engine and session Local class
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
