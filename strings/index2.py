arquivo = open('dados.txt', 'r', encoding='utf-8')
conteudo = arquivo.readline()

print("Tipo de arquivo: ", type(conteudo))

print("Conteúdo retornado pelo readline: ")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado: ")
print(repr(proximo_conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo retornado: ")
print(repr(proximo_conteudo))

arquivo.close()