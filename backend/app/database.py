from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

aConfig = Config()

# Create the database engine
engine = create_engine(aConfig.DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define base model class
Base = declarative_base()

# Dependency to get a database session
def get_db():
    """Creates a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
