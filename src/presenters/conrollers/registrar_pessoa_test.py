from src.infra.configs.config_bd import session
from src.infra.repositorio.pessoas_repositorio import PessoaRepository
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.presenters.conrollers.registrar_pessoa import RegisterPessoaController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker
from PIL import Image
import io

faker = Faker()


def test_insertPessoaController():

      pessoarepositorio = PessoaRepository(session)
      usecase = Registrarpessoa(pessoarepositorio)
      registercontroller = RegisterPessoaController(usecase)

      http_request = HttpRequest()

      data = {'nome': faker.name(),
        'data_nascimento': str(14051990),
        'telefone': '22992239273',
        'email':faker.email(),
        'sexo':'M',
        'estado':faker.name(),
        'cidade':faker.name(),
        'bairro':faker.name(),
        'logradouro':faker.name(),
        'numero':faker.name(),
        'status':True,
        'complemento': 'complemento'}

      http_request.query = data
      http_request.body = None
      http_request.body = None

      response = registercontroller.route_insert(http_request=http_request)


def select_controller():
    pessoarepositorio = PessoaRepository(session)
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()

    response = registercontroller.route_select(http_request=http_request)

    print(response)


def select_by_id_controller():

    pessoarepositorio = PessoaRepository(session)
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()
    http_request.query = {'pessoa_id': 2}

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response.status_code, response.body)


def select_by_name_controller():

    pessoarepositorio = PessoaRepository(session)
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()
    http_request.query = {'nome': 'Alexis Dalton'}

    response = registercontroller.route_select_by_name(http_request=http_request)

    print(response.status_code, response.body)


def update_controller():
    pessoarepositorio = PessoaRepository(session)
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()

    data = {'nome': 'kadu',
            'data_nascimento': str(faker.random_number(digits=8)),
            'telefone': faker.name(),
            'email': faker.email(),
            'sexo': faker.name(),
            'estado': faker.name(),
            'cidade': faker.name(),
            'bairro': faker.name(),
            'logradouro': faker.name(),
            'numero': faker.name(),
            'status': True,
            'complemento': 'complemento',
            'id': 2}

    http_request.query = data
    http_request.body = None
    http_request.body = None

    response = registercontroller.route_update(http_request=http_request)
    print(response)


def delete_controller():

    pessoarepositorio = PessoaRepository(session)
    usecase = Registrarpessoa(pessoarepositorio)
    registercontroller = RegisterPessoaController(usecase)

    http_request = HttpRequest()
    http_request.query = {'pessoa_id': 1}

    response = registercontroller.route_delete(http_request=http_request)

    print(response)

