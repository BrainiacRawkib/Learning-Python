def gensquares(n):
    for i in range(n):
        yield i ** 2


# for i in gensquares(6):
#     print(i, end=' ')

x = gensquares(8)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


def gen():
    for i in range(10):
        x = yield i
        print(x)


g = gen()

print(next(g))
print(g.send(77))
print(g.send(88))
print(next(g))


for num in (x ** 2 for x in range(5)):
    print('{}, {}'.format(num, num / 2.0))


a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))

print(a, b, c)


x = sorted((x ** 3 for x in range(5)), reverse=True)

print(x)


a = [abs(x) * 2 for x in (-1, -2, -3, -4, -5)]

print(a)


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


print(list(both(5)))


x = ' : '.join(str(i) for i in both(5))


print(x)




