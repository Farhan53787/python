file_name = "Shopping.txt"

shopping = open(file_name, "w")

shopping.write("Shopping List\n")

shopping.write("1. Milk\n")

shopping.write("2. Eggs\n")

shopping.write("3. Bread\n")

shopping.write("4. Butter\n")

shopping.close()

shopping = open(file_name, "r")

content = shopping.read()

print(content)