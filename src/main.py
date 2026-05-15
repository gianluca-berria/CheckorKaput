from drug_api import consultar_medicamento
from reminder import (
    adicionar_medicamento,
    listar,
    marcar_como_tomado,
    remover_medicamento,
)
from storage import carregar, salvar


def menu():
    print("\n=== CheckorKaput ===")
    print("1. Adicionar medicamento")
    print("2. Listar medicamentos")
    print("3. Marcar como tomado")
    print("4. Remover medicamento")
    print("5. Consultar informações do medicamento")
    print("6. Sair")


def mostrar_medicamentos(dados):
    medicamentos = listar(dados)

    if not medicamentos:
        print("Nenhum medicamento cadastrado.")
        return

    for medicamento in medicamentos:
        print(f"\nNome: {medicamento['nome']}")
        print(f"Horários: {', '.join(medicamento['horarios'])}")
        print(f"Tomados: {', '.join(medicamento['tomados'])}")


def consultar_info_medicamento():
    nome = input("Nome do medicamento para consulta: ")

    try:
        info = consultar_medicamento(nome)

        if info is None:
            print("Medicamento não encontrado na API.")
            return

        print("\nInformações encontradas:")
        print(f"Nome genérico: {info['nome_generico']}")
        print(f"Nome comercial: {info['nome_marca']}")
        print(f"Fabricante: {info['fabricante']}")
        print(f"Tipo de produto: {info['tipo_produto']}")
        print(f"Aviso: {info['aviso']}")

    except ValueError as erro:
        print(f"Erro: {erro}")
    except Exception:
        print("Erro ao consultar a API pública.")


def remover_info_medicamento(dados):
    nome = input("Nome do medicamento para remover: ")

    if remover_medicamento(dados, nome):
        salvar(dados)
        print("Medicamento removido!")
    else:
        print("Medicamento não encontrado.")


def main():
    dados = carregar()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do medicamento: ")
            horarios = input("Horários (ex: 08:00,20:00): ").split(",")

            try:
                dados = adicionar_medicamento(dados, nome, horarios)
                salvar(dados)
                print("Medicamento adicionado!")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            mostrar_medicamentos(dados)

        elif opcao == "3":
            nome = input("Nome do medicamento: ")

            if marcar_como_tomado(dados, nome):
                salvar(dados)
                print("Registro salvo!")
            else:
                print("Medicamento não encontrado.")

        elif opcao == "4":
            remover_info_medicamento(dados)

        elif opcao == "5":
            consultar_info_medicamento()

        elif opcao == "6":
            print("Encerrando o CheckorKaput.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()