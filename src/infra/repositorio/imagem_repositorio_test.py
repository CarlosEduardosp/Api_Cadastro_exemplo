from .imagem_repositorio import ImagemRepository
from faker import Faker
from src.infra.configs.config_bd import session
from PIL import Image
import io

faker = Faker()


def insert():

    inserir_imagem = ImagemRepository(session)

    # salvando o caminho da imagem
    caminho_da_imagem = 'C:/Users/carol/Downloads/logoga.jpg'

    # Abrir a imagem
    imagem = Image.open(caminho_da_imagem)

    # Salvar a imagem em um objeto BytesIO
    dados_binarios_fake = io.BytesIO()
    imagem.save(dados_binarios_fake, format='JPEG')

    inserir_imagem.criar_imagem(
        id_pessoa=12,
        nome=faker.name(),
        imagem=dados_binarios_fake.getvalue()
    )
    print('inserido')


def select():

    response = ImagemRepository(session)

    response = response.listar_imagens()

    print(response)


def select_id():
    response = ImagemRepository(session)

    response = response.encontrar_imagem_por_id(id_pessoa=12)

    print(response)


def test_delete():

    response = ImagemRepository(session)

    response = response.deletar_imagem(
        id_pessoa=12

    )

    print(response)