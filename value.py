dict = {5 : 10, 6 : 12, 7 : 14, 8 : 16, 9 : 18, 10 : 20}

print(dict)

n = int(input("Enter a number: "))

print("The value for the number", n, "is:", dict.get(n, "number not found"))