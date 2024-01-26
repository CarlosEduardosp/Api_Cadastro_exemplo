from src.infra.configs.config_bd import engine, Base
from src.main.configs.app import app
import uvicorn

# Cria o banco de dados, se já estiver ele ignora.
Base.metadata.create_all(engine)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
