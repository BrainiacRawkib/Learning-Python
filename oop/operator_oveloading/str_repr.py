class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class AddRepr(Adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data


class AddStr(Adder):
    def __str__(self):
        return '[Value: %s]' % self.data


class AddBoth(Adder):
    def __str__(self):
        return '[Value: %s]' % self.data

    def __repr__(self):
        return 'a'


x = AddRepr(23)

x + 45

print(x)

x = AddStr(23)

x + 45

print(str(x), repr(x))
