from routers import routes_especies
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from decouple import config, Csv
from fastapi import FastAPI

import db.schemas as schemas

app = FastAPI(title="Cão 4 Hope")

DATABASE_URL = config("DATABASE_URL", default="postgres://hbbbrzoaithzar:c53b3fdb3674632f8951b7694567c9e71e2d6c0c85b85745e7e1a30cc3dd8a49@ec2-3-209-38-221.compute-1.amazonaws.com:5432/d9sch5r3hpk5bi")

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