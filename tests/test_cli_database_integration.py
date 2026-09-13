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
