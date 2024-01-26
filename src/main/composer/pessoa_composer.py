from src.main.adapter.adapter_interface.adapter_pessoa_interface import RouteInterface
from src.presenters.conrollers.registrar_pessoa import RegisterPessoaController
from src.use_cases.case_inserir_pessoa import Registrarpessoa
from src.infra.repositorio.pessoas_repositorio import PessoaRepository
from src.infra.configs.config_bd import session


def register_pessoa_composer() -> RouteInterface:
    """ composing register pessoa route """

    repository = PessoaRepository(session)
    use_case = Registrarpessoa(repository)
    registrar_pessoa_route = RegisterPessoaController(use_case)

    return registrar_pessoa_route
