from typing import Type
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.conrollers.interface_controller.interfacepessoascontroller import RouteInterface
from .function.calculo_idade import calcular_idade


class RegisterPessoaController(RouteInterface):
    """ Class controller """

    def __init__(self, register_pessoa_use_case: Type[Registrarpessoa]):
        self.register_pessoa_use_case = register_pessoa_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "nome" in query_string_params and
                "data_nascimento" in query_string_params and
                "telefone" in query_string_params and
                "email" in query_string_params and
                "sexo" in query_string_params and
                "estado" in query_string_params and
                "cidade" in query_string_params and
                "bairro" in query_string_params and
                "logradouro" in query_string_params and
                "numero" in query_string_params and
                "status" in query_string_params and
                "complemento" in query_string_params
            ):
                nome = http_request.query['nome']
                data_nascimento = http_request.query['data_nascimento']
                telefone = http_request.query['telefone']
                email = http_request.query['email']
                sexo = http_request.query['sexo']
                estado = http_request.query['estado']
                cidade = http_request.query['cidade']
                bairro = http_request.query['bairro']
                logradouro = http_request.query['logradouro']
                numero = http_request.query['numero']
                status = http_request.query['status']
                complemento = http_request.query['complemento']

                response = self.register_pessoa_use_case.inserirpessoa(
                    nome=nome, data_nascimento=data_nascimento, telefone=telefone,
                    email=email, sexo=sexo, estado=estado, cidade=cidade, bairro=bairro,
                    logradouro=logradouro, numero=numero, status=status, complemento=complemento
                )


                return HttpResponse(status_code=200, body=response["data"])

            else:
                response = {'success': False, 'data': None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            # If no query in http_request
            http_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    def route_select(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select all controllers"""

        try:

            response = self.register_pessoa_use_case.select_pessoas()

            lista_pessoas = []
            if response['success']:
                for item in response['data']:

                    dados = {
                        "id": item.id,
                        "nome": item.nome,
                        "data_nascimento": item.data_nascimento,
                        "telefone": item.telefone,
                        "email": item.email,
                        "sexo": item.sexo,
                        "estado": item.estado,
                        "cidade": item.cidade,
                        "bairro": item.bairro,
                        "logradouro": item.logradouro,
                        "numero": item.numero,
                        "status": item.status,
                        "complemento": item.complemento,
                        "idade": calcular_idade(str(item.data_nascimento)),
                    }
                    lista_pessoas.append(dados)

            return HttpResponse(status_code=200, body=lista_pessoas)

        except:
            return HttpResponse(status_code=400, body=None)

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "pessoa_id" in query_string_params:

                response = self.register_pessoa_use_case.select_by_id(http_request.query['pessoa_id'])

                dados = {
                    "id": response['data'].id,
                    "nome": response['data'].nome,
                    "data_nascimento": response['data'].data_nascimento,
                    "telefone": response['data'].telefone,
                    "email": response['data'].email,
                    "sexo": response['data'].sexo,
                    "estado": response['data'].estado,
                    "cidade": response['data'].cidade,
                    "bairro": response['data'].bairro,
                    "logradouro": response['data'].logradouro,
                    "numero": response['data'].numero,
                    "status": response['data'].status,
                    "complemento": response['data'].complemento,
                    "idade": calcular_idade(str(response['data'].data_nascimento)),
                }

                return HttpResponse(status_code=200, body=dados)
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def route_select_by_name(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by name controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "nome" in query_string_params:

                response = self.register_pessoa_use_case.select_by_nome(http_request.query['nome'])

                return HttpResponse(status_code=200, body=response['data'])
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def route_update(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "nome" in query_string_params and
                "data_nascimento" in query_string_params and
                "telefone" in query_string_params and
                "email" in query_string_params and
                "sexo" in query_string_params and
                "estado" in query_string_params and
                "cidade" in query_string_params and
                "bairro" in query_string_params and
                "logradouro" in query_string_params and
                "numero" in query_string_params and
                "status" in query_string_params and
                "complemento" in query_string_params and
                "id" in query_string_params
            ):
                nome = http_request.query['nome']
                data_nascimento = http_request.query['data_nascimento']
                telefone = http_request.query['telefone']
                email = http_request.query['email']
                sexo = http_request.query['sexo']
                estado = http_request.query['estado']
                cidade = http_request.query['cidade']
                bairro = http_request.query['bairro']
                logradouro = http_request.query['logradouro']
                numero = http_request.query['numero']
                status = http_request.query['status']
                complemento = http_request.query['complemento']
                id = http_request.query['id']

                response = self.register_pessoa_use_case.atualizar_dados(id, http_request.query)

            else:
                response = {'success': False, 'data': None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

            # If no query in http_request
            http_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ delete controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "pessoa_id" in query_string_params:

                pessoa_id = http_request.query['pessoa_id']

                response = self.register_pessoa_use_case.delete(pessoa_id=pessoa_id)

                return HttpResponse(status_code=200, body=response['data'])
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
