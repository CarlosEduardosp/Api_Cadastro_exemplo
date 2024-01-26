from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer
from src.main.validacao.classModelsvalidar.pessoa_id_validar import PessoaId
from src.main.validacao.validar_entrada.validar_dados_entrada import Validar_dados_entrada

router = APIRouter()


@router.delete('/delete')
def delete_pessoa(pessoa_id: PessoaId):

    resposta = Validar_dados_entrada(id=pessoa_id)

    if resposta:

        buscar = AdapterPessoa(
            api_route=register_pessoa_composer(),
            data={
                "pessoa_id": pessoa_id.pessoa_id
            }
        )

        response = buscar.delete_adapter()

        return response

    else:
        return resposta
