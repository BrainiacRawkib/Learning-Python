class DescriptorSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescriptorCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

    def __set__(self, instance, value):
        instance._cube = value


class Powers:
    square = DescriptorSquare()  # instance state
    cube = DescriptorCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


x = Powers(3, 4)
print(x.square, x.cube)

x.square = 34
x.cube = 10
print(x.square, x.cube)


