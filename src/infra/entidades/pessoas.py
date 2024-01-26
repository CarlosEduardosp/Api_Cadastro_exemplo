from ..configs.base import Base
from sqlalchemy import create_engine, Column, Integer, String, Date, BOOLEAN, BLOB


class Pessoa(Base):
    __tablename__ = "Pessoas"

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    sexo = Column(String, nullable=False)
    estado = Column(String, nullable=True)
    cidade = Column(String, nullable=True)
    bairro = Column(String, nullable=True)
    logradouro = Column(String, nullable=True)
    numero = Column(String, nullable=True)
    complemento = Column(String, nullable=True)
    status = Column(BOOLEAN, nullable=False)

