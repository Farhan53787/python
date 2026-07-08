file = open('null.txt', 'r')

go = 0

content = file.read()

colist = content.splitlines('\n')

for i in colist:
    go += 1

print("Total number of lines in the file: ", go)
