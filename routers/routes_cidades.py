import uuid
from models.cidade import Cidade, get_by as get_cidade_by_estado
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.pg import get_db
from uuid import uuid4

import json

router = APIRouter()

@router.get("/by-estado/{estado_id}")
def get_by_estado(estado_id: str, db: Session = Depends(get_db)):
    """
    Endpoint que retornas cidade filtradas pelo estado
    :param estado: estado da cidade
    :param db:  Conexão automática criada
    :return: Json com cidade encontrados
    """

    try:
        cidades = get_cidade_by_estado(estado_id= estado_id, db=db)
        return {'success': True, 'message': '', 'data': cidades}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}