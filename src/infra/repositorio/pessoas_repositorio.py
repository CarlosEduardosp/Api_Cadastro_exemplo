from sqlalchemy.orm import Session
from sqlalchemy import update
from ..entidades.pessoas import Pessoa
from .interfaces_repositorio.interface_repositorio import InterfacePessoaRepository


class PessoaRepository(InterfacePessoaRepository):
    def __init__(self, session: Session):
        self.session = session

    def criar_pessoa(self, nome, data_nascimento, telefone, email, sexo, estado, cidade, bairro, logradouro, numero, status, complemento):
        pessoa = Pessoa(
            nome=nome,
            data_nascimento=data_nascimento,
            telefone=telefone,
            email=email,
            sexo=sexo,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            logradouro=logradouro,
            numero=numero,
            status=status,
            complemento=complemento
        )
        self.session.add(pessoa)
        self.session.commit()
        return pessoa

    def listar_pessoas(self):
        """ Lista todas as pessoas cadastradas """

        response = self.session.query(Pessoa).all()
        return response

    def encontrar_pessoa_por_id(self, pessoa_id):
        response =  self.session.query(Pessoa).filter_by(id=pessoa_id).first()
        return response

    def encontrar_pessoa_por_nome(self, pessoa_nome):
        response =  self.session.query(Pessoa).filter_by(nome=pessoa_nome).first()
        return response

    def atualizar_pessoa(self, pessoa_id, dados_atualizados):
        """Atualiza pessoa, esperando um dicionário com os novos dados como parametro, e o id da pessoa."""

        # Encontrar a pessoa pelo ID
        pessoa = self.session.query(Pessoa).filter_by(id=pessoa_id).first()

        # Atualizar os dados
        if pessoa:
            self.session.query(Pessoa).filter_by(id=pessoa_id).update(dados_atualizados)
            self.session.commit()
            return True
        else:
            return False  # Retorna False se a pessoa não for encontrada

    def deletar_pessoa(self, pessoa_id):
        # Encontrar a pessoa pelo ID
        pessoa = self.session.query(Pessoa).filter_by(id=pessoa_id).first()

        # Deletar a pessoa se encontrada
        if pessoa:
            self.session.delete(pessoa)
            self.session.commit()
            return True
        else:
            return False  # Retorna False se a pessoa não for encontrada
