from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv

env_path= Path('../')/'.env'
load_dotenv(dotenv_path=env_path)

POSTGRESQL_DB_URL= os.getenv('DB_URL_STRING')

engine = create_engine(POSTGRESQL_DB_URL, echo=True)
DBSession = sessionmaker(engine, autoflush=False)
