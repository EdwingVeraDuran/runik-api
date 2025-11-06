from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from app.core.config import settings

Base = declarative_base()

# Create engine
engine = create_engine(settings.DATABASE_URL)

# Create session
SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


# Dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
