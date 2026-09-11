from unittest.mock import patch

from src import main


def test_menu_saida():
    with patch("builtins.input", return_value="6"):
        with patch("builtins.print"):
            main.main()


def test_menu_opcao_invalida():
    entradas = iter(["99", "6"])

    with patch("builtins.input", side_effect=entradas):
        with patch("builtins.print") as mock_print:
            main.main()

    mensagens = [
        chamada.args[0]
        for chamada in mock_print.call_args_list
        if chamada.args
    ]

    assert any(
        "Opção inválida" in mensagem
        for mensagem in mensagens
    )


def test_menu_listar_medicamentos():
    entradas = iter(["2", "6"])

    medicamentos = [
        {
            "id": "med-1",
            "nome": "Dipirona",
            "horarios": ["08:00", "20:00"],
        }
    ]

    with patch(
        "src.main.listar_medicamentos",
        return_value=medicamentos,
    ):
        with patch(
            "builtins.input",
            side_effect=entradas,
        ):
            with patch("builtins.print") as mock_print:
                main.main()

    mensagens = [
        " ".join(str(argumento) for argumento in chamada.args)
        for chamada in mock_print.call_args_list
    ]

    assert any(
        "Dipirona" in mensagem
        for mensagem in mensagens
    )


def test_menu_listar_sem_medicamentos():
    entradas = iter(["2", "6"])

    with patch(
        "src.main.listar_medicamentos",
        return_value=[],
    ):
        with patch(
            "builtins.input",
            side_effect=entradas,
        ):
            with patch("builtins.print") as mock_print:
                main.main()

    mensagens = [
        " ".join(str(argumento) for argumento in chamada.args)
        for chamada in mock_print.call_args_list
    ]

    assert any(
        "Nenhum medicamento" in mensagem
        for mensagem in mensagens
    )