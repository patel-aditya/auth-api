from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = "postgresql://postgres:Aditya%407879%40DataBase@localhost:5432/users"

engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush= False, bind = engine)
Base = declarative_base()


def get_db():
    db = session()
    try: 
        yield db
    finally:
        db.close()

