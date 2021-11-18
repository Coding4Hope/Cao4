from routers import routes_especies
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from decouple import config, Csv
from fastapi import FastAPI

import db.schemas as schemas

app = FastAPI(title="Cão 4 Hope")

DATABASE_URL = config("DATABASE_URL", default="postgresql://postgres:postgres@localhost:5432/cao4")

DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')

schemas.Base.metadata.create_all(bind=create_engine(
    DATABASE_URL, isolation_level="AUTOCOMMIT", pool_size=100, max_overflow=100, pool_recycle=600
))

origins = config('ALLOWED_ORIGINS', cast=Csv(), default='')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_especies.router, prefix="/especie", tags=["espécies"])