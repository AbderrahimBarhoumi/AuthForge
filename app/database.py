from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os
 
#Load PostgreSQL URL 
db_URL = os.getenv("db_URL", "postgresql+psycopg2://postgres:jqik2935@localhost:5432/authforge")

# Create the Base for the classes
base = declarative_base()

# Create the Engine 
Engine = create_engine(db_URL)

# Create the session factory
session_local = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


