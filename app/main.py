from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.routes import auth

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(auth.router, prefix=settings.API_V1_STR)