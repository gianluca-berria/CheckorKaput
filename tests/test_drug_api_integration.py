from src.drug_api import consultar_medicamento


class FakeResponse:
    status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return {
            "results": [
                {
                    "openfda": {
                        "generic_name": ["ACETAMINOPHEN"],
                        "brand_name": ["TYLENOL"],
                        "manufacturer_name": ["JOHNSON AND JOHNSON"],
                        "product_type": ["HUMAN OTC DRUG"],
                    },
                    "warnings": [
                        "Ask a doctor before use if you have liver disease."
                    ],
                }
            ]
        }


def test_consultar_medicamento_com_resposta_da_api(monkeypatch):
    def fake_get(url, params, timeout):
        return FakeResponse()

    monkeypatch.setattr(
        "src.drug_api.requests.get",
        fake_get,
    )

    resultado = consultar_medicamento("acetaminophen")

    assert resultado["nome_generico"] == "ACETAMINOPHEN"
    assert resultado["nome_marca"] == "TYLENOL"
    assert resultado["fabricante"] == "JOHNSON AND JOHNSON"
    assert resultado["tipo_produto"] == "HUMAN OTC DRUG"
    assert (
        resultado["aviso"]
        == "Ask a doctor before use if you have liver disease."
    )


def test_consultar_medicamento_sem_resultados(monkeypatch):
    class FakeResponseSemResultados:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {"results": []}

    def fake_get(url, params, timeout):
        return FakeResponseSemResultados()

    monkeypatch.setattr(
        "src.drug_api.requests.get",
        fake_get,
    )

    resultado = consultar_medicamento("medicamento-inexistente")

    assert resultado is None


def test_consultar_medicamento_erro_404(monkeypatch):
    class FakeResponseErro:
        status_code = 404

        def raise_for_status(self):
            raise Exception("Erro HTTP")

    def fake_get(url, params, timeout):
        return FakeResponseErro()

    monkeypatch.setattr(
        "src.drug_api.requests.get",
        fake_get,
    )

    resultado = consultar_medicamento("acetaminophen")

    assert resultado is None


def test_consultar_medicamento_envia_parametros_corretos(monkeypatch):
    chamadas = []

    def fake_get(url, params, timeout):
        chamadas.append(
            {
                "url": url,
                "params": params,
                "timeout": timeout,
            }
        )
        return FakeResponse()

    monkeypatch.setattr(
        "src.drug_api.requests.get",
        fake_get,
    )

    consultar_medicamento("acetaminophen")

    assert len(chamadas) == 1
    assert chamadas[0]["url"] == (
        "https://api.fda.gov/drug/label.json"
    )
    assert chamadas[0]["params"]["search"] == (
        'openfda.generic_name:"acetaminophen"'
    )
    assert chamadas[0]["params"]["limit"] == 1
    assert chamadas[0]["timeout"] == 10