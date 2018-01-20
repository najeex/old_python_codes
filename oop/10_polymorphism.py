class Animal:
    def __init__(self, name=''):
        self.name = name

    def talk(self):
        pass


class Cat(Animal):

    def talk(self):
        print('Meow!')


class Dog(Animal):
    def talk(self):
        print('woof!')


a = Animal()
a.talk()

c = Cat("Najeeb")
c.talk()

d = Dog("bob")
d.talk()
