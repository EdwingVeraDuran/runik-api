from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# SQL BaseModel
Base = declarative_base()

# Create engine
engine = create_engine(settings.DATABASE_URL, echo=True, future=True)

# Create session
SessionLocal = sessionmaker(bind=engine)


# Get database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
