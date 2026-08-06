file = open('data_two.txt', 'r', encoding='utf-8')

print("Iterating over the file")

for line in file:
    print(repr(line))

file.close()