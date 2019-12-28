def d1(f):
    return lambda: 'X' + f()


def d2(f):
    return lambda: 'Y' + f()


def d3(f):
    return lambda: 'Z' + f()


@d1
@d2
@d3
def func():
    return 'Spam'


print(func())
