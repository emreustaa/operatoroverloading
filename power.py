class power:

    def __init__(self,number):
        self.number = number

    def __pow__(self, other):
        return self.number ** other.number

a = power(2)
b = power(10)

# 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
print(a ** b)