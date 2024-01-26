import datetime

from src.infra.configs.config_bd import session
from src.infra.repositorio.pessoas_repositorio import PessoaRepository
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from faker import Faker
from PIL import Image
import io

faker = Faker()


def inserir_use_case():
    """ testes use case """

    repository = PessoaRepository(session)
    teste = Registrarpessoa(repository)

    response = teste.inserirpessoa(
        nome=faker.name(),
        data_nascimento=str(faker.random_number(digits=8)),
        telefone=faker.name(),
        email=faker.email(),
        sexo=faker.name(),
        estado=faker.name(),
        cidade=faker.name(),
        bairro=faker.name(),
        logradouro=faker.name(),
        numero=faker.name(),
        status=True,
        complemento=faker.name()
    )
    print(response)

def select():
    """ selecting pessoas """

    repository = PessoaRepository(session)
    teste = Registrarpessoa(repository)

    response = teste.select_pessoas()

    print(response)


def select_by_id():

    repository = PessoaRepository(session)
    teste = Registrarpessoa(repository)

    response = teste.select_by_id(pessoa_id=2)

    if response:
        print(response['data'].nome)


def select_by_nome():
    repository = PessoaRepository(session)
    teste = Registrarpessoa(repository)

    response = teste.select_by_nome(nome='kadu')

    if response:
        print(response['data'].email)


def update_use_case():
    """ testes use case """

    # Teste rápidos
    repository = PessoaRepository(session)
    teste = Registrarpessoa(repository)

    dados_atualizados = {
        'nome': 'Caroline',
        'data_nascimento': '14051986',
        'telefone': '22992239273',
        'email': 'eu@carol',
        'sexo': 'M',
        'estado': 'RJ',
        'cidade': 'Araruama',
        'bairro': 'picada',
        'logradouro': 'estrada de são vicente',
        'numero': '11',
        'status': True,
        'complemento': 'complemento'
    }
    teste.atualizar_dados(pessoa_id=1, dados_atualizados=dados_atualizados)


def delete_use_case():
    repository = PessoaRepository(session)
    teste = Registrarpessoa(repository)

    teste.pessoa_repository.deletar_pessoa(pessoa_id="1")
