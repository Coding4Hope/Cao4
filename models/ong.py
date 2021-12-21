from sqlalchemy.orm import Session
from pydantic import BaseModel
from uuid import uuid4
from .cidade import Cidade

import db.schemas as schemas


class ong(BaseModel):
    ong_id: str = str(uuid4())
    nome: str
    email: str
    site: str
    endereco: str
    pet: str
    link_vakinha: str
    cidade = Cidade

    class Config:
        orm_mode = True

class ongIn(BaseModel):
    ong_id: str = str(uuid4())
    nome: str
    email: str
    site: str
    endereco: str
    pet: str
    link_vakinha: str
    cidade = Cidade


def get_by(db: Session, nome: str = None, ong_id: str = None, pet: str = None):
    ongs = db.query(schemas.ONG)

    if nome:
        ongs = ongs.filter(schemas.ONG.nome.contains(nome))

    
    if ong_id:
        ongs = ongs.filter(schemas.ONG.ong_id == ong_id)


    ongs = ongs.all()
    
    return ongs

    

def get_by_id(db: Session, ong_id: str):
    ong = db.query(schemas.Cidade).get(ong_id)

    if ong:
        return ong
    else:
        return None


def get_by_nome(db: Session, nome: str):
    ong = db.query(schemas.Cidade).get(nome)

    if ong:
        return ong
    else:
        return None


def insert(ong: ong, db: Session):
    db_ong = schemas.ONG(
        ong_id=ong["ong_id"],
        nome=ong["nome"]
    )

    db.add(db_ong)
    db.commit()
    db.refresh(db_ong)
    return db_ong


def update(ong: ong, db: Session):
    db_ong = db.query(schemas.ONG).get(ong["ong_id"])

    db_ong.nome = ong["nome"]

    db.flush()
    db.commit()
    db.refresh(db_ong)

    return db_ong


def delete(db: Session, ong_id: str):
    ong = db.query(schemas.ONG).get(ong_id)

    db.delete(ong)
    db.commit()