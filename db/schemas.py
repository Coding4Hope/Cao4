from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Time, Date, Float, Table
from sqlalchemy.orm import relationship
from db.pg import Base


class Especie(Base):
    __tablename__ = "especies"

    especie_id = Column(String, primary_key=True, index=True)
    nome = Column(String)


class Cidade(Base):
    __tablename__ = "cidades"

    cidade_id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    estado_id = Column(String, ForeignKey("estados.estado_id"))


class Estado(Base):
    __tablename__ = "estados"

    estado_id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    cidades = relationship("Cidade")


class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    cpf = Column(String)
    cidade_id = Column(String, ForeignKey("cidades.cidade_id"))
    endereco = Column(String)
    status = Column(String)
    facebook = Column(String)
    instagram = Column(String)
    email = Column(String)
    tipo = Column(String)
    password = Column(String)
