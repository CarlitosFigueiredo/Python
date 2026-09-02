def main():
    try:
        # Tentativa de criar um arquivo em diretório protegido por permissões
        with open("/root/meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("Este é um teste de escrita em um diretório protegido.\n")

    except PermissionError:
        print("Erro: Permissão negada ao tentar escrever no diretório protegido.")

    try:
        # Tentativa de criar um arquivo que já existe
        with open("meu_arquivo_existente.txt", "x", encoding="utf-8") as arquivo:
            arquivo.write("Este é um teste de criação de arquivo que já existe.\n")

    except FileExistsError:
        print("Erro: O arquivo 'meu_arquivo_existente.txt' já existe.")

    try:
        # Tentativa de abrir uma arquivo inexistente
        with open("arquivo_inexistente.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)

    except FileNotFoundError:
        print("Erro: O arquivo 'arquivo_inexistente.txt' não foi encontrado.")

if __name__ == "__main__":
    main()