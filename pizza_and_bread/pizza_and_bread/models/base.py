from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
#databasetype://username:password@host:port/dbname
#above is a typical format of a datbase URL. 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#don't yet fully understand this yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#this is fine
Base = declarative_base()
