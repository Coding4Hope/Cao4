from sqlalchemy.orm import Session
from pydantic import BaseModel
from uuid import uuid4

import db.schemas as schemas


class Usuario(BaseModel):
    usuario_id: str = str(uuid4())
    nome: str
    telefone: str
    cpf: str
    endereco: str
    status: str
    facebook: str
    instagram: str
    email: str
    tipo: str
    password: str

    class Config:
        orm_mode = True


class UsuarioIn(BaseModel):
    usuario_id: str = str(uuid4())
    nome: str
    telefone: str
    cpf: str
    endereco: str
    status: str
    facebook: str
    instagram: str
    email: str
    tipo: str
    password: str

def insert(usuario: Usuario, db: Session):
    db_usuario = schemas.Usuario(
        usuario_id=usuario["usuario_id"],
        nome=usuario["nome"],
        telefone=usuario["telefone"],
        cpf=usuario["cpf"],
        endereco=usuario["endereco"],
        status=usuario["status"],
        facebook=usuario["facebook"],
        instagram=usuario["instagram"],
        email=usuario["email"],
        tipo=usuario["tipo"],
        password=usuario["password"]
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def update(usuario: Usuario, db: Session):
    db_usuario = db.query(schemas.Usuario).get(usuario["usuario_id"])

    db_usuario.nome = usuario["nome"]
    db_usuario.telefone = usuario["telefone"]
    db_usuario.cpf = usuario["cpf"]
    db_usuario.endereco = usuario["endereco"]
    db_usuario.status = usuario["status"]
    db_usuario.facebook = usuario["facebook"]
    db_usuario.instagram = usuario["instagram"]
    db_usuario.email = usuario["email"]
    db_usuario.tipo = usuario["tipo"]
    db_usuario.password = usuario["password"]

    db.flush()
    db.commit()
    db.refresh(db_usuario)

    return db_usuario


def get_by(db: Session, nome: str = None):
    usuarios = db.query(schemas.Usuario)

    if nome:
        usuarios = usuarios.filter(schemas.Usuario.nome.contains(nome))

    usuarios = usuarios.all()
    return usuarios


def get_by_id(db: Session, usuario_id: str):
    usuario = db.query(schemas.Usuario).get(usuario_id)
    
    if usuario:
        return usuario
    else:
        return None

def delete(db: Session, usuario_id: str):
    usuario = db.query(schemas.Usuario).get(usuario_id)

    db.delete(usuario)
    db.commit()