# learn to create class

class Dog:
    name = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")  # method (funciton that goes inside of class)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 24)
print(d.get_name())
print(d.get_age())
d2 = Dog("Bill", 12)
print(d2.get_name())
print(d2.get_age())

d.set_age(47)
print(d.get_name() + "'s new age is " + str(d.get_age()))

