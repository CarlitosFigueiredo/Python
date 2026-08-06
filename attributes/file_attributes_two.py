file = open('data.txt', 'r')

content = file.readline()

print("Type of content:", type(content))

print("Return content from readline():")

print(repr(content))

next_content = file.readline()

print("Next content return:")

print(repr(next_content))

file.close()