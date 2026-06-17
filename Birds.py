class Bird:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Macaw = Bird("Macaw", 5)
Parrot = Bird("Parrot", 3)
Flamingo = Bird("Flamingo", 10)

print("{} is a {}".format(Macaw.name, Macaw.species))
print("{} is also a {}".format(Parrot.name, Parrot.species))
print("{} is also a {}".format(Flamingo.name, Flamingo.species))

print("{}'s maximum age is {}".format(Macaw.name, Macaw.age))
print("{}'s maximum age is {}".format(Parrot.name, Parrot.age))
print("{}'s maximum age is {}".format(Flamingo.name, Flamingo.age))