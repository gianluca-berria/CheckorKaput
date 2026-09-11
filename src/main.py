
from src.database import (
    cadastrar_medicamento,
    listar_medicamentos,
    remover_medicamento,
    registrar_tomada,
    listar_historico,
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
                print("✔ Medicamento adicionado com sucesso!")
            except Exception as erro:
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

            except Exception as erro:
                print(f"Erro ao listar: {erro}")

        # -------------------------
        # 3 - MARCAR COMO TOMADO
        # -------------------------
        elif opcao == "3":
            try:
                medicamentos = listar_medicamentos()

                print("\n--- Medicamentos cadastrados ---")
                for med in medicamentos:
                    print(f"{med['id']} - {med['nome']}")

                medicamento_id = input("\nDigite o ID do medicamento: ")

                registrar_tomada(medicamento_id)

                print(" Medicamento marcado como tomado!")

            except Exception as erro:
                print(f"Erro ao registrar tomada: {erro}")
        # -------------------------
        # 4 - REMOVER
        # -------------------------
        elif opcao == "4":
            try:
                medicamentos = listar_medicamentos()

                print("\n--- Medicamentos cadastrados ---")
                for med in medicamentos:
                    print(f"{med['id']} - {med['nome']}")

                medicamento_id = input("\nDigite o ID do medicamento a remover: ")

                remover_medicamento(medicamento_id)

                print(" Medicamento removido com sucesso!")

            except Exception as erro:
                print(f"Erro ao remover: {erro}")
        # -------------------------
        # 5 - HISTÓRICO
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

            except Exception as erro:
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