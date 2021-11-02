from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Time, Date, Float, Table
from sqlalchemy.orm import relationship
from db.pg import Base


class Especie(Base):
    __tablename__ = "especies"

    especie_id = Column(String, primary_key=True, index=True)
    nome = Column(String)
