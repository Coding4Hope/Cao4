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


@router.get("/by/")
def get_by_info(cpf: str=None, nome: str=None, db: Session = Depends(get_db)):
    """
    Endpoint que retorna usuarios filtradas pelo nome
    :param nome: Nome do usuario
    :param db:  Conexão automática criada
    :return: Json com usuarios encontrados
    """

    try:
        usuarios = get_by(cpf=cpf, nome=nome, db=db)
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


@router.post("/")
def save_usuario(usuario: UsuarioIn, db: Session = Depends(get_db)):
    """
    Endpoint para atualizar o usuario
    """

    usuario = usuario.dict()
    usuario_db = get_usuario_by_id(usuario_id=usuario["usuario_id"], db=db)

    if usuario_db:
        usuario = update(usuario=usuario, db=db)
    else:
        return {'success': False, 'message': 'C eh burru?'}
    return {'success': True, 'message': '', 'data': [usuario]}


@router.put("/")
def create_usuario(data: UsuarioIn, db: Session = Depends(get_db)):
    """
    Endpoint para criar novos usuários
    """
    usuario = data.dict()

    check_usuario = get_by(cpf=usuario["cpf"], db=db)

    print(usuario)

    if not check_usuario:
        usuario["usuario_id"] = str(uuid4())
        print(usuario)

        usuario = insert(usuario=usuario, db=db)
        return {'success': True, 'message': '', 'data': [usuario]}
    else:
        return {'success': False, 'message': 'Usuário já existe!', 'data': []}


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
