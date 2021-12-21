import uuid
from models.estado import Estado, get_by as get_estado_by
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.pg import get_db
from uuid import uuid4

import json

router = APIRouter()

@router.get("")
def get_by(db: Session = Depends(get_db)):
    """
    Endpoint que retornas estados filtradas pelo nome
    :param db:  Conexão automática criada
    :return: Json com estados encontrados
    """

    try:
        estados = get_estado_by(db=db)
        return {'success': True, 'message': '', 'data': estados}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}