from models.especie import Especie, EspecieIn, get_by
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.pg import get_db

router = APIRouter()


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    """
    Endpoint que retorna todos as especies cadastradas
    """
    try:
        especies = get_by(db=db)
        return {'success': True, 'message': '', 'data': especies}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}


@router.get("/by-nome/{nome}")
def get_by_nome(nome: str, db: Session = Depends(get_db)):
    """
    Endpoint que retornas especies filtradas pelo nome
    :param nome: Nome da espécie
    :param db:  Conexão automática criada
    :return: Json com espécies encontrados
    """

    try:
        especies = get_by(nome=nome, db=db)
        return {'success': True, 'message': '', 'data': especies}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}
