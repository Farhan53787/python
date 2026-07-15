with open("null.txt", 'w') as file:
    file.write('Truth is always triumphant')
file.close()

with open("null.txt", 'r') as file:
    content = file.readlines()
    for line in content:
        word = line.split()
    print('the words in the file are:', word)
file.close()