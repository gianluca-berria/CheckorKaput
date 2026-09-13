from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from src.database import (
    cadastrar_medicamento,
    listar_historico,
    listar_medicamentos,
    registrar_tomada,
    remover_medicamento,
)


def test_cadastrar_medicamento_valido():
    medicamento = {
        "id": "med-1",
        "nome": "Dipirona",
        "horarios": ["08:00"],
    }

    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.insert.return_value.execute.return_value = SimpleNamespace(
        data=[medicamento]
    )

    with patch("src.database.get_client", return_value=cliente):
        resultado = cadastrar_medicamento(" Dipirona ", ["08:00"])

    cliente.table.assert_called_once_with("medicamentos")
    tabela.insert.assert_called_once_with(
        {
            "nome": "Dipirona",
            "horarios": ["08:00"],
        }
    )
    assert resultado == medicamento


def test_cadastrar_medicamento_sem_nome():
    with patch("src.database.get_client") as get_client:
        with pytest.raises(
            ValueError,
            match="Nome do medicamento não pode ser vazio",
        ):
            cadastrar_medicamento("   ", ["08:00"])

    get_client.assert_not_called()


def test_cadastrar_medicamento_sem_horario():
    with patch("src.database.get_client") as get_client:
        with pytest.raises(
            ValueError,
            match="Informe pelo menos um horário",
        ):
            cadastrar_medicamento("Dipirona", [])

    get_client.assert_not_called()


def test_listar_medicamentos():
    medicamentos = [
        {
            "id": "med-1",
            "nome": "Dipirona",
            "horarios": ["08:00"],
        }
    ]

    cliente = MagicMock()
    tabela = cliente.table.return_value
    consulta = tabela.select.return_value
    ordenacao = consulta.order.return_value
    ordenacao.execute.return_value = SimpleNamespace(data=medicamentos)

    with patch("src.database.get_client", return_value=cliente):
        resultado = listar_medicamentos()

    cliente.table.assert_called_once_with("medicamentos")
    tabela.select.assert_called_once_with("*")
    consulta.order.assert_called_once_with(
        "created_at",
        desc=True,
    )
    assert resultado == medicamentos


def test_remover_medicamento():
    removido = [
        {
            "id": "med-1",
            "nome": "Dipirona",
        }
    ]

    cliente = MagicMock()
    tabela = cliente.table.return_value
    exclusao = tabela.delete.return_value
    filtro = exclusao.eq.return_value
    filtro.execute.return_value = SimpleNamespace(data=removido)

    with patch("src.database.get_client", return_value=cliente):
        resultado = remover_medicamento("med-1")

    cliente.table.assert_called_once_with("medicamentos")
    tabela.delete.assert_called_once_with()
    exclusao.eq.assert_called_once_with("id", "med-1")
    assert resultado == removido


def test_registrar_tomada():
    registro = {
        "id": "registro-1",
        "medicamento_id": "med-1",
        "tomado_em": "2026-06-12T20:27:06+00:00",
    }

    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.insert.return_value.execute.return_value = SimpleNamespace(data=[registro])

    with patch("src.database.get_client", return_value=cliente):
        resultado = registrar_tomada("med-1")

    cliente.table.assert_called_once_with("registros_tomada")
    tabela.insert.assert_called_once_with(
        {
            "medicamento_id": "med-1",
        }
    )
    assert resultado == registro


def test_listar_historico():
    historico = [
        {
            "id": "registro-1",
            "tomado_em": "2026-06-12T20:27:06+00:00",
            "medicamentos": {
                "nome": "Dipirona",
            },
        }
    ]

    cliente = MagicMock()
    tabela = cliente.table.return_value
    consulta = tabela.select.return_value
    ordenacao = consulta.order.return_value
    ordenacao.execute.return_value = SimpleNamespace(data=historico)

    with patch("src.database.get_client", return_value=cliente):
        resultado = listar_historico()

    cliente.table.assert_called_once_with("registros_tomada")
    tabela.select.assert_called_once_with("id, tomado_em, medicamentos(nome)")
    consulta.order.assert_called_once_with(
        "tomado_em",
        desc=True,
    )
    assert resultado == historico


def test_cadastrar_medicamento_com_horarios_em_branco():
    with patch("src.database.get_client") as get_client:
        with pytest.raises(
            ValueError,
            match="Informe pelo menos um horário",
        ):
            cadastrar_medicamento("Dipirona", ["", "   "])

    get_client.assert_not_called()


@pytest.mark.parametrize(
    "horario_invalido",
    [
        "8:00",
        "24:00",
        "12:60",
        "meio-dia",
    ],
)
def test_cadastrar_medicamento_com_horario_invalido(
    horario_invalido,
):
    with patch("src.database.get_client") as get_client:
        with pytest.raises(
            ValueError,
            match="Horário inválido",
        ):
            cadastrar_medicamento(
                "Dipirona",
                [horario_invalido],
            )

    get_client.assert_not_called()
