class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self.val


x = Number([1])

x += [2]

print(x)


class Number2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Number2(self.val + other)


x = Number2(45)
x += 34

print(x.val)





