with open('file.txt', 'w') as f:

    f.write('Programming is essential for everyone.')

f.close()

with open('file.txt', 'r') as file:
    content = file.readlines()
    
    for line in content:
        words = line.split()
        print(words)

file.close()

new = 'farhan.txt'

import os

if os.path.exists(new):
    print("File: {} exists.".format(new))
else:
    print("File: {} does not exist.".format(new))

new_file = open(new, 'x')

new_file.close()