file_write = open('null.txt', 'w')

file_write.write('File in writing mode....')

file_write.write("Education doesn't depend on difficulty.")

file_write.close()


file_append = open('null.txt', 'a')

file_append.write('File in append mode....')

file_append.write("Education is the key to success.")

file_append.close()


file_read = open('null.txt', 'r')

print("File in reading mode....")

print(file_read.read())

file_read.close()