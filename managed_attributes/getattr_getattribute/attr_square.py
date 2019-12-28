class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattr__(self, attr):
        if attr == 'x':
            return self.value ** 2
        else:
            raise AttributeError(attr)

    def __setattr__(self, key, value):
        if key == 'x':
            key = 'value'  # inserting an else: condition would make key unusable by self.__dict__[key]
        self.__dict__[key] = value  # this defaults to self.value = value, then sends it to getattr, getattribute


a = AttrSquare(3)
b = AttrSquare(32)

print(a.x)
a.x = 4

print(a.x)
print(b.x)

