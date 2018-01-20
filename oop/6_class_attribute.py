class Cat:
    species = 'mammal'

    def __init__(self, name, age):

        self.name = name
        self.age = age


a = Cat('najeeb', 3)
b = Cat('Khan', 4)

print(a.name, a.age)
print(b.name, b.age)

print(Cat.species)
print(a.__class__.species)
print(b.__class__.species)
