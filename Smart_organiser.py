item = [
    "Believe in your ability, even when the path feels uncertain.",
    "Every small step you take today brings you closer to your goals.",
    "Challenges are not roadblocks—they are opportunities to grow stronger.",
    "Stay consistent, stay patient, and keep moving forward.",
    "Your future is shaped by what you choose to do today.",
    "Success belongs to those who refuse to give up."
    ]

file = open("file.txt", "w")

file.writelines(item)

file.close()

print("File: New paragraph has been written successfully.")

n = int(input("Enter the number of characters you want to read from the file: "))

file = open("file.txt", "r")

content = file.read(n)

file.close()

print("Console: The first", n, "characters from the file are previewed:")

print(content)
