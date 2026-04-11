from reminder import adicionar_medicamento, listar, marcar_como_tomado
from storage import carregar, salvar

def menu():
    print("\n=== CheckorKaput ===")
    print("1. Adicionar medicamento")
    print("2. Listar medicamentos")
    print("3. Marcar como tomado")
    print("4. Sair")

def main():
    dados = carregar()

    while True:
        menu()
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome do medicamento: ")
            horarios = input("Horários (ex: 08:00,20:00): ").split(",")

            try:
                dados = adicionar_medicamento(dados, nome, horarios)
                salvar(dados)
                print("Medicamento adicionado!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif op == "2":
            meds = listar(dados)
            if not meds:
                print("Nenhum medicamento cadastrado.")
            for med in meds:
                print(f"\nNome: {med['nome']}")
                print(f"Horários: {', '.join(med['horarios'])}")
                print(f"Tomados: {', '.join(med['tomados'])}")

        elif op == "3":
            nome = input("Nome do medicamento: ")
            if marcar_como_tomado(dados, nome):
                salvar(dados)
                print("Registro salvo!")
            else:
                print("Medicamento não encontrado.")

        elif op == "4":
            break

if __name__ == "__main__":
    main()