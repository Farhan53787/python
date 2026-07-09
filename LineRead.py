user = int(input("Enter the number of characters need to be previewed: "))

file = open("null.txt", "r")

print (file.read(user))

file.close()


file = open("null.txt", "r")

lines = file.readlines()

file.close()

for i in range(len(lines)):
    print(i + 1,".", lines[i].strip())


word = str(input("Skip lines starting with: "))

file = open("null.txt", "r")

for line in file:
    if line.startswith(word):
        print("(Skip)", line.strip().partition(word)[2].strip())
    else:
        print("(Keep)", line.strip())
file.close()


file = open("null.txt", "r")

lines = file.readlines()

file.close()

out = open("null_odd.txt", "w")

for i in range(len(lines)):
    if i % 2 == 0:
        out.write(lines[i])

out.close()

print("Odd lines have been written to null_odd.txt")
