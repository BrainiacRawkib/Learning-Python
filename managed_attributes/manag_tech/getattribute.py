class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, item):
        if item == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif item == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'square':
            self.__dict__['_square'] = value
        elif key == 'cube':
            self.__dict__['_cube'] = value
        else:
            return object.__setattr__(self, key, value)


x = Powers(3, 4)
print(x.square, x.cube)

x.square = 5
x.cube = 5

print(x.square, x.cube)
