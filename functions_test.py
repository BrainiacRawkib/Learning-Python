def intersect(a, b):
    return [x for x in a if x in b]


d = intersect(['er', 3, 4, 1, 2], ('re', 3, 1, 9, 0, 'er'))

print(d)

x = 99


def func(y):
    z = x + y
    return z


print(func(3))


x = 129


def func(x, y):
    z = x + y
    return z


print(func(7, 3))


def all_builtin_exception_classes():
    import builtins

    a = [x for x in dir(builtins) if x[0] == x[0].capitalize() and not x.startswith('__')]

    # for x in dir(builtins):
    #     if x[0] == x[0].capitalize() and not x.startswith('__'):
    #         a.append(x)

    return a


s = all_builtin_exception_classes()

print(s)


def maker(n):
    def action(x):
        return x ** n
    return action


f = maker(2)

print(f(3))


def maker2(n):
    return lambda x: x ** n


g = maker2(3)

print(g(4))


def f1(n):
    # x = 88
    x = int(input('Enter a value for x : '))
    return f2(x) ** n


def f2(x):
    # print(x)
    return x


print(f1(2))
