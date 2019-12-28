from functools import reduce

x = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5, 6])

print(x)

x = reduce((lambda x, y: x * y), [1, 2, 3, 4, 5, 6])

print(x)

x = reduce((lambda x, y: x - y), [1, 2, 3, 4, 5, 6])

print(x)


L = [1, 2, 3, 4, 5]

res = L[0]

for x in L[1:]:
    res += x

print(res)


def myreduce(func, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = func(tally, next)
    return tally


print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5, 6]))


import operator, functools


x = functools.reduce(operator.add, (2, 4, 5, 6))

print(x)
