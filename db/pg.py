from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import main as main

Base = declarative_base()


def get_local_session(sqlalchemy_database_url):
    connection_engine = create_engine(
        sqlalchemy_database_url, isolation_level="AUTOCOMMIT", pool_size=100, max_overflow=100, pool_recycle=600
    )

    session = sessionmaker(bind=connection_engine)

    return session()


def get_db():
    db = get_local_session(sqlalchemy_database_url=main.DATABASE_URL)

    try:
        yield db
    finally:
        db.close()
