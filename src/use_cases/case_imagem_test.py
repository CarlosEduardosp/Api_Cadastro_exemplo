import datetime
from src.infra.configs.config_bd import session
from src.infra.repositorio.imagem_repositorio import ImagemRepository
from src.use_cases.case_imagem import Registrarimagem
from faker import Faker
from PIL import Image
import io

faker = Faker()


def inserir_use_case():
    """ testes use case """

    # Teste rápidos
    repository = ImagemRepository(session)
    teste = Registrarimagem(repository)

    # salvando o caminho da imagem
    caminho_da_imagem = 'C:/Users/carol/Downloads/logoga.jpg'

    # Abrir a imagem
    imagem = Image.open(caminho_da_imagem)

    # Salvar a imagem em um objeto BytesIO
    dados_binarios_fake = io.BytesIO()
    imagem.save(dados_binarios_fake, format='JPEG')

    teste.inseririmagem(
        id_pessoa=12,
        nome=faker.name(),
        imagem=dados_binarios_fake.getvalue()
    )


def select():
    """ selecting pessoas """

    repository = ImagemRepository(session)
    teste = Registrarimagem(repository)

    response = teste.select_imagem()

    print(response)


def select_by_id():

    repository = ImagemRepository(session)
    teste = Registrarimagem(repository)

    response = teste.select_by_id_imagem(id_pessoa=12)

    if response:
        print(response['data'].nome)


def delete_use_case():
    repository = ImagemRepository(session)
    teste = Registrarimagem(repository)

    teste.delete_imagem(id_pessoa=12)
