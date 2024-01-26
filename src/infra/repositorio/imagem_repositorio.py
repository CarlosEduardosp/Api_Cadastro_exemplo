from abc import ABC
from sqlalchemy.orm import Session
from sqlalchemy import update
from ..entidades.imagem import Imagem
from .interfaces_repositorio.interface_imagem_repositorio import InterfaceImagemRepository


class ImagemRepository(InterfaceImagemRepository):
    def __init__(self, session: Session):
        self.session = session

    def criar_imagem(self, id_pessoa, nome, imagem):
        imagem = Imagem(
            id_pessoa=id_pessoa,
            nome=nome,
            imagem=imagem
        )
        self.session.add(imagem)
        self.session.commit()

        return imagem

    def listar_imagens(self):

        response = self.session.query(Imagem).all()
        return response

    def encontrar_imagem_por_id(self, id_pessoa):

        response = self.session.query(Imagem).filter_by(id_pessoa=id_pessoa).first()

        return response

    def deletar_imagem(self, id_pessoa):

        # Encontrar a imagem pelo ID
        imagem = self.session.query(Imagem).filter_by(id_pessoa=id_pessoa).first()

        # Deletar a pessoa se encontrada
        if imagem:
            self.session.delete(imagem)
            self.session.commit()
            return True
        else:
            return False  # Retorna False se a pessoa não for encontrada