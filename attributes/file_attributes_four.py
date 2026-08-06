file = open('data_two.txt', 'r', encoding='utf-8')

conten = file.read()

print('The entire content of the file')
print(repr(conten), '\n')

content_reinterpretation = file.read()
print('The entire content of the file after reinterpreting')
print(repr(content_reinterpretation), '\n')

file.close()

reopened_file = open('data_two.txt', 'r', encoding='utf-8')

content_reopened = reopened_file.read()
print('The entire content of the file after reopening')
print(repr(content_reopened), '\n')

reopened_file.seek(0)

content_after_seek = reopened_file.read()
print('The content of the file, after seeking to the 8th byte')
print(repr(content_after_seek), '\n')

reopened_file.close()