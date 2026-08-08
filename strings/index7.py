minha_lista = ["Arroz", "Feijão", "Macarrão"]

texto1 = ",".join(minha_lista)

with open("texto1.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto1)
    
texto2 = "\n".join(minha_lista)

with open("texto2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto2)