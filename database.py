from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
# connection setting
# pip install psycopg2-binary -> utk postgresql
# next setup

#  session maker for db operations
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

import os
db_username=os.environ.get('DB_USERNAME')
db_password=os.environ.get('DB_PASS')
# engine = create_engine(postgresql://{user}:{pass}@localhost/{dbname})
engine = create_engine(f"postgresql://{db_username}:{db_password}@localhost/fastapi-1", echo=True)

# for models
Base = declarative_base()

# bind to engine
SessionLocal = sessionmaker(bind=engine)
