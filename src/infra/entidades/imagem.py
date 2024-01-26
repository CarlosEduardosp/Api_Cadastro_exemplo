from sqlalchemy import create_engine, Column, Integer, String, Date, BOOLEAN, BLOB
from ..configs.base import Base


class Imagem(Base):
    __tablename__ = "Imagem"

    id = Column(Integer, nullable=False, primary_key=True)
    id_pessoa = Column(Integer, nullable=False)
    nome = Column(String, nullable=False)
    imagem = Column(BLOB, nullable=False)

