from fastapi import APIRouter
from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer
from src.main.validacao.classModelsvalidar.inserir_validar import Item
from src.main.validacao.ValidarNoBanco.validar_dados_no_banco import conferir_pessoa_no_banco
from src.main.validacao.validar_entrada.validar_dados_entrada import Validar_dados_entrada
from PIL import Image
import io

router = APIRouter()


@router.post('/inserir')
def inserir(item: Item):

    # enviando o email para consulta no banco de dados.
    resposta = conferir_pessoa_no_banco(item.email)

    if resposta:

        # validações dos dados de entrada.
        resposta2 = Validar_dados_entrada(
            nome=item.nome,
            data_nascimento=item.data_nascimento,
            telefone=item.telefone,
            email=item.email,
            sexo=item.sexo,
            estado=item.estado,
            cidade=item.cidade,
            bairro=item.bairro,
            logradouro=item.logradouro,
            numero=item.numero,
            status=item.status,
            complemento=item.complemento
        )

        # se resposta igual a true, segue para inserção dos dados no banco.
        if resposta2['success']:

            buscar = AdapterPessoa(
                api_route=register_pessoa_composer(),
                data={
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
                    "complemento": item.complemento
                },
            )

            response = buscar.insert_adapter()
            try:
                if response.status_code == 200:

                    print({"success": True, "message": "Inserido Com Sucesso", "data": response.body.id})
                    return {"success": True, "message": "Inserido Com Sucesso", "data": response.body}
            except:
                return response

        else:
            response = resposta2

            return resposta2
    else:
        response = {"success": False, "data": "Email já cadastrado no banco de dados."}
        return response
