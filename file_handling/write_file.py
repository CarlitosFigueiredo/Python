import os

file = open("file_one.txt", "w", encoding="utf-8")
print('caminho do arquivo:', os.path.abspath("file_one.txt"))

file.write("Hello, World!\n")

print('caminho relativo:', os.path.relpath(file.name))
print('arquivo:', file)

file.close()