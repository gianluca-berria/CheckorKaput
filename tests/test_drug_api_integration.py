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

    monkeypatch.setattr("src.drug_api.requests.get", fake_get)

    resultado = consultar_medicamento("acetaminophen")

    assert resultado["nome_generico"] == "ACETAMINOPHEN"
    assert resultado["nome_marca"] == "TYLENOL"
    assert resultado["fabricante"] == "JOHNSON AND JOHNSON"
    assert resultado["tipo_produto"] == "HUMAN OTC DRUG"
    assert (
        resultado["aviso"]
        == "Ask a doctor before use if you have liver disease."
    )
