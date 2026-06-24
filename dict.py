dict = {1: "apple", 2: 'balls'}

dict = {"name": "John", 1: (2,3,6)}

dict = {"name": "John", "age": "45"}

print(dict["name"])

print(dict.get("age"))

dict['age'] = 12

print(dict)

dict['address'] = 'street'

print(dict)

dict.pop('age')
print(dict)

print("Address:", dict.get("address"))

dict.clear()
print(dict)