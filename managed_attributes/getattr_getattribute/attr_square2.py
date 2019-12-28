class AttrSquare:
    def __init__(self, start):
        self.value = start

    def __getattribute__(self, item):
        if item == 'x':
        #     return self.value ** 2
        # else:
            return object.__getattribute__(self, 'value') ** 2

    def __setattr__(self, key, value):
        if key == 'x':
            key = 'value'
        object.__setattr__(self, key, value)


a = AttrSquare(3)
b = AttrSquare(32)

print(a.x)
a.x = 4

print(a.x)
print(b.x)



