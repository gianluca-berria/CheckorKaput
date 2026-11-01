from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from src.database import registrar_tomada


@pytest.mark.parametrize("medicamento_id", ["", "   "])
def test_tomada_sem_id_nao_acessa_banco(medicamento_id):
    with (
        patch("src.database.get_client") as obter_cliente,
        pytest.raises(ValueError, match="Informe o ID"),
    ):
        registrar_tomada(medicamento_id)

    obter_cliente.assert_not_called()


def test_tomada_inexistente_nao_insere_registro():
    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.select.return_value.eq.return_value.limit.return_value.execute.return_value = (
        SimpleNamespace(data=[])
    )

    with (
        patch("src.database.get_client", return_value=cliente),
        pytest.raises(ValueError, match="Medicamento não encontrado"),
    ):
        registrar_tomada("med-inexistente")

    tabela.select.return_value.eq.assert_called_once_with(
        "id", "med-inexistente"
    )
    tabela.insert.assert_not_called()


def test_tomada_com_resposta_vazia_produz_erro_controlado():
    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.select.return_value.eq.return_value.limit.return_value.execute.return_value = (
        SimpleNamespace(data=[{"id": "med-1"}])
    )
    tabela.insert.return_value.execute.return_value = SimpleNamespace(data=[])

    with (
        patch("src.database.get_client", return_value=cliente),
        pytest.raises(RuntimeError, match="Não foi possível registrar"),
    ):
        registrar_tomada("med-1")
