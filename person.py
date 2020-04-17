class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age:
            return True
        return False

    def __abs__(self):
        return abs(self.age)

    def __iadd__(self, other):
        return self.age + other.age

Nick = Person("Nick",7)
Angela = Person("Angela",5)
print(Nick>Angela)


Kim = Person("Kim",-8)
print(abs(Kim))

Tom = Person("Tom",7)
Mikayla = Person("Mikayla",11)
Tom += Mikayla
print(Tom)
