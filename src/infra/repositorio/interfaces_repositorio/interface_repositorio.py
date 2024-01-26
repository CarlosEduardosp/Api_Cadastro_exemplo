from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from src.infra.entidades.pessoas import Pessoa


class InterfacePessoaRepository(ABC):
    @abstractmethod
    def criar_pessoa(self, nome, data_nascimento, telefone, email, sexo, estado, cidade, bairro, logradouro, numero, status, imagem):
        pass

    @abstractmethod
    def listar_pessoas(self):
        pass

    @abstractmethod
    def encontrar_pessoa_por_id(self, pessoa_id):
        pass

    @abstractmethod
    def encontrar_pessoa_por_nome(self, pessoa_nome):
        pass

    @abstractmethod
    def atualizar_pessoa(self, pessoa_id, dados_atualizados):
        pass

    @abstractmethod
    def deletar_pessoa(self, pessoa_id):
        pass
