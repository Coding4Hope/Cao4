import uuid
from models.especie import Especie, EspecieIn, get_by, update, insert, delete, get_by_id as get_especie_by_id
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.pg import get_db
from uuid import uuid4

import json

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

        
@router.get("/by-id/{id}")
def get_by_id(id: str, db: Session = Depends(get_db)):
    """
    Endpoint que retorna especies filtradas pelo id
    """

    try:
        especies = get_especie_by_id(especie_id=id, db=db)
        return {'success': True, 'message': '', 'data': especies}

    except Exception as err:
        print(err)
        return {'success': False, 'message': 'Deu Ruim'}


@router.post("/")
def save_especie(especie: EspecieIn, db: Session = Depends(get_db)):
    """
    Endpoint para atualizar a especie
    """

    especie = especie.dict()
    especie_db = get_especie_by_id(especie_id=especie["especie_id"], db=db)

    if especie_db:
        especie = update(especie=especie, db=db)
    else:
        return {'success': False, 'message': 'Deu Ruim'}
    return {'success': True, 'message': '', 'data': [especie]}


@router.put("/")
def create_especie(data: EspecieIn, db: Session = Depends(get_db)):
    """
    Endpoint para criar novas espécies
    """
    especie = data.dict()


    check_especie = get_by(nome=especie["nome"], db=db)

    print(especie)

    if not check_especie:
        especie["especie_id"] = str(uuid4())
        print(especie)

        especie = insert(especie=especie, db=db)
        return {'success': True, 'message': '', 'data': [especie]}
    else:
        return {'success': False, 'message': 'Espécie já inserido', 'data': []}



@router.delete("/delete/{especie_id}")
def delete_permission(especie_id: str, db: Session = Depends(get_db)):
    """
    Endpoint que realiza a exclusão da especie
    """

    delete(especie_id=especie_id, db=db)

    return {'success': True, 'message': 'Deu ruim', 'data': []}
