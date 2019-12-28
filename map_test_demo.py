def incr(x):
    return x + 10


counters = [1, 2, 3, 4, 5]

a = list(map(incr, counters))

print(a)


def mymap(func, seq):
    res = []
    for x in seq:
        res.append(func(x))
    return res


def mymap2(func, *seq):
    return [func(*args) for args in zip(*seq)]


print(mymap(incr, counters))


x = list(map(pow, [1, 2, 3], [2, 3, 4]))

print(x)


def gen_mymap(func, *seq):
    res = []
    for args in zip(*seq):
        yield func(*args)


def gen_mymap2(func, *seq):
    return (func(*args) for args in zip(*seq))


