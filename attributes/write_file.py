file_write = open("data_two.txt", "w", encoding='utf-8')

file_write.write("This is the new content of the file.\n")
file_write.write("This is the second line of the new content.\n")

file_write.close()


lines = ["This is the first line of the file.\n", "This is the second line of the file.\n", "This is the third line of the file.\n"]

file_write = open("data_two.txt", "w", encoding='utf-8')
file_write.writelines(lines)

file_write.close()