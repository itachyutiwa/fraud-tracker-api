from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment variable
POSTGRESQL_DB_URL = os.getenv('DB_URL_STRING')

# Create engine
engine = create_engine(POSTGRESQL_DB_URL, echo=True)  # Remove echo=True for production
DBSession = sessionmaker(bind=engine, autoflush=False)  # Include bind parameter

try:
    # Test the connection
    with engine.connect() as connection:
        print("Connected to database successfully!")
except Exception as e:
    print(f"Unable to connect to the database: {e}")
