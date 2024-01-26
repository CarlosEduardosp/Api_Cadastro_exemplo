from src.main.composer.pessoa_composer import register_pessoa_composer
from src.main.adapter.adapter_pessoa import AdapterPessoa
from faker import Faker
from PIL import Image
import io

faker = Faker()


def test_insert_adapter():

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={
            "nome": 'testadapter',
            "data_nascimento": '14051986',
            "telefone": faker.name(),
            "email": faker.email(),
            "sexo": faker.name(),
            "estado": faker.name(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "numero": faker.name(),
            "status": True,
            "complemento": 'complemento'
        },
    )
    response = buscar.insert_adapter()

    print(response)


def select():

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    print(response)


def select_by_id():

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={"pessoa_id": 2}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def select_by_name():

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={"nome": 'Shannon Hernandez'}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def update_adapter():
    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={
            "nome": 'Caroline Padilha',
            "data_nascimento": '11111994',
            "telefone": faker.name(),
            "email": faker.email(),
            "sexo": faker.name(),
            "estado": faker.name(),
            "cidade": faker.name(),
            "bairro": faker.name(),
            "logradouro": faker.name(),
            "numero": faker.name(),
            "status": True,
            "complemento": faker.name(),
            'id': 2
        },
    )
    response = buscar.update_adapter()

    print(response)


def delete_adapter():
    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={
            'pessoa_id':2
        }
    )

    response = buscar.delete_adapter()
    print(response)

