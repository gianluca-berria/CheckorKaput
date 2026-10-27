
import json

from src import storage


def test_carregar_retorna_lista_quando_arquivo_nao_existe(tmp_path, monkeypatch):
    arquivo = tmp_path / "meds.json"
    monkeypatch.setattr(storage, "FILE_PATH", str(arquivo))

    resultado = storage.carregar()

    assert resultado == []


def test_carregar_le_dados_salvos(tmp_path, monkeypatch):
    arquivo = tmp_path / "meds.json"
    dados = [{"nome": "Dipirona", "horario": "08:00"}]
    arquivo.write_text(json.dumps(dados), encoding="utf-8")
    monkeypatch.setattr(storage, "FILE_PATH", str(arquivo))

    resultado = storage.carregar()

    assert resultado == dados


def test_salvar_grava_dados_em_json(tmp_path, monkeypatch):
    arquivo = tmp_path / "meds.json"
    monkeypatch.setattr(storage, "FILE_PATH", str(arquivo))
    dados = [{"nome": "Dipirona", "horario": "08:00"}]

    storage.salvar(dados)

    assert arquivo.exists()
    with arquivo.open("r", encoding="utf-8") as f:
        resultado = json.load(f)

    assert resultado == dados
