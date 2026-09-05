
import os
arquivo_a_remove = "exemplo.txt"

try:
    os.remove(arquivo_a_remove)
    print(f"Arquivo '{arquivo_a_remove}' removido com sucesso.")

except FileNotFoundError:
    print(f"Arquivo '{arquivo_a_remove}' não encontrado.")

except Exception as e:
    print(f"Ocorreu um erro ao tentar remover o arquivo: {e}")