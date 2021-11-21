from sqlalchemy.orm import Session
from pydantic import BaseModel
from uuid import uuid4

import db.schemas as schemas


class Especie(BaseModel):
    especie_id: str = str(uuid4())
    nome: str

    class Config:
        orm_mode = True


class EspecieIn(BaseModel):
    especie_id: str = str(uuid4())
    nome: str


def insert(especie: Especie, db: Session):
    db_especie = schemas.Especie(
        especie_id=especie["especie_id"],
        nome=especie["nome"]
    )

    db.add(db_especie)
    db.commit()
    db.refresh(db_especie)
    return db_especie


def update(especie: Especie, db: Session):
    db_especie = db.query(schemas.Especie).get(especie["especie_id"])

    db_especie.nome = especie["nome"]

    db.flush()
    db.commit()
    db.refresh(db_especie)

    return db_especie


def get_by(db: Session, nome: str = None):
    especies = db.query(schemas.Especie)

    if nome:
        especies = especies.filter(schemas.Especie.nome.contains(nome))

    especies = especies.all()
    return especies


def get_by_id(db: Session, especie_id: str):
    especie = db.query(schemas.Especie).get(especie_id)

    if especie:
        return especie
    else:
        return None


def delete(db: Session, especie_id: str):
    especie = db.query(schemas.Especie).get(especie_id)

    db.delete(especie)
    db.commit()
