
import runpy
from unittest.mock import Mock

import streamlit as st
from src import drug_api


def executar_app(monkeypatch, nome="", clicou=False, resultado=None, erro=None):
    monkeypatch.setattr(st, "set_page_config", Mock())
    monkeypatch.setattr(st, "title", Mock())
    monkeypatch.setattr(st, "write", Mock())
    monkeypatch.setattr(st, "warning", Mock())
    monkeypatch.setattr(st, "error", Mock())
    monkeypatch.setattr(st, "subheader", Mock())
    monkeypatch.setattr(st, "text_input", Mock(return_value=nome))
    monkeypatch.setattr(st, "button", Mock(return_value=clicou))

    consulta = Mock()
    if erro is not None:
        consulta.side_effect = erro
    else:
        consulta.return_value = resultado

    monkeypatch.setattr(drug_api, "consultar_medicamento", consulta)

    runpy.run_path("streamlit_app.py")

    return consulta


def test_app_exibe_titulo_e_aviso(monkeypatch):
    executar_app(monkeypatch)

    st.set_page_config.assert_called_once()
    st.title.assert_called_once_with("CheckorKaput")
    st.warning.assert_called_once()


def test_app_nao_consulta_nome_vazio(monkeypatch):
    executar_app(monkeypatch, nome="   ", clicou=True)

    st.error.assert_called_once_with("Digite o nome de um medicamento.")


def test_app_exibe_aviso_quando_medicamento_nao_encontrado(monkeypatch):
    executar_app(monkeypatch, nome="medicamento-inexistente", clicou=True)

    st.warning.assert_any_call("Medicamento não encontrado na API.")


def test_app_exibe_dados_do_medicamento(monkeypatch):
    resultado = {
        "nome_generico": "Dipirona",
        "nome_marca": "Exemplo",
        "fabricante": "Fabricante Teste",
        "tipo_produto": "Medicamento",
        "aviso": "Uso conforme orientação profissional",
    }

    executar_app(monkeypatch, nome="Dipirona", clicou=True, resultado=resultado)

    st.subheader.assert_called_once_with("Informações encontradas")
    assert st.write.call_count == 6


def test_app_exibe_erro_quando_consulta_falha(monkeypatch):
    executar_app(
        monkeypatch,
        nome="Dipirona",
        clicou=True,
        erro=Exception("Falha simulada"),
    )

    st.error.assert_called_once_with("Erro ao consultar a API pública.")
