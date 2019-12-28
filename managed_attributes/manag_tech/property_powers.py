class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    @property
    def square(self):
        return self._square ** 2

    @square.setter
    def square(self, value):
        print('Meet me first...')
        self._square = value

    @property
    def cube(self):
        return self._cube ** 3

    @cube.setter
    def cube(self, value):
        self._cube = value


x = Powers(3, 4)
print(x.square)
print(x.cube)

x.square = 2
x.cube = 3

print(x.square)
print(x.cube)


