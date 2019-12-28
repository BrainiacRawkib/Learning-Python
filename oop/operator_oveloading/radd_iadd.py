class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other

    def __radd__(self, other):
        print('radd', self.data, other)
        return other + self.data


x = Adder(45)

y = Adder(45)

print(x + 2)

print(23 + x)

print(x + y)



