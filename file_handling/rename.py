import os

nome_antigo = 'exemplo.txt'
nome_novo = 'novo_exemplo.txt'

try:
    os.rename(nome_antigo, nome_novo)
    print(f"Arquivo renomeado de '{nome_antigo}' para '{nome_novo}' com sucesso.")

except FileNotFoundError:
    print(f"Arquivo '{nome_antigo}' não encontrado.")

except Exception as e:
    print(f"Ocorreu um erro ao tentar renomear o arquivo: {e}")