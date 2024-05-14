import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

env_path= Path('../')/'.env'
load_dotenv(dotenv_path=env_path)

POSTGRESQL_DB_URL= os.getenv('DB_URL_STRING')
print(POSTGRESQL_DB_URL)