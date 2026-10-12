from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from src import main


def test_cli_cadastra_medicamento_integrando_database():
    medicamento = {
        "id": "med-1",
        "nome": "Dipirona",
        "horarios": ["08:00", "20:00"],
    }

    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.insert.return_value.execute.return_value = SimpleNamespace(
        data=[medicamento]
    )

    entradas = iter(
        [
            "1",
            " Dipirona ",
            "08:00,20:00",
            "6",
        ]
    )

    with patch(
        "src.database.get_client",
        return_value=cliente,
    ):
        with patch(
            "builtins.input",
            side_effect=entradas,
        ):
            with patch("builtins.print"):
                main.main()

    cliente.table.assert_called_once_with("medicamentos")
    tabela.insert.assert_called_once_with(
        {
            "nome": "Dipirona",
            "horarios": ["08:00", "20:00"],
        }
    )


def test_cli_remocao_sem_resultado_nao_confirma_sucesso(capsys):
    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.select.return_value.order.return_value.execute.return_value = (
        SimpleNamespace(data=[{"id": "med-1", "nome": "Dipirona"}])
    )
    tabela.delete.return_value.eq.return_value.execute.return_value = (
        SimpleNamespace(data=[])
    )

    with (
        patch("src.database.get_client", return_value=cliente),
        patch("builtins.input", side_effect=["4", "med-1", "6"]),
    ):
        main.main()

    tabela.delete.return_value.eq.assert_called_once_with("id", "med-1")
    saida = capsys.readouterr().out
    assert "Medicamento não encontrado." in saida
    assert "removido com sucesso" not in saida


def test_cli_tomada_de_medicamento_removido_apos_listagem(capsys):
    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.select.return_value.order.return_value.execute.return_value = (
        SimpleNamespace(data=[{"id": "med-1", "nome": "Dipirona"}])
    )
    tabela.select.return_value.eq.return_value.limit.return_value.execute.return_value = (
        SimpleNamespace(data=[])
    )

    with (
        patch("src.database.get_client", return_value=cliente),
        patch("builtins.input", side_effect=["3", "med-1", "6"]),
    ):
        main.main()

    tabela.insert.assert_not_called()
    saida = capsys.readouterr().out
    assert "Erro ao registrar tomada: Medicamento não encontrado." in saida
    assert "marcado como tomado" not in saida


def test_cli_registra_tomada_integrando_database(capsys):
    cliente = MagicMock()
    tabela = cliente.table.return_value
    tabela.select.return_value.order.return_value.execute.return_value = (
        SimpleNamespace(data=[{"id": "med-1", "nome": "Dipirona"}])
    )
    tabela.select.return_value.eq.return_value.limit.return_value.execute.return_value = (
        SimpleNamespace(data=[{"id": "med-1"}])
    )
    tabela.insert.return_value.execute.return_value = (
        SimpleNamespace(data=[{"id": "tomada-1", "medicamento_id": "med-1"}])
    )

    with (
        patch("src.database.get_client", return_value=cliente),
        patch("builtins.input", side_effect=["3", "med-1", "6"]),
    ):
        main.main()

    tabela.insert.assert_called_once_with({"medicamento_id": "med-1"})
    assert "Medicamento marcado como tomado!" in capsys.readouterr().out
