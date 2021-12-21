import uuid
from models.ong import ong, ongIn, get_by, update, insert, delete, get_by_id as get_ong_by_id
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.pg import get_db
from uuid import uuid4

import json

router = APIRouter()


@router.get("/by-nome/{nome}")
def get_by_nome(nome: str, db: Session = Depends(get_db)):
    """
    Endpoint que retornas especies filtradas pelo nome
    :param nome: Nome da espécie
    :param db:  Conexão automática criada
    :return: Json com espécies encontrados
    """

    try:
        ongs = get_by(nome=nome, db=db)
        return {'success': True, 'message': '', 'data': ongs}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}

        
@router.get("/by-id/{id}")
def get_by_id(id: str, db: Session = Depends(get_db)):
    """
    Endpoint que retorna especies filtradas pelo id
    """

    try:
        ongs = get_ong_by_id(ong_id=id, db=db)
        return {'success': True, 'message': '', 'data': ongs}

    except Exception as err:
        print(err)
        return {'success': False, 'message': 'Deu Ruim'}