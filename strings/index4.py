with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    contador = texto.count("Olá")
    print(f"{texto}\nTotal de ocorrências de 'Olá': {contador}")