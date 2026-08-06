file = open('file.txt', 'r')

print(file.name)

print(file.mode)

print(file.closed)


content = file.read()
print(content)

contentTwo = file.readline()
print(contentTwo)

contentThree = file.readlines()
print(contentThree)

print(repr(contentThree))
print(type(contentThree))


file.close()

print(file.closed)