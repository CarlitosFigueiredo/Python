import os

file  = open('../test.txt', 'w', encoding='utf-8')

file.write('I thought !')

print(file.name)

file.close()