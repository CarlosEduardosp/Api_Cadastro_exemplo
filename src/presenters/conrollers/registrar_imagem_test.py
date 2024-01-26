from src.infra.configs.config_bd import session
from src.infra.repositorio.imagem_repositorio import ImagemRepository
from src.use_cases.case_imagem import Registrarimagem
from src.presenters.conrollers.registrar_imagem import RegisterImagemController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker
from PIL import Image
import io

faker = Faker()


def insertPessoaController():

      imagemrepositorio = ImagemRepository(session)
      usecase = Registrarimagem(imagemrepositorio)
      registercontroller = RegisterImagemController(usecase)

      http_request = HttpRequest()

      # salvando o caminho da imagem
      caminho_da_imagem = 'C:/Users/carol/Downloads/logoga.jpg'

      # Abrir a imagem
      imagem = Image.open(caminho_da_imagem)

      # Salvar a imagem em um objeto BytesIO
      dados_binarios_fake = io.BytesIO()
      imagem.save(dados_binarios_fake, format='JPEG')

      data = {
        'nome': faker.name(),
        'id_pessoa': 10,
        'imagem': dados_binarios_fake.getvalue()}

      http_request.query = data
      http_request.body = None
      http_request.body = None

      response = registercontroller.route_insert_imagem(http_request=http_request)
      print(response)


def select_controller():
    imagemrepositorio = ImagemRepository(session)
    usecase = Registrarimagem(imagemrepositorio)
    registercontroller = RegisterImagemController(usecase)

    http_request = HttpRequest()

    response = registercontroller.route_select(http_request=http_request)

    print(response)


def select_by_id_controller():

    imagemrepositorio = ImagemRepository(session)
    usecase = Registrarimagem(imagemrepositorio)
    registercontroller = RegisterImagemController(usecase)

    http_request = HttpRequest()
    http_request.query = {'id_pessoa': 10}

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response.status_code, response.body)


def delete_controller():

    imagemrepositorio = ImagemRepository(session)
    usecase = Registrarimagem(imagemrepositorio)
    registercontroller = RegisterImagemController(usecase)

    http_request = HttpRequest()
    http_request.query = {'id_pessoa': 10}

    response = registercontroller.route_delete(http_request=http_request)

    print(response)

