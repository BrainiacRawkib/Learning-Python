def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


print(min1(23, 45, 67, 2))


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


print(min2('er', 're', 'raw', 'a'))


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min3('make', 'sake', 'bake', 'ace', 'aae'))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y):
    return x < y


def grtrthan(x, y):
    return x > y


print(minmax(lessthan, 4, 2, 1, 3, 5, 7, 9))
print(minmax(grtrthan, 4, 2, 1, 3, 5, 7, 9))


print(lessthan(23, 12))
print(grtrthan(23, 12))


def func(a, b, c, d=8, e=7):
    print(a, b, c, d, e)


func(1, *(5, 6))






