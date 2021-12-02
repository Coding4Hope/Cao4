from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from uuid import uuid4

import db.schemas as schemas


class Estado(BaseModel):
    estado_id: str = str(uuid4())
    nome: str
    cidades: List

    class Config:
        orm_mode = True

def get_by(db: Session, nome: str = None):
    estados = db.query(schemas.Estado)

    if nome:
        estados = estados.filter(schemas.Estado.nome.contains(nome))

    estados = estados.all()
    return estados


def get_by_id(db: Session, estado_id: str):
    estado = db.query(schemas.Estado).get(estado_id)

    if estado:
        return estado
    else:
        return None