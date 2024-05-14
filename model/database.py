from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()


POSTGRESQL_DB_URL = os.getenv('DB_URL_STRING')
engine = create_engine(POSTGRESQL_DB_URL, echo=True)  
DBSession = sessionmaker(bind=engine, autoflush=False)

try:
    with engine.connect() as connection:
        print("Connexion réussie!")
except Exception as e:
    print(f"Echec de connexion : {e}")
