from unittest.mock import patch

import pytest

from src import main


@pytest.mark.parametrize("opcao", ["3", "4"])
def test_lista_vazia_nao_solicita_id_nem_executa_operacao(opcao, capsys):
    with (
        patch("src.main.listar_medicamentos", return_value=[]),
        patch("src.main.registrar_tomada") as registrar,
        patch("src.main.remover_medicamento") as remover,
        patch("builtins.input", side_effect=[opcao, "6"]) as entrada,
    ):
        main.main()

    assert entrada.call_count == 2
    registrar.assert_not_called()
    remover.assert_not_called()
    assert "Nenhum medicamento encontrado." in capsys.readouterr().out


@pytest.mark.parametrize("opcao", ["3", "4"])
def test_id_inexistente_nao_executa_operacao(opcao, capsys):
    medicamentos = [{"id": "med-1", "nome": "Dipirona"}]

    with (
        patch("src.main.listar_medicamentos", return_value=medicamentos),
        patch("src.main.registrar_tomada") as registrar,
        patch("src.main.remover_medicamento") as remover,
        patch("builtins.input", side_effect=[opcao, "inexistente", "6"]),
    ):
        main.main()

    registrar.assert_not_called()
    remover.assert_not_called()
    assert "Medicamento não encontrado." in capsys.readouterr().out


def test_remocao_sem_resultado_nao_anuncia_sucesso(capsys):
    medicamentos = [{"id": "med-1", "nome": "Dipirona"}]

    with (
        patch("src.main.listar_medicamentos", return_value=medicamentos),
        patch("src.main.remover_medicamento", return_value=[]) as remover,
        patch("builtins.input", side_effect=["4", "med-1", "6"]),
    ):
        main.main()

    remover.assert_called_once_with("med-1")
    saida = capsys.readouterr().out
    assert "Medicamento não encontrado." in saida
    assert "removido com sucesso" not in saida


@pytest.mark.parametrize(
    ("opcao", "mensagem"),
    [
        ("3", "Medicamento marcado como tomado!"),
        ("4", "Medicamento removido com sucesso!"),
    ],
)
def test_operacao_valida_preservada(opcao, mensagem, capsys):
    medicamentos = [{"id": "med-1", "nome": "Dipirona"}]

    with (
        patch("src.main.listar_medicamentos", return_value=medicamentos),
        patch("src.main.registrar_tomada", return_value={"id": "tomada-1"}) as registrar,
        patch("src.main.remover_medicamento", return_value=medicamentos) as remover,
        patch("builtins.input", side_effect=[opcao, " med-1 ", "6"]),
    ):
        main.main()

    if opcao == "3":
        registrar.assert_called_once_with("med-1")
        remover.assert_not_called()
    else:
        remover.assert_called_once_with("med-1")
        registrar.assert_not_called()

    assert mensagem in capsys.readouterr().out
