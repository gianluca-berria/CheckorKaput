import requests


API_URL = "https://api.fda.gov/drug/label.json"


def consultar_medicamento(nome):
    if not nome or not nome.strip():
        raise ValueError("Nome do medicamento não pode ser vazio")

    params = {
        "search": f'openfda.generic_name:"{nome}"',
        "limit": 1,
    }

    resposta = requests.get(API_URL, params=params, timeout=10)

    if resposta.status_code == 404:
        return None

    resposta.raise_for_status()

    dados = resposta.json()
    resultados = dados.get("results", [])

    if not resultados:
        return None

    resultado = resultados[0]
    openfda = resultado.get("openfda", {})

    return {
        "nome_generico": primeiro_valor(openfda.get("generic_name")),
        "nome_marca": primeiro_valor(openfda.get("brand_name")),
        "fabricante": primeiro_valor(openfda.get("manufacturer_name")),
        "tipo_produto": primeiro_valor(openfda.get("product_type")),
        "aviso": primeiro_valor(resultado.get("warnings")),
    }


def primeiro_valor(valor):
    if isinstance(valor, list) and valor:
        return valor[0]

    if isinstance(valor, str):
        return valor

    return "Não informado"
