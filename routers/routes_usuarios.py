import uuid
from models.usuario import Usuario, UsuarioIn, get_by, update, insert, delete, get_by_id as get_usuario_by_id
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.pg import get_db
from uuid import uuid4

import json

router = APIRouter()


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    """
    Endpoint que retorna todos os usuario cadastradas
    """
    try:
        usuarios = get_by(db=db)
        return {'success': True, 'message': '', 'data': usuarios}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}


@router.get("/by-nomes/{nome}")
def get_by_nome(nome: str, db: Session = Depends(get_db)):
    """
    Endpoint que retorna usuarios filtradas pelo nome
    :param nome: Nome do usuario
    :param db:  Conexão automática criada
    :return: Json com usuarios encontrados
    """

    try:
        usuarios = get_by(nome=nome, db=db)
        return {'success': True, 'message': '', 'data': usuarios}

    except Exception as err:
        return {'success': False, 'message': 'Deu Ruim'}

        
@router.get("/by-id/{id}")
def get_by_id(id: str, db: Session = Depends(get_db)):
    """
    Endpoint que retorna usuario filtrado pelo id
    """

    try:
        usuarios = get_usuario_by_id(usuario_id=id, db=db)
        return {'success': True, 'message': '', 'data': usuarios}

    except Exception as err:
        print(err)
        return {'success': False, 'message': 'Deu Ruim'}


@router.delete("/delete/{usuario_id}")
def delete_permission(usuario_id: str, db: Session = Depends(get_db)):
    """
    Endpoint que realiza a exclusão do usuario
    """
   
    try:
        delete(usuario_id=usuario_id, db=db)
        return {'success': True, 'message': 'Registro excluido com sucesso', 'data': []}
    except:
        return {'success': False, 'message': 'Deu ruim', 'data': []}
