import pytest

from src.reminder import (
    adicionar_medicamento,
    marcar_como_tomado,
    remover_medicamento,
)


def test_adicionar_medicamento():
    lista = []
    resultado = adicionar_medicamento(lista, "Dipirona", ["08:00"])

    assert len(resultado) == 1
    assert resultado[0]["nome"] == "Dipirona"


def test_nome_vazio():
    lista = []

    with pytest.raises(ValueError):
        adicionar_medicamento(lista, "", ["08:00"])


def test_marcar_como_tomado():
    lista = [
        {"nome": "Dipirona", "horarios": ["08:00"], "tomados": []}
    ]

    resultado = marcar_como_tomado(lista, "Dipirona")

    assert resultado is True
    assert len(lista[0]["tomados"]) == 1


def test_remover_medicamento():
    lista = [
        {
            "nome": "Dipirona",
            "horarios": ["08:00"],
            "tomados": [],
        }
    ]

    resultado = remover_medicamento(lista, "Dipirona")

    assert resultado is True
    assert lista == []