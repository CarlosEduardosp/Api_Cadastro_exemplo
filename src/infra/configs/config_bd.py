from sqlalchemy import create_engine
from ..configs.base import Base
from sqlalchemy.orm import sessionmaker

# Criar o banco de dados
engine = create_engine("sqlite:///pessoas.db")
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

