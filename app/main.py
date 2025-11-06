from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.routes import auth
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(auth.router, prefix=settings.API_V1_STR)
