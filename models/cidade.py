from sqlalchemy.orm import Session
from pydantic import BaseModel
from uuid import uuid4
from .estado import Estado

import db.schemas as schemas


class Cidade(BaseModel):
    cidade_id: str = str(uuid4())
    nome: str
    estado_id: str
    estado = Estado

    class Config:
        orm_mode = True


def get_by(db: Session, nome: str = None, estado_id: str = None):
    cidades = db.query(schemas.Cidade)

    if nome:
        cidades = cidades.filter(schemas.Cidade.nome.contains(nome))

    
    if estado_id:
        cidades = cidades.filter(schemas.Cidade.estado_id == estado_id)


    cidades = cidades.all()
    
    return cidades

    

def get_by_id(db: Session, cidade_id: str):
    cidade = db.query(schemas.Cidade).get(cidade_id)

    if cidade:
        return cidade
    else:
        return None

def get_by_nome(db: Session, nome: str):
    cidade = db.query(schemas.Cidade).get(nome)

    if cidade:
        return cidade
    else:
        return None