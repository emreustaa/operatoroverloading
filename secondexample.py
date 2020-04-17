class reverse:

    def __init__(self,age):
        self.age = age

    def __add__(self, other):
        return  self.age + other

    def __radd__(self, other):
        return self.age+other

a = reverse(5)

print(a+9)
print(9+a)