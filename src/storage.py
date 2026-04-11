import json
import os

FILE_PATH = "data/meds.json"

def carregar():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def salvar(dados):
    with open(FILE_PATH, "w") as f:
        json.dump(dados, f, indent=4)