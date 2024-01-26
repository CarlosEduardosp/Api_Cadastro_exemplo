from .pessoas_repositorio import PessoaRepository
from faker import Faker
from src.infra.configs.config_bd import session
from PIL import Image
import io

faker = Faker()


def insert():
    try:

        pessoas = PessoaRepository(session)

        nome = faker.name()
        data_nascimento = str(faker.random_number(digits=8))
        telefone = faker.name()
        email = faker.email()
        sexo = faker.name()
        estado = faker.name()
        cidade = faker.name()
        bairro = faker.name()
        logradouro = faker.name()
        numero = faker.name()
        status = True
        complemento = faker.name()

        response = pessoas.criar_pessoa(
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
        print(response.nome)

    except:
        print('Sem Sucesso')


def test_select_pessoas():
    pessoas = PessoaRepository(session)

    response = pessoas.listar_pessoas()

    for i in response:
        print(i.nome)


def select_by_id():
    pessoas = PessoaRepository(session)

    response = pessoas.encontrar_pessoa_por_id(2)

    print(response.nome)


def select_by_name():
    pessoas = PessoaRepository(session)

    "precisa ser o nome completo, ou identico ao nome no banco de dados."
    response = pessoas.encontrar_pessoa_por_nome('Roger Payne')
    print(response.email)


def update_pessoa():
    pessoas = PessoaRepository(session)

    dados = {
        'nome': 'Kadu',
        'data_nascimento': '14051986',
        'telefone': '22992239273',
        'email': 'carlos.spadilha@yahoo.com.br',
        'sexo': 'M',
        'estado': 'RJ',
        'cidade': 'Araruama',
        'bairro': 'picada',
        'logradouro': 'estrada de são vicente',
        'numero': '11',
        'status': True,
        'complemento': 'complemento'
    }

    pessoa_id = 2
    pessoas.atualizar_pessoa(pessoa_id=pessoa_id, dados_atualizados=dados)


def delete_pessoas():
    pessoas = PessoaRepository(session)

    pessoas.deletar_pessoa(2)





