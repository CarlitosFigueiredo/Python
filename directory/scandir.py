import os

try:
    entradas = os.scandir('meu_diretorio')

    for obj in entradas:
        print(obj)
        print(f"Nome: {obj.name}")
        print(f"Caminho: {obj.path}")
        print(f"Diretório: {obj.is_dir}")
        print(f"É arquivo: {obj.is_file}")
        if obj.is_file():
            print(f"Tamanho: {obj.stat().st_size}, B")

except FileNotFoundError: 
    print("O caminho não existe")

except NotADirectoryError:
    print("O caminho não é de um diretório")

print("Termino do programa")