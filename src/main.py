
from src.database import (
    cadastrar_medicamento,
    listar_historico,
    listar_medicamentos,
    registrar_tomada,
    remover_medicamento,
)


def menu():
    print("\n===== CheckorKaput CLI =====")
    print("1 - Adicionar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Marcar como tomado")
    print("4 - Remover medicamento")
    print("5 - Ver histórico de tomadas")
    print("6 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha: ")

        # 1 - CADASTRAR
        # -------------------------
        if opcao == "1":
            nome = input("Nome do medicamento: ")
            horarios = input("Horários (ex: 08:00,20:00): ").split(",")

            try:
                cadastrar_medicamento(nome, horarios)
                print("âœ” Medicamento adicionado com sucesso!")
            except Exception as erro:  # noqa: BLE001
                print(f"Erro ao cadastrar: {erro}")

            
        # 2 - LISTAR
        # -------------------------
        elif opcao == "2":
            try:
                medicamentos = listar_medicamentos()

                if not medicamentos:
                    print("Nenhum medicamento encontrado.")
                else:
                    print("\n--- Medicamentos cadastrados ---")
                    for med in medicamentos:
                        print(f"- {med['nome']} | Horários: {med['horarios']}")

            except Exception as erro:  # noqa: BLE001
                print(f"Erro ao listar: {erro}")

        # -------------------------
        # 3 - MARCAR COMO TOMADO
        # -------------------------
        elif opcao in ("3", "4"):
            try:
                medicamentos = listar_medicamentos()

                if not medicamentos:
                    print("Nenhum medicamento encontrado.")
                    continue

                print("\n--- Medicamentos cadastrados ---")
                for med in medicamentos:
                    print(f"{med['id']} - {med['nome']}")

                medicamento_id = input("\nDigite o ID do medicamento: ").strip()

                if not any(
                    str(med["id"]) == medicamento_id
                    for med in medicamentos
                ):
                    print("Medicamento não encontrado.")
                    continue

                if opcao == "3":
                    registrar_tomada(medicamento_id)
                    print("Medicamento marcado como tomado!")
                else:
                    removidos = remover_medicamento(medicamento_id)
                    if removidos:
                        print("Medicamento removido com sucesso!")
                    else:
                        print("Medicamento não encontrado.")

            except Exception as erro:  # noqa: BLE001
                operacao = "registrar tomada" if opcao == "3" else "remover"
                print(f"Erro ao {operacao}: {erro}")

        # 5 - HISTÃ“RICO
        # -------------------------
        elif opcao == "5":
            try:
                historico = listar_historico()

                if not historico:
                    print("Nenhum registro de tomadas.")
                else:
                    print("\n--- Histórico de tomadas ---")

                    for item in historico:
                        print(item)

            except Exception as erro:  # noqa: BLE001
                print(f"Erro ao consultar histórico: {erro}")

        # -------------------------
        # 6 - SAIR
        # -------------------------
        elif opcao == "6":
            print("Encerrando CheckorKaput...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
