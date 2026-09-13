
import pytest

from src.reminder import (
    adicionar_medicamento,
    marcar_como_tomado,
    remover_medicamento,
)


def test_adicionar_medicamento():
    lista = []

    resultado = adicionar_medicamento(
        lista,
        "Dipirona",
        ["08:00"],
    )

    assert len(resultado) == 1
    assert resultado[0]["nome"] == "Dipirona"
    assert resultado[0]["horarios"] == ["08:00"]
    assert resultado[0]["tomados"] == []


def test_adicionar_medicamento_com_multiplos_horarios():
    lista = []

    resultado = adicionar_medicamento(
        lista,
        "Dipirona",
        ["08:00", "20:00"],
    )

    assert len(resultado) == 1
    assert resultado[0]["nome"] == "Dipirona"
    assert resultado[0]["horarios"] == ["08:00", "20:00"]


def test_nome_vazio():
    lista = []

    with pytest.raises(ValueError):
        adicionar_medicamento(
            lista,
            "",
            ["08:00"],
        )


def test_marcar_como_tomado():
    lista = [
        {
            "nome": "Dipirona",
            "horarios": ["08:00"],
            "tomados": [],
        }
    ]

    resultado = marcar_como_tomado(
        lista,
        "Dipirona",
    )

    assert resultado is True
    assert len(lista[0]["tomados"]) == 1


def test_marcar_medicamento_inexistente():
    lista = [
        {
            "nome": "Dipirona",
            "horarios": ["08:00"],
            "tomados": [],
        }
    ]

    resultado = marcar_como_tomado(
        lista,
        "Paracetamol",
    )

    assert resultado is False
    assert lista[0]["tomados"] == []


def test_remover_medicamento():
    lista = [
        {
            "nome": "Dipirona",
            "horarios": ["08:00"],
            "tomados": [],
        }
    ]

    resultado = remover_medicamento(
        lista,
        "Dipirona",
    )

    assert resultado is True
    assert lista == []


def test_remover_medicamento_inexistente():
    lista = [
        {
            "nome": "Dipirona",
            "horarios": ["08:00"],
            "tomados": [],
        }
    ]

    resultado = remover_medicamento(
        lista,
        "Paracetamol",
    )

    assert resultado is False
    assert len(lista) == 1
