class myfloat:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def shownumber(self):
        print(f"I am {self.number1}.{self.number2}")

    def __add__(self, other):
        if (self.number2 + other.number2) > 9:
            return myfloat(self.number1 + other.number1 + 1, self.number2 + other.number2 - 10)


ex1 = myfloat(3, 7)
ex1.shownumber()

ex2 = myfloat(4, 6)
ex2.shownumber()

result = ex1 + ex2
print(f"I am {result.number1}.{result.number2}")
print(result)
