import json
import os

ARQUIVO = "essenciasambiente.txt"

def carregar_produtos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return [json.loads(linha.strip()) for linha in f if linha.strip()]

def salvar_produtos(produtos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for produto in produtos:
            f.write(json.dumps(produto, ensure_ascii=False) + "\n")
