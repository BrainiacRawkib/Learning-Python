class Callee:
    def __call__(self, *args, **kwargs):
        print('Called: ', args, kwargs)


c = Callee()
c(1, 2, 3, a=1, b=2, c=4)

c


class Prod:
    def __init__(self, val):
        self.val = val

    def __call__(self, other):
        return self.val * other


x = Prod(34)

print(x(35))

print(x(10))



