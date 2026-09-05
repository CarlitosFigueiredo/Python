import os

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido!")

except PermissionError as erro:
    print("Sem permissão para remover diretório")
    print(f"Descrição: {erro}")

except FileNotFoundError as erro:
    print("Diretório inexistente")
    print(f"Descrição: {erro}")

except OSError as erro:
    print('Outro erro.')
    print("O diretório está vazio?")
    print(f"Descrição: {erro}")