def tracer(func, *pargs, **kargs):
    print('Calling : ', func.__name__)
    return func(*pargs, **kargs)


def functy(a, b, c, d, e, f):
    return a + b + c + d + e + f


print(tracer(functy, 1, 2, c=3, d=4, e=5, f=15))

print(functy(2, 4, 6, 8, 10, 20))


def echo(*args, **kwargs):
    print(args, kwargs)


echo(0, 1, 2, c=3, d=4, e=5)


def knownly(a, *b, c):
    print(a, b, c)


knownly(1, 2, c=3)
knownly(1, 2, 3, c=3)


def knownly_2(a, *, b, c):
    print(a, b, c)


knownly_2(a=1, b=5, c=6)


def knownly_3(a, *, b='foo', c='boo'):
    print(a, b, c)


knownly_3(1)
knownly_3(1, c='dee', b='see')


def f(a, *args, c=6, **kwargs):
    print(a, args, c, kwargs)


f(1, 2, 3, 4, x=12, y=22, z=32)
f(1, 2, 3, 4, x=12, y=22, z=32, c=300)


