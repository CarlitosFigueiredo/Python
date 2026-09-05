import os

try:
    os.mkdir('novo_diretorio')
    print("Diretório criado com sucesso!")

except PermissionError as erro:
    print("Sem permissão para criar o diretório:")
    print(f"Descrição do erro: {erro}")

except FileExistsError as erro:
    print("O diretório já existe. Nenhuma ação foi tomada.")
    print(f"Descrição do erro: {erro}")

print("Termino do programa")
