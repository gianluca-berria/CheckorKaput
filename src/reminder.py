from datetime import datetime

def adicionar_medicamento(lista, nome, horarios):
    if not nome:
        raise ValueError("Nome do medicamento não pode ser vazio")

    lista.append({
        "nome": nome,
        "horarios": horarios,
        "tomados": []
    })
    return lista

def listar(lista):
    return lista

def marcar_como_tomado(lista, nome):
    agora = datetime.now().strftime("%H:%M")

    for med in lista:
        if med["nome"].lower() == nome.lower():
            med["tomados"].append(agora)
            return True

    return False