class C:
    def __init__(self):
        print(self.__class__.__name__, self.__dict__)


x = C()

# x.a = 1
#
# print(x.a)


class D:
    __slots__ = ['a', 'b', '__dict__']

    def __init__(self):
        self.d = 4
        # print(self.__class__.__name__, self.__slots__, self.__dict__)


x = D()

x.a = 10
x.b = 20

for attr in list(getattr(x, '__dict__', [])) + getattr(x, '__slots__', []):
    print(attr, '==> ', getattr(x, attr))

