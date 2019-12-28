class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('Call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


@Tracer
def spam(a, b, c):
    print(a + b + c)


@Tracer
def eggs(x, y):
    print(x ** y)


spam(1, 2, 3)
spam(a=23, b=45, c=90)
spam(23, 45, 67)

eggs(2, 9)
eggs(90, 2)
eggs(23, y=8)

